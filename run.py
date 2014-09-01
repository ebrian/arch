import sys
import re

from parsetools import *
from modules.error import *

symbols = {}

try:
    vortex_source = open(sys.argv[1]).read()
except IOError:
    err_fatal('File could not be opened')
except IndexError:
    err_fatal('File could not be opened')

vortex_lines = vortex_source.split('\n')

i = 1

source = ''

for line in vortex_lines:
    #print str(i) + ': ' + line
    i += 1

    source += str(line.strip()) + '\n'

source = source[:-1]

i = 0

while i < len(source):
    if source[i] == ' ':
        i += eat_space(source[i:])
        continue

    elif source[i:].startswith('//'):
        i += eat_comment(source[i:])
        continue

    elif re.search(r"^[a-z]", source[i:]):
        if is_keyword(source[i:]):
            i += handle_keyword(source[i:])

    else:
        i += 1

# end execution
print ''