Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> for n in range(100)
SyntaxError: invalid syntax
>>> for n in range(1,10+1):
	print(random.randint(1,100))

	
81
39
33
18
69
88
43
63
23
78
>>> myPi=["I","love","myself"]
>>> myPi
['I', 'love', 'myself']
>>> print(myPi)
['I', 'love', 'myself']
>>> print(myPi," ");
['I', 'love', 'myself']  
>>> print()

>>> 
>>> print("String is %s",myPi)
String is %s ['I', 'love', 'myself']
>>> 
>>> print("String is",myPi[])
SyntaxError: invalid syntax
>>> print("String is",myPi[0],myPi[1],myPi[2])
String is I love myself
>>> print(myPi);print()
['I', 'love', 'myself']

>>> print(toString(myPi));
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(toString(myPi));
NameError: name 'toString' is not defined
>>>  print("String is",str(myPi))
 
SyntaxError: unexpected indent
>>> print("String is",str(myPi))
String is ['I', 'love', 'myself']
>>> print(str(myPi));print()
['I', 'love', 'myself']

>>> str.join(myPi)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    str.join(myPi)
TypeError: descriptor 'join' requires a 'str' object but received a 'list'
>>> myPi.join()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    myPi.join()
AttributeError: 'list' object has no attribute 'join'
>>> myPishell=["and","my","family"]
>>> myPi.join(myPishell)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    myPi.join(myPishell)
AttributeError: 'list' object has no attribute 'join'
>>> print "-".join(myPi)
SyntaxError: invalid syntax
>>> print "-".join("chull")
SyntaxError: invalid syntax
>>> str="abc"
>>> str2="def"
>>> str.join(str2)
'dabceabcf'
>>> "-".join(str)
'a-b-c'
>>> "-".join(myPi)
'I-love-myself'
>>> " ".join(myPi)
'I love myself'
>>> print(" ".join(myPi))
I love myself
>>> print(myPi.str())
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(myPi.str())
AttributeError: 'list' object has no attribute 'str'
>>> print(" ".str(myPi))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(" ".str(myPi))
AttributeError: 'str' object has no attribute 'str'
>>> str(myPi)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    str(myPi)
TypeError: 'str' object is not callable
>>> myPi.str()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    myPi.str()
AttributeError: 'list' object has no attribute 'str'
>>> strg=" ".join(myPi);
>>> print(strg.str());
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(strg.str());
AttributeError: 'str' object has no attribute 'str'
>>> print strg
SyntaxError: Missing parentheses in call to 'print'
>>> print((strg)

      ;
      
SyntaxError: invalid syntax
>>> print(strg);
I love myself
>>> print("string is {myPi}")
string is {myPi}
>>> f'string is{myPi}'
SyntaxError: invalid syntax
>>> f'string is{strg}'
SyntaxError: invalid syntax
>>> f'string is {strg}'
SyntaxError: invalid syntax
>>> f"string is {strg}"
SyntaxError: invalid syntax
>>> 
