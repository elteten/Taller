#!/usr/bin/env python
"""
Inventario de materias primas u otros artículos del taller
"""
# Importar la librería para usar archivos .json
import json

# Lista vacia para almacenar los datos
inventario = []

# Variable con el nombre del archivo
nombre_archivo = "inventario.json"

# Función para agregar materiales o artículos
def agregar_producto(nombre, tipo, cantidad, precio):
    producto = {'nombre': nombre, 'tipo': tipo, 'cantidad': cantidad, 'precio': float(precio)}
    inventario.append(producto)

# Función para editar las entradas
def editar_entrada():
    nombre = input("Ingrese el nombre del material que desea editar: ")
    for i, item in enumerate(inventario):
        if item['nombre'] == nombre:
            nuevo_nombre = input("Ingrese el nuevo nombre (dejar en blanco para no cambiar): ") or item['nombre']
            nuevo_tipo = input("Ingrese el nuevo tipo (dejar en blanco para no cambiar): ")
            if nuevo_tipo:
                nuevo_tipo = str(nuevo_tipo)
            else:
                nuevo_tipo = item['tipo']
            nueva_cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            if nueva_cantidad:
                nueva_cantidad = float(nueva_cantidad)
            else:
                nueva_cantidad = item['cantidad']
            nuevo_precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
            if nuevo_precio:
                nuevo_precio = float(nuevo_precio)
            else:
                nuevo_precio = item['precio']
            inventario[i] = {'nombre': nuevo_nombre, 'tipo':nuevo_tipo, 'cantidad': nueva_cantidad, 'precio': nuevo_precio}
            guardar_inventario(nombre_archivo)
            print(f"El material {nombre} ha sido editado exitosamente.")
            return
    print(f"No se encontró ningún material con nombre {nombre}.")

# Función para ver los datos de la lista
def ver_inventario():
    print("\nInventario:")
    print("-" * 70)
    print("Nombre".center(20) + " Tipo".center(20) + " Cantidad".center(5) + "\t Precio".center(10))
    print("-" * 70)
    for item in inventario:
        nombre = item['nombre']
        tipo = item['tipo']
        cantidad = item['cantidad']
        precio = item['precio']
        print (nombre.ljust(20) + "|\t" + tipo.ljust(16) + "|" + f' {cantidad:^5}' + "\t  |" + f'\t$ {precio:<10}' + ' |')

# Función para eliminar un material o artículo por su nombre
def eliminar_producto(nombre):
    for producto in inventario:
        if producto['nombre'] == nombre:
            inventario.remove(producto)

# Función que guarda el archivo .json
def guardar_inventario(nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(inventario, archivo)

# Función que carga el archivo .json
def cargar_inventario(nombre_archivo):
        global inventario
        with open(nombre_archivo, 'r') as archivo:
            inventario = json.load(archivo)

cargar_inventario(nombre_archivo)
     
# Bucle para el menú o interfaz del usuario
while True:
# Un separador
    print("-" * 70)
    opcion = input("Seleccione una opción (agregar, editar, ver, eliminar, salir): ")
    if opcion == 'agregar':
        nombre = input("Ingrese el nombre del producto: ")
        tipo = input("Ingrese el tipo de producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")
        precio = input("Ingrese el precio; ")
        agregar_producto(nombre, tipo, cantidad, precio)
    elif opcion == 'editar':
        editar_entrada()
    elif opcion == 'ver':
        ver_inventario()
    elif opcion == 'eliminar':
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        eliminar_producto(nombre)
    elif opcion == 'salir':
        break

guardar_inventario(nombre_archivo)
