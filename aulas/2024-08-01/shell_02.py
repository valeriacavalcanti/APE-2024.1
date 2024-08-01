Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=== RESTART: Z:/1744888/Documents/ape20241/20240801/exemplo03.py ==
<class 'list'>
6
[11, 3, 5]
[2, 4, 6]
[1, 3, 5, 2, 4, 6]
[11, 3, 5]
>>> v8 = []
>>> v8
[]
>>> type(v8)
<class 'list'>
>>> len(v8)
0
>>> v9 = [] * 100000000000000000
>>> v9
[]
>>> v9.append(10)
>>> v9
[10]
>>> v9.append(20)
>>> v9
[10, 20]
v9.append(30)
v9
[10, 20, 30]
