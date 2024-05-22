class Account:
    def __init__(self, account_number): # constructor
        self.__acount_number = account_number # private
        self.__balance = 0
        self.__limit = 0
    
    @property
    def blance(self):
        return self.__balance
    
    @property
    def account_number(self):
        return self.__acount_number
    
    @property
    def limit(self):
        return self.__limit
    
    @limit.setter
    def limi(self, limit):
        self.__limit = limit

    def bebet(self, amount):
        if amount > self.__limit:
            return # could be a check here, control coupling type 2
        self.__balance -= amount

    def credit(self, amount):
        self.__balance += amount


account_johan = Account("BE32 4857 8126 7302")
account_johan.credit(3540)
account_karel = Account("BE62 8974 2975 6861")
account_karel.credit(327.43)

account_johan.debet(245.45)
account_johan.credit(1200)

account_karel.debet(250.82)
account_karel.credit(240.01)
account_karel.debet(56)

print("Johan van de Genechte:", account_johan.balance)
print("Karel Meenaerts:", account_karel.balance)