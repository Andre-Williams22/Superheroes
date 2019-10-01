import random 

class Ability():
    def __init__(self, name, max_damage):
        ''' <expand for comments>
            Create Instance Variables:
                name: String 
                max_damage: Integer 
            '''
            #TODO: Instatiate the variables listed in the docstring with then 
            #values passed in 
        self.name = name 
        self.max_damage = max_damage
    
    def attack(self):
        ''' <expand for comments>
            Return a value between 0 and the value set by the self.max_damaage.'''
            # TODO: Use random.randint(a, b) to select a random attack value.
            # Return an attack value between 0 and the full attack.
            # Hint: The constructor initializes the maximum attack value.
        attack_strength = random.randint(0, int(self.max_damage))
        return attack_strength

class Weapon(Ability):
    def attack(self):
        ''' <expand for comments>
            This method returns a random value
            between one half to the full attack power of the weapon.
            '''
            # TODO: Use what you learned to complete this method.            
        half_damage = int(self.max_damage) // 2  
        return random.randint(half_damage, int(self.max_damage))

class Armor():
    def __init__(self, name, max_block):
        ''' <expand for comments> 
            Instantiate instance properties:
                name: String
                max_block: Integer
            '''
            #TODO: Create intance variables for the values passed in
        self.name = name 
        self.max_block = max_block
    
    def block(self):
        ''' 
            Return a random value between 0 and the initialized max_block strength. '''
        block_strength = random.randint(0, int(self.max_block))
        return block_strength

class Hero():
    def __init__(self, name, starting_health = 100):
        ''' <expand for comments>
            Instance properties:
                abilities: List
                armors: List
                name: String
                starting_health: Integer
                current_health: Integer
            '''
            # TODO: Initialize instance variables values as instance variables
            # (Some of these values are passed in above,
            # others will need to be set at a starting value)
            # abilities and armors are lists that will contain objects that we can use
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0 

    def add_kills(self, num_kills):
        ''' <expand for commments>
            Update kills with num_kills
            '''
            #TODO: This method should add the number of kills to self.kills 
        self.kills += num_kills  
    
    def add_deaths(self, num_deaths):
        ''' <expand for comments> 
            Update deaths with num_death
            '''
            #TODO: This method should add the number of deaths to self.deaths
        self.deaths += num_deaths
        
    def add_ability(self, ability):
        ''' <expand for comments>
            Add ability to abilities list '''
            #TODO: Add ability object to abilities:List
        self.abilities.append(ability)
    
    def add_weapon(self, weapon):
        ''' <expand for comments>
            Add weapon to self.abilities'''
            # TODO: This method will append the weapon object passed in as an
            # argument to self.abilities.
            # This means that self.abilities will be a list of
            # abilities and weapons.
        self.abilities.append(weapon)

    def add_armor(self, armors):
        ''' <expand for comments>
            Add armor to self.armors
            Armor: Armor Object
            '''
            # TODO: Add armor object that is passed in to `self.armors`
        self.armors.append(armors)
    
    def attack(self):
        ''' <expand for comments>
            Calculate the total damage from all ability attacks.
            return: total:Int
            '''
            # TODO: This method should run Ability.attack() on every ability
            # in self.abilities and returns the total as an integer.
        total_damage = 0 

        for ability in self.abilities:
               total_attack =  ability.attack()
               total_damage += total_attack

        #print("Total damage: {}".format(total_damage))
        return total_damage

    def defend(self, damage_amt = 0):
        ''' <expand for comments>
            Runs `block` method on each armor.
            Returns sum of all blocks
            '''
            # TODO: This method should run the block method on each armor in self.armors
        total_block = 0

        for armor in self.armors:
            block = armor.block()
            total_block += block

        #print("Damage taken: {}".format(damage_amt))

        return abs(damage_amt - total_block)

    def take_damage(self, damage):
        ''' <expand for comments>
            Updates self.current_health to reflect the damage minus the defense.'''
            # TODO: Create a method that updates self.current_health to the current
            # minus the the amount returned from calling self.defend(damage).
        self.current_health = self.current_health - self.defend(damage)

    def is_alive(self):
        ''' <expand for comments>
            Return True or False depending on whether the hero is alive or not.'''
            # TODO: Check whether the hero is alive and return true or false
        return self.current_health > 0 

    def fight(self, opponent):  
        ''' <expand for comments>
            Current Hero will take turns fighting the opponent hero passed in.'''
            # TODO: Fight each hero until a victor emerges.
            # Print the victor's name to the screen.
        while self.is_alive() and opponent.is_alive():
            self_damage = self.attack()
            opp_damage  = opponent.attack()

            opponent.take_damage(self_damage)
            self.take_damage(opp_damage)
            
        if self.is_alive():
            print(f'\n{self.name} won!')
            self.add_kills(1)
            opponent.add_deaths(1)            
        else:
            print(f'\n{opponent.name} won!')
            self.add_deaths(1)
            opponent.add_kills(1)
        
class Team():
    def __init__(self, name):
        ''' <expand for comments>
            Initialize your team with its team name 
            '''
            #TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
        self.name = name
        self.heroes = []
    
    def remove_hero(self, name):
        ''' <expand for comments> 
            Remove hero from heroes list.
            If Hero isn't found return 0.
            '''
            # TODO: Implement this method to remove the hero from the list given their name.
        for hero in self.heroes:
            if len(self.heroes) and name == hero.name:
                self.heroes.remove(hero)
                break
        else:
            return 0 

    def view_all_heroes(self):
        ''' <expand for comments>
            Prints out all heroes to the console.
            '''
            # TODO: Loop over the list of heroes and print their names to the terminal.
        for hero in self.heroes:
            print(hero.name)
    
    def add_hero(self, hero):
        ''' <expand for comments>
            Add Hero object to self.heroes.'''
            # TODO: Add the Hero object that is passed in to the list of heroes in
            # self.heroes
        self.heroes.append(hero)
    
    def attack(self, other_team):
        ''' <expand for comments>
            Battle each team against each other.'''
            # TODO: Randomly select a living hero from each team and have
            # them fight until one or both teams have no surviving heroes.
            # Hint: Use the fight method in the Hero class.
        hero_team = []
        opp_team = []

        for hero in self.heroes:
            if hero.is_alive(): 
                hero_team.append(hero)
        
        for hero in other_team.heroes: 
            if hero.is_alive():
                opp_team.append(hero)
        
        while len(hero_team) > 0 and len(opp_team) > 0:
            hero = random.choice(hero_team)
            opp  = random.choice(opp_team)

            hero.fight(opp) #this is where you have each hero fight each other 

            if hero.is_alive() == True:
                opp_team.remove(opp)
            else: 
                hero_team.remove(hero)
           
    def revive_heroes(self, health=100):
        ''' <expand for comments> 
            Reset all heroes health to starting_health'''
            # TODO: This method should reset all heroes health to their
            # original starting value.
        for hero in self.heroes:
            hero.current_health = health 

    def stats(self):
        ''' <expand for comments>
            Print team statistics'''
            # TODO: This method should print the ratio of kills/deaths for each
            # member of the team to the screen.
            # This data must be output to the console.
            # Hint: Use the information stored in each hero.
        for hero in self.heroes:
            if hero.deaths != 0:
                ratio = (hero.kills / hero.deaths)
                print(f'\n{hero.name}- Kills: {hero.kills} Deaths: {hero.deaths} Ratio: {ratio}')
            else:
                print(f'\n{hero.name}- Kills: {hero.kills} Deaths: {hero.deaths} Ratio: {hero.kills}')
                

class Arena():
    def __init__(self):
        ''' <expand for comments> 
            Instantiate properties
                team_one: None
                team_two: None
            '''
            # TODO: create instance variables named team_one and team_two that
            # will hold our teams.
        team_one = [] 
        team_two = []
    
    def create_ability(self):
        ''' <expand for comments>
            Prompt for Ability information.
            return Ability with values from user Input
            '''
            # TODO: This method will allow a user to create an ability.
            # Prompt the user for the necessary information to create a new ability object.
            # return the new ability object.        
        ability_name = input("Enter an ability name: ")
        max_damage = input(f'Enter damage strength for {ability_name} (0-100): ')
        return Ability(ability_name, max_damage)
    
    def create_weapon(self):
        ''' <expand for comments> 
            Prompt user for Weapon information
            return Weapon with values from user input.
            '''
            # TODO: This method will allow a user to create a weapon.
            # Prompt the user for the necessary information to create a new weapon object.
            # return the new weapon object.
        weapon_name = input("Enter a weapon name: ")
        max_damage  = input(f'Enter damage strength for {weapon_name} (0-100): ')
        return Weapon(weapon_name, max_damage)
    
    def create_armor(self):
        '''<expand for comments> 
            Prompt user for Armor information
            return Armor with values from user input.
            '''
            # TODO:This method will allow a user to create a piece of armor.
            #  Prompt the user for the necessary information to create a new armor
            #  object.            
            #  return the new armor object with values set by user.
        armor_name = input("Enter armor name: ")
        max_block = input(f'Enter max block for {armor_name} (0-100): ')
        return Armor(armor_name, max_block)

    def create_hero(self):
        ''' <expand for comments>
            Prompt user for Hero information
            return Hero with values from user input.
            '''
            # TODO: This method should allow a user to create a hero.
            # User should be able to specify if they want armors, weapons, and
            # abilities.
            # Call the methods you made above and use the return values to build
            # your hero.
            # return the new hero object
        print("\nGreat! Now lets name our Heroes, so we can tell their story!")
        hero_name = input("Name your Hero: ").upper()
        hero = Hero(hero_name)

        equip_ability = True 
        equip_weapon  = True 
        equip_armor   = True 
        
        while equip_ability:
            print(f"\nWould like to equip {hero_name} with abilites?")
            add_ability = input('Y/N: ').upper() 
            if add_ability == 'Y':
                ability = self.create_ability()
                hero.add_ability(ability)
            else:
                equip_ability = False 
        
        while equip_weapon:
            print(f"\nWould like to equip {hero_name} with weapons?")
            add_weapon = input('Y/N: ').upper() 
            if add_weapon == 'Y':
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            else:
                equip_weapon = False 
        
        while equip_armor:
            print(f"\nWould like to equip {hero_name} with armors?")
            add_armor = input('Y/N: ').upper() 
            if add_armor == 'Y':
                armor = self.create_armor()
                hero.add_armor(armor)
            else:
                equip_armor = False 

        return hero 
    
    def build_team_one(self):
        ''' <expand for comments>
            Prompt the user to build team_one 
            '''
            # TODO: This method should allow a user to create team one.
            # Prompt the user for the number of Heroes on team one
            # call self.create_hero() for every hero that the user wants to add to team one.
            # Add the created hero to team one.
        team_name = input("\nCreate a team name for Team 1: ").upper()
        team_count = input(f'How many Heroes do want to add to {team_name}? : ')
        
        self.team_one = Team(team_name)

        for index in range(0, int(team_count)):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        ''' <expand for comments>
            Prompt the user to build team_two
            '''
            # TODO: This method should allow a user to create team two.
            # Prompt the user for the number of Heroes on team two
            # call self.create_hero() for every hero that the user wants to add to team two.
            # Add the created hero to team two.
        team_name = input("\nCreate a team name Team 2: ").upper()
        team_count = input(f'How many Heroes do want to add to {team_name}? : ')
        
        self.team_two = Team(team_name)

        for index in range(0, int(team_count)):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        ''' <expand for comments>
            Battle team_one and team_two together.'''
            # TODO: This method should battle the teams together.
            # Call the attack method that exists in your team objects
            # for that battle functionality.
        self.team_one.attack(self.team_two)
    
    def show_stats(self):
        ''' <expand for comments>
            Prints team statistics to terminal.'''
            # TODO: This method should print out battle statistics
            # including each team's average kill/death ratio.
            # Required Stats:
            #     Declare winning team
            #     Show both teams average kill/death ratio.
            #     Show surviving heroes.
        self.team_one.stats()
        self.team_two.stats()
            


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("\nPlay Again? Y or N: ")

        #Check for Player Input
        if play_again.upper() == "N":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()