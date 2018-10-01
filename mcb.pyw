
# mcb.pyw - Saves and loads pieces if text to the clip board
# Usage py.exe mcb.pyw save <keyword> - Save clipboard to keyword
#       py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#       py.exe mcb.pyw list - Loads all keywords to clipboard

import shelve, os, pyperclip

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3: and sys.argv[1].lower == 'save':

    if sys.argv[1].lower == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()

    elif sys.argv[1].lower == 'delete':
        del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:

    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))

    elif sys.argv[1].lower == 'delete':
        for k in list(mcbShelf.keys()):
            del mcbShelf[k]

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()