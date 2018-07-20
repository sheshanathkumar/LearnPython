#All 10 digit mobile number

import re
s = input("Enter a mobile no ")
r = re.fullmatch('[6-9]\d{9}', s)
if r:
    print("valid")
else:
    print("Invalid")
