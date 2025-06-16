''' Variable is nothing but storing the value
 
variable starts with alphabets or _ not intergers and special characters
python is a case sensitive

a=20
a is variable
20 is value


'''
'''
c=10
print(c)
#output is 10

a,b,c=10
print(a,b,c)
# output is TypeError: cannot unpack non-iterable int object


a,b,c=10,1,2
print(a,b,c)
# output is TypeError: cannot unpack non-iterable int object'

'''

'''

a=b=c=20
print(a)
#output is 20

a=b=c=20
print(a,b,c)
#output is 20 20 20

'''
abc=25
ABC=50
print(abc)
#output is 25

abc=25
ABC=50
print(ABC)
#output is 50

abc=40
print(id(abc))
# ouput is 140716600133768(id is nothing but memory location of variable)