class GunModel:
	def __init__(self, res, cap, lod, cha, skin, magger, story):
		self.reserve = res
		self.capacity = cap
		self.chambered = cha
		self.loaded = lod
		self.skinned = skin
		self.magIn = magger
		self.stored = story

	def get_stored(self):
		return self.stored

	def get_reserve(self): # if no mag then amount of reserve is subbed by how much of the mag was taken away.
		if not self.get_magIn():
			tot = self.reserve - self.get_stored()
		else:
			tot = self.reserve
		return tot

	def get_capacity(self): # if the gun is chambered, capacity is plus one (30 mag to 31 cap total)
		if self.get_chambered():
			tot = self.capacity + 1
		else:
			tot = self.capacity
		return tot

	def get_chambered(self):		
		return self.chambered

	def get_loaded(self): # if mag is out, the amount of rounds in gun is the total loaded subbed by how much of the mag was taken away.
		if not self.get_magIn():
			tot = self.loaded - self.get_stored()

		else:
			tot = self.loaded # else its default
		if tot < 0: #don't go bellow zero
			tot = 0
		return tot

	def get_magIn(self):
		return self.magIn

	def set_reserve(self, x):
		self.reserve = x

	def set_capacity(self, x):
		self.capacity = x

	def set_loaded(self, x):
		self.loaded = x

	def set_chambered(self, x):
		self.chambered = x

	def set_magIn(self, x):
		self.magIn = x

	def set_stored(self, x):
		self.stored = x

	def gunStatus(self): # print the info of the gun object
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

	def canReload(self): # check if can reload.

		if self.get_reserve() <= 0:
			print("No ammo. Can't reload.")
			return False
		elif self.get_capacity() == self.get_loaded():
			print("Already loaded.")
			return False
		elif not self.get_magIn():
			print("You discard your detached mag.")
			return True
		else:
			print("Reloading")
			return True

	def standardReload(self): # calculate how many bullets to fill cap (which changes based on chambered). Then just adjust reserves and loaded based on needed val.
		if self.canReload():

			ammoNeeded = self.get_capacity() - self.get_loaded()

			if ammoNeeded <= self.get_reserve():
				self.set_reserve(self.get_reserve() - ammoNeeded)
				self.set_loaded(self.get_loaded() + ammoNeeded)
			else:
				self.set_reserve(self.get_reserve() - self.get_reserve())
				self.set_loaded(self.get_reserve())
			
			self.set_chambered(True) # helps to keep capacity number updatedl
			self.set_magIn(True) # Tells a mag is in. If the reload happened while the mag was out, the stored ammo is lost since you can't put the old mag back in.
		return "Done"

	def tempFire(self): # reduce loaded by one. If out of ammo, chambered is false. Helps with capacity update.
		if self.get_loaded() <= 0:
			return "No ammo"
		elif self.get_loaded() > 0:
			self.set_loaded(self.get_loaded() - 1)
			if self.get_loaded() <= 0:
				self.set_chambered(False)
				self.set_loaded(0)
		return "Shot"

	def printGun(self): # print skin string ascii.
		return self.skinned

	def tacticalReload(self): # Get the value of a mag. Then regardless of what's needed, reduce reserve by the mag.
		if self.canReload():		
			if self.freshMag() < self.get_reserve():
				self.set_loaded(self.get_capacity())
				self.set_reserve(self.get_reserve() - self.freshMag())
			else:
				self.set_loaded(self.get_reserve())
				self.set_reserve(self.get_reserve() - self.get_reserve())
			self.set_chambered(True)
			self.set_magIn(True)
		return "done"

	def toggleMag(self): # Detach mag from gun leaving a round in the chamber if loaded.
		if self.get_magIn() == True:			
			if not self.get_chambered(): # if the gun isn't chambered, it's impossible for the mag to have rounds. Can be changed to if loaded is < 0 to not go negative which would make the loaded calc turn pos with double neg.
				self.set_stored(0)
			else:
				self.set_stored(self.get_loaded() - 1)
			self.set_magIn(False)
		else:
			self.set_loaded(self.get_stored())
			self.set_magIn(True)
			self.set_chambered(True)
		return "Checkout the gun info now."

	def freshMag(self): # calculates the mag size instead of max capacity. Probs didn't need this if used better object params.
			if self.get_chambered():
				freshMag = self.get_capacity() - 1
			else:
				freshMag = self.get_capacity()	
			return freshMag