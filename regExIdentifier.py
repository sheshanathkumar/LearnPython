#All Yava language identifier
#1. The allowed characters are:
#    Alphabets
#    Digits
#    #
#2. First character should be lower case a to k
#3. Second character should be any digit divisible by 3
#4. Length of identifier should be at least 2

import re
s = input("Enter Identifier: ")
m = re.fullmatch('[a-z][0369][a-zA-Z0-9#]*', s)
if m:
    print(s, "is an Identifier")
else :
    print(s, "is not an Identifier")
