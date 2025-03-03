from funcoes import *

eh_True = True
print(18 * '*', 'Calculadora Python', 18 * '*')

print('\nESCOLHA UMA DAS OPÇÕES')

print('Opção 1 - Soma\n'
      'Opção 2 - Subtração\n'
      'Opção 3 - Divisão\n'
      'Opção 4 - Multiplicação\n')

while eh_True:
    opcao = int(input('Escolha uma das opções de operação: '))

    if opcao == 1:
        num1 = float(input('Escolha o primeiro numero: '))
        num2 = float(input('Escolha o segundo numero: '))

        resultado = soma(num1, num2)
        print(resultado)

    if opcao == 2:
        num1 = float(input('Escolha o primeiro numero: '))
        num2 = float(input('Escolha o segundo numero: '))

        resultado = subtracao(num1, num2)
        print(resultado)

    if opcao == 3:
        num1 = float(input('Escolha o primeiro numero: '))
        num2 = float(input('Escolha o segundo numero: '))

        resultado = divisao(num1, num2)
        print(resultado)

    if opcao == 4:
        num1 = float(input('Escolha o primeiro numero: '))
        num2 = float(input('Escolha o segundo numero: '))

        resultado = multiplicacao(num1, num2)
        print(resultado)

    if opcao not in (1, 2, 3, 4):
        print('Por favor, digite uma opção válida!!!')

    continuar = input('Deseja continuar? (S/N): ').upper()

    if continuar in 'Nn':
        break

print('------- OBRIGADO POR USAR A CALCULADORA! -------')
