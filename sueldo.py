"""
Programa para calcular (aproximadamente) el sueldo del rubro del calzado en Argentina. No es exacto y puede tener diferencias sustanciales con el calculo del contador.
Autor: Dante Fontana
"""
# Funciones remuneraciones
"""
TENGO QUE AGREGAR EL AGUINALDO. NO TENGO CLARO COMO SE CALCULA EL AQUINALDO
"""
def antiguedad():
   porcentaje_antiguedad=anos*0.75
   return porcentaje_antiguedad

def totalhoras():
   total_horas=horas*valorhora
   return total_horas

def totalmerienda():
    total_merienda=horas*merienda
    return total_merienda

def totalferiados():
    total_feriados=(valorhora*8)*feriados
    return total_feriados

def totallicencia():
    total_licencia=(valorhora*8)*licencia
    return total_licencia

def totalantiguedad():
    total_antiguedad=((totalhoras()+totalmerienda()+
    totalferiados())/100)*antiguedad()
    return total_antiguedad

# Funciones descuentos

def jubilacion():
    total_jubilacion=(((totalhoras()+
		totalmerienda()+
		totalferiados()+
		totalantiguedad()+
		premioasistencia+asistenciaperfecta)/100 )*PORCENTAJEJUBILACION)
    return total_jubilacion

def ley19032():
    total_ley19032=(((totalhoras()+
		totalmerienda()+
		totalferiados()+
		totalantiguedad()+
		premioasistencia+asistenciaperfecta)
		/100 )*PORCENTAJELEY19032)
    return total_ley19032

def sindicato():
    total_sindicato=(((totalhoras()+
		totalmerienda()+
		totalferiados()+
		totalantiguedad()+
		premioasistencia+asistenciaperfecta)
		/100 )*PORCENTAJESINDICATO)
    return total_sindicato

def obrasocial():
    total_obrasocial=(((totalhoras()+totalmerienda()+totalferiados()+
        totalantiguedad()+
		premioasistencia+asistenciaperfecta)/100 )*PORCENTAJEOBRASOCIAL)
    return total_obrasocial

# Funciones totales

def totalbruto():
    total_bruto=(totalhoras()+totalmerienda()+totalferiados()
    +totalantiguedad()+premioasistencia+asistenciaperfecta+totallicencia())
    return total_bruto

def totaldescuentos():
    total_descuentos=(jubilacion()+ley19032()+sindicato()+obrasocial())
    return total_descuentos

def totalneto():
    total_neto=((totalbruto()+sumanr)-totaldescuentos())
    return total_neto

# Constantes

PORCENTAJEJUBILACION=11
PORCENTAJELEY19032=3
PORCENTAJESINDICATO=2.5
PORCENTAJEOBRASOCIAL=6

# Variables

horas=float(input('Cuantas horas: '))
valorhora=float(input('Valor por horas: '))
merienda=float(input('Valor merienda: '))
feriados=int(input('Cuantos feriados: '))
licencia=int(input('Cuantos dias de licencia: '))
anos=int(input('Antiguedad años: '))
premioasistencia=float(input('Premio asistencia: '))
asistenciaperfecta=float(input('Asistencia perfecta: '))
sumanr=float(input('Suma no remunerativa: '))

separador='-----------------------------------'

# Menu

while(True):
    print(
        """
        Ingresa el numero de la opción deseada.

      |  1  - Total horas trabajadas |  8  - Descuento obra social  |
      |  2  - Total merienda         |  9  - Total bruto            |
      |  3  - Total feriados         |  10 - Total descuentos       |
      |  4  - Total antiguedad       |  11 - Total neto             |
      |  5  - Descuento Jubilacion   |  12 - Suma no remunerativa   |
      |  6  - Descuento ley 19032    |  13 - Licencia               |
      |  7  - Descuento sindicato    |  14 - Salir del programa     |
        """
        )
    opcion=int(input('Opcion: '))
    print(separador)

# Mostrando los calculos
    match opcion:
        case 1:
            print('Pago horas: ','{:.2f}'.format(totalhoras()))
            print(separador)
        case 2:
            print('Pago merienda: ','{:.2f}'.format(totalmerienda()))
            print(separador)
        case 3:
            print('Pago feriados: ','{:.2f}'.format(totalferiados()))
            print(separador)
        case 4:
            print('Total por antiguedad: ','{:.2f}'.format(totalantiguedad()))
            print(separador)
        case 5:
            print('Descuento jubilacion: ','{:.2f}'.format(jubilacion()))
            print(separador)
        case 6:
            print('Descuento ley 19032: ','{:.2f}'.format(ley19032()))
            print(separador)
        case 7:
            print('Descuento sindicato: ','{:.2f}'.format(sindicato()))
            print(separador)
        case 8:
            print('Descuento obra social: ','{:.2f}'.format(obrasocial()))
            print(separador)
        case 9:
            print('Total bruto: ','{:.2f}'.format(totalbruto()))
            print(separador)
        case 10:
            print('Total descuentos: ','{:.2f}'.format(totaldescuentos()))
            print(separador)
        case 11:
            print('Total neto: ','{:.2f}'.format(totalneto()))
            print(separador)
        case 12:
            print('Suma no remunerativa: ','{:.2f}'.format(sumanr))
            print(separador)
        case 13:
            print('Total licencia: ','{:.2f}'.format(totallicencia()))
            print(separador)
        case 14:
            break
        case _:
            print('Opcion no valida')
            print(separador)
