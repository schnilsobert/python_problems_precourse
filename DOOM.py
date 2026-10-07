import random
#The Player Layout
class Player:
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level
        self.fullhealth = level * 10
        self.fullpower = 2 + (level * 2)
        #temp. für kämpfe:
        self.temp_health = self.fullhealth
        self.temp_power = self.fullpower
#Player is getting attacked
    def player_receive_damage(self, monster_damage: float):
        self.temp_health -= monster_damage
        return self.temp_health 
#Level up after a successfull fight
    def level_up(self):
        self.level += 1
        self.fullhealth += random.randint(8, 14)
        self.fullpower += round(random.uniform(2, 4), 2)
        return
#Player stats
    def stats(self):
        print(f"""
        -----Stats von {self.name}-----
        Level:  {self.level}
        Health: {self.temp_health}/{self.fullhealth}
        Power:  {self.temp_power}
        """)
#resets stats after fight
    def reset_stats(self):
        self.temp_health = self.fullhealth
        self.temp_power = self.fullpower
        return self.temp_health, self.temp_power
#--- Enemy Layout ---
class Monster:
    def __init__(self, monster_name: str, monster_level: int):
        self.monster_name = monster_name 
        self.monster_level = monster_level
        self.monster_fullhealth = monster_level * 10
        self.monster_fullpower = 2 + (monster_level * 2)
        self.monster_temp_health = self.monster_fullhealth
        self.monster_temp_power = self.monster_fullpower
#Enemy gets attacked
    def monster_receive_damage(self, player_damage: float):
        self.monster_temp_health -= player_damage
        return self.monster_temp_health
#last power up before death
    def rage(self) -> bool:
        if True:
            self.monster_temp_power *= 1.05
            return self.monster_temp_power
        else:
            pass 
#Enemy stats        
    def stats(self):
            print(f"""
            -----Stats von {self.monster_name}-----
            Level:  {self.monster_level}
            Health: {self.monster_temp_health}/{self.monster_fullhealth}
            Power:  {self.monster_temp_power}
            """)
#Mapping the whole fight
def kampf(held, ungeziefer) -> bool:
#decision rather to fight or run
    chance = input(f"The scary {ungeziefer.monster_name}, Level {ungeziefer.monster_level} is in front of you! Are you up for a real Battle or do you try and run away, like always? (run/fight) ")
    if chance == "run": 
        #dependent on the player/enemy level ratio calc win chance
        win = random.random() < (held.level / ungeziefer.monster_level)* random.uniform(0.6, 1.0)
        if win:
            #won
            print("Damn you are fast! You successfully got away!")
            return True
        else:
            #lost
            print(f"Too slow! {ungeziefer.monster_name} got you good :( ")
            return False
#fight begins
    print("So you wanna fight? LET'S FIGHT!!!")
    #round count
    runde : int = 1
    while(True):
        print(f"---Runde {runde}---")

        player_damage : float = round(held.temp_power + round((held.temp_power * random.uniform(-0.1, 0.1))) * (-1 if random.random() < 0.1 else 1), 2)
        # 90% für positiven damage am monster
        if player_damage > 0:
            print(f"That's what we call a proper strike! You hit {ungeziefer.monster_name} and dealt {player_damage} damage!")
        # 10% für negativen damage (heal) am monster
        elif player_damage < 0:
            print(f"Uhhh, you slipped and missed. Giving {ungeziefer.monster_name} time to heal {player_damage} health!")
        ungeziefer.monster_receive_damage(player_damage)
        #health = 0 -> enemy besiegt
        if ungeziefer.monster_temp_health <= 0:
            print(f"{ungeziefer.monster_name} couldn't handle you as an enemy. It's over!")
            return True
        # if ungeziefer.monster_temp_health > 0 and ungeziefer.monster_temp_health <= (0.1 * ungeziefer.monster_fullhealth):
        #     ungeziefer.temp_power = ungeziefer.rage(ungeziefer.monster_temp_power)
        #     print(f"{ungeziefer.monster_name} is nearly Dead, but its not over yet!!!")
        ungeziefer.stats()
        monster_damage : float = ungeziefer.monster_temp_power * round((-1 if random.random() < 0.1 else 1), 2)
        if monster_damage > 0:
            print(f"Ouch! {ungeziefer.monster_name} got u good! And dealt {monster_damage} damage!")
        elif monster_damage < 0:
            print(f"Uhhh, you slipped and missed. Giving {ungeziefer.monster_name} time to heal {player_damage} health!")
        held.player_receive_damage(monster_damage)

        if held.temp_health <= 0:
            print(f"DAAMNN, you're dead!")
            return False
        if held.temp_health > 0 and held.temp_health <= (0.1 * held.fullhealth):
            print("It's nearly over, little Puppy!")
        held.stats()
        ungeziefer.stats()
        runde += 1
        print("Ready for the next round?!")
        confirm = input("Press enter to continue ")
        


     
    
        
def main():
    spieler_name = input("Whats your name? ")
    while True:
        try:
            spieler_level = int(input("And your level? "))
            break

        except ValueError:
            print("Give a number you DUMBASS! ")
    held = Player(name = spieler_name, level = spieler_level)
    
    while True:
        monstername = input("Who are you up against? ")
        while True:
            try:
                monsterlevel = int(input("What level is your opponent? "))
                break
            except ValueError:
                print("A number you smartypants! ")
        
        ungeziefer = Monster(monster_name = monstername, monster_level= monsterlevel)
        sieg = kampf(held, ungeziefer)
        if sieg:
            print(f"Congrats, {ungeziefer.monster_name} is defeated!")
            print("Level UP!!!")
            held.level_up()
            held.temp_health = held.fullhealth
            held.temp_power = held.fullpower
            held.stats()

        else: 
            print(f"{ungeziefer.monster_name} won... Better luck next time! LOSER hehe")
            print("Wanna play another round?")
        #weiterspielen?
        weiter = input("Another round? (y/exit) ")
        if weiter == "exit":
            print("Have a good one!")
            break    


if __name__ == "__main__":
    main()