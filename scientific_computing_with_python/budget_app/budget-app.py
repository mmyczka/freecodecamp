class Category:
    def __init__(self, name):
        self.name = name
        self.ledger=[]
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if check := self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
        return check

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)
    
    def get_withdraws(self):
        return sum(item["amount"] for item in self.ledger if item["amount"] < 0)
        

    def transfer(self, amount, category):
        if check := self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")
        return check

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # The lenght of output
        l = 30

        # Title
        result = self.name.center(l, '*') + '\n'

        # All descriptions and amounts
        for item in self.ledger:
            amount = "{:.2f}".format(item["amount"])
            description = item["description"][:l-len(amount) - 1]
            result += description + ' ' * (l - len(description) - len(amount)) + amount + '\n'
        
        # Total
        result += f"Total: {self.get_balance():.2f}"
        
        return result

def create_spend_chart(categories):
    # Title
    title = "Percentage spent by category"

    # Calculate percenatage spend in each Category
    total = sum(category.get_withdraws() for category in categories)
    category_percentages = [(category.name, category.get_withdraws() / total * 100) for category in categories]

    # Generate chart
    chart_lines = []
    for i in range(100, -10, -10):
        line = "{:3d}| ".format(i)
        for name, percentage in category_percentages:
            if percentage >= i:
                line += "o  "
            else:
                line += "   "
        chart_lines.append(line)

    # Category names vertically aligned
    max_length = max(len(name) for name, _ in category_percentages)
    category_names_ljust = [name.ljust(max_length) for name, _ in category_percentages]

    name_lines = ["    " + "-" * len(category_names_ljust) * 3 + "-" ]
    for i in range(max_length):
        line = "     "
        for name in category_names_ljust:
            line  += name[i] + '  '
        name_lines.append(line)
            
    return title + "\n" + "\n".join(chart_lines) + "\n" + "\n".join(name_lines)

# Test
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10, "groceries")
food.withdraw(8, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.deposit(450)
clothing.withdraw(12)
auto = Category("Auto")
print(food)
print (create_spend_chart([food, clothing, auto]))