class Category:
    def __init__(self, name):
        self.name = name
        self.total = 0.00
        self.ledger = list()
    
    def __repr__(self):
        title_line = f"{self.name:*^30}\n"
        accumlated = 0
        for item in self.ledger:
            title_line += f"{item['description'][0:24]}{item['amount']:>{30-len(item['description'])}}\n"
            accumlated += item["amount"]
        title_line += f"Total: {(self.total)}"
        return title_line
    
    def deposit(self, amount, description = ""):
        self.total += amount
        self.ledger.append({"amount":amount, "description":description})

    def withdraw(self, amount, description = ""):
        can_withdraw = self.check_funds(amount)
        if can_withdraw:
            self.total -= amount
            self.ledger.append({"amount":-amount, "description":description})
        return can_withdraw

    def get_balance(self):
        return self.total

    def transfer(self, amount, instance, description = ""):
        Transferrable = self.check_funds(amount)

        if Transferrable:
            self.withdraw(amount, f"Transfer to {instance.name}")
            instance.deposit(amount, f"Transfer from {self.name}")
        return Transferrable

    def check_funds(self, amount):
        if amount > self.total:
            return False
        return True

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
print(food.ledger)
print(str(food))


def create_spend_chart(categories):
    t = "Percentage spent by category\n"
    total = 0
    cats = {}
    #get total of all withdrawals
    for category in categories:
        cats_total = 0

        for item in category.ledger:
            amount = item["amount"]
            if int(amount) < 0:
                total += amount
                cats_total += amount
        cats[category.name] = abs(cats_total)
    print(cats)
    total = abs(total)
    for key, val in cats.items():
        print(key, val)
        percentage = (int(val) /total)*100

    for n in range(100, -1, -10):
        t += f'''{str(n) + '|':>4}\n'''
    print(t)
create_spend_chart([food])