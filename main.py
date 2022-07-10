from numpy import random
from GunModel import GunModel

mylist = ["CHANGING!!!", "NEW MAG!!!", "SPY PLA- I MEAN, TAC RELOAD!!!", "OUT!!!", "NEUGH!!!"]
akSkin = "                                          *@######&%%%%%%%%&&     ,         /&  \n                        ,,,,,,,,,,,,,,,,,,,//((&&&%%&&%%@@%%//(#%%@//(@@@&&/**% \n        &&%%%%%%%%%%%%&/*///*///*///*///*///*//%%%%%%%%%%%@@, \n   @%%%%%%%%%%%%%%%%%%%*  %%%%# @  #/&(//*(@ \n    %%%%%%%%%%%%%@        %%%%         /*(/(& \n    #%%%%%%@             %%%%           */////  \n     %%.                .%%%             %(/#///*  \n                                           &#/*/// \n                                              /(@ "

def menu():
    print("1: AK-47")
    selection = input("Enter weapon number:")

    if selection == "1":
        ak47 = GunModel(90,30,2,True, akSkin, True, 0)
        weaponOptions(ak47, "AK-47")


def weaponOptions(gun, name):

        print("Equipped:" + name)
        print("-----------------")
        print("1: Gun info")
        print("2: Fire")
        print("3: Reload")
        print("4: Inspect weapon")
        print("5: Tactical reload")
        print("6: Manipulate mag")
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
            print("-----------------")
            print(gun.printGun())
            print("-----------------")
        if option == "5":
            print("-----------------")
            gun.tacticalReload()
            print("-----------------")
        if option == "6":
            print("-----------------")
            print(gun.toggleMag())
            print("-----------------")
        weaponOptions(gun, name)
menu()