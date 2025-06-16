'''Data types are 
int,float,boolean,string,complex
List[],Tuple(),Set{},Dictonary{}
Frozen set,none'''

a=1
b="2"
c=1+3j
d=True
print(type(a),type(b),type(c),type(d))# by using type we can find out the datatype of a value
#o/p  <class 'int'> <class 'str'> <class 'complex'> <class 'bool'>


#Type Conversion 
''' Type conversion means it will convert the one datatype to another datatype
built-in methods
1.int()
2.str()
3.float()
4.bool()

Data loss-explicit type conversion ex: 
no Data loss- implicit conversion
'''
#implicit type conversion(no data loss)
a=2
print(float(a))
#o/p 2.0


#explicit type conversion(data loss)
a=5.6
print(int(a))

# o/p is 5

