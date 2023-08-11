#!/usr/bin/env python
"""
Lista de pedidos del taller
"""
import json

class Pedido:
    def __init__(self, id, cliente, descripcion, cantidad, precio):
        self.id = id
        self.cliente = cliente
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

class Taller:
    def __init__(self):
        self.pedidos = []
        self.next_id = 1

    def agregar_pedido(self, cliente, descripcion, cantidad, precio):
        pedido = Pedido(self.next_id, cliente, descripcion, cantidad, precio)
        self.pedidos.append(pedido)
        self.next_id += 1
    
    def listar_pedidos(self):
        # Encabezado de la tabla
        header = "{:<6} {:<30} {:<70} {:<10} {:<10}".format("ID", "Cliente", "Descripción", "Cantidad", "Precio")
        print(header)
        print("=" * 130)  # Línea divisoria
        
        # Filas de datos
        for pedido in self.pedidos:
            row = "{:<6} {:<30} {:<70} {:<10} {:<10}".format(
                pedido.id,
                pedido.cliente,
                pedido.descripcion,
                pedido.cantidad,
                pedido.precio
            )
            print(row)
        print("=" * 130)  # Línea divisoria

    def editar_pedido(self, id, nueva_descripcion, nueva_cantidad, nuevo_precio):
        for pedido in self.pedidos:
            if pedido.id == id:
                pedido.descripcion = nueva_descripcion
                pedido.cantidad = nueva_cantidad
                pedido.precio = nuevo_precio
                print("Pedido editado exitosamente.")
                return
        print("ID de pedido no encontrado.")

    def eliminar_pedido(self, id):
        for pedido in self.pedidos:
            if pedido.id == id:
                self.pedidos.remove(pedido)
                print("Pedido eliminado exitosamente.")
                return
        print("ID de pedido no encontrado.")

    def guardar_datos(self, archivo):
        datos = []
        for pedido in self.pedidos:
            datos.append({
                "id": pedido.id,
                "cliente": pedido.cliente,
                "descripcion": pedido.descripcion,
                "cantidad": pedido.cantidad,
                "precio": pedido.precio
            })

        with open(archivo, "w") as file:
            json.dump(datos, file)

    def cargar_datos(self, archivo):
        try:
            with open(archivo, "r") as file:
                datos = json.load(file)
                for dato in datos:
                    self.agregar_pedido(dato["cliente"], dato["descripcion"], dato["cantidad"], dato["precio"])
        except FileNotFoundError:
            pass

def main():
    taller = Taller()
    taller.cargar_datos("pedidos.json")
    
    while True:
        print("\n1. Agregar pedido")
        print("2. Listar pedidos")
        print("3. Editar pedido")
        print("4. Eliminar pedido")
        print("5. Guardar")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cliente = input("Ingrese el nombre del cliente: ")
            descripcion = input("Ingrese la descripción del pedido: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            taller.agregar_pedido(cliente, descripcion, cantidad, precio)
            print("Pedido agregado exitosamente.")
        
        elif opcion == "2":
            taller.listar_pedidos()
        
        elif opcion == "3":
            id = int(input("Ingrese el ID del pedido a editar: "))
            nueva_descripcion = input("Ingrese la nueva descripción: ")
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            taller.editar_pedido(id, nueva_descripcion, nueva_cantidad, nuevo_precio)
        
        elif opcion == "4":
            id = int(input("Ingrese el ID del pedido a eliminar: "))
            taller.eliminar_pedido(id)
        
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

