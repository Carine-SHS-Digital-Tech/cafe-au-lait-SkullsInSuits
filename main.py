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
Restart = 0

while Restart != 1:
    CapDel = 0
    EspDel = 0
    LatDel = 0
    IceDel = 0
    CapGst = 0
    EspGst = 0
    LatGst = 0
    IceGst = 0
    CapFull = 0
    EspFull = 0
    LatFull = 0
    IceFull = 0
    OpType = input("Press 1 for New Order, press 0 for Daily Summary: ")
    if OpType == "0":
        print("Dine in Quantity: " + str(float(DineInQuantity)))
        print("Take Away Quantity: " + str(float(TakeAwayQuantity)))
        print("Total Orders Today: " + str(float(TotalOrders)))
        print("Total Cups Today: " + str(float(TotalCups)))
        print("Total Daily Income: " + str(float(TotalDayIncome)))
        print("Total Daily Gst: " + str(float(TotalGst)))
        print("Cappuccino Quantity: " + str(float(CappuccinoQuantity)))
        print("Espresso Quantity: " + str(float(EspressoQuantity)))
        print("Latte Quantity: " + str(float(LatteQuantity)))
        print("Iced Coffee Quantity: " + str(float(IcedCoffeeQuantity)))
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
                CapDel = CappuccinoCost * float(1.05)
                EspDel = EspressoCost * float(1.05)
                LatDel = LatteCost * float(1.05)
                IceDel = IcedCoffeeCost * float(1.05)
            else:
                DineInQuantity = DineInQuantity + 1
                CapDel = 0
                EspDel = 0
                LatDel = 0
                IceDel = 0
            print("Your total is $" + str(Total) + " and your grand total with Gst is $" + str(TotalOrderGst))

            print("Enter cash now")
            Currency = float(input("Currency insert here: $"))
            Currency = TotalOrderGst - Currency
            while Currency > 0:
                print("Not enough inserted, you need another $" + str(Currency))
                Currency2 = float(input("Currency insert here: $"))
                Currency = Currency2 - Currency
                Currency2 = 0
            Currency = float(Currency) * float("-1")
            round(Currency, 1)
            print("Here is your change: $" + str(round(Currency, 2)))
            print("Here is your receipt")
            CapGst = CappuccinoCost * float("1.1") - CappuccinoCost
            EspGst = EspressoCost * float("1.1") - EspressoCost
            LatGst = LatteCost * float("1.1") - LatteCost
            IceGst = IcedCoffeeCost * float("1.1") - IcedCoffeeCost
            CapFull = CappuccinoCost + CapGst + CapDel
            EspFull = EspressoCost + EspGst + EspDel
            LatFull = LatteCost + LatGst + LatDel
            IceFull = IcedCoffeeCost + IceGst + IceDel
            print(str(round(Cappuccino,2)) + ", Cappuccino , $" + str(round(CappuccinoCost,2)) + ", gst $" + str(round(CapGst,2)) + ", full price $" + str(round(CapFull,2)))
            print(str(round(Espresso,2)) + ", Espresso , $" + str(round(EspressoCost,2)) + ", gst $" + str(round(EspGst,2)) + ", full price $" + str(round(EspFull,2)))
            print(str(round(Latte,2)) + ", Latte , $" + str(round(LatteCost,2)) + ", gst $" + str(round(LatGst,2)) + ", full price $" + str(round(LatFull,2)))
            print(str(round(IcedCoffee,2)) + ", IcedCoffee , $" + str(round(IcedCoffeeCost,2)) + ", gst $" + str(round(IceGst,2)) + ", full price $" + str(round(IceFull,2)))
            print("Thank you")
            CappuccinoQuantity = CappuccinoQuantity + Cappuccino
            EspressoQuantity = EspressoQuantity + Espresso
            LatteQuantity = LatteQuantity + Latte
            IcedCoffeeQuantity = IcedCoffeeQuantity + IcedCoffee
            TotalCups = TotalCups + Cappuccino + Espresso + Latte + IcedCoffee
            TotalOrders = TotalOrders + 1
            TotalDayIncome = TotalDayIncome + TotalOrderGst
