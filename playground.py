'''
tuple = 'a', 'b', 'c', 'd', 'e'
print (tuple)

a = lambda x,y : x+y

print(a(5, 6))


import array as arr
My_Array=arr.array('i',[1,2,3,4,5])
My_Array[::-1]
print (My_Array[::-1])


from random import shuffle
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)
print(x)

stg='ABCD'
print(stg.lower())

print(stg.lower().capitalize())


print(dir(x))
print (help(tuple))

dict={'Country':'India','Capital':'Delhi','PM':'Modi'}
print (dict['Country'])
print (dict['Capital'])
print (dict['PM'])

# ternarn_operator
x, y = 22, 50
big = x if x < y else y
print(big)


def show_args(* args, ** kwargs):
   for a in args:
      print(type(a))

show_args(1,2,3,"nevim", [1,2], {}, (1, 2, 3))

import string

veta='je to pravda ?'
split_list = veta.split()
print(type(split_list))
print (type(veta.split()))
print(veta.replace('pravda', 'lež'))

import array as arr

a=arr.array('d', [1.1 , 2.1 ,3.1] )
a.append(3.4)
print(a)
a.extend([4.5, 6.3, 6.8])
print(a)
a.insert(2, 3.8)
print(a)


class Employee:
   def __init__(self, name):
      self.name = name

E1=Employee("abc")
print(E1.name)
'''
# monkey watching
class MyClass:
   public
   def f(self):
      print ("f()")


def monkey_f(self):
   print ("monkey_f()")

MyClass.f = monkey_f
obj = MyClass()
obj.f()

