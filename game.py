from enemy import Bounty_Hunter
from player import Player
from enemy import Sith
from enemy import Stomtrooper

class Game:
	def setup(self):
		self.player = Player()
		self.enemies = [
			Stomtrooper(),
			Bounty_Hunter(),
			Sith()						
		]

	def get_next_enemy(self):
		try:
			return self.enemies.pop(0)
		except IndexError:
			return None

	def ask_to_dodge(self):
		dodge_answer = input("Do you want to try and dodge? [Y]es/[N]o").lower()
		if dodge_answer in 'yn':
			if self.player.dodge():
				continue
			else:
				self.player.hit_points -= 1
		else:
			print("Please press Y or N to answer.")
			return self.ask_to_dodge()		



	def enemy_turn(self):
		current_enemy = self.get_next_enemy()
		# check to see if the monster attacks		
		if current_enemy.attack():			
		# if so, tell the player
			attack_message = "You are being attacked by {}".format(current_enemy.__str__())
			print(attack_message)
			# check if the player wants to dodge
			self.ask_to_dodge()
		# if the monster isn't attacking, tell that to the player too.
		else:
			print("The enemy Imperial isn't attacking you. Phew!")
	
	def player_turn(self):
		# let the player attack, rest or quit
		player_choice = input("Do you want to [a]ttack, [r]est, or [q]uit the game?").lower()
		if player_choice in 'arq':
		# if they attack:
			if player_choice === 'a':
			# see if the attack is successful
				if self.player.attack():
					current_enemy.hit_points +
				# if dodged, print that
				# if not dodged, subtract the right num of hit points from the monster
			# if not a good attack, tell the player
		# if they rest:
			# call the player.rest() method
		# if they quit, exit the game
		# if they pick anything else, re-run this method

	def cleanup(self):
		# if the monster has no more hit points:
			# up the player's experience
			# print a message
			# get a new monster

	def __init__(self):
		self.setup()

		while self.player.hit_points and self.enemies:
			print(self.player)
			self.enemy_turn()
			self.player_turn()
			self.cleanup()

		if self.player.hit_points:
			print("You win!")
		elif self.enemies:
			print("You lose!")