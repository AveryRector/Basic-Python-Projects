import re

textToSearch = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'abc')

matches = pattern.finditer(textToSearch)

for match in matches:
    print(match)
