Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import time
>>> time.time()
1634483062.7
>>> time_sec = int(time.time())
>>> print time_sec
1634483101
>>> time_sec/3600
454023
>>> time_sec/86400
18917
>>> epoch = time_sec/86400
>>> print epoch
18917
>>> time_sec//60//60
454023
>>> time_sec//3600
454023
>>> time_sec//(3600*24)
18917
>>> time_sec//(24*60)
1135057
>>> epoch//(3600*24)
0
>>> epoch//3600
5
>>> epoch//60//60
5
>>> time_sec//60//60
454023
>>> time_sec//3600//24
18917
>>> time_sec//3600//60
7567
>>> time_sec//3600//24
18917
>>> epoch//60//60/12
0
>>> epoch//3600
5
>>> time_sec//60//1440
18917
>>> time_sec//1440
1135057
>>> time_sec//3600
454023
>>> time//86400//3600

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    time//86400//3600
TypeError: unsupported operand type(s) for //: 'module' and 'int'
>>> time_sec//86400//3600
5
>>> hour = epoch//3600
>>> epoch//hour/60
63
>>> epoch//hour//60
63
>>> time//hour//60

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    time//hour//60
TypeError: unsupported operand type(s) for //: 'module' and 'int'
>>> time_sec//hour//60
5448277
>>> epoch//hour//60
63
>>> epoch//hour//24
157
>>> epoch//hour*24
90792
>>> epoch//hour*60
226980
>>> time_sec//86400//3600*60
300
>>> time_sec-hour//60
1634483101
>>> epoch-hour//60
18917
>>> epoch*hour//60
1576
>>> epoch*hour//3600
26
>>> minutes = epoch*hour//3600
>>> minutes/60
0
>>> minutes//60
0
>>> minutes*60
1560
>>> minutes*24
624
>>> minutes//60*24
0
>>> minutes//60
0
>>> int(minutes//60)
0
>>> seconds = minutes//60
>>> print ("The current time is: hour, minutes, seconds" and days "since epoch"
       
SyntaxError: invalid syntax
>>> print ("Current time is:", hour, ":",minutes, ":", seconds, ". with", days "since epoch")
SyntaxError: invalid syntax
>>> print ("Current time is",hour,":",minutes,":",seconds,".With",days,"since epoch.")

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print ("Current time is",hour,":",minutes,":",seconds,".With",days,"since epoch.")
NameError: name 'days' is not defined
>>> print ("Current time is",hour,":",minutes,":",seconds,".With",epoch,"since epoch.")
('Current time is', 5, ':', 26, ':', 0, '.With', 18917, 'since epoch.')
>>> print (("Current time is"),hour,":",minutes,":",seconds,".With",epoch,"since epoch.")
('Current time is', 5, ':', 26, ':', 0, '.With', 18917, 'since epoch.')
>>> print "Current time is",hour,":",minutes,":",seconds,".With",epoch,"since epoch."
Current time is 5 : 26 : 0 .With 18917 since epoch.
>>> print ("Current time is",hour,":",minutes,":",seconds,"with",epoch,"since epoch.")
('Current time is', 5, ':', 26, ':', 0, 'with', 18917, 'since epoch.')
>>> print "Current time is",hour,":",minutes,":",seconds,"with",epoch,"since epoch."
Current time is 5 : 26 : 0 with 18917 since epoch.
>>> 
