from validaciones import solicitar_categoria


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


def mostrar_estadisticas(productos, categorias):
    print("ESTADÍSTICAS")
    categoria = solicitar_categoria(categorias)
    print("Cantidad total de productos registrados:", cantidad_productos(productos))
    print("Cantidad de productos del tipo", categoria, ":", cantidad_por_categoria(productos, categoria))
    print("Unidades totales en stock:", unidades_totales_stock(productos))
    print("Valor total del inventario ($):", valor_total_inventario(productos))
