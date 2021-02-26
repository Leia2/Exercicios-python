'''
a = 2
a = 4
a = 6
print(a + a + a)

#Exercício 4

a = "1"
b = 2
print(int(a) + b) 

#Exercício 5 e 6

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[3:6])

#Exercício 7
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[:3])


#Exercício 8
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[-2])

#Exercicio 9
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[-3:])

#Exercício 10
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
#list slicing is [start:end:step]
print(letters[::2])

#Exercicio 11
meu_intervalo = range(1,21)
print(list(meu_intervalo))

#Exercício 12
meu_intervalo = range(10,201, 10)
print(list(meu_intervalo))


#Exercício 13
meu_intervalo = range(1,21)
print(list(map(str,meu_intervalo)))

#Exercício 14
a = ['1', 1, '1', 2]
#Opçao 1
print('Opção 1')
print(list(set(a)))

#Opção 2 - muito lenta se houver muitos dados
print('Opção 2')
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)

#Opção 3
print('Opção 3')
from collections import OrderedDict
a = list(OrderedDict.fromkeys(a))
print(a)

#Exercício 15
print('Opção 1')
meu_dict = dict(a = 1, b= 2)
print(meu_dict)
print('%%%%%%%%%%%%%%%%')
print('Opção 2')
my_dict = {"a":1, "b": 2}
print(my_dict)

#Exercício 16
meu_dict = dict(a = 1, b= 2)
print(meu_dict["b"])

#Exercício 17, 18 e 19
meu_dict = {"a":1, "b":2, "c":3}
#print(meu_dict["a"] + meu_dict["b"])
meu_dict["c"] = 3
print(meu_dict)

#Exercício 20
meu_dict = {"a":1, "b":2, "c":3}
print(sum(meu_dict.values()))

#Exercício 21
#Usando dictionary comprehension
meu_dict = {"a":1, "b":2, "c":3}
meu_dict = dict((key, value) for key, value in meu_dict.items() if value <=1)
print(meu_dict)

#Exercício 22
#Create a dictionary of keys a, b, c where each key has as value a list from 1 to 10, 11 to 20, and 21 to 30 respectively and print out.
dict_22 = {"a": list(range(1,10)),
"b": list(range(11,20)), "c":list(range(21,30))}
print(dict_22)

#Exercício 23 e 24
from pprint import pprint
dict_23 = dict(a= list(range(1,11)), b=list(range(11,21)), c=list(range(21,31)))
#print(dict_23)
#print(dict_23['b'][2])
for key, value in dict_23.items():
    print(key, "has values", value)

#Exercício 25
#Make a script that prints out letters of English alphabet 
#from a to z
import string
for letter in string.ascii_lowercase:
    print(letter)

#Exercício 26
for num in range(1,11):
    print(num)


#Exercício 27
def aceleration(v1, v2, t1, t2):
    a = (v2 - v1) / (t2-t1)
    return a

print(aceleration(0,10,0,20))

#Exercício 28
#Resolvendo erro
import math
def foo(a,b):
    return a + b

x = foo(2,3) * 10
print(x)

#Exercício 29
#Calcular o volume líquido da esfera
from math import pi
def volume(h, r=10):
    v = (4 * pi * r**3)/3 - (pi *h**2 *(3*r - h))/3
    return lv

print(volume(2))

#Exercício 30
def foo(b, a=2):
    return a + b
print(foo(4))

#Exercício 31 
def foo(a=1 , b=2):
    return a + b

x = (foo() -1)
print(x)

#Exercício 34

def foo():
    global c 
    c = 1
    return c  
foo()
print(c)

#Exercício 35
#Create a function that takes any string as input 
#and returns the number of words for that string
def number_words(words):
    list_words = words.split()
    return len(list_words)

print(number_words("Hey, how are you dear?"))

#Exercício 36
# create a Python function that takes a text file as input 
# and returns the number of words contained in the text file.

def count_words(filename):
    with open(filename, 'r') as file:
        obj = file.read()
        list_obj = obj.split()
        return len(list_obj)

print(count_words("original.txt"))

#Exercício 37

#PRIMEIRA OPÇÃO

def count_words2(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    text = text.replace(",", " ")
    string_list = text.split(" ")
    return len(string_list)      

print(count_words2("original2.txt"))

#SEGUNDA OPÇÃO
import re

def count_words_re(filename):
    with open(filename, 'r') as file:
        text = file.read()
    string_list = re.split(",| ", text)
    return len(string_list)

print(count_words_re("original2.txt"))

#Exercício 38
import math
print(int(math.sqrt(9)))

#Exercício 39
import math
print(math.cos(1))

#Exercício 40
import math
print(math.pow(2,3))

#Exercício 41
#Create a script that generates a text file with all letters
# of English alphabet inside it, one letter per line.
import  string
with open("letter.text", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")


#Exercício 42
a = [1, 2, 3]
b = (4, 5, 6)
for i, j in zip(a,b):
    print(i + j)


#Exercício 43
import string
with open("letters2.txt", "w") as file:
    for letter1, letter2 in zip(string.ascii_lowercase[0::1], string.ascii_lowercase[1::2]):
        file.write(letter1 + letter2 + "\n")



#Exercício 44
#Create a script that generates a file where all letters of English
# alphabet are listed three in each line.

#OPÇÃO 1
import string
with open("letters3.txt", "w") as file:
    for letter1, letter2, letter3 in zip(string.ascii_lowercase[0::1], string.ascii_lowercase[1::2], string.ascii_lowercase[2::3]):
        file.write(letter1 + letter2 + letter3 + "\n")

#OPÇÃO 2

import string

letters = string.ascii_lowercase + " "

slice1 = letters[0::3]
slice2 = letters[1::3]
slice3 = letters[3::3]

#Criando o arquivo 
with open("letters4", "w") as file:
    for s1, s2, s3 in zip(slice1, slice2, slice3):
        file.write(s1 + s2 + s3 + "\n")
'''


