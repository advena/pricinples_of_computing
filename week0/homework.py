def clock_helper(total_seconds):
    """
    Helper function for a clock
    """
    seconds_in_minute = total_seconds % 60 

def appendsum(lst):

	'''
	Repeatedly append the sum of the current last three elements of the list
	'''

	for i in range(25):
		current_next = lst[-1] + lst[-2] + lst[-3]
		lst.append(current_next)


	return






class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
 
        self.balance = initial_balance
        self.fees = 0


    def deposit(self, amount):
        """Deposits the amount into the account."""

        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """

        self.balance -= amount
        if self.balance < 0:
        	self.balance -= 5
        	self.fees += 5


    def get_balance(self):
        """Returns the current balance in the account."""

        return self.balance


    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        
        return self.fees

if __name__ == '__main__':
	my_account = BankAccount(10)
	my_account.withdraw(5)
	my_account.deposit(10)
	my_account.withdraw(5)
	my_account.withdraw(15)
	my_account.deposit(20)
	my_account.withdraw(5) 
	my_account.deposit(10)
	my_account.deposit(20)
	my_account.withdraw(15)
	my_account.deposit(30)
	my_account.withdraw(10)
	my_account.withdraw(15)
	my_account.deposit(10)
	my_account.withdraw(50) 
	my_account.deposit(30)
	my_account.withdraw(15)
	my_account.deposit(10)
	my_account.withdraw(5) 
	my_account.deposit(20)
	my_account.withdraw(15)
	my_account.deposit(10)
	my_account.deposit(30)
	my_account.withdraw(25) 
	my_account.withdraw(5)
	my_account.deposit(10)
	my_account.withdraw(15)
	my_account.deposit(10)
	my_account.withdraw(10) 
	my_account.withdraw(15)
	my_account.deposit(10)
	my_account.deposit(30)
	my_account.withdraw(25) 
	my_account.withdraw(10)
	my_account.deposit(20)
	my_account.deposit(10)
	my_account.withdraw(5) 
	my_account.withdraw(15)
	my_account.deposit(10)
	my_account.withdraw(5) 
	my_account.withdraw(15)
	my_account.deposit(10)
	my_account.withdraw(5) 
	print my_account.get_balance(), my_account.get_fees()
	print clock_helper(90)
	sum_three = [0, 1, 2]
	appendsum(sum_three)
	print sum_three[10]
	print sum_three [20]