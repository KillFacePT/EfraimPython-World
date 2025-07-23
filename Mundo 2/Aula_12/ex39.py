from datetime import date
curyear = date.today().year

print('\033[1;31m-'*10,'\033[4;33mCalculadora de Alistamento\033[m','\033[1;31m-\033[m'*10)
birth = int(input('\033[0;33mEscreva o seu ano de nascimento: '))
idd = curyear - birth

print('\033[1;31m-'*48)
if idd >= 18:
    print('\033[1;31m1\033[m \033[33m= \033[32mSim'.center(60))
    print('\033[1;31m2\033[m \033[33m= \033[32mNão'.center(60))
    ynlist = int(input('\033[33mSe já se alistou escreva \033[1;31m1\033[0;33m caso contrario escreva \033[1;31m2\033[33m: '))
    print('\033[1;31m-'*48)

    if ynlist == 1:
        print('\033[32mObrigado \033[33mpor ter cumprido o seu dever militar!')
    elif idd > 18:
        print(f'\033[1;4;31mAtenção!!!\033[0;33m Já deveria ter feito o seu alistamento há \033[1;31m{idd - 18}\033[0;33m {'ano' if idd - 18 < 2 else 'anos'}!')
    else:
        print(f'\033[1;4;31mAtenção!!!\033[0;33m Está na altura de fazer o seu alistamento!')
else:
    print(
        f'\033[1;4;31mAtenção!!!\033[0;33m Faltam \033[1;31m{18 - idd}\033[0;33m {'ano' if idd - 18 < 2 else 'anos'} o seu alistamento!')
