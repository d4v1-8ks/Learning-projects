print('Sempre digite "S" para sim e "N" para não')

pai = input('Digite o nome de seu pai: ')
mae = input('Digite o nome de sua mãe: ')
tem_irmaos = input('Você tem irmão ou irmã?: ')

if tem_irmaos == 'S' or 's':
    irmao1 = input('Digite o nome do seu irmão(a): ')
    tem_mais_irmao = input('Você tem mais irmãos?: ')
    if tem_mais_irmao == 'S' or 's':
        irmao2 = input('Qual o nome de seu outro irmão?: ')


letra = input('Quantos da familia tem a letra: ')

if letra in pai and mae and irmao1 and irmao2:
    print('Esta letra está presente em 4 nomes diferentes da familia')
elif letra in (pai and mae) or (pai and irmao1) or (irmao1 and irmao2) or (pai and irmao2) or (mae and irmao2):
    print('Esta letra está em 2 nomes da familia')
