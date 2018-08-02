pi = 3.14

def volume_centimetros():
    result = input(print('''
    informações digite:-(1)
    se já entende e deseja ir 
    para a soma digite:-(2)
    '''))
    if result == '1':
        print('''
        ex¹: para você saber o volume do cilindro, você precisa informar o comprimento x altura
             calma é basicamente o seguinte "20x10" o 20 é o tamanho e o 10 é a altura..
        ex²: você tem um cilindro com as seguintes medidas ('10x5') ou (20x10) ou (20x20) o calculo
             conssiste em passo 1:( C = 2.pi.r ) dada a formula substituiremos o comprimento pelo comprimento
             informado que é 10 e realizaremos o calculo. passo 2: ( 10 = 2.pi.r ). passo 3: ( 10/2.pi = r ).
             pronto achado o ultimo passo agora vamos achar o volume dada a formula ( V = pi.r².h ). 
             1 passo:  ( V = pi.r².h ) > ( V = pi.(10/2.pi)².h). 2 passo ( V = 3,14.2,5.5 ). 
             O resultado vai ser ( v = 39,25 ) segue-se com os demais.
        ''')
        volume_centimetros()
    elif result == '2':
        compr = float(input(print('informe o comprimento: ')))
        altura = float(input(print('informe a altura: ')))
        raio = compr/2
        volume = pi*((raio/pi)**2)*altura
        return abs(volume)
    else:
        print('Não Compreendi..')
        volume_centimetros()

def altura():
    print('informe o volume: ')
    volume = float(input())
    respo = str(input(print
    ('''
        se for diametro digite:-(1)
        se for raio digite:-----(2)  
    ''')))
    

    if respo == '1':
        print('informe o diametro: ')
        diam = float(input())
        raio = diam/2
        resultado = volume/(pi*raio**2)
        return resultado
    elif respo == '2':
        print('informe o raio: ')
        raio = float(input())
        resultado = volume/(pi*(raio**2))
        return resultado
    else:
        print('escreveu errado.')
        altura()

def volume():
    print('informe a altura: ')
    altura = float(input())
    print('informe o raio: ')
    raio = float(input())
    volum = altura*pi*(raio**2)
    return volum

def area_base():
    print('informe a área da raio: ')
    raio = float(input())
    return float(pi*(raio**2))

def area_lateral():
    print('informe a altura: ')
    lateral = float(input())
    print('informe o raio: ')
    raio = float(input())
    return float(2*pi*raio*lateral)

def area_total():
    print('informe a área do raio: ')
    raio = float(input())
    print('informe a altura: ')
    altura = float(input())
    areabase = pi*(raio**2)
    arealateral = 2*pi*raio*altura
    areaTotal = areabase + arealateral
    return areaTotal

def inicio():
    print('O que deseja?')
    print(
        '''
        para sair digite:-----------------------------(0)
        area da base digite:--------------------------(1)
        area lateral digite:--------------------------(2)
        area total digite:----------------------------(3)
        saber o volume:-------------------------------(4)
        saber a altura:-------------------------------(5)
        saber o volume com compr x alt digite:--------(6)
        ''')
    resultado = input(print('Escolha: '))
    if resultado == '1':
        result = float(area_base())
        print('a area da base é: '+str(result))
        inicio()
    elif resultado == '2':
        result = float(area_lateral())
        print('a area lateral é: '+str(result))
        inicio()
    elif resultado == '3':
        result = float(area_total())
        print('a área total é: '+str(result))
        inicio()
    elif resultado == '4':
        result = volume()
        print('O Volume é: '+str(result))
        inicio()
    elif resultado == '5':
        result = altura()
        print('A altura é: '+str(result))
        inicio()    
    elif resultado == '6':
        result = volume_centimetros()
        print('volume é: '+str(result))
        inicio()
    elif resultado == '0':
        exit()
    else:
        inicio()
        
inicio()