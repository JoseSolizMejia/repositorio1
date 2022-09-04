#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      josel
#
# Created:     01/09/2022
# Copyright:   (c) josel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    lista = [2,4,8,10,12]
    contador=0
    numeros=0
    for x in lista:
        contador = contador + x

    for i in lista:
        numeros = numeros + 1

    promedio = contador / numeros
    print(promedio)
if __name__ == '__main__':
    main()
