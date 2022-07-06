from numpy import random
from GunModel import GunModel

mylist = ["CHANGING!!!", "NEW MAG!!!", "SPY PLA- I MEAN, TAC RELOAD!!!", "OUT!!!", "NEUGH!!!"]
akSkin = "                                          *@######&%%%%%%%%&&     ,         /&  \n                        ,,,,,,,,,,,,,,,,,,,//((&&&%%&&%%@@%%//(#%%@//(@@@&&/**% \n        &&%%%%%%%%%%%%&/*///*///*///*///*///*//%%%%%%%%%%%@@, \n   @%%%%%%%%%%%%%%%%%%%*  %%%%# @  #/&(//*(@ \n    %%%%%%%%%%%%%@        %%%%         /*(/(& \n    #%%%%%%@             %%%%           */////  \n     %%.                .%%%             %(/#///*  \n                                           &#/*/// \n                                              /(@ "

def menu():
    print("1: AK-47")
    selection = input("Enter weapon number:")

    if selection == "1":
        ak47 = GunModel(90,30,31,True, akSkin)
        weaponOptions(ak47)


def weaponOptions(gun):

        print("Equipped AK-47")
        print("-----------------")
        print("1: Gun info")
        print("2: Fire")
        print("3: Reload")
        print("4: Inspect weapon")
        option = input("Choose option number:")

        if option == "1":
            print("-----------------")
            print(gun.gunStatus())
            print("-----------------")         
        if option == "2":
            print("-----------------")
            print(gun.tempFire())
            print("-----------------")
        if option == "3":
            print("-----------------")
            print(gun.standardReload())
            print("-----------------")
        if option == "4":
            print(gun.printGun())
        if option == "5":
            gun.tacticalReload()

        weaponOptions(gun)
menu()