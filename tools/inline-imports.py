#!/usr/bin/env python

import argparse
import os.path as p
import re
from bs4 import BeautifulSoup

DIR_OF_THIS_SCRIPT = p.dirname( p.abspath( __file__ ) )

def getDocument( content ):
  return BeautifulSoup( content, 'html5lib', from_encoding = 'utf-8' )

def generateInlineFile( source_file_path ):
  final_doc = getDocument( '' )
  doc = getDocument( open( source_file_path ).read() )
  already_processed = set()

  # Process each javascript module declared in the original file
  modules = doc.select( 'script[type="module"]' )
  for module in modules:
    module_path = p.join( p.dirname( source_file_path ), module[ 'src' ] )
    module.decompose()
    processJavascriptModule( module_path, already_processed, final_doc )

  # Append other head elements from the original file
  for child in doc.head.children:
    if str( child ).strip():
      final_doc.head.append( child )

  # Append a script tag containing createCustomElement() to the head
  script_tag = generateCreateCustomElementFunction()
  final_doc.head.append( script_tag )

  # Append the stat-block tree to the body
  stat_block_tag = doc.find('stat-block')
  final_doc.body.append( stat_block_tag )

  return final_doc

def processJavascriptModule( module_path, already_processed, final_doc ):
  if module_path in already_processed:
    return
  already_processed.add( module_path )

  content = open( p.abspath(module_path) ).read()

  # Process any imported modules if they haven't been processed already
  imports = re.findall( r'(?<=import \').*(?=\')', content )
  for import_path in imports:
    import_path = import_path.lstrip('/')
    processJavascriptModule( import_path, already_processed, final_doc )

  # Find the last fetch() in the module to get the path to the HTML template
  fetches = re.findall( r'(?<=fetch\(\').*(?=\'\))', content )
  template_path = fetches[-1]
  template_name = p.splitext( p.basename(template_path) )[0]

  # Convert the module into a pair of inline template and script tags,
  # and add them to the body of the final document
  template_tag = generateTemplateTag( template_name, template_path )
  script_tag = generateScriptTag( template_name, content )

  final_doc.body.append( template_tag )
  final_doc.body.append( script_tag )

def generateCreateCustomElementFunction():
  doc = getDocument( '' )
  content = open ( p.abspath( 'src/js/helpers/create-custom-element.js' ) ).read()
  content = content.replace( 'export ', '' )

  script_tag = doc.new_tag( 'script' )
  script_tag.string = content

  return script_tag

def generateTemplateTag( template_name, template_path ):
  content = open( p.abspath( template_path ) ).read()
  template_doc = getDocument( content )

  template_tag = template_doc.new_tag( 'template', id=template_name )
  for child in template_doc.head.children:
    template_tag.append( child )
  for child in template_doc.body.children:
    template_tag.append( child )

  return template_tag

def generateScriptTag( template_name, content ):
  doc = getDocument( '' )
  script_tag = doc.new_tag( 'script' )

  # Special case: Extract additional javascript functions
  #               for the abilities-block tag only
  if template_name == 'abilities-block':
    javascript_content = extractInlineJavascript( content )
    script_tag.string = f"""{{
  {javascript_content}
  let templateElement = document.getElementById('{template_name}');
  createCustomElement('{template_name}', templateElement.content, elementClass);
}}"""
  else:
    script_tag.string = f"""{{
  let templateElement = document.getElementById('{template_name}');
  createCustomElement('{template_name}', templateElement.content);
}}"""

  return script_tag

def extractInlineJavascript( content ):
  extracted_content = '';
  inExtractionMode = False
  for line in content.splitlines():
    if not inExtractionMode:
      if '// Inline extraction START' in line:
        inExtractionMode = True
    elif '// Inline extraction END' in line:
      inExtractionMode = False
    else:
      extracted_content += line + '\n';
  return extracted_content

def parseArgs():
  parser = argparse.ArgumentParser( description='Inlines HTML imports.' )
  parser.add_argument( '--filename', '-f', required=True, help='file to inline' )
  return parser.parse_args()

def main():
  args = parseArgs()
  print( '<!DOCTYPE html>' )
  print( generateInlineFile( p.abspath( args.filename ) ) )

if __name__ == "__main__":
  main()
