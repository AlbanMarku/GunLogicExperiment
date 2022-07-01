def standardReload(a,b,c):
    ammoReserve = a
    ammoCap = b
    ammoLoaded = c

    if ammoReserve <= 0:
        print("Empty ammo. Can't reload.")
    else:

        if ammoLoaded != 0: #Cap size should be plus one when accounting for round remaining in chamber.
            ammoCap += 1

        if ammoCap == ammoLoaded:
            print("Gun already loaded.")
        else:
            print("CHANGING!!!")
            ammoNeeded = ammoCap - ammoLoaded

            if ammoNeeded < ammoReserve:
                ammoReserve -=ammoNeeded
                ammoLoaded += ammoNeeded
            else:
                ammoLoaded += ammoReserve
                ammoReserve -= ammoReserve
            print("Ammo remaining is " + str(ammoReserve) + " and your mag is loaded to " + str(ammoLoaded))
            
        
res = int(input('res?'))
cap = int(input('cap?'))
lod = int(input('lod?'))

standardReload(res,cap,lod)