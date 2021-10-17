Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def first(word):
	return word[0]

>>> def last(word):
	return word[-1]

>>> def middle(word):
	return word[1:-1]

>>> middle('lol')
'o'
>>> middle('a')
''
>>> middle('')
''
>>> def is_palindrome
SyntaxError: invalid syntax
>>> def is_palindrome:
	
SyntaxError: invalid syntax
>>> def is_palindrome(word):
	if len(word) <1:
		return True
	if first(word)!= last(word):
		return False
	return is_palindrome(middle(word))

>>> print(is_palindrome('allen'))
False
>>> print(is_palindrome('lol'))
True
>>> 
