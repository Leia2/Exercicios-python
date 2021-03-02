'''
#Exercício 45
# create a script that generates 26 text files named a.txt,
#  b.txt, and so on up to z.txt. Each file should contain a
#  letter reflecting its filename.

import string, os

if not os.path.exists("letters"):
    os.makedirs("letters")
for letter in string.ascii_lowercase:
    with open("letters/" + letter + ".txt", "w") as file:
        file.write(letter + "\n")

#Exercício 46
#Pegar os dados dos arquivos criados e pegar cada letra e colocar
#na mesma lista em python

import string, glob

alfabeto = []
#Acessando os files no diretório
arq_list  = glob.glob("letters/*.txt")
for  arquivo in arq_list:
    with open(arquivo, "r") as file:
        alfabeto.append(file.read().strip("\n"))
print(alfabeto)


#Exercício 47

#Continuar ttrabalhando com os arquivos do letters
#Verificar se o arquivo em questão está na string "python"
#se sim, salvar a letra em uma lista

import string, glob
letras = []
python_list = []
verifica = "python"
arq_list = glob.iglob("letters/*.txt")
for arquivo in arq_list:
    with open(arquivo, "r") as file:
        letras = file.read().strip("\n")
    if letras in verifica:
        python_list.append(letras)
print(python_list)


#Exercício 48
for letter in "Hello":
    if letter == "e":
        print(letter)

#Exercício 49
#Correção de erro

passsword = input("Please enter your password: ")
print("Seja bem vindo",passsword,"!")

#Exercício 50
#Correção de erro

#OPÇÃO 1
age = input("Wat's your age?")
age_last_year = int(age) - 1
print("Last year you were %s." % age_last_year)

#OPÇÃO 2 
age = int(input("Wat's your age?"))
age_last_year = age - 1
print("Last year you were %s." % age_last_year)

#Exercício 51
#Correção de erro
print(type("Hey".replace("ey", "i")[-1]))

#Exercício 52
#Correção de erro
firstname = input("Enter first name: ")
secondname = input("Enter second name: ")
print("Your first name is %s and your second name is %s" % (firstname, secondname))

#Exercício 53, 54 e 55
#update the dictionary by changing the last name of the second employee 
# from Smith to Smooth

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
#print(d['employees'][1]['lastName'])

#Mudando o sobrenome do employees
d['employees'][1]['lastName'] = "Smooth"
print(d['employees'][1]['lastName'])

#Adicionando um novo employees
d["employees"].append(dict(firstName= "Jessy", lastName= "Petter"))
print(d['employees'])

#Exercício 56 
#Salvando o dicionário em um arquivo json

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

import json
with open("company.json", "w") as file:
    json.dump(d, file, sort_keys=True, indent=4)

#Exercício 57
#Importando um arquivo json

import json
from pprint import pprint
with open("company.json", "r") as file:
    d = json.loads(file.read())
pprint(d)


#Exercício 58
#Importando um arquivo json e adicionando um novo employer
import json 
from pprint import pprint
# r+ : read and write mode
with open("company.json", "r+") as file:
    d = json.loads(file.read())
    d["employees"].append(dict(firstName= "Albert", lastName="Bert"))
    file.seek(0)
    json.dump(d, file, indent=4, sort_keys=True)
    file.truncate()
pprint(d["employees"])

#Exercício 59

a = [1, 2, 3]
for index, item in enumerate(a):
    print("Item %s has index %s" % (item, index))

#Exercício 60
#Prints "Hello" repeatedly.

while True:
    print("Hello")

#Exercício 61
#Create a program that prints out Hello  every two seconds.

import time

while True:
    print("Hello")
    time.sleep(2)

#Exercício 62
# Create a program that once executed the program prints
#  Hello  instantly first, then it prints it after 1 second,
#  then after 2, 3, 4, and so on the interval increases 
# between prints.

import time
i = 0
while True:
    print(i)
    print("Hello")
    i =i + 1
    time.sleep(i)


#Exercício 63
import time
i = 0
while True:
    print(i)
    print("Hello")
    i = i + 1
    if i > 4:
        print("End of the Loop")
        break
    time.sleep(i)

#Exercício 64
while True:
    print("Hello")
    if 2 > 1:
        pass
    print("Hi")

#Exercício 65
while True:
    print("Hello")
    if 2 > 1:
        continue
    print("Hi")


#Exercício 66 e 67

#OPÇÃO 1
d = dict(weather = "clima", earth = "terra", rain = "chuva") 
def traduz(palavra):
    return d[palavra]
palavra = input("Digite uma palavra: ")
if palavra in d.keys():
    print(traduz(palavra))
else:
    print("The word doesn't exist!")

#OPÇÃO 2
d = dict(weather = "clima", earth = "terra", rain = "chuva") 
def traduz(palavra):
    try:
        return d[palavra]
    except KeyError:
        return "That word doesn't exist!"

palavra = input("Digite uma palavra: ")
print(traduz(palavra))

#Exercício 68
d = dict(weather = "clima", earth = "terra", rain = "chuva") 
def traduz(palavra):
    try:
        return d[palavra]
    except KeyError:
        return "That word doesn't exist!"
#Colocando as palavras para minusculo
palavra = (input("Digite uma palavra: ").lower())
print(traduz(palavra))

#Exercício 69
#Teste de request.get()

#Exercício 70 (EXERCÍCIO COM ERRO - BIBLIOTECA)
from requests import*
response = requests.get('http://www.pythonhow.com/data/universe.txt', headers = {'user-agent': 'customUserAgent'})
text = response.text
print(text)

#Exercício 71 (EXERCÍCIO COM ERRO - BIBLIOTECA)
#Count the number of a characters in this text
import requests
response = requests.get("http://www.pythonhow.com/data/universe.txt")
text = response.text
count_a = text.count("a")
print(count_a)


#Exercício 72
#Create a script that the user type in a search term and opens
#and search on the browser for that term on Google
import webbrowser

palavra = input("Enter your Google query:")
webbrowser.open("https://www.google.com/search?q=%s" % palavra)


#Exercício 73
#Create a script that reads this file, multiplies its values
#by to and saves the output in a new text file.

import pandas as pd
data = pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data_2 = data * 2
data_2.to_csv("teste_data_2", index = None)

#Exercício 74
#Concatenate this file with this one to a single text file.

#OPÇÃO 1
import pandas as pd

data1 = pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pd.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")

concatenado = pd.concat([data1, data2], axis=0)
concatenado.to_csv("concatenado_file", index=None)

#OPÇÃO 2import io
import pandas
import requests 
r = requests.get("http://www.pythonhow.com/data/sampledata.txt")
c = r.content
data1 = pandas.read_csv(io.StringIO(c.decode('utf-8')))
data2 = pandas.read_csv("sampledata_x_2.txt")
data12 = pandas.concat([data1, data2])
data12.to_csv("sampledata12.txt", index=None)

#Exercício 75
#Please plot the data of this file into a graph of x and y 
# axis.

import pandas as pd
import pylab as plt

#OPÇÃO 1

data = pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")
x = data['x']
y = data['y']
plt.plot(x, y)
plt.show()

#Opção 2
data = pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data.plot(x = 'x', y='y', kind='scatter')
plt.show()

#Opção 3
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas
 
output_file("bokeh_plot.html")
data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
f = figure()
f.circle(x=data["x"], y=data["y"]) 
show(f)

#Exercício 76
#Make script that prints out the current day, and time. 
from datetime import date

today = date.today()
day = today.strftime("%A %B %d, %Y")
print("Today is %s" % day)

#Exercício 77
from datetime import datetime
idade  = int(input("Qual sua idade?"))
ano_nascimento = datetime.now().year - idade
print("Você nasceu em %s" % ano_nascimento)

#Exercício 78
#Create a program that generates a password of 6 random 
#alphanumeric characters.
import random
characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!?@#$%^&*()"
chosen = random.sample(characters, 6)
password = "".join(chosen)
print(password)

#Exercício 79
#Create a program asks the user to enter a new password and
#check that the submitted password should contain at least 
#one number, one uppercase letter and at least 5 characters.
#If the conditions are generated, print out "Password is fine", otherwise keep prompting the user for a password.

while True:
    psw = input("Enter new password: ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw)>=5:
        print("Password is fine")
        break
    else:
        print("Password is not fine")

#Exercício 80
#Create a script that lets user submit a password until they have satisfied
#three conditions:
#1. Password contains at least one number
#2. Contains one uppercase letter
#3. It is at least 5 chars long
#Give the exact reason why the user has not created a correct password

while True:
    notes = []
    psw = input("Enter new password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 chars long")

    if len(notes) == 0:
        print("Password is fine")
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)
'''
#Exercício 81
#Create a script that lets the user submit a password until they have satisfied
#three conditions:
#1. Password contains at least one number
#2. Contains one uppercase letter
#3. It is at least 5 chars long
#Give the exact reason why the user has not created a correct password
#Before asking for password, ask for username

while True:
    username = input("Enter your name: ")    
    with open('users.txt') as file:
        users = file.readlines()
        users = [i.strip("\n") for i in users]
        
    if username not in users:
        print("Correct Name")
        break        
    else:
        print("Name already exist")
        continue 
while True:
    notes = []
    psw = input("Enter your password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw)<5:
        notes.append("You need at least 5 chars long")
    if len(notes) ==0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)