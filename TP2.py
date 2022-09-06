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
    while True:
        numero = int(input("Ingrese número impar: "))
        if(numero%2!=0):
            print("El numero es impar")
            break
if __name__ == '__main__':
    main()
