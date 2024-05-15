import sys
import re

def cantidad_whiles(whiles):
    """
    Para terminar imprimimos la longitud del arreglo de whiles que se encontraron
    """
    print("Hay un total de "+str(len(whiles))+" de bloques while")

def variables_diferentes(condicion):
    """
    Creamos un texto con el arreglo de las declaraciones condicionales para luego encontrar todas las variables
    de una sola letra minuscula y todos los signos de comparación para guardarlos en un su respectivo arreglo
    """
    variables_texto = "".join(condicion)
    variables = re.findall(r'[a-z]',variables_texto)
    comparacion = re.findall(r'==|<=?|>=?|!=',variables_texto)
    """
    Para encontrar todas las variables distintas creamos un diccionario y iteramos sobre el arreglo de variables
    cada que encontremos una nueva creamos una nueva entrada en el diccionario, si la variable ya existe entonces
    sumamos un valor a la entrada de la variable en el diccionario
    """
    variables_distintas = {}
    for i in range(0,len(variables),1):
          if variables[i] in variables_distintas:
              variables_distintas[variables[i]] += 1
          else:
                variables_distintas[variables[i]] = 1  
    """ 
    Imprimimos la longitud del diccionario de las variables distintas así como el arreglo
    de los operadores de comparación que se encontraron
    """
    print("Hay un total de "+str(len(variables_distintas))+" variables distintas")
    print("Hay un total de "+str(len(comparacion))+" operadores de comparación")

def validar_cadena(cadena): 
    """ 
    Agregar un espacio antes y despues de cada elemento que se aceptado dentro de la cadena,
    al mismo tiempo intercambiamos cualquier sangría o salto de linea por un espacio de esta manera
    tenemos un texto de puros elementos separados unicamente por espacios en blanco
    """
        
    cadena = re.sub(r'\b'+'while'+r'\b',r'\g<0> ',cadena) 
    cadena = re.sub(r'\(',r'\g<0> ',cadena) 
    cadena = re.sub(r'\)',r' \g<0> ',cadena) 
    cadena = re.sub(r'==|<=?|>=?|!=',r' \g<0> ',cadena)
    cadena = re.sub(r'[\t]', " ",cadena) 
    cadena = re.sub(r'[\n]', " ",cadena)
    """
    Separar los elementos del texto por espacio en blanco y filtrar los elementos vaciós del arreglo
    que aparecen cuando hay dos o más espacios en blanco seguidos
    """
    
    cadena = list(filter(None, re.split(r' ', cadena, flags=re.IGNORECASE)))
    """ Creamos el automata de pila, incializandolo con el tope como primer elemento """
    pila = ['T']
    """ Iteramos sobre el arreglo de elementos del texto """
    for token in cadena:
        """
        Si el elemento coincide con la palabra 'while' checamos cual es el último
        elemento del automata de pila, si es el Tope o un corchete abierto
        agregamos 'W', en caso contrario rechazamos la producción.
        """
        if re.match(r'^while$',token): 
            if pila[-1] == 'T':
                pila.append('W')
            elif pila[-1] == '{':
                pila.append('W')
            else:
                return print("Cadena Invalida")
        """
        Si el elemento coincide con un parentesis abierto checamos cual es el ultimo elemento
        del automata de pila, si encontramos 'W' hacemos pop a la pila y añadimos '(' al arreglo.
        Si encontramos una 'C' unicamente hacemos pop a la pila. Si hay algo más en el automata de pila
        rechazamos la producción
        """
        else:
            if re.match(r'^\($',token):
                if pila[-1] == 'W':
                    pila.pop()
                    pila.append('(')
                elif pila[-1] == 'C':
                    pila.pop()
                else:
                    return print("Cadena Invalida")
            """
            Si el elemento coincide con un parentesis cerrado checamos cual es el último elemento
            del automata de pila, si encontramos un '(' le hacemos pop a la pila y agregamos 'F', 
            en cualquier otro caso rechazamos la producción.
            """
            else:
                if re.match(r'^\)$',token):
                    if pila[-1] == '(':
                        pila.pop()
                        pila.append('F')
                    else:
                        return print("Cadena Invalida")
                """ 
                Si el elemento coincide con alguna letra minuscula o un número de un solo digito checamos
                el último elemento del automata de pila, si encontramos un '(' entonces añadimos 'A' a la pila,
                si encontramos una 'C' entonces le hacemos pop a la pila unicamente. En caso contrario rechazamos la producción.
                """
                else: 
                    if re.match(r'^[a-z0-9]$',token):
                        if pila[-1] == '(':
                            pila.append('A')
                        elif pila[-1] == 'C':
                            pila.pop()
                        else:
                            return print("Cadena Invalida")
                    """
                    Si el elemento coincide con un corchete abierto checamos el último valor del automata de pila.
                    Si encontramos una 'F' le hacemos pop a la pila y agregamos un '{', en caso contrario rechazamos
                    la producción
                    """
                    else:
                        if re.match(r'^\{$',token):
                            if pila[-1] == 'F':
                                pila.pop()
                                pila.append('{')
                            else:
                                return print("Cadena Invalida")
                        """ 
                        Si el elemento coincide con un corchete cerrado checamos el último valor del automata de pila.
                        Si encontramos un '{' entonces le hacemos pop a la pila, en caso contrario rechazamos la 
                        producción
                        """
                        else:
                            if re.match(r'^\}$',token):
                                if pila[-1] == '{':
                                    pila.pop()
                                else:
                                    return print("Cadena Invalida")
                            """
                            Si el elemento coincide con uno de los signos de comparación checamos el último valor del automata de pila
                            si encontramos una 'A' entonces hacemos pop a la pila y agregamos una 'C'. En caso contrario rechazamos
                            la producción. Si al final el elemento no coincidio con ninguno de los elementos que checamos igual se
                            rechaza la producción
                            """
                            else:
                                if re.match(r'^==|<=?|>=?|!=$',token):
                                    if pila[-1] == 'A':
                                        pila.pop()
                                        pila.append('C')
                                    else:
                                        return print("Cadena Invalida")
                                else:
                                    return print("Cadena Invalida")
    """
    Si al final de la iteración el último elemento de la pila no es el Tope 
    significa que se usaron los elementos correctos en las declaraciones
    pero no se implementaron de manera correcta por lo que rechazamos la producción.
    """
    if pila.pop() != 'T':
        return print("Cadena Invalida")
    """
    Ya que la cadena ha sido validada convertimos el arreglo en un texto de nuevo y 
    eliminamos todos los espacios para así encontrar todos los signos de comparación y 
    todos los whiles declarados
    """
    cadena = (" ").join(cadena)
    cadena = re.sub(r'\s*',"",cadena)
    condicion = re.findall(r'([a-z0-9]+[==|<=?|>=?|!=]+[a-z0-9])',cadena) #buscar todas las declaraciones condicionales de los while
    whiles = re.findall(r'\b' + "while"+ r'\b',cadena)
    variables_diferentes(condicion)
    cantidad_whiles(whiles)


try: 
    filename = sys.argv[1] """ Tomar el parametro de la linea de comandos """
    try:
        with open(filename, 'r') as file:  """ Leer el archivo y guardar en una variable """
            cadena = file.read() 
    except:
        print("Ingresa un archivo de texto porfavor") """ Si no se detecta un archivo de texto se imprime un mensaje de error """
except:
    print("Ingresa un archivo de texto como parametro porfavor") """ Si no se detecta un parametro se imprime un mensaje de error """
validar_cadena(cadena) """ Validar que la cadena cumple con los requisitos de un while """

