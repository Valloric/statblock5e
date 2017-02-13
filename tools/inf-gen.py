#from ConfigParser import ConfigParser
from ConfigParser import ConfigParser
import sys

TEMPLATE_FILE='template.html'

def _gen_free_sequence(section):
    # Expects a list of (name, value) tuples as you get from section.items
    pass

def template_generator(configfile):
    custom = ''
    charconfig = ConfigParser()
    with open(configfile, 'rb') as config:
        charconfig.readfp(config)

    character = {}
    for name, value in charconfig.items('Character'):
        character[name.upper()] = value

    # Construct the custom strings for Attributes, and Actions.
    # These are a bit more of a pain than the rest is all.
    sections = charconfig.sections()
    sections.remove('Character')
    for section in sections:
        custom += '<h3>%s</h3>\n' % section.title()
        for name, value in charconfig.items(section):
            custom += '<property-block>\n'
            custom += '  <h4>%s</h4>\n' % name.title()
            custom += '  <p>%s</p>\n' % value
            custom += '</property-block>\n'
    character['CUSTOM'] = custom

    with open(TEMPLATE_FILE, 'rb') as template:
        t = template.read()
        processed = t.format(
            **character
        )
        print(processed)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Please provide a config file name")
        sys.exit(1)
    elif len(sys.argv) >= 3:
        print("ARRGHH TOO MANY, TOO MANY! I'M LOST")
        sys.exit(2)
    else:
        template_generator(sys.argv[1])


