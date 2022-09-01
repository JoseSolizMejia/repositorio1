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
    mail = input("Ingrese su mail: ")
    mail11 = mail.replace("@","Q ")
    if (mail11 != mail):
        print("el mail es correcto")
    else:
        print("el mail no es correcto")

if __name__ == '__main__':
    main()
