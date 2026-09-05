def solicitar_numero(mensaje):
    texto = input(mensaje)
    while texto == "":
        print("El valor no puede estar vacío.")
        texto = input(mensaje)
    return texto


def validar_entero(mensaje, minimo):
    numero = int(solicitar_numero(mensaje))
    while numero < minimo:
        print("Ingrese un número entero mayor o igual a", minimo)
        numero = int(solicitar_numero(mensaje))
    return numero


def validar_rango(mensaje, minimo, maximo):
    numero = int(solicitar_numero(mensaje))
    while numero < minimo or numero > maximo:
        print("El valor debe estar comprendido entre", minimo, "y", maximo)
        numero = int(solicitar_numero(mensaje))
    return numero


def validar_precio(mensaje):
    print("Para los decimales use punto. Ejemplo: 1500.50")
    precio = float(solicitar_numero(mensaje))
    while precio <= 0:
        print("El precio debe ser mayor a cero.")
        precio = float(solicitar_numero(mensaje))
    return precio


def validar_texto(mensaje):
    texto = input(mensaje)
    while texto == "":
        print("El texto no puede estar vacío.")
        texto = input(mensaje)
    return texto


def solicitar_categoria(categorias):
    print("TIPOS DE PRODUCTO DISPONIBLES")
    for i in range(len(categorias)):
        print(i + 1, "-", categorias[i])
    opcion = validar_rango("Seleccione un tipo: ", 1, len(categorias))
    return categorias[opcion - 1]
