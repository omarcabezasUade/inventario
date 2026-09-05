from datos import productos, categorias
from crud import alta_producto, consultar_producto, modificar_producto, eliminar_producto
from consultas import mostrar_productos, consultar_por_categoria
from estadisticas import mostrar_estadisticas
from menu import mostrar_menu


opcion = 0
while opcion != 8:
    opcion = mostrar_menu()
    print()
    print("----------------------------------------")
    print()
    if opcion == 1:
        alta_producto(productos, categorias)
    elif opcion == 2:
        consultar_producto(productos)
    elif opcion == 3:
        modificar_producto(productos, categorias)
    elif opcion == 4:
        eliminar_producto(productos)
    elif opcion == 5:
        mostrar_productos(productos)
    elif opcion == 6:
        consultar_por_categoria(productos, categorias)
    elif opcion == 7:
        mostrar_estadisticas(productos, categorias)
    elif opcion == 8:
        print("Fin del programa.")
    if opcion != 8:
        print()
        input("Presione Enter para volver al menú principal...")
