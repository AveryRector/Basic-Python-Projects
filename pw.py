
# pw.py - An insecure password locker program


PASSWORDS = {
            'email': 'BIGBOICOCK!',
            'wow': '5432rewf!',
            'league': '  fdgd ds32!'
}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for %s account copied to clip board' % account)
else:
    print('There is no %s on file.' % account)
