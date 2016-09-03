'''
Created on 3 de set de 2016

@author: Netthacker
'''
name = ""
brute= 0
liquid = 0
discount = 0
while True:
    try:
        name = str(input('Escreva seu nome: '))
        while True:
            try:
                brute = float(input('Digite o seu salário bruto R$ '))
                break
            except:
                print('Somente números !')
        discount = (5*brute)/100
        liquid = brute - discount
        break
    except:
        print('Valores inválidos')

print('%s'%(name))
print('Seu salário bruto é de R$%.2f'%(brute))
print('Seu desconto foi de: R$%.2f'%(discount))
print('Seu salário líquido é de: R$%.2f'%(liquid))