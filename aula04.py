aplicativo = input('Você quer "abrir" ou "fechar" o aplicativo? ')

if aplicativo == 'abrir':
    print('Você abriu o aplicativo')
    print('Aguade alguns instantes ...')
elif aplicativo == 'fechar':
    print('Você fechou o app')
    print('Obrigado por utilizar nosso app')
else:
    print('Você não digitou nem "abrir" nem "fechar"')
    print('Tente novamente!')
