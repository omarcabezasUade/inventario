def calcular_ancho_texto(productos, columna, encabezado):
    ancho = len(encabezado)
    for producto in productos:
        largo = len(str(producto[columna]))
        if largo > ancho:
            ancho = largo
    return ancho + 3


def completar_espacios(texto, ancho):
    while len(texto) < ancho:
        texto = texto + " "
    return texto


def filtrar_por_categoria(productos, categoria):
    filtrados = []
    for producto in productos:
        if producto[2] == categoria:
            filtrados.append(producto)
    return filtrados
