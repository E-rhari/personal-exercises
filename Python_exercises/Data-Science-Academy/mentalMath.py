import math
import random


def soma(a, b):
    return a + b


def multiplicacao(a,b):
    return a*b


def divisao(a,b):
    return a/b


random.seed()

quitCodes = ["q", 'quit', 'exit']
operations = ['soma', 'multiplicacao', 'divisao']
operators = {"soma": "+",
             "multiplicacao": "*",
             "divisao": "/"}
commandFunction = None


level = int(input("Quantas casas decimais?\nR: "))

print("Qual operação: ")
for i in operations:
    print(f"- {i}")
operation = input("R:")

corrects = 0
userInput = ""

while userInput != "q":
    maxValue = 10**level

    x = random.randint(maxValue*-1, maxValue)
    y = random.randint(maxValue*-1, maxValue)
    exec(f"commandFunction = {operation}")
    answer = commandFunction(x,y)

    userInput = int(input(f'{x} {operators[operation]} {y} = '))

    if userInput != answer:
        break
