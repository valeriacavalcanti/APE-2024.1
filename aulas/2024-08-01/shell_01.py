Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
v1 = [10,20,30,40,50,60]
v1
[10, 20, 30, 40, 50, 60]
len(v1)
6
v1[0]
10
v1[5]
60
v1[6]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    v1[6]
IndexError: list index out of range
>>> type(v1)
<class 'list'>
>>> v2 = [1, 'Davi', 54000.32, True]
>>> v2
[1, 'Davi', 54000.32, True]
>>> v2[2] = 100000
>>> v2
[1, 'Davi', 100000, True]
>>> type(v2)
<class 'list'>
>>> type(v2[0])
<class 'int'>
>>> type(v2[1])
<class 'str'>
>>> v3 = [0] * 10
>>> type(v3)
<class 'list'>
>>> len(v3)
10
>>> v3
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> v4 = [10,20,30,40,50,60] * 2
>>> v4
[10, 20, 30, 40, 50, 60, 10, 20, 30, 40, 50, 60]
