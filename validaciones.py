def validar_entero(mensaje, minimo):
    valido = False
    while not valido:
        texto = input(mensaje)
        valido = texto != ""
        numero = 0
        # Se revisa cada carácter antes de convertirlo a número.
        for caracter in texto:
            if caracter < "0" or caracter > "9":
                valido = False
            else:
                numero = numero * 10 + int(caracter)
        if valido and numero < minimo:
            valido = False
        if not valido:
            print("Ingrese un número entero mayor o igual a", minimo)
    return numero


def validar_rango(mensaje, minimo, maximo):
    numero = validar_entero(mensaje, minimo)
    while numero > maximo:
        print("El valor debe estar comprendido entre", minimo, "y", maximo)
        numero = validar_entero(mensaje, minimo)
    return numero


def validar_precio(mensaje):
    valido = False
    while not valido:
        texto = input(mensaje)
        valido = texto != ""
        separadores = 0
        enteros = 0
        decimales = 0
        # Aceptamos un punto o una coma y hasta dos decimales.
        for caracter in texto:
            if caracter == "." or caracter == ",":
                separadores = separadores + 1
            elif caracter >= "0" and caracter <= "9":
                if separadores == 0:
                    enteros = enteros + 1
                else:
                    decimales = decimales + 1
            else:
                valido = False
        if separadores > 1 or enteros == 0 or enteros > 9:
            valido = False
        if decimales > 2 or (separadores == 1 and decimales == 0):
            valido = False
        if valido:
            # Construimos el precio con operaciones aritméticas básicas.
            precio = 0
            divisor = 1
            parte_decimal = False
            for caracter in texto:
                if caracter == "." or caracter == ",":
                    parte_decimal = True
                else:
                    precio = precio * 10 + int(caracter)
                    if parte_decimal:
                        divisor = divisor * 10
            precio = precio / divisor
            if precio <= 0:
                valido = False
        if not valido:
            print("Ingrese un precio positivo, con hasta 9 dígitos enteros y 2 decimales.")
            print("Ejemplos: 1500 o 1500,50. Sin separadores de miles.")
    return precio


def tiene_contenido(texto):
    contenido = False
    for caracter in texto:
        if caracter != " " and caracter != "\t":
            contenido = True
    return contenido


def validar_texto(mensaje):
    texto = input(mensaje)
    while not tiene_contenido(texto):
        print("El texto no puede estar vacío ni contener solamente espacios.")
        texto = input(mensaje)
    return texto


def solicitar_categoria(categorias):
    print("TIPOS DE PRODUCTO DISPONIBLES")
    for i in range(len(categorias)):
        print(i + 1, "-", categorias[i])
    opcion = validar_rango("Seleccione un tipo: ", 1, len(categorias))
    return categorias[opcion - 1]
