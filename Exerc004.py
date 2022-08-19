#valida o conteúdo digitado

continua = True
if __name__ == '__main__':
    while continua == True:

        v1 = input('Digite algo:')

        #tipo primitivo
        print('O tipo pritivo é: {}'.format(type(v1)))

        if v1.isspace() == True:
            print('É espaço ? {}'.format(v1.isspace()))
        else if v1.isnumeric() == True:
            print('É numérico ? {}'.format(v1.isnumeric()))

        else:
            print('É alfabético ? {}'.format(v1.isalpha()))
            print('É alfanumérico ? {}'.format(v1.isalnum()))
            print('É maiúsculo ? {}'.format(v1.isupper()))
            print('É minúsculo ? {}'.format(v1.islower()))

    continua = bool(input('Deseja continuar ? (True/False) '))


