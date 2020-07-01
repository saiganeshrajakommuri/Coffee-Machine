
water = 400
milk = 540
money = 550
beans = 120
cups = 9
def check(w, m, bean, cup):
    global water, milk, beans, cups
    flag = 0
    if water - w < 0:
        flag = 1
        print("Sorry, not enough water!")
        print("")
        welcome()
    elif milk - m < 0:
        print("Sorry, not enough milk!")
        print("")
        welcome()
    elif beans - bean < 0:
        print("Sorry, not enough beans!")
        print("")
        welcome()
    elif cups -cup < 0:
        print("Sorry, not enough cups!")
        print("")
        welcome()
    return flag
def raw_fill():
    global water, milk, beans, cups
    water += int(input("Write how many ml of water do you want to add:"))
    milk += int(input("Write how many ml of milk do you want to add:"))
    beans += int(input("Write how many grams of coffee beans do you want to add:"))
    cups += int(input("Write how many disposable cups of coffee do you want to add:"))
    print("")
    welcome()
def buy():
    global water, milk, money, beans, cups
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    print("")
    if choice == "back":
        welcome()
    elif int(choice) == 2:
        if check(350, 75, 20, 1) != 1:
            print("I have enough resources, making you a coffee!")
            print("")
            water = water - 350
            milk = milk - 75
            beans = beans - 20
            money = money + 7
            cups = cups - 1
            welcome()
    elif int(choice) == 3:
        if check(200, 100, 12, 1) != 1:
            print("I have enough resources, making you a coffee!")
            print("")
            water = water - 200
            milk = milk -100
            beans = beans - 12
            money =money + 6
            cups = cups - 1
            welcome()
    elif int(choice) == 1:
        if check(250, 0, 16, 1) != 1:
            print("I have enough resources, making you a coffee!")
            print("")
            water = water - 250
            beans = beans -16
            money = money + 4
            cups =cups - 1
            welcome()
    return 0
def take():
    global money
    print(f"I gave you ${money}".format(money))
    print("")
    money = 0
    welcome()
    
def printing():
    print(f"""The coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{cups} of disposable cups
{money} of money""".format(water, milk, beans, cups, money))
    print("")
    welcome()
    return 0
def welcome():
    while True:
        action = input("Write action (buy, fill, take, remaining, exit):")
        print("")
        if action == "buy":
            buy()
        elif action == "fill":
            raw_fill()
        elif action == "take":        
            take()
        elif action == "remaining":
            printing()
        elif action == "exit":
            break
        return 0
welcome()
