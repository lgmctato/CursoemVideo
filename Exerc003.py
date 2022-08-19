
#tipos primitivos

#int()
ok = False
if __name__ == '__main__':
    while ok == False:
        ni1 = input('Digite 1o número inteiro:')
        ni2 = input('Digite 2o número inteiro:')
        print('Tipo 1 é numérico ? {} e Tipo 2 é numérico: {}'.format(ni1.isnumeric(), ni2.isnumeric()))
        if ni1.isnumeric() == True:
                if ni2.isnumeric() == True:
                    ok= True
                    print('Tipos corretos. A soma é: {}!'.format(int(ni1)+int(ni2)))


    #float
    fl1 = float(input('Digite 1o número decimal:'))
    fl2 = float(input('Digite 2o número decimal:'))
    print('Tipo 1: {}!'.format(type(fl1)))
    print('Tipo 2: {}!'.format(type(fl2)))
    print('A soma é: {}!'.format(fl1+fl2))

    #boleano
    b1 = bool(input('Digite 1o True ou False:'))
    b2 = bool(input('Digite 2o True ou False:'))
    print('Tipo 1: {}!'.format(type(b1)))
    print('Tipo 2: {}!'.format(type(b2)))
    print('A soma é: {}!'.format(b1+b2))

    #str
    s1 = str(input('Digite 1o número que será tratado como texto:'))
    s2 = str(input('Digite 2o número que será tratado como texto:'))
    print('Tipo 1: {}!'.format(type(s1)))
    print('Tipo 2: {}!'.format(type(s2)))
    print('A concatenação das variáveis é: {}!'.format(s1+s2))

