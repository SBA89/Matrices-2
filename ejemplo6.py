
matriz1 = [['◉','◉','◉','◉','◉'],
           ['◉','◉','◉','◉','◉'],
           ['◉','◉','◉','◉','◉'],
           ['◉','◉','◉','◉','◉'],
           ['◉','◉','◉','◉','◉']]
correcto = '😁'
incorrecto = '💀'
ls_pregunta = ['¿Qué es Python\n\n1. Juego\n2. Lenguage de programación\n3. Marca de auto\n4. Ninguna de las anteriores', 
               '¿Qué es HTML?\n1. Lenguage de maquetaciín\n2. Marca de Gaseosa\n3. Navegador\n4. Perro caliente',
               '¿Apple es una marcá de?\n1. Auto\2. Fruta\n3. Celulares\n4.Ninguna de las anteriores']
ls_respuesta = ['2','1','3']

def fnt_impresion_matriz():
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            print(matriz1[i][j], end='    ')
        print('\n\n')
sw = True
contador = 0

    
for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        import os
        os.system('cls')
        fnt_impresion_matriz()
        print()
        print(ls_pregunta[contador])
        print()
        r = input('--> ')
        if r == ls_respuesta[contador]:
            matriz1[i][j] = correcto
        else:
            matriz1[i][j] = incorrecto
        contador += 1
    