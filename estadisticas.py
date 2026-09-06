from validaciones import solicitar_categoria, validar_rango
from utilidades import filtrar_por_categoria


def cantidad_productos(productos):
    return len(productos)


def cantidad_por_categoria(productos, categoria):
    cantidad = 0
    for producto in productos:
        if producto[2] == categoria:
            cantidad = cantidad + 1
    return cantidad


def unidades_totales_stock(productos):
    total = 0
    for producto in productos:
        total = total + producto[4]
    return total


def valor_total_inventario(productos):
    total = 0
    for producto in productos:
        total = total + producto[3] * producto[4]
    return total


def mostrar_estadisticas_generales(productos):
    print("ESTADÍSTICAS GENERALES")
    print("Cantidad total de productos registrados:", cantidad_productos(productos))
    print("Unidades totales en stock:", unidades_totales_stock(productos))
    print("Valor total del inventario ($):", valor_total_inventario(productos))


def mostrar_estadisticas_por_tipo(productos, categorias):
    categoria = solicitar_categoria(categorias)
    productos_del_tipo = filtrar_por_categoria(productos, categoria)
    print("ESTADÍSTICAS DEL TIPO:", categoria)
    print("Cantidad de productos registrados:", cantidad_productos(productos_del_tipo))
    print("Unidades totales en stock:", unidades_totales_stock(productos_del_tipo))
    print("Valor total del inventario ($):", valor_total_inventario(productos_del_tipo))


def mostrar_estadisticas(productos, categorias):
    print("ESTADÍSTICAS")
    print("1 - Generales")
    print("2 - Por tipo de producto")
    opcion = validar_rango("Seleccione una opción: ", 1, 2)
    if opcion == 1:
        mostrar_estadisticas_generales(productos)
    elif opcion == 2:
        mostrar_estadisticas_por_tipo(productos, categorias)
