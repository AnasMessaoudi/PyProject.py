import time
import os
import data_base
import gui 
from tkinter import messagebox
def clear_screen():
    time.sleep(2)
    os.system("cls")
class Sign_in(gui.Login):
    def __init__(self):
        self.display()
        self.id=int(self.retun_id())
        result=data_base.check_existance(self.id)
        while not result:
            self.show_id_error()
            self.display()
            self.id=int(self.retun_id())
            result=data_base.check_existance(self.id)
        self.pw=self.return_pass()
        test=data_base.check_pw(self.id,self.pw)
        c=0
        while test==False and c<3:
            if self.pw=='':
                self.show_pass_error()
            else:
                self.show_pass_error2()
            self.display()
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
class BankAcc(gui.Signup):
    bs=["attijari","al zaytouna","al islami"]
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
        while self.name=='' or self.age<18 or self.salary==0 or self.__pw=='' or self.get_bank()=='' or self.find(self.get_bank())==False:
            self.display()
            self.name=self.return_name()
            self.age=int(self.return_age())
            self.salary=int(self.return_salary())
            self.set_pw(self.return_pass())
            self.set_bank(self.return_bank())
            if self.name=='':
                self.show_name_error()
            elif self.age<18:
                self.show_age_error()
            elif self.salary==0:
                self.show_salary_error()
            elif self.__pw=='':
                self.show_pass_error()
            elif self.find(self.get_bank())==False or self.get_bank()=='':
                if self.get_bank()=='':
                    self.show_bank_error()
                else:
                    self.show_bank_error2()
    def find(self,string):
        for bank in self.bs:
            if bank==string:
                return True
        return False 
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

class Menu(gui.Home):
    def display_menu(self):
        r=0
        while r!=1 and r!=2:
            self.menu()
            r= int(self.return_choice())
        self.choice = r
        return self.choice
    def display_loan_menu(self):
        o=10
        while o!=2 and o!=1 and o!=3:
            self.loan_menu()
            o=int(self.return_choice())
        return o
class Options(gui.Choices):
    def display_options(self):
        o=10
        while o!=2 and o!=1:
            self.display()
            o=int(self.return_choice())
        return o
    def display_options2(self):#matsir kan ki yabda bch yda5l infos mch bch ya3ml new account
        o=10
        while o!=2 and o!=1 and o!=3 and o!=4:
            self.display2()
            o=int(self.return_choice2())
        return o
class system(gui.NewBank,gui.Choices):
    def __init__(self):
        self.banks=[Bank("attijari"),Bank("al zaytouna"),Bank("al islami")]
        self.menu=Menu()
        self.options=Options()
    def find(self,string):
        for bank in self.banks:
            if bank.Bname==string:
                return bank   
    def run(self):
        r=int(self.menu.display_menu())
        op=0
        if r==1:
            self.client=Sign_in()
            op=self.options.display_options()
            if op==1:
                if self.client.loan==0:
                    new_bank=''
                    test=False
                    while test==False:
                        self.diplay()
                        new_bank=self.return_bank()
                        for bank in self.banks:
                            if bank.Bname==new_bank:
                                test=True
                                break
                        if test==False:
                            messagebox.showerror("ERROR","The bank that you typed is not in our system pls enter an existing bank")
                    self.client.set_bank(new_bank)
                    r=self.find(self.client.get_bank())
                    r.Add_client(self.client)        
                    self.client.current_money=self.client.get_salary()
                    data_base.update_client_bank(self.client.id,self.client.get_bank())
                    messagebox.showinfo("DONE","YOU CHANGED THE BANK SUCCESSFULLY")
                else:
                    messagebox.showinfo("WARNING","YOU CAN CHOOSE ANOTHER BANK ONLY AFTER YOU PAY YOUR LOAN !!!")
            else:
                while True:
                    if self.client.loan!=0:
                        while True:
                            k=self.menu.display_loan_menu()
                            if k==1 :
                                messagebox.showinfo("LOAN AMOUNT",f"the remaining amount of loan is {self.client.loan}")
                            elif k==2:
                                messagebox.showinfo("REMAINING DURATION",f"The remaining payment periode is {self.client.duration} months ")
                            else:
                                break
                    op2=self.options.display_options2()
                    if op2==2:
                        messagebox.showinfo("CURRENT MONEY",f"YOUR CURRENT BALANCE IS {self.client.current_money}")
                    elif op2==3:
                        Q=self.client.current_money
                        self.showw_op3()
                        amount=int(self.return_withdraw_amount())
                        if amount>Q:
                            messagebox.showerror("ERROR",f"YOU DON'T HAVE ENOUGH MONEY !! YOUR ACCOUNT BALANCE IS {self.client.current_money}")
                        else:
                            messagebox.showinfo("THANK YOU","withdraw done successfully !!!")
                            self.client.current_money-=amount
                            data_base.update_client_current_money(self.client.id,self.client.current_money)
                    elif op2==1:
                        if self.client.loan != 0:
                            messagebox.showerror("ERROR","YOU ALREADY HAVE A LOAN THAT YOU NEED TO PAY !!")
                        else:
                            self.show_op1()
                            x=int(self.return_loan_amount())                           
                            self.client.loan+=x
                            data_base.update_client_loan(self.client.id,x)
                            self.client.set_salary(self.client.get_salary()*0.7)
                            data_base.update_client_salary(self.client.id,self.client.get_salary())
                            self.client.duration=(x//(self.client.get_salary()*0.3))+1
                            data_base.update_client_duration(self.client.id,self.client.duration)
                            info=f"""you took the loan successfully !!
from now on we are taking 30% from your salary to pay your debt                
        your current salary is {self.client.get_salary()}  
                     this will proceed for {self.client.duration} months"""
                            messagebox.showinfo("info",info)
                    else:
                        break
        else:
            self.client=BankAcc()
            self.client.current_money=self.client.salary 
            self.client.id=data_base.add_client_to_db(self.client.get_bank(),self.client.name,self.client.age,self.client.get_salary(),self.client.get_pw(),self.client.loan,self.client.duration,self.client.current_money)
            messagebox.showinfo("IMPORTANT",f"Your id is {self.client.id}. YOU MUST REMEMBER THAT SO YOU CAN ACCESS YOUR ACCOUNT !!")
data_base.show_clients()
s=system()
s.run()
data_base.show_clients()
#nzid fazet el transfere etda5l montant w el id mta3 elli t7eb ta3mellah transfere
#nzidou faza bl wa9t yabda kol chhar yna9es ml loan el flous elli y9osouhom 3lih w yna9s el duration bchhar w nzid fazet forgot password wla forgot id