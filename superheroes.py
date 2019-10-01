import random

class Ability:

	def __init__ (self, name, max_damage):
		self.name = name
		self.max_damage = max_damage



	def attack(self):

		return random.randint(0, self.max_damage)

class Armor:

	def __init__ (self, name, max_block):
		# create instance variables for the values passed in 
		self.name = name
		self.max_block = max_block


	def block(self):
		''' Return a random value between 0 and the initialized max_block strength. ''' 
		return random.randint(0, self.max_block)


class Hero:

	def __init__ (self, name, starting_health=100):
		self.name = name 
		self.abilities = []
		self.armors = []
		self.starting_health = starting_health
		self.current_health = starting_health
		self.kills = 0
		self.deaths = 0

	def add_ability(self, ability):
		 
  		# TODO: Add ability object to abilities:List
  		self.abilities.append(ability)

	def attack(self):
		'''Calculate the total damage from all ability attacks.return: total:Int
		'''
    # TODO: This method should run Ability.attack() on every ability
    # in self.abilities and returns the total as an integer.
		hit = 0
		for item in self.abilities:
			hit += item.attack()
		return hit

	def add_armor(self, armor):
		'''Add armor to self.armors Armor: Armor Object'''
		#TODO: Add armor object that is passed in to `self.armors`
		self.armors.append(armor)
	def add_deaths(self, num_deaths):
    		''' Update deaths with num_deaths'''
    		self.deaths += num_deaths
  		
		  
        
	def add_kill(self, num_kills):
    		self.kills += num_kills
    		''' Update kills with num_kills'''


	def defend(self):
		armors = 0 
		for armor in self.armors:
			armors += armor.block()
		return armors

	def take_damage(self, damage):
		health = damage - self.defend()
		self.current_health = health
		


		
	def is_alive(self):
		if self.current_health > 0:
			return True
		else:
			return False
		'''Return True or False depending on whether the hero is alive or not.
		'''
  # TODO: Check whether the hero is alive and return true or false
	def fight(self, opponent):
		''' Current Hero will take turns fighting the opponent hero passed in.'''
		while self.is_alive() >= 0 and opponent.is_alive() >= 0:
			self.take_damage(opponent.attack())
			opponent.take_damage(self.attack())
		if self.current_health < 0:
			print('=' * 24)
			print('BATTLE:\n')
			print(f'\n{self.name} beat {opponent.name} and won!')
			self.add_kill(1)
			opponent.add_deaths(1)
			break
		else:
			print('=' * 24)
			print('Battle:\n')
			opponent.add_deaths(1)
			self.add_kill(1)
			print(f'{opponent.name} won!')


class Team:
	def __init__(self, name):
		self.name = name
		hero_list = []

	def add_hero(self, hero):
		self.hero_list.append(hero)

	def remove_hero(self, name):
		for hero in self.hero_list:
			if hero.name = name:
				self.hero_list.remove(hero)
				break
		return 0

	def view_all_heroes(self):
		for hero in self.hero_list:
			print(hero.name)


	''' Checks to see if members in team are still alive'''
	def team_alive(self):
		heroes = []






		
		    	
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)