from replit import clear
from data import *


clear()
money = 0
while True:
    coffe = get_user_order()
    if coffe == "report":
        print_report(resources, money)
    elif coffe == "off":
        turn_off_machine()
    else:
        if check_resources(resources, coffe) == True:
            cash = process_coins()
            if check_money(cash, coffe) == True:
                reduce_resources(resources, coffe)
                money += MENU[coffe]["cost"]
                print(f"Here is your {coffe}!. Enjoy!")
                print(f"Your change is ${calculate_change(cash, coffe)}")
            else:
                print("Sorry, not enough money!")

        else:
            print("Sorry, not enough resources!")
