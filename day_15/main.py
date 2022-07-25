MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """ Returns True when order can be made, False if ingredients are insufficent. """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry ther is not enough {item}.")
            return False
    return True


def process_coins():
    """ Return the total calculated from coins inserted. """
    total = 0

    print("Please insert coins.")
    total += int(input("How many quaters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_recived, drink_cost):
    """ Return true when the payment is accpeted, or False if money is insufficent. """
    global profit
    if money_recived >= drink_cost:
        profit += drink_cost 
        change = round(money_recived - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else: 
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffe(drink_name, order_ingredients):
    """ Deduct the required ingredients from the resources. """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


is_on = True
while is_on:

# TODO 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):."
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO 2. Turn off the Coffe Machine by entering "off" to the prompt.
    if choice == "off":
        is_on = False

        
    # TODO 3. Print report
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milf: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")


    else:
        # TODO 4. Check resources sufficient? 
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            
            # TODO 5. Process coins
            payment = process_coins()

            # TODO 6. Check transaction successful?
            if is_transaction_successful(payment, drink["cost"]):

                # TODO 7. Make Coffe
                make_coffe(choice, drink["ingredients"])
