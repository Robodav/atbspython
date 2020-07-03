import zombiedice
import random

class MyZombie:
    """Template Zombie class, rolls once then stops."""
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        
        brains = 0
        brains += diceRollResults['brains']
        
class RandomZombie(MyZombie):
    """Randomly decides whether to roll or stop"""
    def __init__(self, name):
        super().__init__(name)
    
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if random.randint(0,1) == 0:
                diceRollResults = zombiedice.roll()
            else:
                break

class TwoBrainsZombie(MyZombie):
    """Stops rolling after getting two brains"""
    def __init__(self, name):
        super().__init__(name)

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains <= 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class TwoShotgunsZombie(MyZombie):
    """Stops rolling after getting two shotguns"""
    def __init__(self, name):
        super().__init__(name)

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class RandomTwoShotguns(MyZombie):
    """Rolls 1 to 4 times but stops after getting two shotguns"""
    def __init__(self, name):
        super().__init__(name)

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        numRolls = random.randint(0,3)
        shotguns = 0
        for i in range(numRolls):
            shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class MoreShotgunsThanBrains(MyZombie):
    """Rolls until it gets more shotguns than brains"""
    def __init__(self, name):
        super().__init__(name)

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        shotguns = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            if shotguns < brains:
                diceRollResults = zombiedice.roll()
            else:
                break

zombies = (
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1\
Shotgun', minShotguns=1),
    MyZombie(name='Roll Once Zombie'),
    RandomZombie(name='Random Zombie'),
    TwoBrainsZombie(name='Until Two Brains Zombie'),
    TwoShotgunsZombie(name='Until Two Shotguns Zombie'),
    RandomTwoShotguns(name='1 to 4 Until Two Shotguns Zombie'),
    MoreShotgunsThanBrains(name='More Shotguns Zombie')
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)