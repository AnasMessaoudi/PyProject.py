import time
import os
import data_base
def clear_screen():
    time.sleep(2)
    os.system("cls")
class Sign_in:
    def __init__(self):
        self.id=int(input("enter your id (only numbers allowed):"))
        result=data_base.check_existance(self.id)
        while not result:
            print("id not found !!")
            self.id=int(input("enter your id:"))
            result=data_base.check_existance(self.id)
        self.pw=input("enter your password: ")
        test=data_base.check_pw(self.id,self.pw)
        c=0
        while test==False and c<3:
            print("the password that you typed is false !!")
            print(f"you have {3-c} trials left !!")
            self.pw=input("enter your password: ")
            test=data_base.check_pw(self.id,self.pw)
            c+=1
        if test==False:
            quit()
        self.age=data_base.get_age(self.id)
        self.name=data_base.get_name(self.id)
        self.__salary=data_base.get_salary(self.id)
        self.loan=data_base.get_loan(self.id)
        self.duration=data_base.get_duration(self.id)
        self.current_money=data_base.get_current_money(self.id)
        self.__bank=data_base.get_bank(self.id)
        
    def set_bank(self,bank):
        self.__bank =bank
    def get_bank(self):
        return self.__bank
    def set_salary(self,salary):
        self.__salary=salary
    def get_salary(self):
        return self.__salary
class BankAcc:#n7eb na3ml menu kima hadha lel clients el gdom w hadha n5alih lel clients el jdod 
    def __init__(self):
        self.id=0
        self.name=''
        self.age=0
        self.salary=0
        self.__pw=''
        self.__bank=''
        self.loan=0
        self.duration=0
        self.current_money=1200
        while self.name=='' or self.age<18 or self.salary==0 or self.__pw=='':
            if self.name=='':
                self.name=input("enter your name:")
            elif self.age<18:
                self.age=int(input("enter you age (MUST BE OVER 18!!):"))
            elif self.salary==0:
                self.salary=int(input("enter your salary"))
            elif self.__pw=='':
                self.__pw=input("Choose your account's password :")
    def set_bank(self,bank):
        self.__bank=bank
    def get_bank(self):
        return self.__bank
    def set_pw(self,pw):
        self.__pw=pw
    def get_pw(self):
        return self.__pw
    def get_salary(self):
        return self.salary
    def get_current_money(self):
        return self.current_money
class Bank:
    no_of_clients=0
    def __init__(self,Bname):
        self.clients=[]
        self.Bname=Bname
    def find_client_in_bank(self,client):
        for item in self.clients:
            if item==client:
                return item
    def Add_client(self,client):
        self.clients.append(client)
        self.no_of_clients+=1
    def get_no_of_clients(self):
        return self.no_of_clients
class Menu:
    def display_menu(self):
        display=f"""
               Welcome   !
               please enter your choice (1 or 2):
               1. Enter personal informations
               2. Create an account 
                """
        print(display)
        self.choice = int(input("choose an option(1 or 2):"))
        return self.choice
    def display_loan_menu(self):
        op="""
        1. Check the loan amount 
        2. Check the remaining payment periode
        3. Quit this menu
        """
        print(op)
        o=10
        while o!=2 and o!=1 and o!=3:
            o=int(input("choose an option(1 or 2 or 3):"))
        return o
class Options:
    def display_options(self):
        op="""
        1. You are trying to choose another bank 
        2. You are staying at your current bank  
        """
        print(op)
        o=10
        while o!=2 and o!=1:
            o=int(input("choose an option(1 or 2):"))
        return o
    def display_options2(self):#matsir kan ki yabda bch yda5l infos mch bch ya3ml new account
        op="""
        1. Take a Loan
        2. Check the amount of money in your account 
        3. Withdraw an amount of money
        4.Quit this menu  
        """
        print(op)
        o=10
        while o!=2 and o!=1 and o!=3 and o!=4:
            o=int(input("choose an option(1 or 2 or 3 or 4):"))
        return o
class system:
    def __init__(self):
        self.banks=[Bank("attijari"),Bank("al zaytouna"),Bank("al islami")]
        self.menu=Menu()
        self.options=Options()
    def find(self,string):
        for bank in self.banks:
            if bank.Bname==string:
                return bank   
    def run(self):
        r=self.menu.display_menu()
        op=0
        if r==1:
            self.client=Sign_in()
            op=self.options.display_options()
            if op==1:
                if self.client.loan==0:
                    self.option1()
                    self.client.current_money=self.client.get_salary()
                    data_base.update_client_bank(self.client.id,self.client.get_bank())
                else:
                    print("YOU CAN CHOOSE ANOTHER BANK ONLY AFTER YOU PAY YOUR LOAN !!!")
            else:
                while True:
                    clear_screen()
                    if self.client.loan!=0:
                        while True:
                            k=self.menu.display_loan_menu()
                            if k==1 :
                                print(f"the remaining amount of loan is {self.client.loan} ")
                                clear_screen()
                            elif k==2:
                                print(f"The remaining payment periode is {self.client.duration} months ")
                                clear_screen()
                            else:
                                break
                    op2=self.options.display_options2()
                    if op2==2:
                        print(self.client.current_money)
                        clear_screen()
                    elif op2==3:
                        Q=self.client.current_money#el Q hadhi dima 0 tetsala7 ki na3ml data base nejbed menha infos
                        amount=int(input("enter the amount of money you'd like to get :"))
                        if amount>Q:
                            print(f"YOU DON'T HAVE ENOUGH MONEY !! YOUR ACCOUNT BALANCE IS {self.client.current_money}")
                        else:
                            print("withdraw done successfully !!!")
                            self.client.current_money-=amount
                            data_base.update_client_current_money(self.client.id,self.client.current_money)
                        clear_screen()
                    elif op2==1:
                        if self.client.loan != 0:
                            print("YOU ALREADY HAVE A LOAN THAT YOU NEED TO PAY !!")
                            clear_screen()
                        else:
                            x=int(input("enter the amount of money you'd like to take as a loan :"))                           
                            self.client.loan+=x
                            data_base.update_client_loan(self.client.id,x)
                            self.client.set_salary(self.client.get_salary()*0.7)
                            data_base.update_client_salary(self.client.id,self.client.get_salary())
                            self.client.duration=(x//(self.client.get_salary()*0.3))+1
                            data_base.update_client_duration(self.client.id,self.client.duration)
                            print("you took the loan successfully !!")
                            print("from now on we are taking 30% from your salary to pay your debt ")
                            print(f"your current salary is {self.client.get_salary()}")
                            print(f"this will proceed for {self.client.duration} months")
                            clear_screen()
                    else:
                        break
        else:
            self.client=BankAcc()
            self.client.current_money=self.client.salary
            self.option1()   
            #nsobouh fl data base
            self.client.id=data_base.add_client_to_db(self.client.get_bank(),self.client.name,self.client.age,self.client.get_salary(),self.client.get_pw(),self.client.loan,self.client.duration,self.client.current_money)
            print(f"Your id is {self.client.id} . YOU MUST REMEMBER THAT SO YOU CAN ACCESS YOUR ACCOUNT !!")
    def  option1(self):
        new_bank=''
        test = False
        while test==False:
            new_bank=input("enter the bank you would like to choose: ")
            for bank in self.banks:
                if bank.Bname==new_bank:
                    test=True
                    break
            if test==False:
                print("The bank that you typed is not in our system pls enter an existing bank")
        self.client.set_bank(new_bank)
        r=self.find(self.client.get_bank())
        r.Add_client(self.client) 

data_base.show_clients()
s=system()
s.run()
data_base.show_clients()
#nzidou faza bl wa9t yabda kol chhar yna9es ml loan el flous elli y9osouhom 3lih w yna9s el duration bchhar w nzid fazet forgot password wla forgot id