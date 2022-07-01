def standardReload(a,b,c):
    ammoReserve = a
    ammoCap = b
    ammoLoaded = c

    if not canReload(ammoReserve,ammoCap,ammoLoaded):
        print("CHANGING!!!")
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
            
def tacticalReload(ammoReserve,ammoCap,ammoLoaded):
    
    if not canReload(ammoReserve,ammoCap,ammoLoaded):
        print("TAC RELOAD!!!")
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

def canReload(ammoReserve, ammoCap, ammoLoaded):
    if ammoReserve <= 0:
        print("No ammo. Can't reload.")
        return True
    elif ammoCap == ammoLoaded:       
        print("Already loaded.")
        return True
    else:
        return False


res = int(input('res?'))
cap = int(input('cap?'))
lod = int(input('lod?'))

tacticalReload(res,cap,lod)