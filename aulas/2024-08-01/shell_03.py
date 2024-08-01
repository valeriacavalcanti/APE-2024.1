Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> v = [10,20,10,30,10,40]
>>> v
[10, 20, 10, 30, 10, 40]
>>> v.pop()
40
>>> v
[10, 20, 10, 30, 10]
>>> v.remove(10)
>>> v
[20, 10, 30, 10]
>>> v.remove(10)
>>> v
[20, 30, 10]
>>> v.remove(10)
>>> v
[20, 30]
>>> v.remove(10)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    v.remove(10)
ValueError: list.remove(x): x not in list
>>> 
=== RESTART: Z:/1744888/Documents/ape20241/20240801/exemplo04.py ==
[8, 7, 10, 7, 1, 3, 4, 2, 5, 8]
