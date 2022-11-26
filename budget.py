class Category:
    def __init__(self, name):
        self.name = name
        self.total = 0 
        self.ledger = list()
    
    def __repr__(self) -> str:
        title_line = self.name.center(30, '*')
        print(title_line)
        #accumlated = 0 
        for item in self.ledger:
            amount = '%.2f' % item["amount"]
            desc = (item["description"][:30 - len(amount)]) if len(item["description"]) > 30 - len(amount) else item["description"]
            #accumlated += item["amount"]
            spaces = " " * (30-(len(desc)+ len(amount)))
            txt = f"{desc:<}{spaces}{amount:>}"
            print(txt)
        print("Total: " + '%.2f'% self.total) 
    
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

    def transfer(self, amount, instance):
        Transferrable = self.check_funds(amount)

        if Transferrable:
            self.withdraw(amount, f"Transfer to {instance.name}")
            instance.deposit(amount, f"Transfer from {self.name}")
        return Transferrable

    def check_funds(self, amount):
        if amount > self.total:
            return False
        return True

food = Category("Entertainment")
food.deposit(1000, "initial deposit")
food.withdraw(10, "groceries")
food.withdraw(15, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
print(food.ledger)
print(food.__repr__())


def create_spend_chart(categories):
    cats_list = []
    withd_list = []
    for category in categories:
        cats = category.name
        cats_list.append(cats)
        long_length = (len(max(cats_list, key=len)))
        padded = [word.ljust(long_length) for word in cats_list]
        #getting abs_total for percentage
        w_total =0
        for item in category.ledger:
            amount = item["amount"]
            if (amount) <0:
                w_total+= (amount)
        withd_list.append(w_total)
    total = int(round(sum(withd_list)))
    percents = []
    for val in withd_list:
        per = (val*100)/total
        per = round(per//10)*10
        percents.append(per)

    #coding for chart
    #padded = [word.ljust(long_length) for word in cats_list]
    chart = "Percentage spent by category\n"
    for num in range(100, -1, -10):
        chart += f"{str(num) + '|':>4}"
        for percent in percents:
            if percent >= num:
                chart += " o "
            else:
                chart += "   "
        chart += ' \n'
    chart += "    " + ("-"*((len(cats_list)+2)*2)) +'\n'
    for row in zip(*padded):
        chart += "     " + ('  '.join(row)) +'  \n'
    return (chart.rstrip("\n"))


    # t = "Percentage spent by category\n"
    # total = 0
    # cats = {}

    # #get total of all withdrawals
    # for category in categories:
    #     cats_total = 0

    #     for item in category.ledger:
    #         amount = float(item["amount"])
    #         if float(amount) < 0:
    #             total += amount
    #             cats_total += amount
    #     cats[category.name] = abs(cats_total)
    # #print(cats)
    # total = abs(total)
    # for key, val in cats.items():
    #     percentage = (int(val) /total)*100
    #     cats[key] = percentage
    # #print(cats)

    # for n in range(100, -1, -10):
    #     t += f'''{str(n) + '|':>4}'''
    #     for val in cats.values():
    #         if val >= n:
    #             t +=  " o "
    #     t += "\n"
    
    # l = len(cats.values())
    # print(cats.values())
    # t += f"    {(l*3 +1) * '-'}\n"

    # i = 0
    # while True:
    #     try:
    #         tempo_string = ""
    #         for key in cats.keys():
    #             #print(key)
    #             tempo_string += (key[i]).ljust(3)
    #         i += 1
    #         t += f"     {tempo_string}\n"
    #     except:
    #         break
          
    # return print(t)
    # categories  = ['Food', 'Auto', 'Clothing']
    # chart = "Percentage spent by category\n"
    # long_length = (len(max(categories, key=len)))
    # padded = [cats.ljust(long_length) for cats in categories]
    # percentages = [10, 70, 30]
    # for num in range(100, -1, -10):
    #     chart += f"{str(num) + '|':>4}"
    #     for percent in percentages:
    #         if percent >= num:
    #             chart += " o "
    #         else:
    #             chart += "   "
    #     chart += ' \n'
    # chart += "    " + "-"*10 +'\n'
    # for category in zip(*padded):
    #     chart += "     " + ('  '.join(category)) +'  \n'
    # print(chart.rstrip("\n"))