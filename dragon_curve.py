#TODO Ajustar la resolucion segun el trazo
#TODO 
# x = TRAZO
# x = x/(sqrt(2))^i i = iteraciones

import re, turtle, sys, math

TRAZO = 300


def replace(substitution):
    """
        Funcion que matchea segun una key y un value.\n
        Recibe un diccionario, donde la key del dict es el caracter que hay que matchear,\n
        y el value el valor a reemplazar en caso de match.
    """
    return lambda match: substitution[match.group(0)]



def dragon_curve(n:int=None):
    """
        Funcion que genera la gramatica n del fractal Dragon Curve.\n
        Tambien lo dibuja con turtle...
        Argumentos:
        n --- Cantidad de iteraciones de la gramatica
    """

    del sys.argv[0]
    args = ' '.join([str(s) for s in sys.argv])
    
    #Chequeo el arg de iteraciones con una regex
    m = re.fullmatch(r'(-i)\s(\d{1,})', args)
    
    if not m:
        print(f'No se especifico ningun parametro o esta mal especificado.\nArgs recibidos: {args}')
        return False

    n = int(m.group(2)) # El numero de iteraciones siempre se va a encontrar en el segundo grupo

    cadena = 'FX'
    reglas_prod = {'X':'X+YF+', 'Y':'-FX-Y'}
    no_terminales = re.compile('[XY]')

    for x in range(0, n):  
        cadena = re.sub(no_terminales, replace(reglas_prod), cadena)

    draw_dragon_curve(cadena, n)
    
    return cadena


def calc_scale(n):
    return TRAZO/pow(math.sqrt(2), n)

def config_window(window, turtle, x):
    window.setup(width=1024, height=768)
    window.title('Dragon Curve')
    turtle.up()
    turtle.goto((x, 0))
    turtle.down()
    turtle.speed(0)
    turtle.rt(90)

def draw_dragon_curve(cadena, n):
    
    distance = calc_scale(n) if (n>2) else TRAZO
    x =  200 if(n >= 15) else -150
    w = turtle.Screen()
    t = turtle.Turtle()
    config_window(w, t, x)

    regex = re.compile('[XY]')
    cadena = re.sub(regex, '', cadena)

    for c in cadena:
        
        if(c == 'F'):
            t.backward(distance)

        if(c == '+'):
            t.rt(90)
        
        if(c == '-'):
            t.lt(90)
    
    turtle.done()
    

dragon_curve()