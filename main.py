from replit import clear


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 30,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 60,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

clear()
money = 0

# define a function that ask the user What would you like? (espresso/latte/cappuccino):
def get_user_order():
    # ask the user what they want
    user_order = input("What would you like? (espresso/latte/cappuccino): ")
    # return the user's order
    return user_order


#define a function that turn off the machine
def turn_off_machine():
    # print a message to the user
    print("Thank you for using our coffee machine!")
    # exit the program
    exit()


#define a function that return the resources
def get_resources():
    # return the resources
    return resources


#define a function that print the report
def print_report(resources, money):
    # print the report
    print("The coffee machine has:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


#define a function that check if the resources are enough
def check_resources(resources, user_order):
    # get the ingredients
    ingredients = MENU[user_order]['ingredients']
    # check if the resources are enough
    if user_order == 'espresso':
        if resources['water'] >= ingredients['water'] and resources['coffee'] >= ingredients['coffee']:
            return True
        else:
            return False
    elif resources['water'] >= ingredients['water'] and resources['milk'] >= ingredients['milk'] and resources['coffee'] >= ingredients['coffee']:
        # return True
        return True
    else:
        # return False
        return False

#define a function that process coins
def process_coins():
    # ask the user how much money they want to put in
    print('Please insert the bills: ')
    veinte = int(input('20$ bills: '))
    cincuenta = int(input('50$ bills: '))
    cien = int(input('100$ bills: '))
    doscientos = int(input('200$ bills: '))
    quinientos = int(input('500$ bills: '))
    # calculate the money
    client_money = (veinte * 20) + (cincuenta * 50) + (cien * 100) + (doscientos * 200)
    # return the money
    return client_money
    

#define a function that check if the money is enough
def check_money(client_money, user_order):
    # get the cost
    cost = MENU[user_order]['cost']
    # check if the money is enough
    if client_money >= cost:
        return True
    else:
        # return False
        return False

#define a function that reduces the resources from the user's order
def reduce_resources(resources, user_order):
    # get the ingredients
    ingredients = MENU[user_order]['ingredients']
    # reduce the resources
    if user_order == 'espresso':
        resources['water'] -= ingredients['water']
        resources['coffee'] -= ingredients['coffee']
    else:
        resources['water'] -= ingredients['water']
        resources['milk'] -= ingredients['milk']
        resources['coffee'] -= ingredients['coffee']
    # return the resources
    return resources

#define a function that calculate the change
def calculate_change(client_money, user_order):
    # get the cost
    cost = MENU[user_order]['cost']
    # calculate the change
    change = client_money - cost
    # return the change
    return change



while True:
    coffe = get_user_order()
    if coffe == 'report':
        print_report(resources, money)
    elif coffe == 'off':
        turn_off_machine()
    else:
        if check_resources(resources, coffe) == True:
            cash = process_coins()
            if check_money(cash, coffe) == True:
                reduce_resources(resources, coffe)
                money += MENU[coffe]['cost']
                print(f'Here is your {coffe}!. Enjoy!')
                print(f'Your change is ${calculate_change(cash, coffe)}')
            else:
                print('Sorry, not enough money!')

        else:
            print('Sorry, not enough resources!')
