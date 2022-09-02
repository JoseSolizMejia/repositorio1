#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      josel
#
# Created:     01/09/2022
# Copyright:   (c) josel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    lista = [2,4,6,8,10,12]
    bajo=lista[0]
    numeros=0
    for i in range(0,len(lista)):
        if lista[i]<bajo:
            bajo=lista[i]
    print(bajo)

if __name__ == '__main__':
    main()
