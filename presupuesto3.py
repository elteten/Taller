#!/usr/bin/env python

"""
Programa para hacer presupuestos del taller de Teten
"""
from datetime import date
import os

def costo():
    calculo=cantidades[x]*precios[x]
    return calculo

def costo_pintura():
    calculo_pintura=cantidades[x]*(precios[x]/1000)
    return calculo_pintura

def costo_seismts():
    calculo_seismts=cantidades[x]*(precios[x]/600)
    return calculo_seismts

def costo_alambre():
    calculo_alambre=cantidades[x]*(precios[x]/800)
    return calculo_alambre

def costo_chapa():
    calculo_chapa=cantidades[x]*(precios[x]/20000)
    return calculo_chapa

### REDEFINIDO EL COSTO DE OTROS INSUMOS +- 90%

def costo_insumos():
    calculo_insumos=((precio_horas*horas)*1.1)
    return calculo_insumos

def manodeobra():
    suma_horas=precio_horas*horas
    return suma_horas

# Debería cambiar el margen. Estoy ganando un poco poco
# Probando con un 90 +- por ciento

def margen():
    margen_material=(sum(total)/1.1)
    return margen_material

def totales():
    suma_total=(sum(total)+manodeobra()
    +costo_insumos()+margen())
    return suma_total

#### Listas ####

materiales=[]
cantidades=[]
precios=[]
total=[]

#### Variable para un divisor ;-) ####
divisor='-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-'

#### Mensaje de presentación ####

print ('--------------------------------------------------')
print ('|  Programa para sumar costos de un presupuesto  |')
print ('--------------------------------------------------')
print ('Podés usar las siguientes palabras clave:')
print ('\"hierro\" o \"Hierro" , \"caño\" o \"Caño" y \"planchuela\" o \"Planchuela"')
print ('para ingresar la cantidad en centimetros y el precio del tirón de seis metros')
print ('\"alambre\" o \"Alambre"')
print ('para ingresar la cantidad en centimetros y el precio de 1 kg (8 mts)')
print ('\"chapa\" o \"Chapa"')
print ('para ingresar la cantidad en centimetros cuadrados y el precio de la chapa de 200x100 cm')
print ('\"pintura\" o \"Pintura"')
print ('para ingresar la cantidad en centímetros cúbicos y el precio por litro')
print ('Otras palabras en material va a multiplicar la cantidad por el precio')
print ('En Materiales ingresá \"no\" para terminar')

#### Bucle para pedir los datos ####

while(True):
    material=str(input('Ingresa material (\"no\" para terminar): '))
    if (material == 'no'):
        break
    cantidad=float(input('Ingresa cantidad: '))
    precio=float(input('Ingresa precio: '))
    materiales.append(material)
    cantidades.append(cantidad)
    precios.append(precio)
horas=float(input('Ingresa las horas de trabajo: '))
precio_horas=float(input('Ingresa el precio de la hora: '))

#### Imprimir datos ####

print(divisor)
for  x in range(len(materiales)):
    if ('caño' in materiales[x] or 'Caño' in materiales[x]):
        total.append(costo_seismts())
        print ('El costo de ',materiales[x], 'es: $',
        '{:.2f}'.format(costo_seismts()))
    elif ('planchuela' in materiales[x] or 'Planchuela' in materiales[x]):
        total.append(costo_seismts())
        print ('El costo de ',materiales[x],  'es: $',
        '{:.2f}'.format(costo_seismts()))
    elif ('hierro' in materiales[x] or 'Hierro' in materiales[x]):
        total.append(costo_seismts())
        print ('El costo de ',materiales[x],  'es: $',
        '{:.2f}'.format(costo_seismts()))
    elif ('alambre' in materiales[x] or 'Alambre' in materiales[x]):
        total.append(costo_alambre())
        print ('El costo de ',materiales[x],  'es: $',
        '{:.2f}'.format(costo_alambre()))
    elif ('chapa' in materiales[x] or 'Chapa' in materiales[x]):
        total.append(costo_chapa())
        print ('El costo de ',materiales[x],  'es: $',
        '{:.2f}'.format(costo_chapa()))
    elif ('pintura' in materiales[x] or 'Pintura' in materiales[x]):
        total.append(costo_pintura())
        print ('El costo de ',materiales[x], 'es: $',
        '{:.2f}'.format(costo_pintura()))
    else:
        print ('El costo de ',materiales[x], 'es : $',
        '{:.2f}'.format(costo()))
        total.append(costo())
print('Una estimación aproximada de otros insumos: $',
'{:.2f}'.format(costo_insumos()))
print('El margen de ganancia es: $','{:.2f}'.format(margen()))
print('El costo de mano de obra es: $','{:.2f}'.format(manodeobra()))
print('El precio final es: $','{:.2f}'.format( totales()))
print(divisor)

#### Escribir en un archivo el resultado del presupuesto ####

cliente=input('Nombre del cliente: ')
nombre=input('Nombre del archivo: ')
carpeta=input('Carpeta: ')

# Crear la carpeta si no existe
if not os.path.exists(carpeta):
    os.makedirs(carpeta)

# Combinar la carpeta y el nombre del archivo para formar la ruta completa
ruta_archivo = os.path.join(carpeta, nombre)

# Abrir el archivo en la carpeta especificada
with open(ruta_archivo, 'w') as archivo:
    print('--------------------------------------------------', file=archivo)
    print('##  PRESUPUESTO PRELIMINAR  ##', file=archivo)
    print('--------------------------------------------------', file=archivo)
    print('|', date.today(), file=archivo)
    print('|  Presupuesto para', cliente, file=archivo)
    print('|', file=archivo)

# Seguir trabajando en el tema de las cantidades 
    for x in range(len(materiales)):
        if ('caño' in materiales[x] or 'Caño' in materiales[x]):
            print('|  El costo de', materiales[x], 'es: $',
                  '{:.2f}'.format(costo_seismts()), ' - ', cantidades[x], file=archivo)
        elif ('pintura' in materiales[x] or 'Pintura' in materiales[x]):
            print('|  El costo de', materiales[x], 'es: $',
                  '{:.2f}'.format(costo_pintura()), ' - ', cantidades[x], file=archivo)
        elif ('planchuela' in materiales[x] or 'Planchuela' in materiales[x]):
            print('|  El costo de', materiales[x], 'es: $',
                  '{:.2f}'.format(costo_seismts()), ' - ', cantidades[x], file=archivo)
        elif ('hierro' in materiales[x] or 'Hierro' in materiales[x]):
            print('|  El costo de', materiales[x], 'es: $',
                  '{:.2f}'.format(costo_seismts()), ' - ', cantidades[x], file=archivo)
        elif ('alambre' in materiales[x] or 'Alambre' in materiales[x]):
            print('|  El costo de', materiales[x], 'es: $',
                  '{:.2f}'.format(costo_alambre()), ' - ', cantidades[x], file=archivo)
        elif ('chapa' in materiales[x] or 'Chapa' in materiales[x]):
            print('|  El costo de', materiales[x], 'es: $',
                  '{:.2f}'.format(costo_chapa()), ' - ', cantidades[x], file=archivo)
        else:
            print('|  El costo de', materiales[x], 'es : $',
                  '{:.2f}'.format(costo()), ' - ', cantidades[x], file=archivo)

    print('|  Una estimación aproximada de otros insumos: $',
          '{:.2f}'.format(costo_insumos()), file=archivo)
    print('|  El margen de ganancia es: $',
          '{:.2f}'.format(margen()), file=archivo)
    print('|  El costo de mano de obra es: $',
          '{:.2f}'.format(manodeobra()), file=archivo)
    print('|', file=archivo)
    print('|  El precio final es: $',
          '{:.2f}'.format(totales()), file=archivo)
    print('|', file=archivo)
    print('--------------------------------------------------', file=archivo)
    print('     El Teten.-', file=archivo)

print(f"Archivo guardado exitosamente en {ruta_archivo}")
