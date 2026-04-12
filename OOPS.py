
# Encapsulation: Wrapping data and methods into a single unit (class) and restricting access to some of the object's components.
# Inheritance: A mechanism where a new class (child class) inherits properties and behaviors (attributes and methods) from an existing class (parent class).


class BankAccount:
    def __init__(self,ownerName,balance,family):
        self.__ownerName=ownerName
        self.__balance=balance
        self.family=family
    
    def depositAmount(self,amount):
        if amount<=0:
            print("Invalid Amount")
        else:
            self.__balance+=amount
            print("Amount Deposited Successfully")

    def _getBalance(self):
        return self.__balance

    def withdrawAmount(self,amount):
        if amount>self.__balance:
            print("Insufficient Balance")
        elif amount<=0:
            print("Invalid Amount")
        else:
            self.__balance-=amount
            print("Amount Withdrawn Successfully")

    def displayBalance(self):
        print("Account Owner Name:",self.__ownerName)
        print("Account Balance:",self.__balance)

    def monthly_summary(self):
        print("Monthly Summary:")
        print("Account Owner Name:",self.__ownerName)
        print("Account Balance:",self.__balance)
        print("Family Account:",self.family)

    def __str__(self):
        return f"Account[{self.__ownerName}]-Balance:${self.__balance}"
    
class SavingsAccount(BankAccount):

    def __init__(self,ownerName,balance,family,interestRate):
        super().__init__(ownerName,balance,family)
        self.__interestRate=interestRate

    def applyInterest(self):
        amount=self._getBalance() * self.__interestRate / 100
        self._BankAccount__balance+=amount

    def monthly_summary(self):
        print(self.displayBalance())
        print("Interest Rate:",self.__interestRate,"%")
        print("Before Interest",self._getBalance())
        restAmount=(self._getBalance()) * (self.__interestRate / 100)
        print("After Interest",restAmount + self._getBalance())

    def __str__(self):
        return f"SavingsAccount[{self._BankAccount__ownerName}]-Balance:${self._BankAccount__balance}-Interest Rate:{self.__interestRate}%"

class CurrentAccount(BankAccount):
    def __init__(self,ownerName,balance,family,overdraftLimit):
        super().__init__(ownerName,balance,family)
        self.__overdraftLimit=overdraftLimit

    def monthly_summary(self):
        print(self.displayBalance())
        print("Overdraft Limit:",self.__overdraftLimit)
    
    def withDrawAmount(self,withDrawAmount):
        if withDrawAmount>self._BankAccount__balance + self.__overdraftLimit:
            print("Overdraft Limit Exceeded")
        elif withDrawAmount<=0:
            print("Invalid Amount")
        else:
            self._BankAccount__balance-=withDrawAmount
            print("Amount Withdrawn Successfully")



person0 = BankAccount("John", 500,True)    
person1 = SavingsAccount("Alice", 1000,True,5)
person2 = CurrentAccount("Bob", 2000,False,500)

for person in [person0, person1, person2]:
    print(person)                  # __str__ test
    person.monthly_summary()


# print(person1)                  # __str__ test
# person1.depositAmount(500)      # should work
# person1.depositAmount(-100)     # should reject
# person1.withdrawAmount(200)     # should work
# person1.withdrawAmount(5000)    # should reject - insufficient
# person1.withdrawAmount(-50)     # should reject - invalid
# person1.displayBalance()        # final balance should be 1300
# person1.applyInterest()         # interest applied 5%
# person1.displayBalance()        # final balance should be 1365
# print("BOB'S ACCOUNT TESTS")
# person2.depositAmount(1000)      # should work
# person2.displayBalance()        # final balance should be 3000
# person2.withDrawAmount(3500)     # should work - within overdraft limit


# print(person1)


# --------------------------------------------

class ShoppingCart:
    def __init__(self):
        self.__items = {}  # {"Laptop": 1000}

    # Add / update item
    def add_item(self, itemName, itemPrice):
        self.__items[itemName] = itemPrice

    # Get all items
    def getItems(self):
        return self.__items

    # Remove item (FIXED)
    def remove_item(self, item):
        if item in self.__items:
            del self.__items[item]   # ✅ correct way
        else:
            print("Item not found in cart.")

    # View cart (IMPROVED)
    def view_cart(self):
        print("Items in Cart:")
        for item, price in self.__items.items():
            print(f"{item}: ${price}")

    # Merge carts (FIXED logic)
    def merge_cart(self, other_cart):
        for item, price in other_cart.getItems().items():
            self.__items[item] = price

    # Get price
    def getPrice(self, item):
        return self.__items.get(item, None)

    # Length (use dunder)
    def __len__(self):
        return len(self.__items)

    # Contains (use dunder)
    def __contains__(self, item):
        return item in self.__items

    # ✅ ADD operator overloading
    def __add__(self, other):
        new_cart = ShoppingCart()

        # copy current cart
        new_cart.__items = self.__items.copy()

        if isinstance(other, ShoppingCart):
            for item, price in other.getItems().items():
                new_cart.__items[item] = price

        elif isinstance(other, tuple):
            item, price = other
            new_cart.__items[item] = price

        else:
            raise TypeError("Can only add ShoppingCart or (item, price)")

        return new_cart

    # Pretty print
    def __str__(self):
        return str(self.__items)
    

    # List comprehension example

    # Without list comprehension:
squares = []
for i in range(1, 11):
    squares.append(i ** 2)

squares=[i**2 for i in range(1,11)]  # With list comprehension


# Write a generator function that yields even numbers up to n
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

for num in even_numbers(20):
    print(num)

# Write a lambda that takes a list of prices and applies 10% discount
prices = [100, 250, 80, 430, 60]

discounted = list(map( lambda x: x * 0.9, prices))  # Apply 10% discount
print(discounted)





