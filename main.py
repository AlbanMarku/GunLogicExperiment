from numpy import random
from GunModel import GunModel

mylist = ["CHANGING!!!", "NEW MAG!!!", "SPY PLA- I MEAN, TAC RELOAD!!!", "OUT!!!", "NEUGH!!!"]

# def standardReload(ammoReserve,ammoCap,ammoLoaded):

#     if not canReload(ammoReserve,ammoCap,ammoLoaded):
#         print(mylist[random.randint(len(mylist))])
#         ammoNeeded = ammoCap - ammoLoaded

#         if ammoNeeded < ammoReserve:
            
#             if ammoLoaded == 0:
#                 ammoLoaded += ammoNeeded - 1
#                 ammoReserve -=ammoNeeded -1
#             else:
#                 ammoLoaded += ammoNeeded
#                 ammoReserve -=ammoNeeded
#         else:
#             ammoLoaded += ammoReserve
#             ammoReserve -= ammoReserve
#         printGun()
#         print("Ammo remaining is " + str(ammoReserve) + " and your mag is loaded to " + str(ammoLoaded))
    
#     tempAskStats()
            
def tacticalReload(ammoReserve,ammoCap,ammoLoaded):
    
    if not canReload(ammoReserve,ammoCap,ammoLoaded):
        print(mylist[random.randint(len(mylist))])
        if ammoCap < ammoReserve:
            if ammoLoaded == 0:
                ammoLoaded = ammoCap - 1
                ammoReserve -= ammoCap - 1
            else:
                ammoLoaded = ammoCap
                ammoReserve -= ammoCap - 1
        else:
            ammoLoaded = ammoReserve
            ammoReserve -= ammoReserve
        printGun()
        print("Ammo remaining is " + str(ammoReserve) + " and your mag is loaded to " + str(ammoLoaded))

    tempAskStats()

        
# def canReload(ammoReserve, ammoCap, ammoLoaded):
#     if ammoReserve <= 0:
#         print("No ammo. Can't reload.")
#         return True
#     elif ammoCap == ammoLoaded:       
#         print("Already loaded.")
#         return True
#     else:
#         return False

def tempAskStats():
    res = int(input('Reserve ammo remaining? Typically you got like 90 without scavanger pro:'))
    cap = int(input('Magazine size including the chamber? 31 is typical you know how it is:'))
    lod = int(input('Amount in the mag?:'))
    userInput = int(input("1: Conserve ammo or 2: fast reload?:"))

    if userInput == 1:
        standardReload(res,cap,lod)
    else:
        tacticalReload(res,cap,lod)

def printGun():
    print("                                          *@######&%%%%%%%%&&     ,         /&  \n                        ,,,,,,,,,,,,,,,,,,,//((&&&%%&&%%@@%%//(#%%@//(@@@&&/**% \n        &&%%%%%%%%%%%%&/*///*///*///*///*///*//%%%%%%%%%%%@@, \n   @%%%%%%%%%%%%%%%%%%%*  %%%%# @  #/&(//*(@ \n    %%%%%%%%%%%%%@        %%%%         /*(/(& \n    #%%%%%%@             %%%%           */////  \n     %%.                .%%%             %(/#///*  \n                                           &#/*/// \n                                              /(@ ")

# tempAskStats()
# testing class

def menu():
    print("1: AK-47")
    selection = input("Enter weapon number:")

    if selection == "1":
        print("poop")
        ak47 = GunModel(90,30,31,True)
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
            printGun()

        weaponOptions(gun)
menu()