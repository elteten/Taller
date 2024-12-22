#!/usr/bin/env python
import os
import pandas as pd
from rich.console import Console
from rich.table import Table

FILENAME = "finanzas.csv"
console = Console()

# Cargar o inicializar el archivo CSV
def cargar_datos():
    if os.path.exists(FILENAME):
        return pd.read_csv(FILENAME)
    else:
        return pd.DataFrame(columns=["ID", "Fecha", "Tipo", "Descripción", "Monto"])

# Guardar datos en el archivo CSV
def guardar_datos(df):
    df.to_csv(FILENAME, index=False)

# Mostrar el balance actual
def mostrar_balance(df):
    ingresos = df[df["Tipo"] == "Ingreso"]["Monto"].sum()
    egresos = df[df["Tipo"] == "Egreso"]["Monto"].sum()
    saldo = ingresos - egresos

    table = Table(title="Balance Actual")
    table.add_column("Tipo", justify="left")
    table.add_column("Monto", justify="right")
    table.add_row("Total Ingresos", f"${ingresos:.2f}")
    table.add_row("Total Egresos", f"${egresos:.2f}")
    table.add_row("Saldo Actual", f"${saldo:.2f}")
    console.print(table)

# Registrar una nueva transacción
def nueva_transaccion(df):
    nuevo_id = df["ID"].max() + 1 if not df.empty else 1
    tipo = console.input("Tipo (Ingreso/Egreso): ").capitalize()
    descripcion = console.input("Descripción: ")
    monto = float(console.input("Monto: "))
    fecha = pd.Timestamp.now().strftime("%Y-%m-%d")
    nueva_fila = {"ID": nuevo_id, "Fecha": fecha, "Tipo": tipo, "Descripción": descripcion, "Monto": monto}
    df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
    guardar_datos(df)
    console.print("[green]Transacción registrada correctamente.[/green]")
    return df

# Mostrar historial de transacciones
def mostrar_historial(df):
    table = Table(title="Historial de Transacciones")
    table.add_column("ID", justify="center")
    table.add_column("Fecha", justify="center")
    table.add_column("Tipo", justify="left")
    table.add_column("Descripción", justify="left")
    table.add_column("Monto", justify="right")

    for _, row in df.iterrows():
        color = "blue" if row["Tipo"] == "Ingreso" else "red"
        table.add_row(
            str(int(row["ID"])),
            row["Fecha"],
            row["Tipo"],
            row["Descripción"],
            f"[{color}]${row['Monto']:.2f}[/{color}]"
        )
    console.print(table)

# Editar o eliminar transacciones
def editar_eliminar_transaccion(df):
    mostrar_historial(df)
    try:
        trans_id = int(console.input("Ingrese el ID de la transacción a editar o eliminar: "))
        if trans_id not in df["ID"].values:
            console.print("[red]ID no encontrado.[/red]")
            return df

        console.print("[1] Editar transacción")
        console.print("[2] Eliminar transacción")
        opcion = console.input("Elija una opción: ")

        if opcion == "1":
            tipo = console.input("Nuevo Tipo (Ingreso/Egreso): ").capitalize()
            descripcion = console.input("Nueva Descripción: ")
            monto = float(console.input("Nuevo Monto: "))
            df.loc[df["ID"] == trans_id, ["Tipo", "Descripción", "Monto"]] = [tipo, descripcion, monto]
            guardar_datos(df)
            console.print("[green]Transacción editada correctamente.[/green]")
        elif opcion == "2":
            df = df[df["ID"] != trans_id]
            guardar_datos(df)
            console.print("[green]Transacción eliminada correctamente.[/green]")
        else:
            console.print("[red]Opción inválida.[/red]")
    except ValueError:
        console.print("[red]Entrada inválida. Asegúrese de ingresar un número.[/red]")
    return df

# Menú principal
def menu():
    df = cargar_datos()
    while True:
        console.print("\n[bold]Menú Principal:[/bold]")
        console.print("[1] Registrar nueva transacción")
        console.print("[2] Mostrar balance actual")
        console.print("[3] Ver historial de transacciones")
        console.print("[4] Editar o eliminar transacción")
        console.print("[5] Salir")
        opcion = console.input("Elige una opción: ")

        if opcion == "1":
            df = nueva_transaccion(df)
        elif opcion == "2":
            mostrar_balance(df)
        elif opcion == "3":
            mostrar_historial(df)
        elif opcion == "4":
            df = editar_eliminar_transaccion(df)
        elif opcion == "5":
            console.print("[cyan]¡Buena suerte con la platita ;-) ![/cyan]")
            break
        else:
            console.print("[red]Opción inválida, intenta de nuevo.[/red]")

# Ejecutar el programa
if __name__ == "__main__":
    menu()

