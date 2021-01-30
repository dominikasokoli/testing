print("Welcome to the coffee shop. Check out beverages we offer today: ")

menu = {
            'espresso':{'price': 3, 'mililiters': 60, 'code':1},
            'cappuccino':{'price': 8,'mililiters': 180, 'code':2},
            'latte_machiato':{'price': 15, 'mililiters': 200,'code':3},
            'tea':{'price': 5, 'mililiters': 250, 'code':4}
        }

for x, y in menu.items():
    print(x)
    for d in y:
        print(d + ':', y[d])

bar = int(input("enter code of the item you wish to order: "))
sum = 0
price = []
products = []
for key in menu:
    if menu[key]['code'] == int(bar):
        print("beverage was added to your basket")
        print(key)
        print("price: %s" % menu[key]['price'])
        price.append(menu[key]['price'])
        products.append(key)
        while True:
            choice = input("Would you like to buy another beverage? y/n ")
            if choice == 'y':
                bar = int(input("enter code of the item you wish to order: "))
                for key in menu:
                    if menu[key]['code'] == int(bar):
                        print("beverage was added to your basket")
                        print(key)
                        print("price: %s" % menu[key]['price'])
                        price.append(menu[key]['price'])
                        products.append(key)
            if choice == 'n':
                for x in range(0, len(price)):
                    sum = sum + price[x]
                print("Total cost: ", sum)
                break
        promocode = str(input("Please input your promotion code: "))
        promocode_list = ["1234", "DISCOUNT", "IloveCoffee"]
        if promocode in promocode_list:
            print("Discount was added")
        else:
            print("Your promotion code is not valid")
            choice = input("Would you like to retype? y/n ")
            if choice == 'y':
                promocode_two = str(input("Please input your promotion code: "))
                if promocode in promocode_list:
                    print("Discount was added")
                else:
                    print("There's been an error")
            if choice == 'n':
                print("You will be redirected to checkout")
