def standardReload(a,b,c):
    ammoReserve = a
    ammoCap = b
    ammoLoaded = c

    if ammoReserve <= 0:
        print("Empty ammo. Can't reload.")
    else:

        if ammoCap == ammoLoaded:
            print("Gun already loaded.")
        else:
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
            
def tacticalReload(a,b,c):
    ammoReserve = a
    ammoCap = b
    ammoLoaded = c

    if ammoReserve <= 0:
        print("Empty ammo. Can't reload.")
    else:

        if ammoCap == ammoLoaded:
            print("Gun already loaded")
        else:
            print("TAC RELOAD!!!")
            ammoNeeded = ammoCap - ammoLoaded
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

res = int(input('res?'))
cap = int(input('cap?'))
lod = int(input('lod?'))

standardReload(res,cap,lod)