'''
Strings:collection of characters
we can decalring string into 3 ways
1.single quote---'ab'/in single quote we can't use ' this
2.double quotes---"ab"/in double quotes we can use ' this
3.triple quotes---''' ''' /this triple quotes we can write multiple lines


methods of strings
Lower()--lower case
Upper()--upper case
ends with()
strats with()
repalce()
split()--string change to list
count()--count of letters/words
Rstrip()-remove right side of word
Lstrip()--Remove left side of word
strip()--remove extra space in the words
removeprefix()
removesuffix()
Index()--word index/if no word is there o/p is error
Find()--word index/if no word is there o/p is -1


'''

#Lower()
'''
pythonlife="MOUNIKA SANNIBOYINA"
print(pythonlife.lower())
o/p--mounika sanniboyina
'''
#upper()
'''
pythonlife="mounika sanniboyina"
print(pythonlife.upper())
#o/p--MOUNIKA SANNIBOYINA'
'''
#endswith()
'''
python="mounika sanniboyina"
print(python.endswith('a'))
print(python.endswith('sanniboyina'))
#o/p--True

'''
#startswith()
'''
python="mounika sanniboyina"
print(python.startswith('m'))
#print(python.startswith('mounika'))
o/p-- True
'''
#replace()
'''
python="mounika sanniboyina"
print(python.replace('sanniboyina','mokka'))
o/p--mounika mokka
'''

#split()
python="mounika sanniboyina"
print(python.split())
#o/p--['mounika', 'sanniboyina']

python="mounika sanniboyina"
print(python.count('n'))
#o/p-- 4

#removeprefix()
python="mounika sanniboyina"
print(python.removeprefix('mounika'))
#o/p--sanniboyina

#removesuffix()
python="mounika sanniboyina"
print(python.removesuffix('sanniboyina'))
#o/p is mounika 

#Lstrip()
python="   mounika sanniboyina   "
print(python.lstrip())
#o/p--mounika sanniboyina

#rstrip
python="   mounika sanniboyina    "
print(python.rstrip())
#o/p--    mounika sanniboyina

#strip()
python="   mounika sanniboyina    "
print(python.strip())
#o/p --mounika sanniboyina


#index()
python="   mounika sanniboyina    "
print(python.index('mounika'))
#o/p -- 3

'''
python="   mounika sanniboyina    "
print(python.index('bhanu'))
#o/p -- error
'''

#find
python="   mounika sanniboyina    "
print(python.find('mounika'))
#o/p--3


python="   mounika sanniboyina    "
print(python.find('bhanu'))
#o/p---1