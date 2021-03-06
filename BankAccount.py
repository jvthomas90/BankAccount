import random
import string

def get_random_string(length):
    digits = string.digits
    randomized = ''.join((random.choice(digits) for i in range(length)))
    return randomized

class BankAccount:
    
    #Creates a bank account class with 5 methods for various functions defined below
    def __init__(self, full_name, account_number, routing_number, balance):
        """
        Constructor that initializes a new instance of a bank account class
        with the user's name, a randomly generated account number, and balance amount.
        """
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = 38914091
        self.balance = 0  

    def deposit(self,amount):
        """
        The deposit function increaes the user's bank account balance by the quantity passed in the amount parameter
        """
        self.balance = amount + self.balance
        print("Amount Deposited: ${:,.2f}".format(amount))

    def widthdraw(self,amount):
        """
        The withdraw function attempts to subtract from the user's bank account balance by the quantity passed in the amount parameter
        If there are insufficient funds, an overdraft fee is applied
        """

        if amount > self.balance:
            self.balance = self.balance - amount
            print("Insufficient Funds")
            self.balance = self.balance - 20
            print(f'Amount Withdrawn ${amount}')
        else:
            self.balance -= amount
            print(f'Amount Withdrawn: ${amount}')

    def get_balance(self):
        """Prints a welcome message, then prints the balance of the user's account"""
        print(f'Hello, {self.full_name}')
        print(f'Your balance is ${round(self.balance,2)}')

    def add_interest(self):
        """Applies a fixed interest rate to bank account balance"""
        interest = self.balance *  0.00083
        self.balance = self.balance + interest

    def print_receipt(self):
        """Securely outputs censored info of bank account details"""
        print()
        print(self.full_name)
        censored_for_security = "****"
        print(f'Account number: {censored_for_security + self.account_number[4:9]}')
        print(f'Routing number: {self.routing_number}')
        print(f'Balance: ${round(self.balance,2)}')

#Initialization of various different accounts
JaneDoe = BankAccount('Jane Doe', get_random_string(8),38914091, 1000)
JohnSMith = BankAccount('John Smith', get_random_string(8), 38914091, 500.00)
JoelThomas = BankAccount('Joel Thomas', get_random_string(8),38914091,250)
JohnDoe = BankAccount('John Doe', get_random_string(8), 38914091, 25)

print("\nHello, I'm BankBot, your personal banking assistant!\n")

#Example of the get_balance function
JohnSMith.get_balance()

#Example of the deposit function
JohnSMith.deposit(6.53)

#Example of the withdraw function
JohnSMith.widthdraw(8.00)

#Example of adding interest
JohnSMith.add_interest()

#Print the new balance 
JohnSMith.get_balance()

#Print reciepts
JohnSMith.print_receipt()
JoelThomas.print_receipt()
JaneDoe.print_receipt()
JohnDoe.print_receipt()
