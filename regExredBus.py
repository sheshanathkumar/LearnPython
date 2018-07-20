import re, urllib
import urllib.request
u = urllib.request.urlopen("https://www.redbus.in/info/contactus")
text = u.read()
f1 = open("output.txt",'w')
num = re.findall('[0-9]{3}[-][0-9]{8}', str(text))
for n in num:
    f1.write(str(n)+"\n")
f1.close()
