valor1 = float(input('Digite um valor: \n'))
valor2 = float(input('Digite outro valor: \n'))
operacao = input('Digite uma operação matemática básica\n soma\n subtração\n divisão ou\n multiplicação\n ')


if operacao == 'soma':
    print(f"{valor1} mais {valor2} é: ", valor1 + valor2)
elif operacao == 'subtração':
    print(f'{valor1} menos {valor2} é: ',valor1 - valor2)
elif operacao == 'divisão':
    print(f'{valor1} dividido por {valor2} é: ', valor1 / valor2)
elif operacao == 'multiplicação':
    print(f'{valor1} multiplicado por {valor2} é: ', valor1 * valor2)


