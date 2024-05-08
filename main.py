import sys
import re

def cantidad_whiles(whiles):
    print("Hay un total de "+str(len(whiles))+" de bloques while")

def variables_diferentes(condicion):
    variables_texto = "".join(condicion)
    variables = re.findall(r'[a-z]',variables_texto)
    comparacion = re.findall(r'==|<|<=|>|>=|!=',variables_texto)
    variables_distintas = {}
    for i in range(0,len(variables),1):
          if variables[i] in variables_distintas:
              variables_distintas[variables[i]] += 1
          else:
                variables_distintas[variables[i]] = 1  
    print(variables_distintas)
    print("Hay un total de "+str(len(variables_distintas))+" variables distintas")
    print("Hay un total de "+str(len(comparacion))+" operadores de comparación")

def validar_cadena(cadena): #funcion para validar que la cadena cumple con los requisitos de los while loops y del proyecto
    cadena = re.sub(r'\b'+'while'+r'\b',r'\g<0> ',cadena)
    cadena = re.sub(r'\(',r'\g<0> ',cadena)
    cadena = re.sub(r'\)',r' \g<0> ',cadena)
    cadena = re.sub(r'==|<=?|>=?|!=',r' \g<0> ',cadena)
    cadena = re.sub(r'[\t]', " ",cadena) #eliminar los espacios en blanco del texto
    cadena = re.sub(r'[\n]', " ",cadena)
    cadena = list(filter(None, re.split(r' ', cadena, flags=re.IGNORECASE)))
    pila = ['T']
    for token in cadena:
        print(token)
        if re.match(r'^while$',token):
            if pila[-1] == 'T':
                pila.append('W')
            elif pila[-1] == '{':
                pila.append('W')
        if re.match(r'^\($',token):
            if pila[-1] == 'W':
                pila.pop()
                pila.append('(')
            elif pila[-1] == 'C':
                pila.pop()
                pass
        if re.match(r'^\)$',token):
            if pila[-1] == '(':
                pila.pop()
                pila.append('F')
        if re.match(r'^[a-z0-9]$',token):
            if pila[-1] == '(':
                pila.append('A')
            elif pila[-1] == 'C':
                pila.pop()
        if re.match(r'^\{$',token):
            if pila[-1] == 'F':
                pila.pop()
                pila.append('{')
        if re.match(r'^\}$',token):
            if pila[-1] == '{':
               pila.pop()
        if re.match(r'^==|<=?|>=?|!=$',token):
            if pila[-1] == 'A':
                pila.pop()
                pila.append('C')
        print(pila)   
    if pila.pop() != 'T':
        return print("Cadena Invalida")
    cadena = (" ").join(cadena)
    cadena = re.sub(r'\s*',"",cadena)
    print(cadena)
    condicion = re.findall(r'([a-z0-9]+[==|<|<=|>|>=|!=]+[a-z0-9])',cadena) #buscar todas las declaraciones condicionales de los while
    whiles = re.findall(r'\b' + "while"+ r'\b',cadena)
    variables_diferentes(condicion)
    cantidad_whiles(whiles)


try: 
    filename = sys.argv[1] #Tomar el parametro de la linea de comandos 
    try:
        with open(filename, 'r') as file:  #Leer el archivo y guardar en una variable
            cadena = file.read() 
    except:
        print("Ingresa un archivo de texto porfavor") #Si no se detecta un archivo de texto se imprime un mensaje de error
except:
    print("Ingresa un archivo de texto como parametro porfavor") #Si no se detecta un parametro se imprime un mensaje de error
validar_cadena(cadena) #Validar que la cadena cumple con los requisitos de un while

