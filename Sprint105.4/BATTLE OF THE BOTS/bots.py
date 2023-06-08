from abc import ABC, abstractmethod
import random


class SpaceBotInterface(ABC):
    initial_health = 100
    initial_ammo = 80

    def __init__(self, name):
        """"
        Initialises the bot with the initial health and ammo, and the given name.
        """
        self._name = str(name)
        self._health = SpaceBotInterface.initial_health
        self._ammo = SpaceBotInterface.initial_ammo

    def get_name(self):
        """"
        Returns the name of the bot.
        """
        return self._name

    def get_health(self):
        """"
        Returns the health level of the bot.
        """
        return self._health

    def add_health(self, points):
        """"
        Adds the given points to the instance helath points
        """
        try:
            assert points > 0
            self._health += points
        except Exception:
            return

    def is_alive(self):
        """"
        Returns True if bot is alive (health more than 0), False if it's dead.
        """
        return self._health > 0

    def get_ammo(self):
        """"
        Returns the ammo of the bot.
        """
        return self._ammo

    def add_ammo(self, points):
        """"
        Adds the given points to the instance ammo points
        """
        try:
            assert points > 0
            self._ammo += points
        except Exception:
            return

    def deduct_ammo(self, points):
        """"
        Deducts the given points to the instance ammo points
        """
        try:
            assert points > 0
            self._ammo -= points
        except Exception:
            return

    def take_attack(self, amount):
        """"
        Takes the attack, if health is below 0, it should be set to 0
        """
        try:
            assert amount > 0
            self._health = max([self._health - amount, 0])
        except Exception:
            return

    @abstractmethod
    def attack(self, other_bots):
        """"
        This will be implemented in the child objects. This function gets a list of SpaceBots,
        It should return the selected target for attack (SpaceBot object), and the amount of ammo to use (int).
        Note:
           - If the function raises exception, you will use your turn!
           - If you use more ammo than you have, you will use your turn!
           - If you return values of the wrong type, you will use your turn!
        """
        pass


class RandomAttacker(SpaceBotInterface):

    def attack(self, other_bots):
        """"
        This attack will select a random target, and attack it with 20 ammo.
        """
        target = random.choice(other_bots)
        return target, 20

class IbrahimAttacker1(SpaceBotInterface):
    def attack(self, other_bots):
        """"
        This attack selects the target with the lowest health and uses the exact ammo needed to defeat that target.
        """
        min_health_bot = min(other_bots, key=lambda bot: bot.get_health())

        # Calculate the exact ammo needed to defeat the target
        ammo_needed = min_health_bot.get_health() + 1

        # If the bot has enough ammo, attack with the exact ammo needed; otherwise, attack with available ammo
        ammo_to_use = min(ammo_needed, self.get_ammo())

        return min_health_bot, ammo_to_use

class IbrahimAttacker2(SpaceBotInterface):
    def __init__(self, name):
        super().__init__(name)
        self._attack_count = 0

    def attack(self, other_bots):
        """"
        This attack follows a strategy of 25% ammo attack, followed by a random 15% ammo attack after every two 25% attacks.
        """
        if self._attack_count % 3 == 2:
            # Random 15% ammo attack
            ammo_to_use = int(self.get_ammo() * 0.15)
        else:
            # 25% ammo attack
            ammo_to_use = int(self.get_ammo() * 0.25)

        target = random.choice(other_bots)
        self._attack_count += 1

        return target, ammo_to_use


class Room6Attacker(SpaceBotInterface):
    def attack(self, other_bots):
        for bot in other_bots:
            ordered_health = sorted(other_bots, key=lambda bot: bot.get_health())
            if self._ammo >= ordered_health[0].get_health():
                return ordered_health[0], ordered_health[0].get_health()
            elif self._ammo >= ordered_health[-1].get_health()/4:
                return ordered_health[-1], ordered_health[-1].get_health()/4
            else:
                target = random.choice(other_bots)
                if self._ammo < 20:
                    return  target, self._ammo
                return target, 20


class SmartAttacker(SpaceBotInterface):
    def attack(self, other_bots):
        # Sort the other bots based on their health in ascending order
        sorted_bots = sorted(other_bots, key=lambda bot: bot.get_health())

        # Check if there is a bot with health less than or equal to 1/4 of the attacker's ammo
        for bot in sorted_bots:
            if self._ammo >= self._ammo / 4:
                ammo_to_use = self._ammo / 4
            else:
                ammo_to_use = self._ammo
            if ammo_to_use >= bot.get_health():
                return bot, bot.get_health()

        # If no suitable target found, target the weakest bot with lowest health
        target = sorted_bots[0]
        ammo_to_use = min(self._ammo, 20)
        return target, ammo_to_use


