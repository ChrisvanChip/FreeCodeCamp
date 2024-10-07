import math

def align_evenly(width_chars, left, right):
    amount_spaces = width_chars - len(left) - len(right)
    return left + ' ' * amount_spaces + right

# From first project 
def padding(string, req_length, pattern=' '):
    padding_str = ''
    for i in range(req_length - len(string)):
        padding_str += pattern
    return padding_str + string

# Class definition
class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ledger = []

    def check_funds(self, amount):
        return amount <= self.balance

    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })
        self.balance += amount

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        self.ledger.append({
            'amount': -amount,
            'description': description
        })
        self.balance -= amount
        
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        transaction = self.withdraw(amount, f'Transfer to {category.name}')
        if not transaction:
            return False
        category.deposit(amount, f'Transfer from {self.name}')
        return True
    
    def __str__(self):
        # Title
        # Discovered: multiplying string
        name = self.name[0:30]
        amount = (30 - len(name)) / 2
        string = ''
        string += "*" * math.ceil(amount)
        string += name
        string += "*" * math.floor(amount)
        string += "\n"

        # Each line in ledger
        for line in self.ledger:
            left = line['description'][0:23]
            right = str("{:.2f}".format(line['amount']))[0:7]
            string += align_evenly(30, left, right)
            string += "\n"
        
        string += "Total: " + "{:.2f}".format(self.balance)
        return string

def create_spend_chart(categories):
    # Init
    lines = []
    lines.append('Percentage spent by category')

    # Calculate spend
    data = {}
    total = 0
    for category in categories:
        data[category.name] = 0
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                data[category.name] += -transaction['amount']
                total += -transaction['amount']
    for category in data:
        data[category] = (data[category] / total) * 100
        data[category] = math.floor(data[category] / 10) * 10
    
    # Visualize bars
    for percentage in range(100, -1, -10):
        string = '|'
        for category in data:
            if data[category] >= percentage:
                string += " o "
            else:
                string += " " * 3

        lines.append(padding(str(percentage), 3) + string + " ")

    # Dashes
    string = " " * 4
    for category in data:
        string += "-" * 3
    string += "-"
    lines.append(string)

    # Name, letter per line
    maxLines = 0
    for category in data:
        if len(category) > maxLines:
            maxLines = len(category)
    for i in range(maxLines):
        string = " " * 4
        for category in data:
            if len(category) > i:
                string += ' ' + category[i] + ' '
            else:
                string += ' ' * 3
        lines.append(string + " ")

    # Stringify lines
    result = ''
    for line in lines:
        if len(result) > 0:
            result += "\n"
        result += line
    return result
