from validaciones import validar_entero, validar_texto, validar_precio
from validaciones import solicitar_categoria, tiene_contenido


def buscar_producto(productos, codigo):
    posicion = -1
    i = 0
    while i < len(productos) and posicion == -1:
        if productos[i][0] == codigo:
            posicion = i
        i = i + 1
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
    codigo = validar_entero("Código: ", 1)
    posicion = buscar_producto(productos, codigo)
    if posicion == -1:
        print("El código", codigo, "no ha sido encontrado.")
    else:
        mostrar_producto(productos[posicion])


def modificar_producto(productos, categorias):
    print("MODIFICACIÓN DE PRODUCTO")
    codigo = validar_entero("Código: ", 1)
    posicion = buscar_producto(productos, codigo)
    if posicion == -1:
        print("El código", codigo, "no ha sido encontrado.")
    else:
        mostrar_producto(productos[posicion])
        print("Presione Enter para conservar el nombre.")
        nombre = input("Nuevo nombre: ")
        while nombre != "" and not tiene_contenido(nombre):
            print("Ingrese un nombre o presione Enter para conservarlo.")
            nombre = input("Nuevo nombre: ")
        if nombre != "":
            productos[posicion][1] = nombre
        productos[posicion][2] = solicitar_categoria(categorias)
        productos[posicion][3] = validar_precio("Precio ($): ")
        productos[posicion][4] = validar_entero("Stock disponible: ", 0)
        print("Producto modificado correctamente.")


def eliminar_producto(productos):
    print("ELIMINACIÓN DE PRODUCTO")
    codigo = validar_entero("Código: ", 1)
    posicion = buscar_producto(productos, codigo)
    if posicion == -1:
        print("El código", codigo, "no ha sido encontrado.")
    else:
        mostrar_producto(productos[posicion])
        confirmacion = input("¿Confirma la eliminación? S/N: ")
        while confirmacion != "S" and confirmacion != "s" and confirmacion != "N" and confirmacion != "n":
            confirmacion = input("Ingrese S para confirmar o N para cancelar: ")
        if confirmacion == "S" or confirmacion == "s":
            productos.pop(posicion)
            print("Producto eliminado correctamente.")
        else:
            print("Eliminación cancelada.")
