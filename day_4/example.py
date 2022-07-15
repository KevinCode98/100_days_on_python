import random 
import my_module

random_integer = random.randint(1,10)
# print(random_integer)

random_float = random.random()
# print(random_float)

# How to create a random decimal number between 0 and 5
random_number = round(random_float * 5)
print(random_number)

love_score = random.randint(1, 100)
print(f'Your love score is {love_score}')


# print(my_module.pi) 

# List
states_of_america = ["Delaware", "Pennsylvania"]

print(states_of_america[0])

# states_of_america[-1] -> Last state in the list

states_of_america[1] = "PencilVania"
print(states_of_america)

# Add a new item to end of the list
states_of_america.append("Kevin")
print(states_of_america)

# Add a new list to end of the list
states_of_america.extend(["Pepe", "Juan"])
print(states_of_america)
