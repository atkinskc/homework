Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> word = 'banana'
>>> count = 0
>>> for letter in word:
	if letter == 'a':
		count = count + 1

		
>>> print(count)
3
>>> word = 'banana'
>>> print(count('a'))

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(count('a'))
TypeError: 'int' object is not callable
>>> word = 'banana'
>>> print(count('a')in('banana'))

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(count('a')in('banana'))
TypeError: 'int' object is not callable
>>> count('a').print('banana')
SyntaxError: invalid syntax
>>> print(count('a'))

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(count('a'))
TypeError: 'int' object is not callable
>>> print(word.count('a'))
3
>>>  
