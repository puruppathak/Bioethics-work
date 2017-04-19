import re


str1 = 'VER001-4 is in DUR001-301 and also A8841004 but 3 is not 5'
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

'''
tuples = re.findall(r'(\w+)@', str)
# If-statement after search() tests if it succeeded
print (tuples)  ## [('alice', 'google.com'), ('bob', 'abc.com')]

for tuple in tuples:
    print (tuple[0])  ## username
    print (tuple[1])
    '''

tuples = re.findall(r'[A-Z0-9-]+', str1)
#tuples1 = re.findall(r'[A-Z0-9]+',str1)
for tuple in tuples:
    if len(tuple)>1:
        print(tuple)

#print (tuples)