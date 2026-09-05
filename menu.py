from validaciones import validar_rango


def mostrar_menu():
    print()
    print("SISTEMA DE GESTIÓN DE INVENTARIO")
    print("1 - Alta de producto")
    print("2 - Consultar producto")
    print("3 - Modificar producto")
    print("4 - Eliminar producto")
    print("5 - Mostrar todos los productos")
    print("6 - Consultar productos por tipo")
    print("7 - Mostrar estadísticas")
    print("8 - Salir")
    return validar_rango("Seleccione una opción: ", 1, 8)
