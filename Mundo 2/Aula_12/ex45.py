import random
from time import sleep as slp

print('\033[1;31m-'*16,'\033[4;33mJokenpô\033[m','\033[1;31m-\033[m'*17)

ppt = ['pedra','papel','tesoura']
rppt = random.choice(ppt)

esc = str(input('\033[0;33mEscreve pedra, papel ou tesoura: ')).strip().lower()
print('\033[1;31m-'*42)
slp(1)
if esc not in ['pedra', 'papel', 'tesoura']:
   print('\033[1;31mPara jogares deves escrever pedra, papel ou tesoura!')
else:
    print('\033[1;4;31;43m','Vamos Jogar'.center(40),'\033[m\033[1;31m')
    slp(3)
    print(f'Pedra'.center(42),'\033[m\033[1;31m')
    slp(1)
    print(f'Papel'.center(42),'\033[m\033[1;31m')
    slp(1)
    print(f'Tesoura'.center(42),'\033[m')
    slp(1)
    print('\033[1;31m-'*42)


    if rppt == 'pedra':
        print('\033[1;33mEu escolhi\033[1;31m Pedra')
        if esc == 'pedra':
            print('\033[1;33mEu escolhi\033[1;31m Pedra\033[1;33m. Empatamos!')

        elif esc == 'tesoura':
            print(f'\033[1;33mEu escolhi\033[1;34m Pedra\033[1;33m.\033[1;31m PERDESTE! \033[1;33mA\033[1;34m Pedra\033[1;33m ganha da \033[1;34m Tesoura\033[1;33m!')

        elif esc == 'papel':
            print(f'\033[1;33mEu escolhi\033[1;34m Pedra\033[1;33m.\033[1;32m GANHASTE! \033[1;33mO\033[1;34m Papel\033[1;33m ganha da \033[1;34m Pedra\033[1;33m!')

        else:
            print()


    elif rppt == 'papel':
        print('\033[1;33mEu escolhi\033[1;31m Papel')
        if esc == 'papel':
            print('\033[1;33mEu escolhi\033[1;31m Papel\033[1;33m. Empatamos!')

        elif esc == 'pedra':
            print(f'\033[1;33mEu escolhi\033[1;34m Papel\033[1;33m.\033[1;31m PERDESTE! \033[1;33mO\033[1;34m Papel\033[1;33m ganha da \033[1;34m Pedra\033[1;33m!')

        elif esc== 'tesoura':
            print(f'\033[1;33mEu escolhi\033[1;34m Papel\033[1;33m.\033[1;32m GANHASTE! \033[1;33mA\033[1;34m Tesoura\033[1;33m ganha do \033[1;34m Papel\033[1;33m!')

        else:
            print()

    elif rppt == 'tesoura':
        print('\033[1;33mEu escolhi\033[1;31m Tesoura')
        if esc == 'tesoura':
            print('\033[1;33mEu escolhi\033[1;31m Tesoura\033[1;33m. Empatamos!')

        elif esc == 'papel':
            print(f'\033[1;33mEu escolhi\033[1;34m Pedra\033[1;33m.\033[1;31m PERDESTE! \033[1;33mA\033[1;34m Tesoura\033[1;33m ganha do \033[1;34m Papel\033[1;33m!')

        elif esc == 'pedra':
            print(f'\033[1;33mEu escolhi\033[1;34m Pedra\033[1;33m.\033[1;32m GANHASTE! \033[1;33mA\033[1;34m Pedra\033[1;33m ganha da \033[1;34m Tesoura\033[1;33m!')
        else:
            print()
    else:
        print()
