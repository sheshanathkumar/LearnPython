from sys import argv

script, name = argv
prompt = '>'

print ("Hello %s, this is script %s" %(name, script))
print ("Where do you live ")
city = input(prompt)
print ("Where do you study ");
college = input(prompt)

print ("I am %s from %s studying in %s " %(name, city, college))