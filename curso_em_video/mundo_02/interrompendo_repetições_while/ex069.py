# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

mais18 = qtd_homens = fem_menos_20 = 0
while True:
    # pede idade
    idade = int(input('Digite sua idade: '))
    if idade > 18:
        mais18 += 1  # add +1 a cada > 18 anos
    # pede sexo
    sexo = input('Selecione seu sexo [M]/[F]: ').strip().upper()[0]
    if sexo == 'M':
        qtd_homens += 1  # Se do sexo masc +1
    # adiciona aos contadores se mulher menor de 20 anos
    if idade < 20 and sexo == 'F':
        fem_menos_20 += 1
    # pergunta se quer continuar
    opc = input('Deja continuar? [S/N]:').strip().upper()[0]
    while opc not in 'SN':
        opc = input('Deja continuar? [S/N]:').strip().upper()[0]
    if opc == 'N':
        break

# A: quantas tem mais de 18 anos
print(f'{mais18} desta lista tem mais de 18 anos.')

# B: Quantos homens foram cadastrados
print(f'Foram cadastrados {qtd_homens} homens.')

# C: Quantas mulehres tem menos de 20 anos
print(f'{fem_menos_20} mulheres da lista tem menos de 20 anos.')
