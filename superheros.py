import random

class Ability:

	def __init__ (self, name, max_damage):
		self.name = name
		self.max_damage = max_damage
		pass



	def attack(self):

		attack_strength = random.randint(0, self.max_damage)

		return attack_strength

class Armor:

	def __init__ (self, name, max_block):
		# create instance variables for the values passed in 
		self.name = name
		self.max_block = max_block

		pass


	def block(self):
		''' Return a random value between 0 and the initialized max_block strength. ''' 

		block_amt = random.randint(0, self.max_block)

		pass

class Hero:

	def __init__ (self, name, starting_health=100, current_health):
		self.name = name 
		self.abilities = []
		self.armors = []
		self.starting_health = starting_health
		# current health in constructor?

		self.current_health = current_health
		






if __name__ =='__main__':
	# If you run this file from the terminal
	# this block is executed
	my_hero = Hero("Grace Hopper", 200)
	print(my_hero.name)
	print(my_hero.current_health())
