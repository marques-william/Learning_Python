# Calculadora Python #
choice = 'S'
while choice == 'S':
    print('-' * 60)
    print('+                       Calculadora                        +')
    print('-' * 60)
    print('[1]Adição')
    print('[2]Subtração')
    print('[3]Multiplicação')
    print('[4]Divisão')
    print('[5]Módulo(resto da divisão)')
    print('[6]Número²')
    print('[7]Número³')
    print('[8]Raiz² do número')
    print('[9]Raiz³ do número')
    print('-' * 60)
    opc = input('Selecione uma das opções acima para calcular: ')
    if opc == '1':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite outro número: '))
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma:.2f}.')
        choice = input('Deseja realizar outra operação?[S/N] ')
    elif opc == '2':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite outro número: '))
        subt = n1 - n2
        print(f'A subtração de {n1} por {n2} é {subt:.2f}.')
        choice = input('Deseja realizar outra operação?[S/N] ')
    elif opc == '3':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite outro número: '))
        mult = n1 * n2
        print(f'A multiplicação de {n1} por {n2} é {mult:.2f}.')
        choice = input('Deseja realizar outra operação?[S/N] ')
    elif opc == '4':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite outro número: '))
        divs = n1 / n2
        print(f'A divisão de {n1} por {n2} é {divs:.2f}.')
        choice = input('Deseja realizar outra operação?[S/N] ')
    elif opc == '5':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite outro número: '))
        modl = n1 % n2
        print(f'O módulo de {n1} por {n2} é {modl:.2f}.')
        choice = input('Deseja realizar outra operação?[S/N] ')
    elif opc == '6':
        n = float(input('Digite o número: '))
        nmqd = n ** 2
        print(f'{n}² é {nmqd:.2f}.')
        choice = input('Deseja realizar outra operação?[S/N] ')
    elif opc == '7':
        n = float(input('Digite o número: '))
        nmcb = n ** 3
        print(f'{n}² é {nmcb:.2f}.')
        choice = input('Deseja realizar outra operação?[S/N] ')
    elif opc == '8':
        n = float(input('Digite o número: '))
        raiz = n ** (1/2)
        print(f'A raiz² de {n}, é {raiz:.3f}.')
        choice = input('Deseja realizar outra operação?[S/N] ')
    elif opc == '9':
        n = float(input('Digite o número: '))
        raiz = n ** (1/3)
        print(f'A raiz³ de {n}, é {raiz:.3f}.')
        choice = input('Deseja realizar outra operação?[S/N] ')
print('Até mais!')
