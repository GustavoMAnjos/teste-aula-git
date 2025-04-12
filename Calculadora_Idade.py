from datetime import datetime

nascimento_str = input('Insira sua data de nascimento no formato dd/mm/aaaa:')

try:
    nascimento = datetime.strptime(nascimento_str, r'%d/%m/%Y')
    hoje = datetime.today()

    idade = hoje.year - nascimento.year

    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1

    print(f'Você tem {idade} anos de idade')

    diferença = hoje - nascimento
    dias = diferença.days
    meses = dias // 30

    print(f'\nVeja sua idade em meses e em dias:\nVocê tem {meses} meses de idade ou {dias} dias')

except ValueError:
    print('Formato inválido! Use dd/mm/aaaa (incluindo as barras, ex: 20/02/2005)')
