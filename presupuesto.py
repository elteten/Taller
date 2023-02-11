"""
Programa para hacer presupuestos del taller de Teten
Será posible hacer funcionar algo así en un servidor?
"""
def costo():
    calculo=cantidades[x]*precios[x]
    return calculo

def costo_pintura():
    calculo_pintura=cantidades[x]*(precios[x]/1000)
    return calculo_pintura

def costo_seismts():
    calculo_seismts=cantidades[x]*(precios[x]/6)
    return calculo_seismts

def costo_hierro():
    calculo_hierro=cantidades[x]*(precios[x]/12)
    return calculo_hierro

def costo_insumos():
    calculo_insumos=((precio_horas*horas)/6)
    return calculo_insumos

def manodeobra():
    suma_horas=precio_horas*horas
    return suma_horas

def margen():
    margen_material=(sum(total)/3)
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
divisor='-.' * 16
linea='-' * 50
#### Mensaje de presentación ####

print (linea)
print ('|  Programa para sumar costos de un presupuesto  |')
print (linea)
print ('Podés usar las siguientes palabras clave:')
print ('\"caño\" o \"Caño" y \"planchuela\" o \"Planchuela"')
print ('para ingresar la cantidad en metros y el precio del tirón de seis metros')
print ('\"hierro\" o \"Hierro"')
print ('para ingresar la cantidad en metros y el precio del tirón de doce metros')
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
    elif ('pintura' in materiales[x] or 'Pintura' in materiales[x]):
        total.append(costo_pintura())
        print ('El costo de ',materiales[x], 'es: $',
        '{:.2f}'.format(costo_pintura()))
    elif ('planchuela' in materiales[x] or 'Planchuela' in materiales[x]):
        total.append(costo_seismts())
        print ('El costo de ',materiales[x],  'es: $',
        '{:.2f}'.format(costo_seismts()))
    elif ('hierro' in materiales[x] or 'Hierro' in materiales[x]):
        total.append(costo_hierro())
        print ('El costo de ',materiales[x],  'es: $',
        '{:.2f}'.format(costo_hierro()))
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
archivo=open(nombre, 'w')
print(divisor, file=archivo)
print('##  PRESUPUESTO PRELIMINAR  ##', file=archivo)
print(divisor, file=archivo)
print('|', file=archivo)
print('|  Presupuesto para ',cliente, file=archivo)
print('|', file=archivo)
for  x in range(len(materiales)):
    if ('caño' in materiales[x] or 'Caño' in materiales[x]):
        print ('|  El costo de ',materiales[x], 'es: $',
        '{:.2f}'.format(costo_seismts()), file=archivo)
    elif ('pintura' in materiales[x] or 'Pintura' in materiales[x]):
        print ('|  El costo de ',materiales[x], 'es: $',
        '{:.2f}'.format(costo_pintura()), file=archivo)
    elif ('planchuela' in materiales[x] or 'Planchuela' in materiales[x]):
        print ('|  El costo de ',materiales[x],  'es: $',
        '{:.2f}'.format(costo_seismts()), file=archivo)
    else:
        print ('|  El costo de ',materiales[x], 'es : $',
        '{:.2f}'.format(costo()), file=archivo)
print('|  Una estimación aproximada de otros insumos: $',
'{:.2f}'.format(costo_insumos()), file=archivo)
print('|  El margen de ganancia es: $',
'{:.2f}'.format(margen()), file=archivo)
print('|  El costo de mano de obra es: $',
'{:.2f}'.format(manodeobra()), file=archivo)
print('|',file=archivo)
print('|  El precio final es: $',
'{:.2f}'.format( totales()), file=archivo)
print('|',file=archivo)
print(divisor, file=archivo)
print('     El Teten.-', file=archivo)
archivo.close()
