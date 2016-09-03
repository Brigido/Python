'''
Created on 3 de set de 2016

@author: Netthacker
'''
print('Programa que soma os pares e multiplica os impares ')
print('Digite 9999 para sair')
num = 0
par = 0
impar = 0
somapar = 0
produtoimpar = 1
entrada = 9999
while True:
        while True:
            try:
                num = int(input('Digite um número: '))
                break
            except:
                print('Somente números')
        if num == 9999:
            break
            
        if num %2 == 0:
            somapar+=num
            par+=1
        else:
            impar+=1
            produtoimpar*=num
print('A soma dos números pares: %d'%(somapar))
print('O produto dos números ímpares é: %d'%(produtoimpar))
if impar ==0:
    print('Não há números ímpares')
if par ==0:
    print('Não há números pares')
