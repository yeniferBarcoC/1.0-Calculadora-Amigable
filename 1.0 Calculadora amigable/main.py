""" Programa calculadora artimética amigable#
    Realiza las 4 operaciones (+,-,* /) 
    incorpora al modulo calculadora_aritmetica.py
    Oscar Franco-Bedoya
    Mayo 3-2021 """

#---------------- Zona librerias------------
import calculadora_aritmetica as calc

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
def menu_operaciones():
  print("==================================================")
  print("| Menu")
  print("==================================================")
  print("| Ingresa un numero para realizar la operacion.")
  print("==================================================")
  print("| 1. Calcular suma: (1)")
  print("==================================================")
  print("| 2. Calcular la resta: (2)")
  print("==================================================")
  print("| 3. Calcular multiplicación: (3)")
  print("==================================================")
  print("==================================================")
  print("| 4. Calcular dicvisión: (3)")
  print("==================================================")
   
  opcion = int(input())
  return opcion

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
operacion=menu_operaciones()
numero_1=float(input("ingrese el numero 1:"))
numero_2=float(input("ingrese el numero 2:"))

if operacion==1:
    suma=numero_1+numero_2
    print("la suma es : ", suma)
elif operacion==2:
    resta=numero_1-numero_2
    print("la resta es: ", resta)
elif operacion==3:
    multiplicacion=calc.multiplicar_numeros(numero_1,numero_2)
    print("la multiplicacion es:", multiplicacion)
elif operacion==4:
    division=calc.dividir_numeros(numero_1,numero_2)
    print("La division es:", division)
else:
    print("Ingrese un número valido")


