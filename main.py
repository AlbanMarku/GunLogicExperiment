def standardReload(a,b,c):
    ammoReserve = a
    ammoCap = b
    ammoLoaded = c

    if ammoReserve <= 0:
        print("Empty ammo. Can't reload.")

    elif ammoCap == ammoLoaded:
        print("Gun already loaded.")
    else:
        print("CHANGING!!!")
        ammoNeeded = ammoCap - ammoLoaded
        
        if ammoNeeded < ammoReserve:
            ammoReserve = ammoReserve - ammoNeeded
            ammoLoaded = ammoLoaded + ammoNeeded
        else:
            ammoLoaded = ammoLoaded + ammoReserve
            ammoReserve = 0
        print("Ammo remaining is " + str(ammoReserve) + " and your mag is loaded to " + str(ammoLoaded))
        
        
res = int(input('res?'))
cap = int(input('cap?'))
lod = int(input('lod?'))

standardReload(res,cap,lod)