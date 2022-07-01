from numpy import random

mylist = ["CHANGING!!!", "NEW MAG!!!", "SPY PLA- I MEAN, TAC RELOAD", "OUT!!!", "NEUGH!!!"]

def standardReload(ammoReserve,ammoCap,ammoLoaded):

    if not canReload(ammoReserve,ammoCap,ammoLoaded):
        print(mylist[random.randint(len(mylist))])
        ammoNeeded = ammoCap - ammoLoaded

        if ammoNeeded < ammoReserve:
            
            if ammoLoaded == 0:
                ammoLoaded += ammoNeeded - 1
                ammoReserve -=ammoNeeded -1
            else:
                ammoLoaded += ammoNeeded
                ammoReserve -=ammoNeeded
        else:
            ammoLoaded += ammoReserve
            ammoReserve -= ammoReserve
        print("Ammo remaining is " + str(ammoReserve) + " and your mag is loaded to " + str(ammoLoaded))
    tempAskStats()
            
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
        print("Ammo remaining is " + str(ammoReserve) + " and your mag is loaded to " + str(ammoLoaded))
        tempAskStats()

        
def canReload(ammoReserve, ammoCap, ammoLoaded):
    if ammoReserve <= 0:
        print("No ammo. Can't reload.")
        return True
    elif ammoCap == ammoLoaded:       
        print("Already loaded.")
        return True
    else:
        return False

def tempAskStats():
    res = int(input('res?'))
    cap = int(input('cap?'))
    lod = int(input('lod?'))
    userInput = int(input("1: Conserve ammo or 2: fast reload?"))

    if userInput == 1:
        standardReload(res,cap,lod)
    else:
        tacticalReload(res,cap,lod)

tempAskStats()