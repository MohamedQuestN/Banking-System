from person import Personal_details
class Admin(Personal_details):
    
    def __init__(self,user_name, password, full_rights,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.user_name = user_name
        self.password = password
        self.full_admin_rights = full_rights
    
  
    
    def set_username(self, uname):
        self.user_name = uname
        
    def get_username(self):
        return self.user_name
        
    def get_address(self):
        return self.address      
    
    def update_password(self, password):
        self.password = password
    
    def get_password(self):
        return self.password
    
    def set_full_admin_right(self, admin_right):
        self.full_admin_rights = admin_right

    def has_full_admin_right(self):
        return self.full_admin_rights
    

    def account_menu2(self):
        print ("1) Update Admin name")
        print ("2) Update Admin address")
        print ("3) Back")
        print (" ")
        option = int(input ("Choose your option: "))
        return option      
    def run_account_options_admin(self):
        loop = 1
        while loop ==1:
            choice=self.account_menu2()
            if choice == 1:
                #STEP A.4.2
                fname=input("\n Enter new Admin first name: ")
                self.update_first_name(fname)
                sname = input("\nEnter new Admin last name: ")
                self.update_last_name(sname)
                self.save_bank_data()
               
                
            elif choice == 2:
                Door_number = input("Enter your New street number : ")
                Street_Name = input("Enter your New street name : ")
                City = input("Enter your New city : ")
                Post_code = input("Enter your New postcode : ")
                Address=Door_number,Street_Name,City,Post_code
                self.update_address(Address)
                self.save_bank_data()
                
            
            elif choice == 3:
                loop = 0
        print ("\n Exit account operations")  
        
        
        
        
    def save_bank_data(self):
        # Add logic to save bank data specific to StudentAccount
        print("Saving bank data for Account...")
        # Add your saving logic here
        print("Bank data saved.")     