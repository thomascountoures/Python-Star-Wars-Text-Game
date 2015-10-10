import random
from combat import Combat


class Player(Combat):
	base_hit_points = 10
	base_armor		= 5
	attack_limit 	= 10
	experience 		= 0
	dodge_limit		= 10

	def __init__(self, **kwargs):
		self.name		= input("Name: ")
		self.weapon 	= self.get_weapon()
		self.hit_points = self.base_hit_points
		self.armor 		= self.base_armor		

		for key, value in kwargs.items():
			setattr(self, key, value)

	def __str__(self):
		return '{}, HP: {}, XP: {}'.format(self.name, self.hit_points, self.experience)


	def get_weapon(self):
		weapon_choice = input("Weapon: ([S]word, [L]ightsaber, S[t]eel Chair")

		if weapon_choice in 'slt':
			if weapon_choice == 's':
				return 'sword'
			elif weapon_choice == 'l':
				return 'lightsaber'
			elif weapon_choice == 't':
				return 'steel chair'
		else:
			print("Please press S, L, or T to get a weapon.")
			return self.get_weapon()
		

	def attack(self):
		roll = random.randint(1, self.attack_limit)

		if self.weapon == 'sword':
			roll += 1
		elif self.weapon == 'lightsaber':
			roll += 1

		 if roll > 4:
		 	self.experience += 1
		 	return true

	def rest(self):
		if self.hit_points < self.base_hit_points:
			self.hit_points += 1

	def leveled_up(self):
		return self.experience >= 5



	

	
