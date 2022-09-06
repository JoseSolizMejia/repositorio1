#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      josel
#
# Created:     01/09/2022
# Copyright:   (c) josel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    numero = int(input("Ingrese un número: "))
    numero2 = int(input("Ingrese otro número: "))
    print ("1.SUMAR","2.RESTAR","3.MULTIPLICAR")
    while True:
        opciones = ["restar","sumar","multiplicar"]
        opcion = input("Ingrese una opción: ").lower()
        if opcion == "sumar":
            print(numero+numero2)
            break
        if opcion == "restar":
            print(numero-numero2)
            break
        if opcion == "multiolicar":
            print(numero*numero2)
            break



if __name__ == '__main__':
    main()
