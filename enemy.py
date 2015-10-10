import random
from combat import Combat

class Enemy(Combat):

	colors 		   = ['Green', 'Yellow', 'Purple', 'Orange']	
	min_hit_points = 1
	max_hit_points = 1
	min_armor	   = 1
	max_armor	   = 1
	min_experience = 1
	max_experience = 1
	weapon 		   = 'Sword'
	sound		   = 'roar'


	def __init__(self, **kwargs):
		self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
		self.experience = random.randint(self.min_hit_points, self.max_hit_points)
		self.armor 	    = random.randint(self.min_armor, self.max_armor)

		for key, value in kwargs.items():
			setattr(self, key, value)

	def __str__(self):
		return '{}, HP: {}, XP: {}'.format(self.name, self.hit_points, self.experience)

	def speak(self):
		return self.sound.upper()


class Sith(Enemy):
	min_hit_points = 10
	max_hit_points = 15
	min_armor	   = 5
	max_armor	   = 8
	attack_limit   = 14
	dodge_limit	   = 10
	sound		   = 'I have you now.'
	weapon		   = 'Lightsaber'


class Bounty_Hunter(Enemy):
	min_hit_points = 5
	max_hit_points = 10
	min_armor	   = 3
	max_armor	   = 5
	attack_limit   = 4
	dodge_limit	   = 8
	sound		   = 'I am a bounty hunter.'
	weapon		   = 'blaster'


class Stormtrooper(Enemy):
	min_hit_points = 1
	max_hit_points = 2
	min_armor	   = 0
	max_armor	   = 0	
	sound		   = 'These aren\'t the droids we\'re looking for.'
	weapon		   = 'blaster'



	

