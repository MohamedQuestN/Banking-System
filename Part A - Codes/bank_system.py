import os

from customer_account import CustomerAccount
from admin import Admin
from customer_account import StudentAccount
from customer_account import BasicAccount
from customer_account import PremiumAccount

accounts_list = []
admins_list = []

class BankSystem(object):
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data()
        self.current_account_number = 1230
        
    
    def load_bank_data(self):
        
        file_path=os.path.join(os.getcwd(),"Customer.txt")
        try:
            with open(file_path,"r") as file:
                 for line in file:
                     
                     Data=line.strip().split(',')
                     if Data[0]=="StudentAccount":
            
                         Customer_account,Balance,first_Name,last_Name,*address=Data[1:]
                     
                         CustInfo=StudentAccount(Customer_account, Balance, first_Name, last_Name,address)
                         self.accounts_list.append(CustInfo)
                         
                     if Data[0]=="BasicAccount":
                         Customer_account,Balance,first_Name,last_Name,*address=Data[1:]
                     
                         CustInfo=BasicAccount(Customer_account, Balance, first_Name, last_Name,address)
                         self.accounts_list.append(CustInfo)
                     if Data[0]=="PremiumAccount":
                        Customer_account,Balance,first_Name,last_Name,*address=Data[1:]
                    
                        CustInfo=PremiumAccount(Customer_account, Balance, first_Name, last_Name,address)
                        self.accounts_list.append(CustInfo)   
                        
                         
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}") 
        
     
        file_path=os.path.join(os.getcwd(),"Admins.txt")
        try:
            with open(file_path,"r") as file:
                 for line in file:
                     
                     XS=line.strip().split(',')
            
                     User_number,Password,Full_rights,First_Name,Last_Name,*Address=XS[0:]
                     
                     A=Admin(User_number, Password, Full_rights, First_Name, Last_Name, Address)
                     self.admins_list.append(A)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
            
            
            
            
    


    def save_bank_data(self):
    
        customer_file_path = os.path.join(os.getcwd(),"Customer.txt")
        with open(customer_file_path, "w") as customer_file:
            for account in self.accounts_list:
                if isinstance(account, CustomerAccount):
                    account_info = [
                    account.__class__.__name__,
                    account.get_account_no(),
                    str(account.get_balance()),
                    account.get_first_name(),
                    account.get_last_name(),
                    *account.get_address()
                ]
                customer_file.write(','.join(account_info) + '\n')

    
        admin_file_path =os.path.join(os.getcwd(), "Admins.txt")
        with open(admin_file_path, "w") as admin_file:
            for admin in self.admins_list:
                if isinstance(admin,Admin):
                    admin_info = [
                        admin.get_username(),
                        admin.get_password(),
                        str(admin.has_full_admin_right()),
                        admin.get_first_name(),
                        admin.get_last_name(),
                        *admin.get_address()
            ]   
                admin_file.write(','.join(admin_info) + '\n')           
                    
        
      
        
    def New_account(self,Account_Type,Balance, first_Name, last_Name,address):
        
        
            customer_account = self.generate_sequential_account_number()   

        
            while self.search_customers_by_account_no(customer_account):
                customer_account = self.generate_sequential_account_number()      

            Cust_info = None  

            if Account_Type == "Student":
                Cust_info = StudentAccount(customer_account, Balance, first_Name, last_Name, address,)
            elif Account_Type == "Basic":
                Cust_info = BasicAccount(customer_account, Balance, first_Name, last_Name, address,)
            elif Account_Type == "Premium":
                Cust_info = PremiumAccount(customer_account, Balance, first_Name, last_Name, address,)

            if Cust_info:
                self.accounts_list.append(Cust_info) 
                self.save_bank_data()
                return (f"\nNew {Account_Type} account created successfully.\n")
                
        
    

    def search_admins_by_name(self, admin_username):
    # STEP A.2
        found_admin = None
        for a in self.admins_list:
            username = a.get_username()
            print(f"Comparing {username} with {admin_username}")
            if username.strip().lower() == admin_username.lower():
                found_admin = a
                break
        if found_admin is None:
                print("\nThe Admin %s does not exist! Try again...\n" % admin_username)
        return found_admin
    def search_admins_by_password(self,oldpassword):
    # STEP A.2
        found_admin = None
        for a in self.admins_list:
            password = a.get_password()
            print(f"Comparing {password} with {oldpassword}")
            if password== oldpassword:
                found_admin = a
                break
        if found_admin is None:
                print("\nThe Admin %s does not exist! Try again...\n" % oldpassword)
        return found_admin
        
    def search_customers_by_name(self, customer_lname):
        #STEP A.3
        found_customer = None
        for a in self.accounts_list:
            lname = a.get_last_name()
            if lname == customer_lname:
                found_customer = a
                break
        if found_customer == None:
           print("\n The customer %s does not exist! Try again...\n" %customer_lname)
        return found_customer
    
    def search_customers_by_account_no(self, account_no):
    # STEP A.3
        found_customer_account = None
        for a in self.accounts_list:
            if a.get_account_no() == account_no:
                found_customer_account = a  
                break

        return found_customer_account
    
    def search_customers_by_account_no_str(self, account_no):
    # STEP A.3
        found_customer_account = None
        for a in self.accounts_list:
            account_number = a.get_account_no()
            if account_number == account_no:
                found_customer_account = account_number  
                break
        return found_customer_account

    def Close_account(self,account_number):
        
        found_customer_account = None
        for account in self.accounts_list:
            if account.get_account_no() == account_number:
                found_customer_account = account
                break

        if found_customer_account is None:
            print(f"\nThe customer with account number {account_number} does not exist! Try again...\n")
        else:
                try:
                    self.accounts_list.remove(found_customer_account)
                    print(f"Customer with account number {account_number} deleted successfully.")
                except ValueError as e:
                        print(f"Error removing customer: {e}")

        self.save_bank_data()
        
        
    def Return_true(self,username,password):
        msg, admin_obj = self.admin_login(username, password)
        return admin_obj.has_full_admin_right()=="True"
        


    def transferMoney(self, sender_account_no, receiver_account_no, amount):
    
        sender = self.search_customers_by_account_no(sender_account_no)
        receiver = self.search_customers_by_account_no(receiver_account_no)

        try:
            sender_balance = float(sender.balance)
            sender_draft = float(sender.draft)
            if sender_balance + sender_draft >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                self.save_bank_data()
                new_balance=receiver.get_balance()
                return (f"Transfer successful New balance: {new_balance}")
            else:
                return "Insufficient funds in the sender's account for the transfer."
        except ValueError:
                return "Error: Invalid balance or draft values for the sender."
            
    def withdraw_money_now(self, account_no, amount):
            # ToDo
                account = self.search_customers_by_account_no(account_no)

                try:
                    account_balance=float(account.balance)
                    account_draft=float(account.draft)
                    if account_balance + account_draft>=amount:
                        account.withdraw(amount)
                        self.save_bank_data()
                        return f"New balance: {account.balance}"
                    else:
                        return "Insufficient funds for withdrawal."
                except ValueError as e:
                    if str(e)=="Insufficient funds for withdrawal.":
                        return "Insufficient funds for withdrawal."
                    else:
                        return str(e)
    def address(self,account_no, address):
    # ToDo
        account_no=self.search_customers_by_account_no(account_no)

        try:
            
            if account_no:
                
                account_no.update_address(address)
                self.save_bank_data()
                return "Address Updated."
            else:
                return f"Customer with account number {account_no} not found."
        except ValueError:
                return "Error: ."   
    def address_admin(self,account_no, address):
    # ToDo
        account_no=self.search_admins_by_name(account_no)

        try:
            
            if account_no:
                
                account_no.update_address(address)
                self.save_bank_data()
                return "Address Updated."
            else:
                return f"Admin with account number {account_no} not found."
        except ValueError:
                return "Error: ."          
               
    def Name(self,account_no, First,Last):
    # ToDo
        account_no=self.search_customers_by_account_no(account_no)

        try:
            
            if account_no:
                
                account_no.update_first_name(First)
                account_no.update_last_name(Last)
                self.save_bank_data()
                return "Name Updated."
            else:
                return f"Customer with account number {account_no} not found."
        except ValueError:
                return "Error: ." 
    def Admin_Name(self,account_no, First,Last):
    # ToDo
        account_no=self.search_admins_by_name(account_no)

        try:
            
            if account_no:
                
                account_no.update_first_name(First)
                account_no.update_last_name(Last)
                self.save_bank_data()
                return "Name Updated."
            else:
                return f"Customer with account number {account_no} not found."
        except ValueError:
                return "Error" 
            
    def Admin_pass(self,newpassword,user):
     # ToDo
         account_no=self.search_admins_by_name(user)

         try:
             
             if account_no:
                 
                 account_no.update_password(newpassword)
                 
                 self.save_bank_data()
                 return "Password Updated."
             else:
                 return f"Customer with account number {account_no} not found."
         except ValueError:
                 return "Error"         
         
    def deposit_money(self, account_no, amount):
    # ToDo
        account = self.search_customers_by_account_no(account_no)

        try:
            # Check if the account is found
            if account:
                try:
                    account.deposit(amount)
                except:
                        return "Insufficient funds for withdrawal"
                self.save_bank_data()
                return f"New balance: {account.balance}"
            else:
                return f"Customer with account number {account_no} not found."
        except ValueError:
                return "Error: Invalid balance or draft values for the account."
    
                    
    def PD(self,account_no):
       
        account=self.search_customers_by_account_no(account_no)
        if account:
            details = f"Account Number: {account.get_account_no()}\n"
            details = f"Account Number: {account.get_account_no()}\n"
            details += f"Balance: {account.get_balance()}\n"
            details += f"First Name: {account.get_first_name()}\n"
            details += f"Last Name: {account.get_last_name()}\n"
            details += f"Address: {', '.join(account.get_address())}\n"
            
            return details    
        else:
            return f"Customer with account number {account_no} not found."
    def PD_balance(self,account_no):
       
        account=self.search_customers_by_account_no(account_no)
        if account:
            details = f"Account Number: {account.get_account_no()}\n"
            details = f"Account Number: {account.get_account_no()}\n"
            details += f"Balance: {account.get_balance()}\n"
            
            
            return details    
        else:
            return f"Customer with account number {account_no} not found."    
    def details(self):
        details_msg=""
        for customer in self.accounts_list:
            details = f"Account Type: {customer.__class__.__name__}\n"
            details += f"Account Number: {customer.get_account_no()}\n"
            details += f"Balance: {customer.get_balance()}\n"
            details += f"First Name: {customer.get_first_name()}\n"
            details += f"Last Name: {customer.get_last_name()}\n"
            details += f"Address: {', '.join(customer.get_address())}\n"
            details += "-------------------------------------------------"
            details_msg += details + "\n" 
        return details_msg    
    
    def Number_of_customer(self):
         Number_cust=[]
         
         
         for a in self.accounts_list:
             Account=a.get_account_no()
             
             Number_cust.append(Account)
             
             Number_cust_system=str(len(Number_cust))
             
         if Number_cust_system:
                 Total_number = max(map(int, Number_cust_system))
                 details=(f"\n Total number of customers in the system is: {Total_number}")
                 return details
                 
             
             
    def sum_of_balance(self):
         B=[]
         for a in self.accounts_list:
             
             Balance=int(a.get_balance())
             
             B.append(Balance)
             
         sumB=sum(B)

         details=(f"\n The sum of all money the customers currently have in their bank account is : {sumB}")
         return details
                 
                 
    def overdrafts(self):
        Overdraft = []
        details = ""

        for a in self.accounts_list:
            B = int(a.get_balance())
            if B < 0:
                Overdraft.append(B)

        Ov = sum(Overdraft)
        
        if Ov < 0:
            details = f"\n Total amount of overdrafts currently taken by all customers is : {Ov}"

        return details
    def sum_of_interest(self):
        interest_summary = {"StudentAccount": 0.0, "BasicAccount": 0.0, "PremiumAccount": 0.0}

        for account in self.accounts_list:
            account_type = account.__class__.__name__
            balance = float(account.get_balance())
            if balance > 0:
                interest_rate = float(account.interest) if hasattr(account, 'interest') else 0.0
                interest = balance * interest_rate * 1
                interest_summary[account_type] += interest

        details = ""
        for account_type, total_interest in interest_summary.items():
            details += f"\n Sum of interest for {account_type}: {total_interest}"

        return details
                    


    def generate_sequential_account_number(self):
        
        self.current_account_number += 1
        
        return str(self.current_account_number)    

        

                
    def admin_login(self, username, password):
		  #STEP A.1
          found_admin = self.search_admins_by_name(username)
          msg = "\n Login failed"
          if found_admin != None:
              if found_admin.get_password() == password:
                  msg = "\n Login successful"
                  return msg, found_admin
              else:
                  return msg, None
        

    
            
                



