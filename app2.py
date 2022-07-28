import math

prices = {
    1: 2.00,
    2: 3.50,
    3: 4.00,
    4: 4.99
}


class CoffeeShop:
    global data
    data = {}

    def promptUser(self):
        print("\nHello, welcome to my coffee shop, what is your name? ")
        name = input("")

        print("\n\tOur menu\n\n\t1) Black coffee\n\t2) Espresso\n\t3) Latte\n\t4) Cappuccino\n\n\tYour choice: ")
        order = int(input("\t"))

        print("\nQuantity: ")
        quantity = int(input())

        if order == 1: #black coffee
            total = prices[1] * quantity
            data['name'] = name
            data['type'] = 'Black Coffee'
            data['total'] = str(math.floor(total))

        elif order == 1:  # espresso
            total = prices[2] * quantity
            data['name'] = name
            data['type'] = 'Espresso'
            data['total'] = str(math.floor(total))

        elif order == 3:  # latte
            total = prices[3] * quantity
            data['name'] = name
            data['type'] = 'Latte'
            data['total'] = str(math.floor(total))

        elif order == 4:  # cappuccino
            total = prices[4] * quantity
            data['name'] = name
            data['type'] = 'Cappuccino'
            data['total'] = str(math.floor(total))

        return data

    def receit(self, promptUser):

        print("Receipt for customer")

        name = promptUser['name']
        type = promptUser['type']
        total = promptUser['total']

        print("Name:" + name
              +"\nCoffee type: " + type
              +"\nTotal: $" + total + "\n")



coffee = CoffeeShop()
coffee.receit(coffee.promptUser())

print("\nDo you want to calculate for another customer?")
choice = input("")

if choice != "No":
    coffee.receit(coffee.promptUser())
else:
    exit(0)
