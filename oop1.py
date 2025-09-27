class Customer:
    #deposit & withdraw
    def __init__(self,name,phone_num):
        self.name = name
        self.phone_num = phone_num


class Account:
    def __init__(self,customer,acc_num,balance=0):
        self.customer = customer
        self.acc_num = acc_num
        self.balance = balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance = self.balance + amount
            print(f"Deposited {amount}.New balance is {self.balance}")
        else:
            print("Invalid deposit amount")


    def withdraw(self,amount):
        if 0<amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Withdraw {amount}.New balace is {self.balance}")
        elif amount<=0:
            print("Invalid withdrwal amount")
        else:
            print("Insufficient balance")


customer = Customer("Siri","9736738")
account = Account(customer,"123456",1000)

print(f"Account Holder: {account.customer.name}")
print(f"Account Number: {account.acc_num}")
print(f"Initial_Balace: {account.balance}")


account.deposit(500)
account.withdraw(200)



