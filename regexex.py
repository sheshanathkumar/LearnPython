import re

x = int(input())
text = ''
for _ in range(x) :
    text = text + input();
text = re.sub(r'<!.+-->',r' ', text)
print('------\n'+text+'-----------\n')
for tagval in re.findall(r'<([^/][^>]*)>', text):
    if ' ' in tagval:
        for val in re.findall(r'([a-z]+)? *([a-z-]+)="([^"]+)', tagval):
            if val[0]:
                print(val[0])
            print('->'+val[1]+' > '+ val[2])
    else :
        print(tagval)

# text = ''
# for _ in range(int(input())):
#     text = re.sub(r'<!.+-->',r' ',(text+input()))
# print(text)
# for er in re.findall(r'<([^/][^>]*)>', text):
#     if ' ' in er:       
#         for ere in re.findall(r'([a-z]+)? *([a-z-]+)="([^"]+)', er):
#             if ere[0]:
#                 print(ere[0])          
#             print('-> '+ere[1]+' > '+ere[2])
#     else:
#         print(er)