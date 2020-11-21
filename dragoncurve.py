#TODO Solucionar el factor de escala iteracion 0 a un numero fijo, cada dos iteraciones el numero de factor / 2, calcular antes de dibujar

import re
import turtle
import sys

def replace(substitution):
    return lambda match: substitution[match.group(0)]

def dragon_curve(n:int=None):
    
    #TODO ver el parseo con groups en python

    del sys.argv[0]
    args = ' '.join([str(s) for s in sys.argv])
    
    m = re.fullmatch(r'(-i)\s(\d)', args)
    
    if not m:
        print(f'No se especifico ningun parametro o esta mal especificado.\nArgs recibidos: {args}')
        return False

    n = int(m.group(2)) # El numero de iteraciones siempre se va a encontrar en el segundo grupo

    cadena = 'FX'
    reglas_prod = {'X':'X+YF+', 'Y':'-FX-Y'}
    no_terminales = re.compile('[XY]')

    for x in range(0, n):  
        cadena = re.sub(no_terminales, replace(reglas_prod), cadena)
    
    return cadena


def draw_dragon_curve(cadena):
    window = turtle.Screen()
    window.setup(width=800, height=800)
    window.title('Dragon Curve')
    t = turtle.Turtle()
    t.up()
    t.goto((-300, 300))
    t.down()    
    t.speed(0)

    regex = re.compile('[XY]')
    cadena = re.sub(regex, '', cadena)

    for c in cadena:
        
        if(c == 'F'):
            t.forward(10)

        if(c == '+'):
            t.rt(90)
        
        if(c == '-'):
            t.lt(90)
    
    turtle.done()
    

dragon_curve(3)
