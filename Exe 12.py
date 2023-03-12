valor = float(input('Digite o valor do produto: '))
desconto = valor*(5/100)
total = valor-desconto

print ('Você ganhou um desconto de 5%, o preço agora é R${:.2f}, \n Você economizou R${:.2f}'.format(total, desconto))
