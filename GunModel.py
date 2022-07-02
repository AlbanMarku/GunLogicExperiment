class GunModel:
	def __init__(self, res, cap, lod, cha):
		self.reserve = res
		self.capacity = cap
		self.chambered = cha
		if cha:
			self.loaded = lod + 1
		else:
			self.loaded = lod

	def get_reserve(self):
		return self.reserve

	def get_capacity(self):
		return self.capacity

	def get_loaded(self):
		return self.loaded

	def get_chambered(self):		
		return self.chambered

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
		rounds = str(self.loaded) + " rounds in gun"
		capper = str(self.capacity) + " mag capacity"
		remain = str(self.reserve) + " ammo remaining"
		print(rounds)
		print(capper)
		print(remain)
		print(dialogue)

	def canReload(self):

		if self.get_reserve() <= 0:
			print("No ammo. Can't reload.")
			return True
		elif self.get_capacity() + 1 == self.get_loaded():
			print("Already loaded.")
			return True
		else:
			print("Reloading")
			print(str(self.get_capacity()) + str(self.get_loaded()) + str(self.get_chambered()))
			return False