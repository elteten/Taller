#!/usr/bin/env python
"""
Lista de pedidos del taller
AGREGAR PRECIO TOTAL para tener precio unitario y total
"""
import json

class Pedido:
    def __init__(self, id, cliente, descripcion, cantidad, precio, fecha):
        self.id = id
        self.cliente = cliente
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio
        self.fecha = fecha

class Taller:
    def __init__(self):
        self.pedidos = []
        self.next_id = 1

    def agregar_pedido(self, cliente, descripcion, cantidad, precio, fecha):
        pedido = Pedido(self.next_id, cliente, descripcion, cantidad, precio, fecha)
        self.pedidos.append(pedido)
        self.next_id += 1
    
    def listar_pedidos(self):
        # Encabezado de la tabla
        header = "{:<6} {:<30} {:<70} {:<10} {:<10} {:<20}".format("ID", "Cliente", "Descripción", "Cantidad", "Precio", "Fecha")
        print(header)
        print("=" * 150)  # Línea divisoria
        
        # Filas de datos
        for pedido in self.pedidos:
            row = "{:<6} {:<30} {:<70} {:<10} {:<10} {:<20}".format(
                pedido.id,
                pedido.cliente,
                pedido.descripcion,
                pedido.cantidad,
                pedido.precio,
                pedido.fecha
            )
            print(row)
        print("=" * 150)  # Línea divisoria

    def editar_pedido(self, id, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_fecha):
        for pedido in self.pedidos:
            if pedido.id == id:
                pedido.descripcion = nueva_descripcion
                pedido.cantidad = nueva_cantidad
                pedido.precio = nuevo_precio
                pedido.fecha = nueva_fecha
                print("Pedido editado exitosamente.")
                return
        print("ID de pedido no encontrado.")

    def eliminar_pedidos(self, ids):
        pedidos_a_eliminar = [pedido for pedido in self.pedidos if pedido.id in ids]

        if not pedidos_a_eliminar:
            print("Ningún pedido encontrado con los IDs proporcionados.")
            return

        for pedido in pedidos_a_eliminar:
            self.pedidos.remove(pedido)

        print("Pedido(s) eliminado(s) exitosamente.")

    def guardar_datos(self, archivo):
        datos = []
        for pedido in self.pedidos:
            datos.append({
                "id": pedido.id,
                "cliente": pedido.cliente,
                "descripcion": pedido.descripcion,
                "cantidad": pedido.cantidad,
                "precio": pedido.precio,
                "fecha": pedido.fecha
            })

        with open(archivo, "w") as file:
            json.dump(datos, file)

    def cargar_datos(self, archivo):
        try:
            with open(archivo, "r") as file:
                datos = json.load(file)
                for dato in datos:
                    self.agregar_pedido(dato["cliente"], dato["descripcion"], dato["cantidad"], dato["precio"], dato["fecha"])
        except FileNotFoundError:
            pass

def main():
    taller = Taller()
    taller.cargar_datos("pedidos.json")
    
    while True:
        print("\n1. Agregar pedido - 2. Listar pedidos - 3. Editar pedido - 4. Eliminar pedido - 5. Guardar - 6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cliente = input("Ingrese el nombre del cliente: ")
            descripcion = input("Ingrese la descripción del pedido: ")
            cantidad = int(input("Ingrese la cantidad: "))
            # Si es necesario hacer operaciones matematicas con precio hay que definirlo como float.
            precio = float(input("Ingrese el precio: "))
            fecha = (input("Ingrese la fecha: "))
            taller.agregar_pedido(cliente, descripcion, cantidad, precio, fecha)
            print("Pedido agregado exitosamente.")
        
        elif opcion == "2":
            taller.listar_pedidos()
        
        elif opcion == "3":
            id = int(input("Ingrese el ID del pedido a editar: "))
            nueva_descripcion = input("Ingrese la nueva descripción: ")
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            nueva_fecha = input("Ingrese la nueva fecha: ")
            taller.editar_pedido(id, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_fecha)
        
        elif opcion == "4":
            ids_str = input("Ingrese los IDs de los pedidos a eliminar (separados por comas): ")
            ids = [int(id) for id in ids_str.split(',')]
            taller.eliminar_pedidos(ids)

        elif opcion == "5":
            taller.guardar_datos("pedidos.json")
            print("Datos guardados.")

        elif opcion == "6":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

