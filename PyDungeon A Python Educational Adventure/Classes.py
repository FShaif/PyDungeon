import random


class Item: # Has 3 subclasses Weapon, Armor, Potion
    def __init__(self, name ='Unknown', amount = 0, price = 0):
        self.name = name
        self.amount = amount
        self.price = price


class Weapon(Item): # w1 = Weapon(name, amount, price, attack_damage, crit_chance)
    def __init__(self, name, amount, price, damage = 0, crit = 0):
        super().__init__(name, amount, price)
        self.attack_damage = damage
        self.crit_chance = crit

    def __str__(self):
        return f"{self.name} , You currently have x{self.amount} in bag, each worth {self.price} Gold, " \
               f"it Provides {self.attack_damage} Attack, and {self.crit_chance} Critical chance when equipped"


commonSword = Weapon("Common Sword", 0, 10, 5, 0)
rareSword = Weapon("Rare Sword", 0, 30, 10, 2)
epicSword = Weapon("Epic Sword", 0, 70, 20, 4)
legendarySword = Weapon("Legendary Sword", 0, 200, 30, 6)


class Armor(Item): # a1 = Armor(name, amount, price, defence_pt, dodge_chance)
    def __init__(self, name, amount, price, defence_pt = 0, dodge_chance = 0):
        super().__init__(name, amount, price)
        self.defence_pt = defence_pt
        self.dodge_chance = dodge_chance

    def __str__(self):
        return f"{self.name} , You currently have x{self.amount} in bag, each worth {self.price} Gold, " \
               f"it Provides {self.defence_pt} Defence, and {self.dodge_chance} Dodging chance when equipped"


commonArmor = Armor("Common Armor", 0, 10, 1, 0)
rareArmor = Armor("Rare Armor", 0, 30, 4, 2)
epicArmor = Armor("Epic Armor", 0, 70, 6, 4)
legendaryArmor = Armor("Legendary Armor", 0, 200, 8, 6)


class Potion(Item): # drink it to heal
    def __init__(self, name, amount, price, restore_hp = 0):
        super().__init__(name, amount, price)
        self.restore_hp = restore_hp

    def __str__(self):
        return f"{self.name} , You currently have x{self.amount} in bag, each worth {self.price} Gold, " \
               f"it Provides {self.restore_hp} Health points when used"


smallPotion = Potion("Small Potion", 0, 10, 10)
mediumPotion = Potion("Medium Potion", 0, 20, 20)
largePotion = Potion("Large Potion", 0, 30, 40)


# has 1 object computer and 1 sub class Human
class Player:
    def __init__(self, name , base_health_points = 100, base_attack_damage = 20, base_defence = 2, base_crit_chance = 1,
                 base_dodge_chance = 1):
        self.name = name
        self.base_health_points = base_health_points
        self.health_points = self.base_health_points
        self.base_attack_damage = base_attack_damage
        self.attack_damage = self.base_attack_damage
        self.base_defence = base_defence
        self.defence_pt = self.base_defence
        self.base_crit_chance = base_crit_chance
        self.crit_chance = self.base_crit_chance
        self.base_dodge_chance = base_dodge_chance
        self.dodge_chance = self.base_dodge_chance

    def __str__(self):
        return f"Name: {self.name}, Current Health: {self.health_points} / {self.base_health_points}\n" \
               f"Attack Damage: {self.attack_damage}, Defence Point: {self.defence_pt}\n" \
               f"Chance of inflicting a critical hit on the enemy: {self.crit_chance}/10\n" \
               f"Chance of dodging the enemy attack: {self.dodge_chance}/10\n"

    def attack(self, other):
        chance_to_hit = random.randint(0, 10)
        if chance_to_hit > other.dodge_chance:
            damage = (self.attack_damage - other.defence_pt)
            chance_to_critically_hit = random.randint(1, 10)
            if chance_to_critically_hit <= self.crit_chance:
                damage_dealt = (random.randint(damage // 2, damage)) * 2
                other.health_points = other.health_points - damage_dealt
                print(self.name + " deals " + str(damage_dealt) + " Critical Damage !")
            else:
                damage_dealt = random.randint(damage // 2, damage)
                other.health_points = other.health_points - damage_dealt
                print(self.name + " deals " + str(damage_dealt) + " damage !")
        else:
            print(self.name + " Missed !!!")


# has one object human
class Human(Player):
    def __init__(self, name, base_health_points = 100, base_attack_damage = 10, base_defence = 2, base_crit_chance = 0,
                 base_dodge_chance = 0, gold = 100,  current_weapon = commonSword, current_armor = commonArmor):
        super().__init__(name , base_health_points, base_attack_damage, base_defence, base_crit_chance,
                 base_dodge_chance)

        self.list0fWeapons = [commonSword, rareSword, epicSword, legendarySword]
        self.list0fArmors = [commonArmor, rareArmor, epicArmor, legendaryArmor]
        self.list0fPotions = [smallPotion, mediumPotion, largePotion]
        self.gold = gold
        self.current_weapon = current_weapon
        current_weapon = self.list0fWeapons[0]
        self.current_armor = current_armor
        current_armor = self.list0fArmors[0]

    def __str__(self):
        return f"Name: {self.name}, Current Health: {self.health_points} / {self.base_health_points}\n" \
               f"Attack Damage:{self.attack_damage}, Defence Point:{self.defence_pt}\n" \
               f"Chance of inflicting a critical hit on the enemy: {self.crit_chance}/10\n" \
               f"Chance of dodging the enemy attack: {self.dodge_chance}/10\n" \
               f"{self.current_weapon.name} and {self.current_armor.name} currently equipped\n" \
               f"You currently have:\n" \
               f"{self.gold} Gold Coins\n" \
               f"x{smallPotion.amount} of Small Potions\n" \
               f"x{mediumPotion.amount} of Medium Potions\n" \
               f"x{largePotion.amount} of Large Potions\n"

    def get_reward(self): # only reward potions for now
        randPotion = random.randint(1,3)
        if randPotion == 1:
            print("Player found L potion x1 !!!")
            largePotion.amount += 1
        elif randPotion == 2:
            print("Player found M potion x1 !!!")
            mediumPotion.amount += 1
        elif randPotion == 3:
            print("Player found S potion x1 !!!")
            smallPotion.amount += 1


    def modify_attack_damage(self):
        if self.current_weapon == self.list0fWeapons[0]:
            self.attack_damage = self.base_attack_damage + self.list0fWeapons[0].attack_damage
            self.crit_chance = self.base_crit_chance + self.list0fWeapons[0].crit_chance

        if self.current_weapon == self.list0fWeapons[1]:
            self.attack_damage = self.base_attack_damage + self.list0fWeapons[1].attack_damage
            self.crit_chance = self.base_crit_chance + self.list0fWeapons[1].crit_chance

        if self.current_weapon == self.list0fWeapons[2]:
            self.attack_damage = self.base_attack_damage + self.list0fWeapons[2].attack_damage
            self.crit_chance = self.base_crit_chance + self.list0fWeapons[2].crit_chance

        if self.current_weapon == self.list0fWeapons[3]:
            self.attack_damage = self.base_attack_damage + self.list0fWeapons[3].attack_damage
            self.crit_chance = self.base_crit_chance + self.list0fWeapons[3].crit_chance

        return self.attack_damage, self.crit_chance


    def modify_defence_pt(self):
        if self.current_armor == self.list0fArmors[0]:
            self.defence_pt = self.base_defence + self.list0fArmors[0].defence_pt
            self.dodge_chance = self.base_dodge_chance + self.list0fArmors[0].dodge_chance

        if self.current_armor == self.list0fArmors[1]:
            self.defence_pt = self.base_defence + self.list0fArmors[1].defence_pt
            self.dodge_chance = self.base_dodge_chance + self.list0fArmors[1].dodge_chance

        if self.current_armor == self.list0fArmors[2]:
            self.defence_pt = self.base_defence + self.list0fArmors[2].defence_pt
            self.dodge_chance = self.base_dodge_chance + self.list0fArmors[2].dodge_chance

        if self.current_armor == self.list0fArmors[3]:
            self.defence_pt = self.base_defence + self.list0fArmors[3].defence_pt
            self.dodge_chance = self.base_dodge_chance + self.list0fArmors[3].dodge_chance

        return self.defence_pt, self.dodge_chance

    def attack(self, other):
        chance_to_hit = random.randint(0, 10)
        if chance_to_hit > other.dodge_chance:
            damage = (self.attack_damage - other.defence_pt)
            chance_to_critically_hit = random.randint(1, 10)
            if chance_to_critically_hit <= self.crit_chance:
                damage_dealt = (random.randint(damage // 2, damage)) * 2
                other.health_points = other.health_points - damage_dealt
                print(self.name + " deals " + str(damage_dealt) + " Critical Damage !")
            else:
                damage_dealt = random.randint(damage // 2, damage)
                other.health_points = other.health_points - damage_dealt
                print(self.name + " deals " + str(damage_dealt) + " damage !")
        else:
            print(self.name + " Missed !!!")





