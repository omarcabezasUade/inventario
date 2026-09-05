from validaciones import validar_entero, validar_texto, validar_precio
from validaciones import solicitar_categoria
from menu import mostrar_menu_modificacion


def buscar_producto(productos, codigo):
    posicion = -1
    i = 0
    while i < len(productos) and posicion == -1:
        if productos[i][0] == codigo:
            posicion = i
        i = i + 1
    return posicion


def solicitar_producto(productos):
    posicion = -1
    if len(productos) == 0:
        print("No hay productos cargados.")
    else:
        codigo = validar_entero("Código (0 para cancelar): ", 0)
        while codigo != 0 and posicion == -1:
            posicion = buscar_producto(productos, codigo)
            if posicion == -1:
                print("El código", codigo, "no ha sido encontrado. Intente nuevamente.")
                codigo = validar_entero("Código (0 para cancelar): ", 0)
        if codigo == 0:
            print("Operación cancelada.")
    return posicion


def mostrar_producto(producto):
    print("Código:", producto[0])
    print("Nombre:", producto[1])
    print("Tipo de producto:", producto[2])
    print("Precio ($):", producto[3])
    print("Stock disponible:", producto[4])


def alta_producto(productos, categorias):
    print("ALTA DE PRODUCTO")
    # último código + 1. Si se vació la matriz, usamos 101.
    codigo = 101
    if len(productos) > 0:
        codigo = productos[len(productos) - 1][0] + 1
    # Se comprueba que el identificador no esté repetido.
    while buscar_producto(productos, codigo) != -1:
        codigo = codigo + 1
    nombre = validar_texto("Nombre: ")
    categoria = solicitar_categoria(categorias)
    precio = validar_precio("Precio ($): ")
    stock = validar_entero("Stock disponible: ", 0)
    productos.append([codigo, nombre, categoria, precio, stock])
    print("Producto cargado con éxito. Código asignado:", codigo)


def consultar_producto(productos):
    print("CONSULTA DE PRODUCTO")
    posicion = solicitar_producto(productos)
    if posicion != -1:
        mostrar_producto(productos[posicion])


def modificar_producto(productos, categorias):
    print("MODIFICACIÓN DE PRODUCTO")
    posicion = solicitar_producto(productos)
    if posicion != -1:
        mostrar_producto(productos[posicion])
        opcion = 0
        while opcion != 5:
            opcion = mostrar_menu_modificacion()
            if opcion == 1:
                productos[posicion][1] = validar_texto("Nuevo nombre: ")
            elif opcion == 2:
                productos[posicion][2] = solicitar_categoria(categorias)
            elif opcion == 3:
                productos[posicion][3] = validar_precio("Nuevo precio ($): ")
            elif opcion == 4:
                productos[posicion][4] = validar_entero("Nuevo stock: ", 0)
            if opcion != 5:
                print()
                print("Producto modificado correctamente.")
                mostrar_producto(productos[posicion])



def eliminar_producto(productos):
    print("ELIMINACIÓN DE PRODUCTO")
    posicion = solicitar_producto(productos)
    if posicion != -1:
        mostrar_producto(productos[posicion])
        confirmacion = input("¿Confirma la eliminación? S/N: ")
        while confirmacion != "S" and confirmacion != "s" and confirmacion != "N" and confirmacion != "n":
            confirmacion = input("Ingrese S para confirmar o N para cancelar: ")
        if confirmacion == "S" or confirmacion == "s":
            productos.pop(posicion)
            print("Producto eliminado correctamente.")
        else:
            print("Eliminación cancelada.")
