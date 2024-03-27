"""Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""
opcao = int(input("(1-Binário)\n(2-octal)\n(3-Hexadecimal)\nEscolha a conversão que deseja: "))
numero = int(input("Digite um número: "))

if opcao == 1:
    print(bin(numero)[2:])
elif opcao == 2:
    print(oct(numero)[2:])
elif opcao == 3:
    print(hex(numero)[2:])
else:
    print("Opção não-existente, tente novamente!")
