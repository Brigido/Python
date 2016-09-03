'''
Created on 3 de set de 2016

@author: Netthacker
'''

#Definindo as variáveis
x = int(input('Digite o número de x: '))
n = int(input('Digite o número n: '))
exp = 3
sinal = -1
sen= x
cont=1
#definido cont como o contador.
while cont < n:
    fat = 1
    #Numerador é elevado ao exp, sendo exp = 3
    numerador = (x**exp)
    # para i começando em 1 e indo até o exp 3, temos o fatorial
    for i in range(1,exp+1):
        fat *=i
    #O seno do número é o numerador/ fatorial *sinal para gera a mudança de sinal.
    sen += (numerador/fat)*sinal
    #após isso, o sinal vai mudar, o contador também e o expoente tbm nas linhas seguintes
    sinal*= -1
    cont+=1
    exp+=2
print('Sen(%d) é = %.2f'%(x,sen))