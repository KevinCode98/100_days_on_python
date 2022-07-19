programming_dictionary = {
        "Bug": "An error in a program that prevents the program from running as expected.",
        "Function": "A piece of code that you can easily call over and over again.",
        123: "This is a example about key number"
        }

print(programming_dictionary["Function"])
print(programming_dictionary[123])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The  action of doing something over and over again."
print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictiornary
programming_dictionary["Bug"]  = "A moth in your computer."
print(programming_dictionary)


# Loop through a dictionary
for key in programming_dictionary:
    print(str(key) + ": ", programming_dictionary[key])

##############################################

#Nesting
capitals = {
        "France": "Paris",
        "Germany": "Berlin",
        }

# Nesting a List in a Dictionary
travel_log = {
        "France": ["Paris", "Lille", "Dijon"],
        "Germany": ["Berlin", "Hamburg", "Stuttgart"],
        }

# Nesting Dictionary in a Dictionary
travel_log = {
        "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visit": 12},
        "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visit": 5},
        }

# Nesting Dictionary in a List
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visit": 12
        },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visit": 5
    },
]
