#match a mobile no
import re
s = input("Enter mobile no ")
if len(s) == 10:
    r = re.fullmatch('[6-9]\d{9}', s)
    if r:
        print("valid")
    else :
        print("Invalid")
elif len(s) == 11:
    r = re.fullmatch('[0][6-9]\d{9}', s)
    if r:
        print("valid")
    else :
        print("Invalid")
elif len(s) == 12:
    r = re.fullmatch('[9][1][6-9]\d{9}', s)
    if r:
        print("valid")
    else :
        print("Invalid")
elif len(s) == 13:
    r = re.fullmatch('[+][9][1][6-9]\d{9}', s)
    if r:
        print("valid")
    else :
        print("Invalid")
else :
    print("Invalid")
    
