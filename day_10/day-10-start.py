# Functions with Outputs 
a
def format_name(f_name, l_name):
    """
    Take a first and last name and format it
    to return the title case version of the name.
    """

    if f_name == '' or l_name == '':
        return "You didn't provide valid inputs."
    return f_name + " " + l_name
    
    
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

print (format_name(first_name, last_name))

# Alredy used functions with outputs.
length = len(format_name(first_name, last_name))
print(length)
