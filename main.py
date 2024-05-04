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
    cadena = re.sub(r"[ ]", "",cadena) #eliminar los espacios en blanco del texto
    cadena = re.sub(r'\t+',"",cadena) #eliminar las sangrías 
    cadena = re.split(r'[\b]',cadena)    
    cadena = re.split(r'\n+',cadena[0])
    pila = []
    count = 0
    for i in range(0,len(cadena)-1,1):
        if re.match(r'\bwhile\b\([a-z0-9](==|<|<=|>|>=|!=)[a-z0-9]\){$',cadena[i]):
            count += 1
            pila.append("{")
        if re.match(r'\bwhile\b\([a-z0-9](==|<|<=|>|>=|!=)[a-z0-9]\){}',cadena[i]):
            count += 1
            pass
        elif re.match(r'}$',cadena[i]):
            count += 1
            try:
                pila.pop()
            except:
                pila.append('}')
        if count == 0:
            return print("Cadena Invalida") 
        count = 0  
    if pila:
        return print("Cadena Invalida")
    cadena = (" ").join(cadena)
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

