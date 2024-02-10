"""CALCULADORA COM WHILE"""

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador que será usado (+-/*): ')
    
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são invalidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos: #SE O OPERADOR DIGITADO NÃO ESTIVER ENTRE OS PERMITIDOS...
        print('Operador Inválido!')
        continue

    if len(operador) > 1:   #SE A QUANTIDADE DE OPERADORES FOR MAIR DO QUE 1...
        print('Digite apenas um operador!')
        continue

        ###
    print('Realizando o calculo. Confira o resultado abaixo.')

    if operador == '+':
        print(f'{num_1_float} + {num_2_float}=', num_1_float + num_2_float)
        
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float}=', num_1_float - num_2_float)
        
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float}=', num_1_float / num_2_float)
        
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float}=', num_1_float * num_2_float)
        
    else:
        print('Nunca deveria ter chegado até aqui.')

    sair = input("Deseja sair? [s]im: ").lower().startswith('s')
    #sair = sair.lower() #CONVERTE TUDO QUE FOR ESCRITO EM MAIUSCULO PARA MINUSCULO.
    print(sair)

    if sair is True:
        break

    