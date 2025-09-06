import tkinter
from tkinter import messagebox


from bank_system import BankSystem




class Entry_GUI:
    accounts_list = []
    admins_list = []

    def __init__(self):
        self.mw=tkinter.Tk()
        self.output=tkinter.StringVar()
        
        
        self.current_account_number = 0
        
        label_dashboard = tkinter.Label(self.mw, text="Online Banking System ")
        self.label1=tkinter.Label(self.mw,text="Admin username")
        self.entry1=tkinter.Entry(self.mw,width=15)
        
        self.label2=tkinter.Label(self.mw,text="Admin password")
        self.entry2=tkinter.Entry(self.mw,width=15)
        self.entry2.config(show="*");

        
        self.button1=tkinter.Button(self.mw,text="Login",command=self.capture_credentials_and_login)
        self.label3=tkinter.Label(self.mw,textvariable=self.output)
        
        self.button2=tkinter.Button(self.mw, text="Quit", command=self.mw.destroy)
       
        label_dashboard.grid(row=0, column=1, padx=5, pady=5)
        self.label1.grid(row=1,column=1,padx=15,pady=15)
        self.entry1.grid(row=1,column=2,padx=15,pady=15)

        
        self.label2.grid(row=2,column=1,padx=15,pady=15)
        self.entry2.grid(row=2,column=2,padx=15,pady=15)
        
        self.button1.grid(row=3,column=2,padx=15,pady=15) 
        self.label3.grid(row=3,column=1,padx=15,pady=15)
        
        self.button2.grid(row=0,column=0,padx=15,pady=15) 
        
        
        
        self.app=BankSystem()
    def create_button(self, text, command, row, column):
        button = tkinter.Button(self.mw, text=text, command=command, width=40, height=2)  
        button.grid(row=row, column=column, padx=15, pady=15)
        return button 
    def create_button2(self, text, command, row, column):
        button = tkinter.Button(self.mw, text=text, command=command, width=5, height=1)  
        button.grid(row=row, column=column, padx=15, pady=15)
        return button
    def create_button3(self, text, command, row, column):
        button = tkinter.Button(self.mw, text=text, command=command, width=7, height=1)  
        button.grid(row=row, column=column, padx=15, pady=15)
        return button
        
    def capture_credentials_and_login(self):
        
        username = self.entry1.get()
        password = self.entry2.get()
        

        
        msg, found_admin = self.app.admin_login(username, password)

        
        
        if found_admin is not None:
            self.mainboard() 
            
        else:    
            error_msg1 = "Incorrect"
            self.output.set(error_msg1)   
            
    def mainboard(self):
        
        self.hide_widgets()

        
        label_dashboard = tkinter.Label(self.mw, text="Welcome to the Dashboard!")
        transfer=self.create_button(text="Transfer money",command=self.transfer,row=1,column=0)
        Customer=self.create_button(text="Customer account operations & profile settings",command=self.customer_account,row=2,column=0)
        Close=self.create_button(text="Close customer account",command=self.True_close,row=3,column=0)
        New=self.create_button(text="Add new customer",command=self.True_add,row=4,column=0)
        Print=self.create_button(text="Print all customers detail",command=self.print_details,row=5,column=0)
        Admin=self.create_button(text="Admin account operations & profile settings",command=self.Admin_setting,row=6,column=0)
        reprot=self.create_button(text="Management report",command=self.True_Report,row=7,column=0)
        
       
        
        
        button_logout = self.create_button2(text="Logout", command=self.logout,row=8,column=0)
        
    

        label_dashboard.grid(row=0, column=0, padx=5, pady=5)
        button_logout.grid(row=8, column=0, padx=25, pady=25)   
        transfer.grid(row=1, column=0, padx=5, pady=5)
        Customer.grid(row=2, column=0, padx=5, pady=5)
        Close.grid(row=3, column=0, padx=5, pady=5)
        New.grid(row=4, column=0, padx=5, pady=5)
        Print.grid(row=5, column=0, padx=5, pady=5)
        Admin.grid(row=6, column=0, padx=5, pady=5)
        reprot.grid(row=7, column=0, padx=5, pady=5)
        
    def True_add(self):
        username = self.entry1.get()
        password = self.entry2.get()
        is_admin = self.app.Return_true(username, password)
    
        if is_admin:
        
            self.New_acc()
        else:
            self.access_Stoped()  
    
    
    def True_close(self):
        
        username = self.entry1.get()
        password = self.entry2.get()
        is_admin = self.app.Return_true(username, password)
    
        if is_admin:
       
            self.close_account()
        else:
            self.access_Stoped()    
    def True_Report(self):
        
        username = self.entry1.get()
        password = self.entry2.get()
        is_admin = self.app.Return_true(username, password)
    
        if is_admin:
        
            self.Management_report()
        else:
            self.access_Stoped()
    def access_Stoped(self):
        message_label = tkinter.Label(self.mw, text="Access Denied! Invalid credentials.")
        message_label.grid(row=9, column=0, padx=5, pady=5)
        
       

        
        
    def customer_account(self):
        self.hide_widgets()
        
        label_dashboard = tkinter.Label(self.mw, text="View Customer Setting")
        self.account = tkinter.Label(self.mw, text="Enter Customer Account number you wish to access: ")
        self.enter_button_name = tkinter.Button(self.mw, text="Enter", command=self.capture_credentials)
        button_logout = self.create_button2(text="Logout", command=self.logout,row=0,column=4)
        button_logoutt = self.create_button2(text="Back", command=self.logout5,row=0,column=0)
        
        self.accountentry = tkinter.Entry(self.mw, width=15)
        self.accountentry.grid(row=1, column=2, padx=15, pady=15)
        
        self.account.grid(row=1, column=1, padx=5, pady=5)
        self.enter_button_name.grid(row=1, column=4, padx=15, pady=15)                                  
        label_dashboard.grid(row=0, column=1, padx=5, pady=5)
        button_logout.grid(row=0, column=4, padx=5, pady=5)      
        button_logoutt.grid(row=0, column=0, padx=5, pady=5)
        
    def capture_credentials(self):
        
        username = self.accountentry.get()
        

        
        found_Customer = self.app.search_customers_by_account_no(username)

        
        
        if found_Customer is not None:
            self.Customer_setting()       
        
        
        
        
    def Customer_setting(self): 
        self.hide_widgets()

        
        label_dashboard = tkinter.Label(self.mw, text="Transaction Options!")
        transfer=self.create_button(text="Deposit money",command=self.deposit_Mon,row=1, column=1)
        withdraw=self.create_button(text="Withdraw money",command=self.withdraw_mon,row=2, column=1)
        balance=self.create_button(text="Check Balance",command=self.balance_money_details,row=3,column=1)
        update=self.create_button(text="Update customer name",command=self.Update_name_now,row=4,column=1)
        address=self.create_button(text="Update customer address",command=self.update_addr_now,row=5,column=1)
        details=self.create_button(text="Show Customer Details",command=self.Customer_detail,row=6,column=1)
        button_logoutt = self.create_button2(text="Logout", command=self.logout,row=0, column=2)
        button_logoutt.grid(row=0, column=3, padx=5, pady=5)  
        
        
        button_logout =self.create_button2(text="Back", command=self.logout5,row=0,column=0)
        
    

        label_dashboard.grid(row=0, column=1, padx=5, pady=5)
         
        transfer.grid(row=1, column=1, padx=5, pady=5)
        withdraw.grid(row=2, column=1, padx=5, pady=5)
        balance.grid(row=3,column=1,padx=5,pady=5)
        update.grid(row=4,column=1,padx=5,pady=5)
        address.grid(row=5,column=1,padx=5,pady=5)
        details.grid(row=6,column=1,padx=5,pady=5)
        button_logout.grid(row=0, column=0, padx=5, pady=5)
        
    def deposit_Mon(self):  
        self.hide_widgets()
        label_dashboard = tkinter.Label(self.mw, text="Deposit Money")
        self.amount = tkinter.Label(self.mw, text="Amount: ")
        
        self.transfer_button = self.create_button3( text="Deposit", command=self.deposit_money,row=1,column=3)
        self.amountenter = tkinter.Entry(self.mw, width=15)
        self.output_label = tkinter.Label(self.mw, textvariable = self.output)
        button_logoutt = self.create_button2(text="Back", command=self.logout6,row=0,column=0)
        button_logout = self.create_button2(text="Logout", command=self.logout,row=0,column=3)
        button_logout.grid(row=0, column=3, padx=5, pady=5) 
        
       
        self.amount.grid(row=1, column=0, padx=5, pady=5)
        
        self.amountenter.grid(row=1, column=1, padx=15, pady=15)
        self.transfer_button.grid(row=1, column=3, padx=15, pady=15)
        
        self.output_label.grid(row=2,column=1,padx=15,pady=15)
        button_logoutt.grid(row=0, column=0, padx=5, pady=5)
        label_dashboard.grid(row=0, column=1, padx=5, pady=5)
    def deposit_money(self):
        amount = float(self.amountenter.get())  
        account_number = self.accountentry.get()
    
        

        customer_account = self.app.search_customers_by_account_no(account_number)
        if customer_account:
            
            msg=self.app.deposit_money(account_number,amount)
            print(msg) 
            self.output.set(msg)
            
            
            
        else:
                print(f"Customer with account number {account_number} not found.")
    def withdraw_mon(self):
        self.hide_widgets()
        
        label_dashboard = tkinter.Label(self.mw, text="Withdraw Money")
        self.amount_NO = tkinter.Label(self.mw, text="Amount:")
        
        self.amountenter_NO = tkinter.Entry(self.mw, width=15)
        self.output_label = tkinter.Label(self.mw, textvariable = self.output)
        
        self.withdraw_button = self.create_button3(text="Withdraw", command=self.withdraw_money,row=1,column=3) 
        button_logoutt = self.create_button2(text="Back", command=self.logout6,row=0,column=0)
        
        button_logout = self.create_button2(text="Logout", command=self.logout,row=0,column=3)
        button_logout.grid(row=0, column=3, padx=5, pady=5) 
        
        self.amount_NO.grid(row=1, column=0, padx=5, pady=5)
        
        self.amountenter_NO.grid(row=1, column=1, padx=15, pady=15)
        
        self.output_label.grid(row=3,column=0,padx=15,pady=15)
        self.withdraw_button.grid(row=1, column=3, padx=15, pady=15)
        button_logoutt.grid(row=0, column=0, padx=5, pady=5)
        label_dashboard.grid(row=0, column=1, padx=5, pady=5)
    def withdraw_money(self):
        amount = float(self.amountenter_NO.get())  
        account_number_no = self.accountentry.get()
    
       

        customer_account = self.app.search_customers_by_account_no(account_number_no)
        if customer_account:
            
            msg=self.app.withdraw_money_now(account_number_no,amount)
            if "Insufficient funds" in msg:
                self.output.set("Insufficient funds")
        
            print(msg)
            self.output.set(msg)
        else:
              self.output.set(f"Customer with account number {account_number_no} not found.")            
   
       
    def balance_money_details(self):
       account_number_no = self.accountentry.get()
   
       print_window = tkinter.Toplevel(self.mw)
       print_window.title("Customer Details")

      
       text_widget = tkinter.Text(print_window, height=20, width=50)
       text_widget.pack()

       

       details_msg=self.app.PD_balance(account_number_no)
      

       text_widget.insert(tkinter.END, details_msg)

      
       close_button = tkinter.Button(print_window, text="Close", command=print_window.destroy)
       close_button.pack() 
       
       
    
    
        
    def Customer_detail(self):
        account_number_no = self.accountentry.get()
    
        print_window = tkinter.Toplevel(self.mw)
        print_window.title("Customer Details")

        
        text_widget = tkinter.Text(print_window, height=20, width=50)
        text_widget.pack()

        

        details_msg=self.app.PD(account_number_no)
       

        text_widget.insert(tkinter.END, details_msg)

       
        close_button = tkinter.Button(print_window, text="Close", command=print_window.destroy)
        close_button.pack() 
        
    def update_addr_now(self):
        self.hide_widgets()
        label_dashboard = tkinter.Label(self.mw, text="Update Customer Address")
        self.door = tkinter.Label(self.mw, text=" Door number: ")
        self.street = tkinter.Label(self.mw, text=" Street name: ")
        self.city = tkinter.Label(self.mw, text=" City: ")
        self.postcode = tkinter.Label(self.mw, text=" Post Code: ")
        button_logout = tkinter.Button(self.mw, text="Logout", command=self.logout)
        button_logout.grid(row=0, column=5, padx=5, pady=5) 
        
        self.enter_button_name = self.create_button3( text="Enter", command=self.update_addr_NOW,row=5,column=3)
        self.output_label = tkinter.Label(self.mw, textvariable = self.output)
        
        self.doorenter = tkinter.Entry(self.mw, width=15)
        self.streetenter = tkinter.Entry(self.mw, width=15)
        self.cityenter = tkinter.Entry(self.mw, width=15)
        self.postcodeenter = tkinter.Entry(self.mw, width=15)
       
        button_logoutt = self.create_button2(text="Back", command=self.logout6,row=0,column=0)
        
        
        
        self.door.grid(row=1, column=1, padx=5, pady=5)
        self.street.grid(row=2, column=1, padx=5, pady=5)
        self.city.grid(row=3, column=1, padx=5, pady=5)
        self.postcode.grid(row=4, column=1, padx=5, pady=5)
        
        self.output_label.grid(row=5,column=1,padx=15,pady=15)
        self.doorenter.grid(row=1, column=2, padx=15, pady=15)
        self.streetenter.grid(row=2, column=2, padx=5, pady=5)
        self.cityenter.grid(row=3, column=2, padx=5, pady=5)
        self.postcodeenter.grid(row=4, column=2, padx=5, pady=5)
        self.enter_button_name.grid(row=5, column=3, padx=15, pady=15)
        button_logoutt.grid(row=0, column=0, padx=5, pady=5)
        label_dashboard.grid(row=0, column=2, padx=5, pady=5)
        
    def update_addr_NOW(self):
        Door_number = self.doorenter.get()
        Street_Name= self.streetenter.get()
        City=self.cityenter.get()
        Post_code=self.postcodeenter.get()
        account_number = self.accountentry.get()
        Address=Door_number,Street_Name,City,Post_code
        
        print(f"Account Number: {account_number}")  

        customer_account = self.app.search_customers_by_account_no(account_number)
        if customer_account:
            
            msg=self.app.address(account_number, Address)
            print(msg)  
            
            
            self.output.set(msg)
        else:
                print(f"Customer with account number {account_number} not found.")      
    def Update_name_now(self):
        self.hide_widgets()
        label_dashboard = tkinter.Label(self.mw, text="Update Customer Name")
        self.Fname = tkinter.Label(self.mw, text=" Customer first name: ")
        self.Lname=tkinter.Label(self.mw, text=" Customer last name: ")
        
        self.enter_button_name = self.create_button3(text="Enter", command=self.Update_Name_NOW,row=3,column=4)
        
        self.output_label = tkinter.Label(self.mw, textvariable = self.output)
        self.FirstNameenter = tkinter.Entry(self.mw, width=15)
        self.LastNameenter = tkinter.Entry(self.mw, width=15)
       
        button_logoutt = self.create_button2(text="Back", command=self.logout6,row=0,column=0)
        button_logout = tkinter.Button(self.mw, text="Logout", command=self.logout)
        button_logout.grid(row=0, column=5, padx=5, pady=5) 
        
        
        
        self.Fname.grid(row=1, column=1, padx=5, pady=5)
        self.Lname.grid(row=2, column=1, padx=5, pady=5)
        
        self.output_label.grid(row=3,column=1,padx=15,pady=15)
        self.FirstNameenter.grid(row=1, column=2, padx=15, pady=15)
        self.LastNameenter.grid(row=2, column=2, padx=5, pady=5)
        self.enter_button_name.grid(row=3, column=4, padx=15, pady=15)
        button_logoutt.grid(row=0, column=0, padx=5, pady=5)
        label_dashboard.grid(row=0, column=2, padx=5, pady=5)
        
    def Update_Name_NOW(self):
        Firstname = self.FirstNameenter.get() 
        LastName= self.LastNameenter.get()
        account_number = self.accountentry.get()
    
        print(f"Account Number: {account_number}")  

        customer_account = self.app.search_customers_by_account_no(account_number)
        if customer_account:
            
            msg = self.app.Name(account_number,Firstname,LastName)
            
            print(msg)  
            
            
            self.output.set(msg)
        else:
                print(f"Customer with account number {account_number} not found.")      
                   
        
    def Management_report(self):
        self.hide_widgets()
        label_dashboard = tkinter.Label(self.mw, text="Management Report !")
        Total_Customer=self.create_button(text="Total number of customers",command=self.Total_Nums,row=1,column=1)
        Sum=self.create_button(text="Sum of all money customers",command=self.Total_sum,row=2,column=1)
        Total_over=self.create_button(text="Total amount of overdrafts",command=self.Total_over,row=3,column=1)
        Interest=self.create_button(text="Sum of interest rate",command=self.Total_int,row=4,column=1)
        button_logout = self.create_button2(text="Logout", command=self.logout,row=0,column=3)
        button_logout = self.create_button2(text="Back", command=self.logout5,row=0,column=0)
        
        button_logout.grid(row=0, column=3, padx=5, pady=5) 
        
        label_dashboard.grid(row=0, column=1, padx=5, pady=5)
        
        
        Total_Customer.grid(row=1,column=1,padx=5,pady=5)
        Sum.grid(row=2,column=1,padx=5,pady=5)
        Total_over.grid(row=3,column=1,padx=5,pady=5)
        Interest.grid(row=4,column=1,padx=5,pady=5)
        
        button_logout.grid(row=0, column=0, padx=5, pady=5)
        
    def Total_Nums(self):
        print_window = tkinter.Toplevel(self.mw)
        print_window.title("Customer Details")

        
        text_widget = tkinter.Text(print_window, height=20, width=50)
        text_widget.pack()

        

        details_msg=self.app.Number_of_customer()
       

        text_widget.insert(tkinter.END, details_msg)

       
        close_button = tkinter.Button(print_window, text="Close", command=print_window.destroy)
        close_button.pack() 
    def Total_sum(self):
        print_window = tkinter.Toplevel(self.mw)
        print_window.title("Customer Details")

        
        text_widget = tkinter.Text(print_window, height=20, width=50)
        text_widget.pack()

        

        details_msg=self.app.sum_of_balance()
       

        text_widget.insert(tkinter.END, details_msg)

       
        close_button = tkinter.Button(print_window, text="Close", command=print_window.destroy)
        close_button.pack() 
    def Total_over(self):
        print_window = tkinter.Toplevel(self.mw)
        print_window.title("Customer Details")

        
        text_widget = tkinter.Text(print_window, height=20, width=50)
        text_widget.pack()

        

        details_msg=self.app.overdrafts()
       

        text_widget.insert(tkinter.END, details_msg)

       
        close_button = tkinter.Button(print_window, text="Close", command=print_window.destroy)
        close_button.pack()
    def Total_int(self):
        print_window = tkinter.Toplevel(self.mw)
        print_window.title("Customer Details")

        
        text_widget = tkinter.Text(print_window, height=20, width=50)
        text_widget.pack()

        

        details_msg=self.app.sum_of_interest()
       

        text_widget.insert(tkinter.END, details_msg)

       
        close_button = tkinter.Button(print_window, text="Close", command=print_window.destroy)
        close_button.pack()     
        
    def Admin_setting(self):
        self.hide_widgets()
        label_dashboard = tkinter.Label(self.mw, text="Admin Setting!")
        update=self.create_button(text="Update Name",command=self.Name_update,row=1,column=1)
        address=self.create_button(text="Update Address",command=self.Address_update,row=2,column=1)
        password=self.create_button(text="Update Password",command=self.Password_update,row=3,column=1)
        button_logout = tkinter.Button(self.mw, text="Logout", command=self.logout)
        button_logout.grid(row=0, column=3, padx=5, pady=5) 
        
        button_logout = self.create_button2(text="Back", command=self.logout5,row=0,column=0)
        label_dashboard.grid(row=0, column=1, padx=5, pady=5)
        update.grid(row=1,column=1,padx=5,pady=5)
        address.grid(row=2,column=1,padx=5,pady=5)
        password.grid(row=3, column=1, padx=5, pady=5)
        
        button_logout.grid(row=0, column=0, padx=5, pady=5)
        
    def Password_update(self):
        self.hide_widgets()
        label_dashboard = tkinter.Label(self.mw, text="Password Setting!")
        self.old_Pass = tkinter.Label(self.mw, text=" Enter old Password : ")
        self.New_pass=tkinter.Label(self.mw, text=" Enter new Password : ")
        self.New_pass2=tkinter.Label(self.mw, text=" Enter new Password again: ")
        self.output_label = tkinter.Label(self.mw, textvariable = self.output)
        self.enter_button_name = self.create_button3(text="Submit", command=self.Admin_Pass_update,row=4,column=3)
        button_logout = tkinter.Button(self.mw, text="Logout", command=self.logout)
        button_logout.grid(row=0, column=4, padx=5, pady=5) 
        
        self.oldpassenter = tkinter.Entry(self.mw, width=15)
        self.newpasseneter = tkinter.Entry(self.mw, width=15)
        self.newpasseneter2= tkinter.Entry(self.mw, width=15)
       
        button_logoutt = self.create_button2(text="Back", command=self.logout4,row=0,column=0)
        
        
        
        
        self.old_Pass.grid(row=1, column=1, padx=5, pady=5)
        self.New_pass.grid(row=2, column=1, padx=5, pady=5)
        self.New_pass2.grid(row=3, column=1, padx=5, pady=5)
        label_dashboard.grid(row=0, column=2, padx=5, pady=5)
        self.output_label.grid(row=4,column=1,padx=15,pady=15)
        self.oldpassenter.grid(row=1, column=2, padx=15, pady=15)
        self.newpasseneter.grid(row=2, column=2, padx=5, pady=5)
        self.newpasseneter2.grid(row=3, column=2, padx=5, pady=5)
        self.enter_button_name.grid(row=4, column=3, padx=15, pady=15)
        button_logoutt.grid(row=0, column=0, padx=5, pady=5)
        
    def Admin_Pass_update(self):
        
        oldpassword = self.oldpassenter.get() 
        newpassword= self.newpasseneter.get()
        newpassword2= self.newpasseneter2.get()
        user=self.entry1.get()
        if newpassword==newpassword2:
        
    
           

            admin_account = self.app.search_admins_by_password(oldpassword)
            if admin_account:
            
                msg = self.app.Admin_pass(newpassword,user)
            
                print(msg)  
            
            
                self.output.set(msg)
            
                
        else:
            error_msg = "Password do not match."
            self.output.set(error_msg)
        
        
    def Name_update(self):
        self.hide_widgets()
        label_dashboard = tkinter.Label(self.mw, text="Update admin Name")
        self.Fname = tkinter.Label(self.mw, text="First name: ")
        self.Lname=tkinter.Label(self.mw, text="Last name: ")
        self.output_label = tkinter.Label(self.mw, textvariable = self.output)
        self.enter_button_name = tkinter.Button(self.mw, text="Enter", command=self.Admin_name_update)
        button_logout = tkinter.Button(self.mw, text="Logout", command=self.logout)
        button_logout.grid(row=0, column=4, padx=5, pady=5) 
        
        self.FirstNameenter = tkinter.Entry(self.mw, width=15)
        self.LastNameenter = tkinter.Entry(self.mw, width=15)
       
        button_logoutt = self.create_button2(text="Back", command=self.logout4,row=0,column=0)
        
        
        
        
        self.Fname.grid(row=1, column=1, padx=5, pady=5)
        self.Lname.grid(row=2, column=1, padx=5, pady=5)
        label_dashboard.grid(row=0, column=2, padx=5, pady=5)
        self.output_label.grid(row=3,column=1,padx=15,pady=15)
        self.FirstNameenter.grid(row=1, column=2, padx=15, pady=15)
        self.LastNameenter.grid(row=2, column=2, padx=5, pady=5)
        self.enter_button_name.grid(row=3, column=3, padx=15, pady=15)
        button_logoutt.grid(row=0, column=0, padx=5, pady=5)
        
    def Admin_name_update(self):
        User=self.entry1.get()
        Firstname = self.FirstNameenter.get() 
        LastName= self.LastNameenter.get()
        
    
        print(f"Account Number: {User}")  

        admin_account = self.app.search_admins_by_name(User)
        if admin_account:
            
            msg = self.app.Admin_Name(User,Firstname,LastName)
            
            print(msg)  
            
            
            self.output.set(msg)
        else:
                print(f"admin with account number {User} not found.")
                
    def Address_update(self):
        self.hide_widgets()
        label_dashboard = tkinter.Label(self.mw, text="Address Setting!")
        self.door = tkinter.Label(self.mw, text=" Enter new door number: ")
        self.street = tkinter.Label(self.mw, text=" Enter new street name: ")
        self.city = tkinter.Label(self.mw, text=" Enter new city: ")
        self.postcode = tkinter.Label(self.mw, text=" Enter new Post Code: ")
        self.output_label = tkinter.Label(self.mw, textvariable = self.output)
        button_logout = tkinter.Button(self.mw, text="Logout", command=self.logout)
        button_logout.grid(row=0, column=4, padx=5, pady=5) 
        
        self.enter_button_name = tkinter.Button(self.mw, text="Enter", command=self.Admin_updated)
        
        label_dashboard.grid(row=0, column=2, padx=5, pady=5)
        self.doorenter = tkinter.Entry(self.mw, width=15)
        self.streetenter = tkinter.Entry(self.mw, width=15)
        self.cityenter = tkinter.Entry(self.mw, width=15)
        self.postcodeenter = tkinter.Entry(self.mw, width=15)
       
        button_logoutt =self.create_button2(text="Back", command=self.logout4,row=0,column=0)
        
        
        self.output_label.grid(row=6,column=0,padx=15,pady=15)
        self.door.grid(row=2, column=1, padx=5, pady=5)
        self.street.grid(row=3, column=1, padx=5, pady=5)
        self.city.grid(row=4, column=1, padx=5, pady=5)
        self.postcode.grid(row=5, column=1, padx=5, pady=5)
        
        
        self.doorenter.grid(row=2, column=2, padx=15, pady=15)
        self.streetenter.grid(row=3, column=2, padx=5, pady=5)
        self.cityenter.grid(row=4, column=2, padx=5, pady=5)
        self.postcodeenter.grid(row=5, column=2, padx=5, pady=5)
        self.enter_button_name.grid(row=6, column=3, padx=15, pady=15)
        button_logoutt.grid(row=0, column=0, padx=5, pady=5)
        
        
    def Admin_updated(self):
        account_number=self.entry1.get()
        Door_number = self.doorenter.get()
        Street_Name= self.streetenter.get()
        City=self.cityenter.get()
        Post_code=self.postcodeenter.get()
        
        Address=Door_number,Street_Name,City,Post_code
    
        print(f"Account Number: {account_number}")  

        customer_account = self.app.search_admins_by_name(account_number)
        if customer_account:
            
            msg=self.app.address_admin(account_number, Address)
            print(msg)  
            
            
            self.output.set(msg)
        else:
                print(f"Customer with account number {account_number} not found.")
            
                
                
                
        
        
    def print_details(self):
        
        
        
        print_window = tkinter.Toplevel(self.mw)
        print_window.title("Customer Details")

        
        text_widget = tkinter.Text(print_window, height=20, width=50)
        text_widget.pack()

        

        details_msg=self.app.details()
       

        text_widget.insert(tkinter.END, details_msg)

       
        close_button = tkinter.Button(print_window, text="Close", command=print_window.destroy)
        close_button.pack() 
        
    def close_print_window(self):
        if hasattr(self, 'print_window') and self.print_window.winfo_exists():
            self.print_window.destroy()
        self.hide_widgets()    
        
    def New_acc(self):
        
        self.hide_widgets()
        
        self.balance = tkinter.Label(self.mw, text="Balance: ")
        self.Fname = tkinter.Label(self.mw, text=" Enter customer first name: ")
        self.Lname=tkinter.Label(self.mw, text=" Enter customer last name: ")
        self.door = tkinter.Label(self.mw, text=" Enter door number: ")
        self.street = tkinter.Label(self.mw, text=" Enter street name: ")
        self.city = tkinter.Label(self.mw, text=" Enter city: ")
        self.postcode = tkinter.Label(self.mw, text=" Enter Post Code: ")
        self.account_type_label = tkinter.Label(self.mw, text="Select Account Type: ")
        self.output_label = tkinter.Label(self.mw, textvariable = self.output)
        button_logout = tkinter.Button(self.mw, text="Logout", command=self.logout)
        button_logout.grid(row=0, column=4, padx=5, pady=5) 
       
        
       
        
        
        self.balanceneter=tkinter.Entry(self.mw,width=15)
        self.FirstNameenter = tkinter.Entry(self.mw, width=15)
        self.LastNameenter = tkinter.Entry(self.mw, width=15) 
        
        self.doorenter = tkinter.Entry(self.mw, width=15)
        self.streetenter = tkinter.Entry(self.mw, width=15)
        self.cityenter = tkinter.Entry(self.mw, width=15)
        self.postcodeenter = tkinter.Entry(self.mw, width=15)
        
        self.options=tkinter.StringVar()
        
        self.options.set("Student")
        
        
        
        
        self.student=tkinter.Radiobutton(self.mw,text="Student",variable=self.options,value="Student")
        self.basic=tkinter.Radiobutton(self.mw,text="Basic",variable=self.options,value="Basic")
        self.premium=tkinter.Radiobutton(self.mw,text="Premium",variable=self.options,value="Premium")
        
        
        self.student.grid(row=1, column=1, padx=5, pady=5)
        self.basic.grid(row=1, column=2, padx=5, pady=5)
        self.premium.grid(row=1, column=3, padx=5, pady=5)
        
        
       
       
        
        submit_button = tkinter.Button(self.mw, text="Enter", command=self.NEWACCOUNT)
        submit_button.grid(row=9, column=3, columnspan=2, pady=10)
        
        
        
        
        button_logoutt = tkinter.Button(self.mw, text="Back", command=self.logout2)
        self.balance.grid(row=2, column=1, padx=5, pady=5)
        self.Fname.grid(row=3, column=1, padx=5, pady=5)
        self.Lname.grid(row=4, column=1, padx=5, pady=5)
        self.door.grid(row=5, column=1, padx=5, pady=5)
        self.street.grid(row=6, column=1, padx=5, pady=5)
        self.city.grid(row=7, column=1, padx=5, pady=5)
        self.postcode.grid(row=8, column=1, padx=5, pady=5)
        self.account_type_label.grid(row=0, column=2, padx=5, pady=5)
        
        self.balanceneter.grid(row=2, column=2, padx=15, pady=15)
        self.FirstNameenter.grid(row=3, column=2, padx=15, pady=15)
        self.LastNameenter.grid(row=4, column=2, padx=5, pady=5)
        self.doorenter.grid(row=5, column=2, padx=15, pady=15)
        self.streetenter.grid(row=6, column=2, padx=5, pady=5)
        self.cityenter.grid(row=7, column=2, padx=5, pady=5)
        self.postcodeenter.grid(row=8, column=2, padx=5, pady=5)
        self.output_label.grid(row=9,column=2,padx=15,pady=15)
        
        button_logoutt.grid(row=0, column=0, padx=5, pady=5)
        
    def NEWACCOUNT(self):
       AccountType = self.options.get()
       Balance=self.balanceneter.get() 
       Fname=self.FirstNameenter.get()
       Lname=self.LastNameenter.get()
       Door_number = self.doorenter.get()
       Street_Name= self.streetenter.get()
       City=self.cityenter.get()
       Post_code=self.postcodeenter.get()
       
       
       Address=Door_number,Street_Name,City,Post_code
       
       msg=self.app.New_account(AccountType, Balance, Fname, Lname, Address)
       
       self.output.set(msg)
        
    def close_account(self):
        self.hide_widgets()
        self.output.set("")
        self.account = tkinter.Label(self.mw, text="Account number you wish to close: ")
        self.output_label = tkinter.Label(self.mw, textvariable = self.output)
        label_dashboard = tkinter.Label(self.mw, text="Close account")
        self.accountentry = tkinter.Entry(self.mw, width=15)
        self.enter_button_name = tkinter.Button(self.mw, text="Enter", command=self.Close_account)
        button_logout = tkinter.Button(self.mw, text="Logout", command=self.logout)
        button_logout.grid(row=0, column=4, padx=5, pady=5) 
        self.account.grid(row=1, column=1, padx=5, pady=5)
        self.accountentry.grid(row=1, column=2, padx=15, pady=15)
        self.enter_button_name.grid(row=3, column=3, padx=15, pady=15)                                  
        label_dashboard.grid(row=0, column=2, padx=5, pady=5)
        button_logoutt =self.create_button2(text="Back", command=self.logout2,row=0,column=0)     
        button_logoutt.grid(row=0, column=0, padx=5, pady=5)
        self.output_label.grid(row=3,column=1,padx=15,pady=15)

                           
    def Close_account(self):
        account_no = self.accountentry.get()
        
        Confirm = messagebox.askyesno("Close Account", f"Are you sure you want to close account {account_no}?")

        if Confirm:
           
           self.app.Close_account(account_no)
           self.output.set(f"Account {account_no} closed successfully.")
        else:
           
           self.output.set("Account closure canceled.")
         

    def transfer(self):
        self.hide_widgets()
        self.output.set("")
        label_dashboard = tkinter.Label(self.mw, text="Online Transfers")
        self.sender = tkinter.Label(self.mw, text="Sender account number: ")
        self.amount = tkinter.Label(self.mw, text="Amount: ")
        self.receiver = tkinter.Label(self.mw, text="Receiver account number: ")
        button_logout = self.create_button2(text="Back", command=self.logout2,row=0,column=0)
        self.transfer_button = tkinter.Button(self.mw, text="Transfer", command=self.transferMoney)
        self.output_label = tkinter.Label(self.mw, textvariable = self.output)
        self.senderentry = tkinter.Entry(self.mw, width=15)
        self.amountentry = tkinter.Entry(self.mw, width=15)
        self.receiverentry = tkinter.Entry(self.mw, width=15)
        button_logoutt = tkinter.Button(self.mw, text="Logout", command=self.logout)
        button_logoutt.grid(row=0, column=4, padx=5, pady=5) 
        button_logout.grid(row=0, column=0, padx=5, pady=5)
        self.sender.grid(row=1, column=1, padx=5, pady=5)
        self.senderentry.grid(row=1, column=2, padx=15, pady=15)
        self.amount.grid(row=2, column=1, padx=5, pady=5)
        self.amountentry.grid(row=2, column=2, padx=15, pady=15)
        self.receiver.grid(row=3, column=1, padx=5, pady=5)
        self.receiverentry.grid(row=3, column=2, padx=15, pady=15)
        self.transfer_button.grid(row=4, column=3, padx=5, pady=5)
        self.output_label.grid(row=4,column=2,padx=15,pady=15)
        label_dashboard.grid(row=0, column=2, padx=5, pady=5)
        
    def transferMoney(self):
        
        sender = self.senderentry.get()
        amount = float(self.amountentry.get())
        receiver = self.receiverentry.get()

    
        sender_account = self.app.search_customers_by_account_no(sender)
        receiver_account = self.app.search_customers_by_account_no(receiver)

        if sender_account and receiver_account:
            
            msg = self.app.transferMoney(sender_account.get_account_no(), receiver_account.get_account_no(), amount)
            print(msg)  
            
            self.output.set(msg)
        else:
        
            error_msg = "Error: Sender or receiver account not found."
            print(error_msg)
            self.output.set(error_msg)
           
    def logout(self):
        
        self.mw.destroy()
        self.__init__()
        
    def logout2(self):
        
        self.mainboard() 
        self.output.set("")
    def logout3(self):
        
        
        self.Custboard()  
        self.output.set("")
    def logout4(self):
        
        self.Admin_setting()
        self.output.set("")
        
        
    def logout5(self):
       self.mainboard()
       self.output.set("")
       
    def logout7(self):
        self.customer_account()
        self.output.set("")
        
        
    def logout6(self):
        self.Customer_setting()
        self.output.set("")
        
        
    def clear_widgets(self):
        
        for widget in self.mw.winfo_children():
            widget.destroy() 
    def hide_widgets(self):
   
        for widget in self.mw.winfo_children():
            try:
                widget.grid_remove()
            except AttributeError:
                try:
                    widget.pack_forget()
                except AttributeError:
                
                    if hasattr(widget, 'place_forget'):
                        widget.place_forget()
            
            
            
            
            
       
        
               
                
if __name__ =="__main__":             
    gui=Entry_GUI()  

gui.mw.mainloop()
