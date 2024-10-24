# faça um programa que leia dados do usuario
questao =int(input('Digite um numero 1 ou 2 '))
if(questao == 1):
 nome = input('nome ')
 sobrenome = input('sobrenome ')
 idade = int(input('idade '))
 listaA = [nome, sobrenome, idade]
 print(listaA[2])


# Faça um programa onde o usuario informa um numero de 1 a 12 em seguida imprima qual mes que se refere
else: 
    
 listames = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
 n = int(input('Digite um número de 1 a 12 referente ao mes '))
 n = n - 1

print(listames[n])


#extra: Faça um menu onde o usuario consiga selecionar qual questao quer executar

