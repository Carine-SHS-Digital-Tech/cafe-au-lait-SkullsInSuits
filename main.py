DineInQuantity = 0
TakeAwayQuantity = 0
TotalOrders = 0
TotalCups = 0
TotalDayIncome = 0
TotalGst = 0
CappuccinoQuantity = 0
EspressoQuantity = 0
LatteQuantity = 0
IcedCoffeeQuantity = 0
OpType = 1
OpType = input("Press 1 for New Order, press 0 for Daily Summary: ")
if OpType == "0":
    print("Dine in Quantity: " + str(DineInQuantity))
    print("Take Away Quantity: " + str(TakeAwayQuantity))
    print("Total Orders Today: " + str(TotalOrders))
    print("Total Cups Today: " + str(TotalCups))
    print("Total Daily Income: " + str(TotalDayIncome))
    print("Total Daily Gst: " + str(TotalGst))
    print("Cappuccino Quantity: " + str(CappuccinoQuantity))
    print("Espresso Quantity: " + str(EspressoQuantity))
    print("Latte Quantity: " + str(LatteQuantity))
    print("Iced Coffee Quantity: " + str(IcedCoffeeQuantity))
else:
    DeliveryType = input("Press 1 for Dine in, press 2 for Take Away: ")
    print("Our menu includes Cappuccinos, Espressos, Lattes and Iced Coffees")
    print("We will go down our menu and you will say the quantity of each you would like. If you do not want that beverage, put in 0")
    print("Cappuccino: $3.00, Espresso: $2.25, Latte: $2.50, Iced Coffee: $2.50")
    Cappuccino = int(input("How many Cappuccinos would you like? "))
    Espresso = int(input("How many Espressos would you like? "))
    Latte = int(input("How many Lattes would you like? "))
    IcedCoffee = int(input("How many Iced Coffees would you like? "))
    Cappuccino = Cappuccino * int(3)
    Espresso = Espresso * int(2.25)
    Latte = Latte * int(2.5)
    IcedCoffee = IcedCoffee * int(2.5)
    Total = Cappuccino + Espresso + Latte + IcedCoffee
    TotalOrderGst = Total * int(1.1)
    if DeliveryType == "2":
        TotalOrderGst = TotalOrderGst * int(1.05)
    print("Your total is " + Total + " and your grand total with Gst is " + TotalOrderGst)

