# This represents the Items Available within the Burger Fest Restuarant
itemList = ["Chicken Fillet -20AED", "Chilli Cheeseburger -25AED",
            "The classic Cheeseburger - 25AED", "Fanta -5.25AED", "Water -7.00AED", "Coke - 5.25AED"]
# This represents the AddOns Available within the Burger Fest Restuarant
AddOnList = ["Chicken Nuggets -5.00AED",
             "McMuffins -10.00AED", "Extra Ketchup -3.00AED"]

# A class for representing listed items


class ListObject():
    def __init__(self, name, menuArray):
        self.name = name
        self.menuArray = menuArray

    def __str__(self):
        return self.name

    def get_list(self):
        return self.menuArray

# The base class for each item on the burger fest Menu


class item():
    def __init__(self, name, size="S", AddOnItem=None):
        self.name = name
        self.AddOnItem = AddOnItem
        self.size = size
        self.price = 0

    def __str__(self) -> str:
        return self.name

    def get_cost(self):
        for i in range(len(self.name)):
            if self.name[i] == "-":
                tempValue = self.name[i+1:]
                self.price = float(tempValue[0: len(tempValue) - 3])
        if self.size.lower() == "m":
            self.price += 10
        elif self.size.lower() == "l":
            self.price += 20
        return self.price

    def get_size(self):
        return self.size

# The Burger Class Inherits properties from the item class and evaluates the cost for the burger and the corresponding AddOn


class Burger(item):
    def __init__(self, name, size, AddOnItem, burger_type):
        super().__init__(name, size)
        self.burger_type = burger_type
        self.AddOnItem = AddOnItem

    def get_cost(self):
        addOnCost = 0
        if self.AddOnItem == None:
            return super().get_cost()
        elif self.AddOnItem == "":
            return super().get_cost()
        else:
            addOnCost = self.AddOnItem.get_cost()
        return super().get_cost() + addOnCost

    def __str__(self) -> str:
        addonstring = ""
        if self.AddOnItem == None or "":
            addonstring = ""
        else:
            addonstring = f"({self.AddOnItem})"
        return f"{super().__str__()} size:{self.size.upper()} {addonstring} ----> {self.get_cost()}AED"

# The Drink Class Inherits properties from the item class


class Drink(item):
    def __init__(self, name, size="S", temperature="cold"):
        super().__init__(name, size)
        self.temperature = temperature

    def get_cost(self):
        return super().get_cost()

    def __str__(self) -> str:
        return f"{super().__str__()} size:{self.size.upper()} at {self.temperature} ---->{self.get_cost()}AED"

# The AddOn Class Inherits properties from the item class


class AddOn(item):
    def __init__(self, name, size="S"):
        super().__init__(name, size=size)

    def get_cost(self):
        return super().get_cost()

    def __str__(self) -> str:
        return super().__str__()

# The Receipt class Inherits from the listObject class and is responsible for
# evaluating the total cost of all orders made by a customer


class Receipt(ListObject):
    def __init__(self, name, menuArray):
        super().__init__(name, menuArray)
        self.menuArray = menuArray

    def get_list(self):
        return super().get_list()

    def Get_order_cost(self):
        self.total = 0
        for i in self.menuArray:
            self.total += i.get_cost()
        return self.total

# This function is responsible for creating the look of each menu used within Burger Fest


def boxMenu(menuObject, maxLineLength, total=0):
    menu = menuObject.get_list()
    print(menuObject)
    for i in range(maxLineLength):
        print("-", end="")
    print("")
    for i in range(len(menu)):
        menuItem = f"{i+1}) {menu[i]}"
        print(menuItem)
    if total != 0:
        print(f"TOTAL: {total}AED")
    for i in range(maxLineLength):
        print("-", end="")
    print("")
