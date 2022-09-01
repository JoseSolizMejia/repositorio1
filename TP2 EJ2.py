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

    opcion = input("Ingrese una opción: ").lower()
    if opcion == "restar":
            print(numero - numero2)
    elif (opcion == "sumar"):
            print(numero + numero2)
    else:
            print(numero * numero2)
if __name__ == '__main__':
    main()
