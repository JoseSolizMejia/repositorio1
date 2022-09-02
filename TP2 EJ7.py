#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      josel
#
# Created:     02/09/2022
# Copyright:   (c) josel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    lista = [2,4,6,8,10,12]
    alto=lista[0]
    numeros=0
    for i in range(0,len(lista)):
        if lista[i]>alto:
            alto=lista[i]
    print(alto)

if __name__ == '__main__':
    main()
