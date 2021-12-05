from items import *
# This program acts as an interface for buying food items from a Restaurant
# reciept for the order of the customer
print("Welcome to Burger Fest")
proceed = True
orderList = []
# This creates menu object with the list of items on the Burger Fest Menu
menu = ListObject("BURGER FEST MENU", itemList)
AddOnMenu = ListObject("ADD ON MENU", AddOnList)
# the get_order function prompts the user to enter valid information need to create an order


def get_order(value):
    # orderList is populated with each order that is made by the user
    # the orderList is needed evaluate the customers receipt
    global orderList
    # value which is user input indicates which item on the menu that is selected
    name = menu.get_list()[value]
    # prompts the user to enter the size of the current order
    size = input("small -s, Medium -m, Large -l? ")
    # this conditional seperates burger orders from drink orders and hence asks appropriate questions for each item ordered
    if(value <= 3):
        # prompts the user to enter the burger type, you can skip this by hitting the enter button
        burger_type = input(
            "NORMAL or SPICY: ")
        if burger_type.lower != "normal" or "spicy":
            burger_type = "normal"
            # prompts the user to purchase an AddOn , you can skip this by hitting the enter button
        _askAddOn = input(
            "would you like an AddOn -YES or NO: ")
        print("")
        if (_askAddOn.lower() == "yes"):
            # if the user wants to purchase an AddOn print the AddOn Menu
            boxMenu(AddOnMenu, 40)
            # prompts the user enter the number of the AddOn as shown on the menu
            _askAddOn = int(
                input("\npick the number of the AddOn you wish to add to your order:"))
            # creates the AddOn object
            itemAddOn = AddOn(AddOnList[_askAddOn - 1], size)
        elif(_askAddOn.lower() == "no"):
            itemAddOn = None
        else:
            itemAddOn = ""
        # The burger item is then added to the orderList
        orderList.append(
            Burger(name, size, itemAddOn, burger_type))
    else:
        # prompts the user enter what temperature he/she wants the drink in
        temperature = input(
            "please enter the what temperature of drink you would like COLD or HOT? :")
        if(temperature == "cold"):
            temperature = "15C"
        elif(temperature == "hot"):
            temperature = "25C"
        # The drink item is then added to the orderList
        orderList.append(
            Drink(name))
    # Prompts the user to order again or not
    reOrder = input(
        "Would you like to continue ordering? YES or NO? :")
    # if yes then call the order function again
    if(reOrder.lower() == "yes"):
        print("\n")
        Order()
    # if no or if the user enters an invalid input the create a receipt object and then print the receipt details
    else:
        receipt = Receipt("RECIEPT", orderList)
        boxMenu(receipt, 40, receipt.Get_order_cost())


def Order():
    # This boxMenu creates a box list containing the Menu file
    boxMenu(menu, 40)

    while proceed:
        # take the users input for the order item
        user_input = int(input(
            "\nplease enter your order number as listed in Burger Fest's Menu: "))
        # the get_order functions takes the users input and starts preparing the items information
        # it does this in order to create a single order, this is wrapped in a while loop
        get_order(user_input - 1)


while True:
    purchase = input(
        "Would you like to make an order \nEnter yes or no to proceed: ")
    if (purchase.lower()) == "yes":
        print("welcome customer\nThe Burger Fest Menu")
        # a prompt asking for the user if he would like to make an order
        # if yes then the Order function is called
        Order()
        break
        # if no then end the program
    elif (purchase.lower() == "no"):
        break
    else:
        # if the user provides an invalid input then prompt the user to enter a valid input
        print("please enter a valid input")
        continue
