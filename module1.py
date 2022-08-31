#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      josel
#
# Created:     31/08/2022
# Copyright:   (c) josel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    a = 10
    b = 15
    print(a+b)
    #este codigp suma las variables

    a = "¿Como "
    b = "estas?"
    print(a+b)
    #este codigo contatena las variables

    nombre = input("Ingrese su nombre")
    dni = input("Ingrese su dni")
    print(f'El nombre del usuario es {nombre}')
    print(f'La dni es {dni}')
    #este codigo pide al usuario que ingrese sus datos que le solicitamos

if __name__ == '__main__':
    main()
