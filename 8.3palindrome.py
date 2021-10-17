Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'
>>> def is_palindrome
SyntaxError: invalid syntax
>>> def is_palindrome:
	
SyntaxError: invalid syntax
>>> def is_palindrome(word):
	print word == word[::-1]
	
SyntaxError: Missing parentheses in call to 'print'
>>> def is_palindrome(word):
	print (word) ==word[::-1]

	
>>> is_palindrome('banana')
banana
>>> is_palindrome(banana)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    is_palindrome(banana)
NameError: name 'banana' is not defined
>>> def is_palindrome(word):
	print (string)==word[::-1]

	
>>> is_palindrome(word)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    is_palindrome(word)
NameError: name 'word' is not defined
>>> is_palindrome('word')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    is_palindrome('word')
  File "<pyshell#13>", line 2, in is_palindrome
    print (string)==word[::-1]
NameError: name 'string' is not defined
>>> print(is_palindrome('allen'_
		    
SyntaxError: invalid syntax
>>> print(is_palindrome('allen')
def is_palindrome(word):
      
SyntaxError: invalid syntax
>>> def is_palindrome(word):
	print (word) == word[::-1]

	
>>> print(is_palindrome('allen'))
allen
None
>>> print(is_palindrome('kennedy'))
kennedy
None
>>> 
