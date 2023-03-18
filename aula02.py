# Mostrar na tela as informções pedidas e calcular o seu IMC

nome = input('Qual é o seu nome? ')
altura = float(input('Quanto você mede em metros? '))
peso = float(input('Quanto você pesa em kg? '))
imc = peso / altura ** 2

# Fala seu imc e como ele está em relação a tabela de imc

print(f'Olá {nome}, \nVocê mede {altura}m, \nPesa {peso}kg \n\nEntão seu IMC é de {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso, fale com um nutricionista e melhore sua alimentação')
elif imc >= 18.5 and imc <= 24.9:
    print('Seu peso está normal')
    print('-'*30, 'Parabéns, continue assim', '-'*30)
elif imc >= 25 and imc <= 29.9:
    print('Você está com excesso de peso, fale com um nutricionista e melhore sua alimentação')
elif imc >= 30 and imc <= 34.9:
    print('!'*10, 'Você está com Obesidade classe 1, procure um profissional da saúde', '!'*10)
else:
    print('Você está muito acima do peso, procure um profissional da saúde urgente')
