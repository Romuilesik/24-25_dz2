import random

class Seller:
    def __init__(self, name, products):
        self.name = name
        self.products = products
        self.income = 0

    def sell(self, product_name, quantity, buyer):
        if product_name in self.products and self.products[product_name] >= quantity:
            price = self.products[product_name] * quantity
            self.income += price
            buyer.money -= price
            print(f"{buyer.name} bought {quantity} {product_name}(s) from {self.name} for ${price}.")
            self.products[product_name] -= quantity
        else:
            print(f"{self.name} doesn't have enough {product_name}(s).")

    def status(self):
        print(f"Seller {self.name} - Products: {self.products}, Income: ${self.income}")

class Buyer:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.inventory = {}

    def buy(self, product_name, quantity, seller):
        if self.money >= seller.products[product_name] * quantity:
            seller.sell(product_name, quantity, self)
            if product_name in self.inventory:
                self.inventory[product_name] += quantity
            else:
                self.inventory[product_name] = quantity
        else:
            print(f"{self.name} doesn't have enough money to buy {quantity} {product_name}(s).")

    def status(self):
        print(f"Buyer {self.name} - Money: ${self.money}, Inventory: {self.inventory}")

class Simulation:
    def __init__(self):
        self.sellers = [Seller(f"Seller {i+1}", {"apple": 10, "banana": 20}) for i in range(2)]
        self.buyers = [Buyer(f"Buyer {i+1}", random.randint(50, 150)) for i in range(3)]

    def run_market(self, days):
        for day in range(days):
            seller = random.choice(self.sellers)
            buyer = random.choice(self.buyers)
            product = random.choice(list(seller.products.keys()))
            quantity = random.randint(1, 5)
            buyer.buy(product, quantity, seller)
            if day % 10 == 0:
                self.show_status()

    def show_status(self):
        for seller in self.sellers:
            seller.status()
        for buyer in self.buyers:
            buyer.status()

simulation = Simulation()
simulation.run_market(30)
simulation.show_status()
