#!c:\study\submissions\csn291\termproject\virtualenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'zxcvbn==4.4.28','console_scripts','zxcvbn'
__requires__ = 'zxcvbn==4.4.28'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('zxcvbn==4.4.28', 'console_scripts', 'zxcvbn')()
    )
