valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))


if valor1 > valor2:
    print(f'{valor1} é maior que {valor2}')
elif valor1 < valor2:
    print(f'{valor2} é maior que {valor1}')
elif valor1 == valor2:
    print('Os valores são iguais')
else:
    print('Valor irreconhecido')
