class Category:
    def __init__(self,name):
        self.name = name
        self.ledger=[]

    def deposit (self,amount,description=''):
        
        self.ledger.append({"amount": amount, "description": description})
        
    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.ledger.append ({"amount":-amount ,"description": description})
            return True
        else:
            return False
       

    def get_balance(self):
        total_balance =0
        for item in self.ledger:
            total_balance += item["amount"]
        return total_balance

    def transfer(self,amount, other_category):
       if self.withdraw(amount,f"Transfer to {other_category.name}"):
        other_category .deposit(amount,f"Transfer from {self.name}")
        return True
       else:
            return False

    def check_funds(self,amount):
        if amount > self.get_balance():
            return False

        return True
    
    def __str__(self):
        title=self.name.center(30, "*") + "\n"

        item =""
        for entry in self.ledger:
            description=entry ['description'][:23].ljust(23)

            amount=f"{entry['amount']:.2f}" [:7].rjust(7)
        
            item += description +amount + "\n"
        total = f"Total: {self.get_balance():.2f}"
        
        return title + item + total
 
    

def create_spend_chart(categories):
    withdrawals = []
    for category in categories:
        spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        withdrawals.append(spent)

    total_spent = sum(withdrawals)

    percentages = []
    for spent in withdrawals:
        if total_spent > 0:
            percent = int((spent / total_spent) * 100) // 10 * 10
        else:
            percent = 0
        percentages.append(percent)

    res = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        res += f"{i:>3}| "
        for p in percentages:
            res += "o  " if p >= i else "   "
        res += "\n"

    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names = [category.name for category in categories]
    max_len = max(len(name) for name in names)

    for r in range(max_len):
        res += "    "
        for name in names:
            char = name[r] if r < len(name) else " "
            res += f" {char} "
        res += " "
        if r < max_len - 1:
            res += "\n"

    return res