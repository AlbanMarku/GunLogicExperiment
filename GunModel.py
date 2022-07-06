class GunModel:
	def __init__(self, res, cap, lod, cha, skin):
		self.reserve = res
		self.capacity = cap
		self.chambered = cha
		self.loaded = lod
		self.skinned = skin

	def get_reserve(self):
		return self.reserve

	def get_capacity(self):
		if self.get_chambered():
			tot = self.capacity + 1
		else:
			tot = self.capacity
		return tot

	def get_chambered(self):		
		return self.chambered

	def get_loaded(self):
		return self.loaded

	def set_reserve(self, x):
		self.reserve = x

	def set_capacity(self, x):
		self.capacity = x

	def set_loaded(self, x):
		self.loaded = x

	def set_chambered(self, x):
		self.chambered = x

	def gunStatus(self):
		if self.get_chambered() == True:
			dialogue = "Gun is chambered"
		else:
			dialogue = "Gun is empty"
		rounds = str(self.get_loaded()) + " rounds in gun"
		capper = str(self.get_capacity()) + " mag capacity"
		remain = str(self.get_reserve()) + " ammo remaining"
		print(rounds)
		print(capper)
		print(remain)
		print(dialogue)
		return "Updated info"

	def canReload(self):

		if self.get_reserve() <= 0:
			print("No ammo. Can't reload.")
			return False
		elif self.get_capacity() == self.get_loaded():
			print("Already loaded.")
			return False
		else:
			print("Reloading")
			return True

	def standardReload(self):
		if self.canReload():

			ammoNeeded = self.get_capacity() - self.get_loaded()

			if ammoNeeded <= self.get_reserve():
				self.set_reserve(self.get_reserve() - ammoNeeded)
				self.set_loaded(self.get_loaded() + ammoNeeded)
			else:
				self.set_reserve(self.get_reserve() - self.get_reserve())
				self.set_loaded(self.get_reserve())
			
			self.set_chambered(True)
		return "Done"

	def tempFire(self):
		if self.get_loaded() > 0:
			self.set_loaded(self.get_loaded() - 1)
			if self.get_loaded() <= 0:
				self.set_chambered(False)
				self.set_loaded(0)
		return "Shot"

	def printGun(self):
		return self.skinned

	def tacticalReload(self):
		if self.canReload():

			if self.get_capacity() < self.get_reserve():
				self.set_loaded(self.get_capacity())
				self.set_reserve(self.get_reserve() - self.get_capacity())
			else:
				self.set_loaded(self.get_reserve())
				self.set_reserve(self.get_reserve() - self.get_reserve())

			self.set_chambered(True)

# def tacticalReload(ammoReserve,ammoCap,ammoLoaded):
    
#     if not canReload(ammoReserve,ammoCap,ammoLoaded):
#         print(mylist[random.randint(len(mylist))])
#         if ammoCap < ammoReserve:
#             if ammoLoaded == 0:
#                 ammoLoaded = ammoCap - 1
#                 ammoReserve -= ammoCap - 1
#             else:
#                 ammoLoaded = ammoCap
#                 ammoReserve -= ammoCap - 1
#         else:
#             ammoLoaded = ammoReserve
#             ammoReserve -= ammoReserve
#         printGun()
#         print("Ammo remaining is " + str(ammoReserve) + " and your mag is loaded to " + str(ammoLoaded))

#     tempAskStats()