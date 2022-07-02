class GunModel:
	def __init__(self, res, cap, lod, cha):
		self.reserve = res
		self.capacity = cap
		self.chambered = cha
		self.loaded = lod

	def get_reserve(self):
		return self.reserve

	def get_capacity(self):
		return self.capacity

	def get_chambered(self):		
		return self.chambered

	def get_loaded(self):
		if self.get_chambered():
			tot = self.loaded + 1
		else:
			tot = self.loaded
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

	def canReload(self):

		if self.get_reserve() <= 0:
			print("No ammo. Can't reload.")
			return False
		elif self.get_capacity() + 1 == self.get_loaded():
			print("Already loaded.")
			return False
		else:
			print("Reloading")
			print(str(self.get_capacity()) + str(self.get_loaded()) + str(self.get_chambered()))
			return True

	def standardReload(self):
		if self.canReload():
			if self.get_chambered():
				cap = self.get_capacity() + 1
			else:
				cap = self.get_capacity()

			ammoNeeded = cap - self.get_loaded()

			if ammoNeeded <= self.get_reserve():
				self.set_reserve(self.get_reserve() - ammoNeeded)
				self.set_loaded(self.get_loaded() + ammoNeeded)
			else:
				self.set_reserve(self.get_reserve() - self.get_reserve())
				self.set_loaded(self.get_reserve())
			
			self.set_chambered(True)
		return self.gunStatus()