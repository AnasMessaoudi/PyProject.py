from tkinter import *
from tkinter import messagebox
class Home():
    def menu(self):
        self.window=Tk()
        self.window.title("HOME")
        self.window.geometry("340x440")
        self.txt=Label(self.window,text="please enter your choice (1 or 2):")
        self.op1=Label(self.window,text="1. Enter personal informations ")
        self.op2=Label(self.window,text="2. Create an account")
        self.txt.grid(row=0,column=3)
        self.op1.grid(row=1,column=3)
        self.op2.grid(row=2,column=3)
        self.choice=Entry(self.window)
        self.choice.grid(row=3,column=3)
        submit_btn = Button(self.window, text="Submit", command=self.get_choice1)
        submit_btn.grid(row=4, column=3, columnspan=2)
        self.window.mainloop()
    def get_choice1(self):
        self.user_choice=self.choice.get()
        self.window.destroy()
    def return_choice(self):
        return self.user_choice 
    def loan_menu(self):
        self.window=Tk()
        self.window.title("LOAN MENU")
        self.window.geometry("340x440")
        self.op1=Label(self.window,text="1. Check the loan amount")
        self.op2=Label(self.window,text="2. Check the remaining payment periode ")
        self.op3=Label(self.window,text="3. Quit this menu")
        self.op1.grid(row=0,column=3)
        self.op2.grid(row=1,column=3)
        self.op3.grid(row=2,column=3)
        self.choice=Entry(self.window)
        self.choice.grid(row=3,column=3)
        submit_btn = Button(self.window, text="Submit", command=self.get_loan_menu_choice)
        submit_btn.grid(row=4, column=3, columnspan=2)
        self.window.mainloop()
    def get_loan_menu_choice(self):
        self.user_choice=self.choice.get()
        self.window.destroy()
    def return_choice(self):
        return self.user_choice 
class NewBank():
    def diplay(self):
        self.window=Tk()
        self.window.title("NEW BANK")
        self.window.geometry("340x440")
        self.user_new_bank=Label(self.window,text="enter the name of the new bank")
        self.user_new_bank.grid(row=1,column=1)
        self.user_new_bank_entry=Entry(self.window)
        self.user_new_bank_entry.grid(row=1,column=2)
        self.btn=Button(self.window,text="SUBMIT",command=self.confirm)
        self.btn.grid(row=3,column=2)
        self.window.mainloop()
    def confirm(self):
        self.b=self.user_new_bank_entry.get()
        self.window.destroy()
    def return_bank(self):
        return self.b
class loan():
    pass

class Choices():
    def display(self):
        self.window=Tk()
        self.window.title("BANK MENU")
        self.window.geometry("340x440")
        self.op1=Label(self.window,text="1. You are trying to choose another bank").grid(row=0,column=3)
        self.op2=Label(self.window,text="2. You are staying at your current bank ").grid(row=1,column=3)
        self.choice=Entry(self.window)
        self.choice.grid(row=2,column=3)
        submit_btn = Button(self.window, text="Submit", command=self.get_choice)
        submit_btn.grid(row=4, column=3, columnspan=2)
        self.window.mainloop()
    def get_choice(self):
        self.user_choice=self.choice.get()
        self.window.destroy() 
    def return_choice(self):
        return self.user_choice   
    def display2(self):
        self.window=Tk()
        self.window.title("OPTIONS")
        self.window.geometry("340x440")
        self.op1=Label(self.window,text="1. Take a Loan").grid(row=0,column=3)
        self.op2=Label(self.window,text="2. Check the amount of money in your account  ").grid(row=1,column=3)
        self.op3=Label(self.window,text="3. Withdraw an amount of money ").grid(row=2,column=3)
        self.op4=Label(self.window,text="4.Quit this menu ").grid(row=3,column=3)
        self.choice2=Entry(self.window)
        self.choice2.grid(row=4,column=3)
        submit_btn2 = Button(self.window, text="Submit", command=self.get_choice2)
        submit_btn2.grid(row=5, column=3, columnspan=2)
        self.window.mainloop()
        #ennajm na3ml el traitement hni fi 3oudh fi el bank.py w na3ml affichage selon el option
    def show_op1(self):
        self.window=Tk()
        self.window.title("OPTIONS")
        self.window.geometry("340x440")
        self.user_amount=Label(self.window,text="enter how much you would like to take as a loan").grid(row=1,column=1,columnspan=2)
        self.user_amount_entry=Entry(self.window)
        self.user_amount_entry.grid(row=1,column=3)
        self.op1btn=Button(self.window,text="SUBMIT",command=self.get_op1)
        self.op1btn.grid(row=3,column=2)
        self.window.mainloop()
    def get_op1(self):
        self.amount=self.user_amount_entry.get()
        self.window.destroy()
    def return_loan_amount(self):
        return self.amount
    def showw_op3(self):
        self.window=Tk()
        self.window.title("OPTIONS")
        self.window.geometry("340x440")
        self.user_wamount=Label(self.window,text="enter how much you would like to withdraw").grid(row=1,column=1,columnspan=2)
        self.user_wamount_entry=Entry(self.window)
        self.user_wamount_entry.grid(row=1,column=3)
        self.op3btn=Button(self.window,text="SUBMIT",command=self.get_op3)
        self.op3btn.grid(row=3,column=2)
        self.window.mainloop()
    def get_op3(self):
        self.wamount=self.user_wamount_entry.get()
        self.window.destroy()
    def return_withdraw_amount(self):
        return self.wamount
    def get_choice2(self):
        self.user_choice2=self.choice2.get()
        self.window.destroy()
    def return_choice2(self):
        return self.user_choice2
class Login():
    def display(self):
        self.window=Tk()
        self.window.title("log in")
        self.window.geometry("340x440")
        self.userid_label=Label(self.window,text="id")
        self.userid_label.grid(row=1,column=2)
        self.userpw_label=Label(self.window,text="password")
        self.userpw_label.grid(row=2,column=2)
        self.userpw_entry=Entry(self.window,show='*')
        self.userpw_entry.grid(row=2,column=3)
        self.userid_entry=Entry(self.window)
        self.userid_entry.grid(row=1,column=3)
        self.button=Button(self.window,text="log in",command=self.confirm)
        self.button.grid(row=3,column=3)
        self.window.mainloop()
    def confirm(self):
        self.user_id=self.userid_entry.get()
        self.user_pass=self.userpw_entry.get()
        self.window.destroy()
    def retun_id(self):
        return self.user_id
    def return_pass(self):
        return self.user_pass
    def show_id_error(self):
        messagebox.showerror("Error", "id not found")
    def show_pass_error(self):
        messagebox.showerror("Error", "non empty string required")
    def show_pass_error2(self):
        messagebox.showerror("Error", "wrong password")
class Signup():
    def display(self):
        self.window=Tk()
        self.window.title("SIGN UP")
        self.window.geometry("340x440")
        self.username=Label(self.window,text="enter your name:")
        self.username.grid(row=1,column=2)
        self.username_entry=Entry(self.window)
        self.username_entry.grid(row=1,column=3)
        self.userage_label=Label(self.window,text="enter age(MUST BE OVER 18!!):")
        self.userage_label.grid(row=2,column=2)
        self.userage_entry=Entry(self.window)
        self.userage_entry.grid(row=2,column=3)
        self.user_salary=Label(self.window,text="enter your salary:")
        self.user_salary.grid(row=3,column=2)
        self.user_salary_entry=Entry(self.window)
        self.user_salary_entry.grid(row=3,column=3)
        self.user_pass=Label(self.window,text="choose a password:")
        self.user_pass.grid(row=4,column=2)
        self.user_pass_entry=Entry(self.window)
        self.user_pass_entry.grid(row=4,column=3)
        self.user_bank=Label(self.window,text="choose a bank:")
        self.user_bank.grid(row=5,column=2)
        self.user_bank_entry=Entry(self.window)
        self.user_bank_entry.grid(row=5,column=3)
        self.button=Button(self.window,text="SIGN UP",command=self.confirm).grid(row=7,column=3)
        self.window.mainloop()
    def confirm(self):
        self.name=self.username_entry.get()
        self.salary=self.user_salary_entry.get()
        self.bank=self.user_bank_entry.get()
        self.age=self.userage_entry.get()
        self.pw=self.user_pass_entry.get()
        self.window.destroy()
    def return_name(self):
        return self.name
    def return_age(self):
        return self.age
    def return_salary(self):
        return self.salary
    def return_pass(self):
        return self.pw
    def return_bank(self):
        return self.bank
    def show_name_error(self):
        messagebox.showerror("Error", "YOU NEED TO ENTER YOUR NAME")
    def show_age_error(self):
        messagebox.showerror("Error", "YOU MUST BE OVER 18")
    def show_salary_error(self):
        messagebox.showerror("Error", "SALARY MUST BE OVER 0$")
    def show_pass_error(self):
        messagebox.showerror("Error", "non empty string required")
    def show_bank_error(self):
        messagebox.showerror("Error","YOU SHOULD ENTER A BANK NAME")
    def show_bank_error2(self):
        messagebox.showerror("Error","YOU SHOULD ENTER A VALID BANK NAME")
        messagebox.showinfo("BANKS INFO","THESE ARE THA VALID BANKS :ATTIJARI, AL ZAYTOUNA, AL ISLAMI")
l=Login()
#el login na9sah el quit button el login ki nenzel 3laha lazmha t5arjni 