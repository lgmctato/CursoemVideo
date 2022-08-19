#valida o conteúdo digitado

continua = True
if __name__ == '__main__':
    while continua == True:

        v1 = input('Digite algo:')
        # tipo primitivo
        print('O tipo pritivo é: {}'.format(type(v1)))
        print('É espaço ? {}'.format(v1.isspace()))
        print('É ASCII ? {}'.format(v1.isascii()))

        print('É numérico ? {}'.format(v1.isnumeric()))
        print('É decimal ? {}'.format(v1.isdecimal()))
        print('É digito ? {}'.format(v1.isdigit()))
        print('É printable ? {}'.format(v1.isprintable()))
        print('É identifier ? {}'.format(v1.isidentifier()))

        print('É alfabético ? {}'.format(v1.isalpha()))
        print('É alfanumérico ? {}'.format(v1.isalnum()))
        print('Está em maiúsculo ? {}'.format(v1.isupper()))
        print('Está em minúsculo ? {}'.format(v1.islower()))
        print('Está capitalizado ? {}'.format(v1.istitle()))


        continua = bool(input('Deseja continuar ? (True/False) '))

