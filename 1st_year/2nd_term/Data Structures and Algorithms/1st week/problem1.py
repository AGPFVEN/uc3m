class CreditCard:
    def __init__(self, name, id, balance, limit):
        self.name = name
        self.id = id
        self.balance = balance
        self.limit = limit

    def charge(self, amount:float):
        if(amount < 0):
            print("Invalid operation")

        elif (self.balance + amount <= self.limit):
            self.balance += amount

    def make_deposit(self, deposit:float): 
        if(deposit < 0):
            print("Invalid operation")

        elif deposit > self.balance:
            print("Invalid operation")

        else:
            self.balance -= deposit