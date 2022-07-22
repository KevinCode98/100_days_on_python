################### Scope ####################

# Modifying Global Scope

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


# Local Scope 
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength) -> Error! 

# Global Scope 
player_healt = 10
def game():
    def drink_potion():
        potion_strength = 2
        print(player_healt)

    drink_potion()

game()
print(player_healt)

# There is no Block Scope

game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombies", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

# print(new_enemy)



# Global Constants 
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

    
