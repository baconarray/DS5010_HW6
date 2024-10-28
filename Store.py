'''
Tyler Beaulieu
DS5010, Fall 2023
Homework 6, Problem 5
October 24, 2024
'''

class Store:
    ''' Class: Store
        Attributes: balance, inventory
        Methods: addItems(), sellItems()'''
    
    def __init__(self, balance = 0.0, inventory = {'apple' : 0, 'banana' : 0}):
        self.balance = balance
        self.inventory = inventory
        self.price = {'apple' : 2.0, 'banana' : 1.0}

    def addItem(self, item, quantity):
        if item in self.inventory.keys():
            print("Added",quantity,item,"into inventory.")
            self.inventory[item] += quantity
        else:
            print(f"Item '{item}' is not available in this store.")

    def sellItem(self, item, quantity):
        if item in self.inventory.keys():
            if quantity <= self.inventory[item]:
                cost = quantity * self.price[item]
                print(f"Sold {quantity} {item}(s) for ${cost}")
                self.inventory[item] -= quantity
                self.balance += cost
            else:
                print(f"Cannot fulfill request, due to insufficient inventory for {item}.")
        else:
            print(f"Item '{item}' is not available in this store.")             

    def __str__(self):
        return f"Balance: ${self.balance}\nInventory: {self.inventory}"