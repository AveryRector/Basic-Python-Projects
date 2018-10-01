
# phoneAndEmails.py - Finds phone numbers and emails on clipboard
import re, pyperclip, sys

phoneNumberRegex = re.compile(r'''(
    (\d{3} | \(\d{3}\))?            # Area code
    (\. | - | \s)?                  # Seperator
    (\d{3})                           # First 3 digits
    (\. | - | \s)                   # Seperator
    (\d{4})                           # Last 4 digits
    (\s*(ext|x|ext.) \s*(\d{3,5}))?   # Extension
    )''', re.VERBOSE)


emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # Username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                   # Domain Username
    (\.[a-zA-Z]{2,4})               # dot-something
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []

for groups in phoneNumberRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if(len(matches) > 0):
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email adresses found')
