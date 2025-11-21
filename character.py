class Character:
    def __init__(self,name,health,attack_power):
        self.name=name
        self.health=health
        self.max_health=health
        self.attack_power=attack_power

    def __str__(self):
        return f"{self.name} | {self.health} | {self.max_health} | {self.attack_power}"

    def attack(self,target):
        damage=self.attack_power
        print(f"{self.name} attacks {target.name} for {damage} damage!")

        target.take_damage(damage)

    def take_damage(self,damage_amount):
        self.health-=damage_amount
        if self.health <= 0:
            self.health = 0
        print(f"{self.name} takes {damage_amount} damage! Remaining HP: {self.health}")

    def is_alive(self):
        return self.health>0


class Player(Character):
    def __init__(self,name,health,attack_power,mana):
        super().__init__(name,health,attack_power)
        self.max_mana=mana
        self.mana=mana

    def __str__(self):
        base_status=super().__str__()
        return f"[player] {base_status} | {self.mana}"


    def cast_spell(self,target):
        spell_cost=20
        spell_damage=self.attack_power*3

        if self.mana>=spell_cost:
            self.mana-=spell_cost

            print(f"{self.name} casts a Fireball at {target.name} for {spell_damage} damage!")
            print(f"(Mana remaining: {self.mana})")

            target.take_damage(spell_damage)
        else:
            print(f"{self.name} tries to cast a spell, but not enough mana!")


class Monster(Character):
    def __init__(self,name,health,attack_power,species):
        super().__init__(name,health,attack_power)
        self.species=species

    def __str__(self):
        base_status = super().__str__()
        return f"{base_status} [{self.species}]"





