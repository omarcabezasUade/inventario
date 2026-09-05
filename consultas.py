from utilidades import calcular_ancho_texto, completar_espacios, filtrar_por_categoria
from validaciones import solicitar_categoria


def mostrar_productos(productos):
    if len(productos) == 0:
        print("No hay productos para mostrar.")
    else:
        encabezados = ["CÓDIGO", "NOMBRE", "TIPO DE PRODUCTO", "PRECIO ($)", "STOCK"]
        anchos = []
        linea = ""
        for columna in range(len(encabezados)):
            ancho = calcular_ancho_texto(productos, columna, encabezados[columna])
            anchos.append(ancho)
            linea = linea + completar_espacios(encabezados[columna], ancho)
        print(linea)
        for producto in productos:
            linea = ""
            for columna in range(len(encabezados)):
                linea = linea + completar_espacios(str(producto[columna]), anchos[columna])
            print(linea)


def consultar_por_categoria(productos, categorias):
    print("CONSULTA POR TIPO DE PRODUCTO")
    categoria = solicitar_categoria(categorias)
    filtrados = filtrar_por_categoria(productos, categoria)
    print("Productos del tipo:", categoria)
    mostrar_productos(filtrados)
