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
Cappuccino = 0
Espresso = 0
Latte = 0
IcedCoffee = 0
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
    while Cappuccino < 0 or Espresso < 0 or Latte < 0 or IcedCoffee < 0:
        print("Please make sure all quantities are a full positive number or 0")
        Cappuccino = 0
        Espresso = 0
        Latte = 0
        IcedCoffee = 0
        Cappuccino = int(input("How many Cappuccinos would you like? "))
        Espresso = int(input("How many Espressos would you like? "))
        Latte = int(input("How many Lattes would you like? "))
        IcedCoffee = int(input("How many Iced Coffees would you like? "))
    else:
        CappuccinoCost = Cappuccino * int(3)
        EspressoCost = Espresso * float(2.25)
        LatteCost = Latte * float(2.5)
        IcedCoffeeCost = IcedCoffee * float(2.5)
        Total = CappuccinoCost + EspressoCost + LatteCost + IcedCoffeeCost
        TotalOrderGst = Total * float(1.1)
        TotalGst = TotalOrderGst - Total + TotalGst
        if DeliveryType == "2":
            TotalOrderGst = TotalOrderGst * float(1.05)
            TakeAwayQuantity = TakeAwayQuantity + 1
        else:
            DineInQuantity = DineInQuantity + 1
        print("Your total is $" + str(Total) + " and your grand total with Gst is $" + str(TotalOrderGst))
        CappuccinoQuantity = CappuccinoQuantity + Cappuccino
        EspressoQuantity = EspressoQuantity + Espresso
        LatteQuantity = LatteQuantity + Latte
        IcedCoffeeQuantity = IcedCoffeeQuantity + IcedCoffee
        TotalCups = TotalCups + Cappuccino + Espresso + Latte + IcedCoffee
        TotalOrders = TotalOrders + 1
        TotalDayIncome = TotalDayIncome + TotalOrderGst
