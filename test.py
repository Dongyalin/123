#! python3

import re

begins = re.compile('H\\w{2}l')
mo = begins.search(r'Hello word')

res = (mo != None)

print(res)
