from person import Personal_details

class CustomerAccount(Personal_details):
    def __init__(self, account_no, balance,*args,**kwargs):
        super().__init__(*args,**kwargs)
       
        self.account_no = account_no
        self.balance = float(balance)
    
  
    
    def deposit(self, amount):
        
        self.balance+=amount
        self.save_bank_data()
        return (f"Deposit successful. New balance: {self.balance}")
        
    def decrease(self,amount):
        self.balance-=amount
  
        
    def withdraw(self, amount):
        try:
            amount = float(amount)

            if self.balance + self.draft >= amount:
                self.balance -= amount
                return f"Withdrawal successful. New balance: {self.balance}"
            else:
                return ValueError("Insufficient funds for withdrawal.")
        except ValueError:
            return "Invalid withdrawal amount. Please enter a valid number."
               
        
    def print_balance(self):
        print("\n The account balance is %.2f" %self.balance)
        
    def get_balance(self):
        return self.balance
    
    def get_account_no(self):
        return self.account_no
    
    
    
    def account_menu(self):
        print ("\n Customer Operations :")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Deposit money")
        print ("2) Withdraw money")
        print ("3) Check balance")
        print ("4) Update customer name")
        print ("5) Update customer address")
        print ("6) Show customer details")
        print ("7) Back")
        print (" ")
        option = int(input ("Choose your option: "))
        return option
    
    
    def print_details(self):
        #STEP A.4.3
        print("First name: %s" %self.fname)
        print("Last name: %s" %self.lname)
        print("Account No: %s" %self.account_no)
        print("Address: %s" %self.address[0])
        print(" %s" %self.address[1])
        print(" %s" %self.address[2])
        print(" %s" %self.address[3])
        print(" ")
        
    def print_Details(self):
         #STEP A.4.3
         print("Account Type : %s" %self.__class__.__name__)
         print("Interest Rate: %.2f%%" % (self.interest * 100))
         print("Overdraft Limit: %.2f" % self.draft)
         print(" ")
         print("First name: %s" %self.fname)
         print("Last name: %s" %self.lname)
         print("Account No: %s" %self.account_no)
         if len(self.address)>=4:
             print("Address: %s" %self.address[0])
             print(" %s" %self.address[1])
             print(" %s" %self.address[2])
             print(" %s" %self.address[3])
         else:
             print("Address: N/A")
         print("The Current account balance is %s" %self.balance)
         print(" ")   
         
   
        
   
    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                #STEP A.4.1
                amount=float(input("\n Please enter amount to be deposited: "))
                self.deposit(amount)
                self.print_balance()
                
                
            elif choice == 2:
                amount=float(input("\n Please enter amount to be Withdraw: "))
                self.withdraw(amount)
                
                self.print_balance()
                
            elif choice == 3:
                #STEP A.4.4
                self.print_balance()
                
            elif choice == 4:
                #STEP A.4.2
                fname=input("\n Enter new customer first name: ")
                self.update_first_name(fname)
                sname = input("\nEnter new customer last name: ")
                self.update_last_name(sname)
                self.save_bank_data()
                
            elif choice == 5:
                Door_number = input("Enter your New street number : ")
                Street_Name = input("Enter your New street name : ")
                City = input("Enter your New city : ")
                Post_code = input("Enter your New postcode : ")
                Address=Door_number,Street_Name,City,Post_code
                self.update_address(Address)
                self.save_bank_data()
            
            elif choice == 6:
                self.print_details()
            elif choice == 7:
                loop = 0
        print ("\n Exit account operations")
        
        
class PremiumAccount(CustomerAccount):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.interest = 0.1
        self.draft = 5000 
    def print_Details(self):
        super().print_Details()
        print("Account Type: %s" % self.__class__.__name__)
        print("Interest Rate: %.2f%%" % (self.interest * 100))
        print("Overdraft Limit: %.2f" % self.draft)
        print(" ")

    def save_bank_data(self):
        # Add logic to save bank data specific to StudentAccount
        print("Saving bank data for PremiumAccount...")
        # Add your saving logic here
        print("Bank data saved.")    
        
        
        
class BasicAccount(CustomerAccount):
    def __init__ (self,*args,**kwargs):
        super().__init__(*args, **kwargs) 
        self.interest=0.1
        self.draft=1000
    def print_Details(self):
        super().print_Details()
        print("Account Type: %s" % self.__class__.__name__)
        print("Interest Rate: %.2f%%" % (self.interest * 100))
        print("Overdraft Limit: %.2f" % self.draft)
        print(" ")

    def save_bank_data(self):
        # Add logic to save bank data specific to StudentAccount
        print("Saving bank data for BasicAccount...")
        # Add your saving logic here
        print("Bank data saved.")     
        
class StudentAccount(CustomerAccount):
    def __init__ (self,*args,**kwargs):
        super().__init__(*args, **kwargs) 
        self.interest=0.05
        self.draft=1500
        
   
    
        
        
    def print_Details(self):
        super().print_Details()
        print("Account Type: %s" % self.__class__.__name__)
        print("Interest Rate: %.2f%%" % (self.interest * 100))
        print("Overdraft Limit: %.2f" % self.draft)
        print(" ")

    def save_bank_data(self):
        # Add logic to save bank data specific to StudentAccount
        print("Saving bank data for Account...")
        # Add your saving logic here
        print("Bank data saved.")    
    
    
    