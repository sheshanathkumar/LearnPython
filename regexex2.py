# A valid UID must follow the rules below:

# It must contain at least 2 uppercase English alphabet characters.
# It must contain at least 3 digits ( - ).
# It should only contain alphanumeric characters ( a-z , A - Z &  0-9 ).
# No character should repeat.
# There must be exactly 10 characters in a valid UID.

import re

for _ in range (int(input())):
    uid = ''.join(sorted(input()))
    print(uid)
    try:
        assert len(uid) == 10
        assert re.search(r'[A-Z]{2}', uid)
        assert re.search(r'\d\d\d', uid)
        assert re.search(r'[A-Za-z0-9]',uid)
        assert not re.search(r'(.)\1',uid)
    except:
        print('Invalid')
    else:
        print('Valid')