# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Digite um número para exibir seu fatorial: '))  # pede o número
cont = 1  # var contadora
fat = 1
while cont <= n:  # vai de 1 até o número fatorial
    fat *= cont  # multiplica primeiro por 1 depois atualiza o fat com a próx multiplicação
    cont += 1  # adicona 1 ao contador

fatf = 1
for i in range(1, n + 1):
    fatf *= i

print(f'O valor do fatorial de {n} é: {fat} #com while')  # exibe resultados
print(f'O valor do fatorial de {n} é: {fatf} #com for')  # exibe resultados
