def greet():
    print("Hello Kevin")
    print("How do you do Jack Bauer?")
    print("Isn't the wather nice today?")
    
greet()

# Functions that allows for input

def greet_with_name(name):
    print(f'Hello {name}')
    print(f'How do you do {name}?')

greet_with_name("Angela")

# Function with mora than 1 input
def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}')

greet_with('Juan', 'Guadalajara')


# Function with keword arguments
greet_with(location='Mexico', name='Ruben')
