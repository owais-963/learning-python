Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 8+8
16
>>> 9-8
1
>>> 9*8
72
>>> 9/3
3.0
>>> 6*6*6
216
>>> 6**3
216
>>> 2//8
0
>>> 2%54
2
>>> 'owais'
'owais'
>>> "owais ali"
'owais ali'
>>> print("owais ali ap k abbu")
owais ali ap k abbu
>>> print("owais ali's PC")
owais ali's PC
>>> print('owais ali\'s "PC")
      
SyntaxError: EOL while scanning string literal
>>> print('owais ali\'s "PC"')
owais ali's "PC"
>>> 22%54
22
>>> 
================================ RESTART: Shell ================================
>>> 
[DEBUG ON]
>>> 2+8*3
26
[DEBUG ON]
>>> 
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 
>>> 2+8*3
26
>>> (2+8)*3
30
>>> "IT's happen just because python follow the rule of BODMAS"
"IT's happen just because python follow the rule of BODMAS"
>>> print('c:\docs\owais')
c:\docs\owais
>>> print(r'c:\docs\Owais')
c:\docs\Owais
>>> x=2
>>> x3
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    x3
NameError: name 'x3' is not defined
>>> x+3
5
>>> y
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> x+y
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    x+y
NameError: name 'y' is not defined
>>> y=3
>>> x+y
5
>>> y
3
>>> x
2
>>> x-9
-7
>>> x=7
>>> x+y
10
>>> x+10
17
>>> 17+y
20
>>> _+y
23
>>> x+10
17
>>> _+y
20
>>> name='youtube'
>>> name
'youtube'
>>> name+ 'owais'
'youtubeowais'
>>> name' owais'
SyntaxError: invalid syntax
>>> name ' owais'
SyntaxError: invalid syntax
>>> name = ' owais'
>>> name
' owais'
>>> name + ' ali'
' owais ali'
>>> namw[0]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    namw[0]
NameError: name 'namw' is not defined
>>> name[0]
' '
>>> name[1]
'o'
>>> name[2]
'w'
>>> name[3]
'a'
>>> name[4]
'i'
>>> name[5]
's'
>>> name[-6]
' '
>>> name[-1]
's'
>>> name[-5]
'o'
>>> name[-4]
'w'
>>> name[-3]
'a'
>>> name[-2]
'i'
>>> name[-1]
's'
>>> name[0:] + ' ali'
' owais ali'
>>> [:3]
SyntaxError: invalid syntax
>>> name[:6]
' owais'
>>> name[:3]
' ow'
>>> name[:4]
' owa'
>>> name[:5}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> name[:5]
' owai'
>>> name[;6]
SyntaxError: invalid syntax
>>> name[:6]
' owais'
>>> 10*'owais'
'owaisowaisowaisowaisowaisowaisowaisowaisowaisowais'
>>> 10*' owais'
' owais owais owais owais owais owais owais owais owais owais'
>>> nums=[25,58,,8,7,5787,45454]
SyntaxError: invalid syntax
>>> nums=[884,1848,8484,448,484821,4,5498,0,9,7,1,2]
>>> nums
[884, 1848, 8484, 448, 484821, 4, 5498, 0, 9, 7, 1, 2]
>>> name=[owais]
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    name=[owais]
NameError: name 'owais' is not defined
>>> name=['owais' , 'uzair' , 'usaid' 'humaid']
>>> name
['owais', 'uzair', 'usaidhumaid']
>>> name=['Arshad' , 'Shaheen' , 'Owais' , 'Uzair' , 'Usaid' , 'Humaid']
>>> name
['Arshad', 'Shaheen', 'Owais', 'Uzair', 'Usaid', 'Humaid']
>>> values=['owais', 17, ' uzair', 16, 'Usaid' ]
>>> values
['owais', 17, ' uzair', 16, 'Usaid']
>>> mil=[nums+name+values]
>>> mil
[[884, 1848, 8484, 448, 484821, 4, 5498, 0, 9, 7, 1, 2, 'Arshad', 'Shaheen', 'Owais', 'Uzair', 'Usaid', 'Humaid', 'owais', 17, ' uzair', 16, 'Usaid']]
>>> nums.append(80)
>>> nums
[884, 1848, 8484, 448, 484821, 4, 5498, 0, 9, 7, 1, 2, 80]
>>> nums.insert(2,99)
>>> nums
[884, 1848, 99, 8484, 448, 484821, 4, 5498, 0, 9, 7, 1, 2, 80]
>>> nums.pop(2)
99
>>> nums
[884, 1848, 8484, 448, 484821, 4, 5498, 0, 9, 7, 1, 2, 80]
>>> nums.remove(80)
>>> nums
[884, 1848, 8484, 448, 484821, 4, 5498, 0, 9, 7, 1, 2]
>>> nums.clear(2)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    nums.clear(2)
TypeError: clear() takes no arguments (1 given)
>>> nums.sort
<built-in method sort of list object at 0x01119948>
>>> nums
[884, 1848, 8484, 448, 484821, 4, 5498, 0, 9, 7, 1, 2]
>>> nums.sort()
>>> nums
[0, 1, 2, 4, 7, 9, 448, 884, 1848, 5498, 8484, 484821]
>>> nums.sort(2,6)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    nums.sort(2,6)
TypeError: sort() takes no positional arguments
>>> nums.sort(0:6)
SyntaxError: invalid syntax
>>> d