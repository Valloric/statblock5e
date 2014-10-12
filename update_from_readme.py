#!/usr/bin/env python

from bs4 import BeautifulSoup
from markdown import markdown
import requests
import tarfile
import tempfile
import shutil
import glob
import os.path as p


DIR_OF_THIS_SCRIPT = p.dirname( p.abspath( __file__ ) )
TARBALL_URL = 'https://github.com/Valloric/statblock5e/tarball/master'

def downloadTarball():
  tempdir = tempfile.mkdtemp()
  filename = p.join( tempdir, 'archive.tar.gz')
  chunk_size = 1024 ** 2
  print 'Downloading archive...'
  response = requests.get( TARBALL_URL, stream=True )
  with open( filename, 'wb' ) as fd:
      for chunk in response.iter_content( chunk_size ):
          fd.write( chunk )
  print 'Download complete.'
  return filename


def updateSources():
  archive = downloadTarball()
  tempdir = p.dirname( archive )
  print 'Extracting archive...'
  tfile = tarfile.open( archive, 'r:gz' )
  tfile.extractall( tempdir )
  print 'Extraction complete.'
  folder = glob.glob( p.join( tempdir, 'Valloric*' ) )[ 0 ]

  shutil.rmtree( p.join( DIR_OF_THIS_SCRIPT, 'src' ), ignore_errors = True )
  shutil.copytree( p.join( folder, 'src' ),
                   p.join( DIR_OF_THIS_SCRIPT, 'src' ) )

  for html_file in glob.glob( p.join( folder, '*.html' ) ):
    shutil.copy( html_file,
                 p.join( DIR_OF_THIS_SCRIPT, p.basename( html_file ) ) )

  shutil.copy( p.join( folder, 'README.md' ),
               p.join( DIR_OF_THIS_SCRIPT, 'README.md' ) )

  shutil.rmtree( tempdir )


# HTML5 spec says code should be marked with 'language-XXX' class (where XXX is
# the language).
def fixCodeBlockClasses( doc ):
  for elem in doc.select( 'code[class]'):
    language = elem[ 'class' ][ 0 ]
    if language == 'html':
      # Prism.js wants markup instead of html.
      language = 'markup'
    elem[ 'class' ] = [ 'language-' + language ]


def main():
  updateSources()
  markdown_source = open( 'README.md' ).read()

  with open( 'index.html', 'r+' ) as content_file:
    content = content_file.read()

    new_contents = markdown( unicode( markdown_source, 'utf-8' ),
                            extensions=['fenced_code'] )
    new_tags = BeautifulSoup( new_contents, 'html5lib' )
    fixCodeBlockClasses( new_tags )

    soup = BeautifulSoup( content, "html5lib" )
    elem = soup.find( id='main_content' )
    elem.clear()
    for new_elem in new_tags.body.contents:
      elem.append( new_elem )

    content_file.seek( 0 )
    content_file.truncate()
    content_file.write( str( soup ) )


if __name__ == "__main__":
  main()
