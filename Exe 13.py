salario = float(input('Qual o seu salário atual ?: '))
aumento = salario*(15/100)
total = salario+aumento

print ('\n \n PARABÉNS VOCÊ GANHOU UM AUMENTO DE 15% NO SEU SALÁRIO \n Seu salário agora é \n R${:.2f}'.format(total))