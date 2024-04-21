'''This is a program that provides a GUI for an online bank management system'''
import random
import mysql.connector as m
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
import tkinter.ttk as ttk
mydb = m.connect(host="localhost", user="root", password="Manu9321", database="bank")
c = mydb.cursor()

def master():
    root = tk.Tk()
    style = Style()
    style.configure('W.TButton', font=('calibri', 10))
    root.geometry('500x500')
    root.title("Bank Management System")
    root.iconbitmap(r'C:\Users\shash\OneDrive\Desktop\School projects\bankicon.ico')
    welcome = tk.Label(root, text='Welcome To Bank Management System')
    welcome.place(relx=0.5,rely=0.2,anchor='center')

    def login():
        root.destroy()
        next_win = tk.Tk()
        next_win.geometry('500x500')
        next_win.title("Bank Management System")
        next_win.iconbitmap(r'C:\Users\shash\OneDrive\Desktop\School projects\bankicon.ico')
        entercid = tk.Label(next_win, text='Enter customer ID: ')
        entercid.place(relx=0.5,rely=0.1,anchor='e')
        cid = tk.Entry(next_win)
        cid.place(relx=0.5,rely=0.1,anchor='w')
        cid.focus_force()
        enterpwd = tk.Label(next_win, text='Enter password: ')
        enterpwd.place(relx=0.5, rely=0.2, anchor='e')
        pwd = tk.Entry(next_win, show='*')
        pwd.place(relx=0.5, rely=0.2, anchor='w')
        def correct():
            if len(cid.get()) == 0:
                messagebox.showerror('Error','Customer ID field cannot be left empty')
            elif len(pwd.get())==0:
                messagebox.showerror('Error', 'Password not entered')
            else:
                c.execute("SELECT Customer_ID FROM customer")
                x = c.fetchall()
                st1 = "SELECT Password FROM Customer WHERE Customer_ID = %s"
                c.execute(st1, (cid.get(),))
                p = c.fetchall()
                if (cid.get(),) not in (x):
                    messagebox.showerror('Error','Customer not found')
                elif (cid.get(),) in (x) and (pwd.get(),) not in (p):
                    messagebox.showerror('Error', 'Incorrect Password')
                elif (cid.get(),) in (x) and (pwd.get(),) in (p):
                    cid1=cid.get()
                    next_win.destroy()

                    def main_page():
                        mainpage = tk.Tk()
                        mainpage.geometry('500x500')
                        mainpage.title("Bank Management System")
                        mainpage.iconbitmap(r'C:\Users\shash\OneDrive\Desktop\School projects\bankicon.ico')
                        def logoutsure(win):
                            t = messagebox.askyesno('', 'Are you sure you want to logout?')
                            if t:
                                win.destroy()
                                master()
                            else:
                                pass

                        def transactions():
                            mainpage.destroy()
                            next_win1 = tk.Tk()
                            next_win1.geometry('500x500')
                            next_win1.title("Bank Management System")
                            next_win1.iconbitmap(r'C:\Users\shash\OneDrive\Desktop\School projects\bankicon.ico')

                            def deposit():
                                next_win1.destroy()
                                next_win2 = tk.Tk()
                                next_win2.geometry('500x500')
                                next_win2.title("Bank Management System")
                                next_win2.iconbitmap(r'C:\Users\shash\OneDrive\Desktop\School projects\bankicon.ico')

                                def donedepositing():
                                    stat0 = "SELECT Account_ID FROM Account_master WHERE Customer_ID = %s"
                                    c.execute(stat0, (cid1,))
                                    idi = c.fetchall()
                                    status = "SELECT ACTIVE FROM Account_master WHERE Account_ID = %s"
                                    c.execute(status, (accid.get(),))
                                    yesorno = c.fetchall()
                                    if len(accid.get()) != 0:
                                        if len(amt.get()) != 0:
                                            if (accid.get(),) in (idi) and yesorno[0][0] == "YES":
                                                if amt.get().isdigit() and int(amt.get()) <= 1000000:
                                                    if int(amt.get())>0:
                                                        stat6 = "SELECT Account_Type FROM Account_master WHERE Account_ID = %s"
                                                        c.execute(stat6, (accid.get(),))
                                                        account_type = c.fetchall()
                                                        st = "SELECT Opening_balace FROM Account_master WHERE Account_ID = %s"
                                                        value1 = (accid.get(),)
                                                        c.execute(st, value1)
                                                        x = c.fetchall()
                                                        from datetime import date as date
                                                        today = date.today()
                                                        date = today.strftime("%Y-%m-%d")
                                                        new_balance = x[0][0] + int(amt.get())
                                                        # updating
                                                        st1 = "UPDATE Account_master SET Opening_balace = %s  WHERE Account_ID = %s"
                                                        value = (new_balance, accid.get())
                                                        c.execute(st1, value)
                                                        mydb.commit()
                                                        # for transaction record
                                                        transaction_st = "INSERT INTO Account_transaction (Customer_ID, Account_ID, Account_Type, Transaction_date, Amount_Deposited, Balance) VALUES (%s,%s,%s,%s,%s,%s)"
                                                        transaction_values = (
                                                        cid1, accid.get(), account_type[0][0], date, int(amt.get()),
                                                        new_balance)
                                                        c.execute(transaction_st, transaction_values)
                                                        mydb.commit()
                                                        message = 'Rs.' + amt.get() + ' deposited successfully to account ID: ' + accid.get() + ' (' + \
                                                                  account_type[0][0] + ')'
                                                        messagebox.showinfo('Deposit successful', message)
                                                        deposit_2['state'] = 'disabled'
                                                        logout = Button(next_win2, text='Logout', style='W.TButton',command=lambda:[logoutsure(next_win2)])
                                                        logout.place(relx=0.5, rely=0.4, anchor='center')
                                                    else:
                                                        messagebox.showerror('Error','Incorrect deposit amount. Deposit amount must be more than Rs.0')
                                                else:
                                                    messagebox.showerror('Error',
                                                                         'Incorrect Deposit amount. Deposit amount must be in whole numbers. Maximum amount for deposit at one time is Rs.1000000')
                                            else:
                                                messagebox.showerror('Error', 'Invalid Account ID')
                                        else:
                                            messagebox.showerror('Error', 'Please enter deposit amount')
                                    else:
                                        messagebox.showerror('Error', 'Please enter account ID')

                                accid_l = tk.Label(next_win2, text="Enter account ID:")
                                accid_l.place(relx=0.5, rely=0.1, anchor='e')
                                accid = tk.Entry(next_win2)
                                accid.place(relx=0.5, rely=0.1, anchor='w')
                                accid.focus_force()
                                amt_l = tk.Label(next_win2, text="Enter amount to be deposited:")
                                amt_l.place(relx=0.5, rely=0.15, anchor='e')
                                amt = tk.Entry(next_win2)
                                amt.place(relx=0.5, rely=0.15, anchor='w')
                                deposit_2 = Button(next_win2, text='Deposit', style='W.TButton', command=donedepositing)
                                deposit_2.place(relx=0.5, rely=0.2, anchor='center')
                                back = Button(next_win2, text='back', style='W.TButton',command=lambda: [next_win2.destroy(), main_page()])
                                back.place(relx=0.5, rely=0.3, anchor='center')
                            def withdraw():
                                next_win1.destroy()
                                next_win3 = tk.Tk()
                                next_win3.geometry('500x500')
                                next_win3.title("Bank Management System")
                                next_win3.iconbitmap(r'C:\Users\shash\OneDrive\Desktop\School projects\bankicon.ico')

                                def donewithdrawing():
                                    stat1 = "SELECT Account_ID FROM Account_master WHERE Customer_ID = %s"
                                    c.execute(stat1, (cid1,))
                                    idi1 = c.fetchall()
                                    status = "SELECT ACTIVE FROM Account_master WHERE Account_ID = %s"
                                    c.execute(status, (accid.get(),))
                                    yesorno = c.fetchall()
                                    if len(accid.get()) != 0:
                                        if len(amt.get()) != 0:
                                            if (accid.get(),) in (idi1) and yesorno[0][0] == "YES":
                                                if amt.get().isdigit() and int(amt.get()) <= 100000:
                                                    if int(amt.get())>0:
                                                        stat3 = "SELECT Opening_balace FROM Account_master WHERE Account_ID = %s"
                                                        c.execute(stat3, (accid.get(),))
                                                        opening_bal = c.fetchall()
                                                        stat4 = "SELECT Account_Type FROM Account_master WHERE Account_ID = %s"
                                                        c.execute(stat4, (accid.get(),))
                                                        account_type = c.fetchall()
                                                        from datetime import date as date
                                                        today = date.today()
                                                        date = today.strftime("%Y-%m-%d")
                                                        if account_type[0][0] == "savings":
                                                            if (opening_bal[0][0] - int(amt.get())) >= 500:
                                                                new_bal = opening_bal[0][0] - int(amt.get())
                                                                stat5 = "UPDATE Account_master SET Opening_balace = %s  WHERE Account_ID = %s"
                                                                values5 = (new_bal, accid.get())
                                                                c.execute(stat5, values5)
                                                                mydb.commit()
                                                                transaction_st = "INSERT INTO Account_transaction (Customer_ID, Account_ID, Account_Type, Transaction_date, Amount_Withdrawn, Balance) VALUES (%s,%s,%s,%s,%s,%s)"
                                                                transaction_values = (cid1, accid.get(), account_type[0][0], date, int(amt.get()), new_bal)
                                                                c.execute(transaction_st, transaction_values)
                                                                mydb.commit()
                                                                message = 'Rs.' + amt.get() + ' withdrawn successfully from account ID: ' + accid.get() + ' (' + account_type[0][0] + ')'
                                                                messagebox.showinfo('Withdrawal successful', message)
                                                                withdraw_2['state'] = 'disabled'
                                                                logout = Button(next_win3, text='Logout', style='W.TButton',command=lambda:[logoutsure(next_win3)])
                                                                logout.place(relx=0.5, rely=0.4, anchor='center')

                                                            else:
                                                                msg = 'Insufficient balance for withdrawal from savings account. Minimum Balance must be Rs.500. Your balance is: '+str(opening_bal[0][0])
                                                                messagebox.showerror('Error',msg)

                                                        elif account_type[0][0] == "current":
                                                            if (opening_bal[0][0] - int(amt.get())) >= 1000:
                                                                new_bal = opening_bal[0][0] - int(amt.get())
                                                                stat5 = "UPDATE Account_master SET Opening_balace = %s  WHERE Account_ID = %s"
                                                                values5 = (new_bal, accid.get())
                                                                c.execute(stat5, values5)
                                                                mydb.commit()
                                                                transaction_st = "INSERT INTO Account_transaction (Customer_ID, Account_ID, Account_Type, Transaction_date, Amount_Withdrawn, Balance) VALUES (%s,%s,%s,%s,%s,%s)"
                                                                transaction_values = (cid1, accid.get(), account_type[0][0], date, int(amt.get()),new_bal)
                                                                c.execute(transaction_st, transaction_values)
                                                                mydb.commit()
                                                                message = 'Rs.' + amt.get() + ' withdrawn successfully from account ID: ' + accid.get() + ' (' + account_type[0][0] + ')'
                                                                messagebox.showinfo('Withdrawal successful', message)
                                                                withdraw_2['state'] = 'disabled'
                                                                logout = Button(next_win3, text='Logout', style='W.TButton',command=lambda:[logoutsure(next_win3)])
                                                                logout.place(relx=0.5, rely=0.4, anchor='center')
                                                            else:
                                                                msg = 'Insufficient balance for withdrawal from current account. Minimum Balance must be Rs.1000. Your balance is: ' + str(opening_bal[0][0])
                                                                messagebox.showerror('Error', msg)
                                                    else:
                                                        messagebox.showerror('Error','Incorrect withdrawal amount. Amount must be more than Rs.0')
                                                else:
                                                    messagebox.showerror('Error','Incorrect withdrawal amount. Withdraw amount must be in whole numbers. Maximum amount for withdrawal at one time is Rs.100000')
                                            else:
                                                messagebox.showerror('Error', 'Invalid Account ID')
                                        else:
                                            messagebox.showerror('Error', 'Please enter deposit amount')
                                    else:
                                        messagebox.showerror('Error', 'Please enter account ID')

                                accid_l = tk.Label(next_win3, text="Enter account ID:")
                                accid_l.place(relx=0.5, rely=0.1, anchor='e')
                                accid = tk.Entry(next_win3)
                                accid.place(relx=0.5, rely=0.1, anchor='w')
                                accid.focus_force()
                                amt_l = tk.Label(next_win3, text="Enter amount for withdrawal:")
                                amt_l.place(relx=0.5, rely=0.15, anchor='e')
                                amt = tk.Entry(next_win3)
                                amt.place(relx=0.5, rely=0.15, anchor='w')
                                withdraw_2 = Button(next_win3, text='Withdraw', style='W.TButton',command=donewithdrawing)
                                withdraw_2.place(relx=0.5, rely=0.2, anchor='center')
                                back = Button(next_win3, text='back', style='W.TButton',command=lambda: [next_win3.destroy(), main_page()])
                                back.place(relx=0.5, rely=0.3, anchor='center')

                            def transfer():
                                next_win1.destroy()
                                next_win4 = tk.Tk()
                                next_win4.geometry('500x500')
                                next_win4.title("Bank Management System")
                                next_win4.iconbitmap(r'C:\Users\shash\OneDrive\Desktop\School projects\bankicon.ico')

                                def donetransfer():
                                    your_acc = "SELECT Account_ID FROM Account_master WHERE Customer_ID = %s"
                                    c.execute(your_acc, (cid1,))
                                    allaccountID = c.fetchall()
                                    status = "SELECT ACTIVE FROM Account_master WHERE Account_ID = %s"
                                    c.execute(status, (accid.get(),))
                                    yesorno = c.fetchall()
                                    if len(accid.get())!=0:
                                        if len(otheracc_id.get())!=0:
                                            if len(amt.get())!=0:
                                                if (accid.get(),) in allaccountID and yesorno[0][0] == "YES":
                                                    other_acc = "SELECT Account_ID FROM Account_master WHERE Account_ID = %s"
                                                    c.execute(other_acc, (otheracc_id.get(),))
                                                    allotheraccountID = c.fetchall()
                                                    status = "SELECT ACTIVE FROM Account_master WHERE Account_ID = %s"
                                                    c.execute(status, (otheracc_id.get(),))
                                                    yesorno = c.fetchall()
                                                    if (otheracc_id.get(),) in allotheraccountID and yesorno[0][0] == "YES":
                                                        at = "SELECT Account_Type FROM Account_master WHERE Account_ID = %s"
                                                        c.execute(at, (accid.get(),))
                                                        account_type = c.fetchall()
                                                        if account_type[0][0] == 'savings':
                                                            ourob = "SELECT Opening_balace FROM Account_master WHERE Account_ID = %s"
                                                            c.execute(ourob, (accid.get(),))
                                                            opening_balance = c.fetchall()
                                                            if amt.get().isdigit():
                                                                if int(amt.get()) <= 25000 and int(amt.get()) > 0 and (opening_balance[0][0] - int(amt.get())) >= 500:
                                                                    theirat = "SELECT Account_Type FROM Account_master WHERE Account_ID = %s"
                                                                    c.execute(theirat, (otheracc_id.get(),))
                                                                    account_type1 = c.fetchall()
                                                                    from datetime import date as date
                                                                    today = date.today()
                                                                    date = today.strftime("%Y-%m-%d")
                                                                    #for acc master of user acc
                                                                    your_account_new_balance = opening_balance[0][0] - int(amt.get())
                                                                    update_bal = "UPDATE Account_master SET Opening_balace = %s  WHERE Account_ID = %s"
                                                                    values10 = (your_account_new_balance, accid.get())
                                                                    c.execute(update_bal, values10)
                                                                    mydb.commit()
                                                                    # for transaction record of user acc
                                                                    transaction_st = "INSERT INTO Account_transaction (Customer_ID, Account_ID, Account_Type, Transaction_date, Amount_Withdrawn, Balance) VALUES (%s,%s,%s,%s,%s,%s)"
                                                                    transaction_val = (cid1, accid.get(), account_type[0][0], date, int(amt.get()),your_account_new_balance)
                                                                    c.execute(transaction_st, transaction_val)
                                                                    mydb.commit()
                                                                    #for acc master of other acc
                                                                    ob = "SELECT Opening_balace FROM Account_master WHERE Account_ID = %s"
                                                                    c.execute(ob, (otheracc_id.get(),))
                                                                    otheracc_ob = c.fetchall()
                                                                    other_acc_new_balance = otheracc_ob[0][0] + int(amt.get())
                                                                    update_bal1 = "UPDATE Account_master SET Opening_balace = %s  WHERE Account_ID = %s"
                                                                    values11 = (other_acc_new_balance, otheracc_id.get())
                                                                    c.execute(update_bal1, values11)
                                                                    mydb.commit()
                                                                    #for transaction record of other acc
                                                                    other_cid = "SELECT Customer_ID FROM Account_master WHERE Account_ID = %s"
                                                                    otheraccountval = (otheracc_id.get(),)
                                                                    c.execute(other_cid, otheraccountval)
                                                                    othercustomer_ID = c.fetchall()
                                                                    transaction_st = "INSERT INTO Account_transaction (Customer_ID, Account_ID, Account_Type, Transaction_date, Amount_Deposited, Balance) VALUES (%s,%s,%s,%s,%s,%s)"
                                                                    transaction_val = (othercustomer_ID[0][0], otheracc_id.get(), account_type1[0][0], date,int(amt.get()), other_acc_new_balance)
                                                                    c.execute(transaction_st, transaction_val)
                                                                    mydb.commit()
                                                                    transfer1['state'] = 'disabled'
                                                                    msg = 'Rs.' + amt.get() + ' is successfully transferred from ' + accid.get() + ' (' + str(account_type[0][0]) + ')' + ' to ' + otheracc_id.get() + ' (' + str(account_type1[0][0]) + ')'
                                                                    messagebox.showinfo('Funds Transferred successfully',msg)
                                                                    logout = Button(next_win4, text='Logout',style='W.TButton', command=lambda:[logoutsure(next_win4)])
                                                                    logout.place(relx=0.5, rely=0.4, anchor='center')
                                                                else:
                                                                    m = 'Invalid amount. Amount must be more than zero. Maximum transfer amount is Rs.25000. Balance in account must be more than Rs.500 for savings account. Your balance is Rs.'+ str(opening_balance[0][0])
                                                                    messagebox.showerror('Error',m)
                                                            else:
                                                                messagebox.showerror('Error','Amount must be in whole numbers.')
                                                        elif account_type[0][0] == 'current':
                                                            ourob = "SELECT Opening_balace FROM Account_master WHERE Account_ID = %s"
                                                            c.execute(ourob, (accid.get(),))
                                                            opening_balance = c.fetchall()
                                                            if amt.get().isdigit():
                                                                if int(amt.get()) <= 25000 and int(amt.get())>0 and (opening_balance[0][0] - int(amt.get())) >= 1000:
                                                                    theirat = "SELECT Account_Type FROM Account_master WHERE Account_ID = %s"
                                                                    c.execute(theirat, (otheracc_id.get(),))
                                                                    account_type1 = c.fetchall()
                                                                    from datetime import date as date
                                                                    today = date.today()
                                                                    date = today.strftime("%Y-%m-%d")
                                                                    # for acc master of user acc
                                                                    your_account_new_balance = opening_balance[0][0] - int(amt.get())
                                                                    update_bal = "UPDATE Account_master SET Opening_balace = %s  WHERE Account_ID = %s"
                                                                    values10 = (your_account_new_balance, accid.get())
                                                                    c.execute(update_bal, values10)
                                                                    mydb.commit()
                                                                    # for transaction record of user acc
                                                                    transaction_st = "INSERT INTO Account_transaction (Customer_ID, Account_ID, Account_Type, Transaction_date, Amount_Withdrawn, Balance) VALUES (%s,%s,%s,%s,%s,%s)"
                                                                    transaction_val = (cid1, accid.get(), account_type[0][0], date, int(amt.get()),your_account_new_balance)
                                                                    c.execute(transaction_st, transaction_val)
                                                                    mydb.commit()
                                                                    # for acc master of other acc
                                                                    ob = "SELECT Opening_balace FROM Account_master WHERE Account_ID = %s"
                                                                    c.execute(ob, (otheracc_id.get(),))
                                                                    otheracc_ob = c.fetchall()
                                                                    other_acc_new_balance = otheracc_ob[0][0] + int(amt.get())
                                                                    update_bal1 = "UPDATE Account_master SET Opening_balace = %s  WHERE Account_ID = %s"
                                                                    values11 = (other_acc_new_balance, otheracc_id.get())
                                                                    c.execute(update_bal1, values11)
                                                                    mydb.commit()
                                                                    # for transaction record of other acc
                                                                    other_cid = "SELECT Customer_ID FROM Account_master WHERE Account_ID = %s"
                                                                    otheraccountval = (otheracc_id.get(),)
                                                                    c.execute(other_cid, otheraccountval)
                                                                    othercustomer_ID = c.fetchall()
                                                                    transaction_st = "INSERT INTO Account_transaction (Customer_ID, Account_ID, Account_Type, Transaction_date, Amount_Deposited, Balance) VALUES (%s,%s,%s,%s,%s,%s)"
                                                                    transaction_val = (othercustomer_ID[0][0], otheracc_id.get(), account_type1[0][0], date,int(amt.get()), other_acc_new_balance)
                                                                    c.execute(transaction_st, transaction_val)
                                                                    mydb.commit()
                                                                    transfer1['state']='disabled'
                                                                    msg = 'Rs.'+amt.get()+' is successfully transferred from '+accid.get()+' ('+str(account_type[0][0])+')'+' to '+otheracc_id.get()+' ('+str(account_type1[0][0])+')'
                                                                    messagebox.showinfo('Funds Transferred successfully',msg)
                                                                    logout = Button(next_win4, text='Logout',style='W.TButton', command=lambda:[logoutsure(next_win4)])
                                                                    logout.place(relx=0.5, rely=0.4, anchor='center')
                                                                else:
                                                                    m = 'Invalid amount. Amount must be more than zero. Maximum transfer amount is Rs.25000. Balance in account must be more than Rs.1000 for current account. Your balance is Rs.' + str(opening_balance[0][0])
                                                                    messagebox.showerror('Error', m)
                                                            else:
                                                                messagebox.showerror('Error','Amount must be in whole numbers.')
                                                    else:
                                                        messagebox.showerror('Wrong Account ID', 'Account ID to which funds are to be transferred is invalid')
                                                else:
                                                    messagebox.showerror('Wrong Account ID','Your account ID is invalid')
                                            else:
                                                messagebox.showerror('Error','Please fill the amount to be transferred.')
                                        else:
                                            messagebox.showerror('Error','Please fill the account ID to which funds are to be transferred.')
                                    else:
                                        messagebox.showerror('Error','Please fill your account ID.')

                                accid_l = tk.Label(next_win4, text="Enter account ID:")
                                accid_l.place(relx=0.6, rely=0.1, anchor='e')
                                accid = tk.Entry(next_win4)
                                accid.place(relx=0.6, rely=0.1, anchor='w')
                                accid.focus_force()
                                otheracc_id_l = tk.Label(next_win4, text = "Enter account ID to which money must be transferred:")
                                otheracc_id_l.place(relx=0.6, rely=0.167, anchor='e')
                                otheracc_id = tk.Entry(next_win4)
                                otheracc_id.place(relx=0.6, rely=0.17, anchor='w')
                                amt_l = tk.Label(next_win4, text="Enter amount for transfer:")
                                amt_l.place(relx=0.6, rely=0.25, anchor='e')
                                amt = tk.Entry(next_win4)
                                amt.place(relx=0.6, rely=0.25, anchor='w')
                                transfer1 = Button(next_win4, text='Transfer', style='W.TButton',command=donetransfer)
                                transfer1.place(relx=0.5, rely=0.3, anchor='center')
                                back = Button(next_win4, text='back', style='W.TButton',command=lambda: [next_win4.destroy(), main_page()])
                                back.place(relx=0.5, rely=0.35, anchor='center')
                            heading = tk.Label(next_win1, text='Transactions')
                            heading.place(relx=0.5, rely=0.2, anchor='center')
                            deposit = Button(next_win1, text='Deposit', style='W.TButton', command=deposit)
                            deposit.place(relx=0.4, rely=0.4, anchor='e')
                            withdraw_b = Button(next_win1, text='Withdraw', style='W.TButton',command=withdraw)
                            withdraw_b.place(relx=0.6, rely=0.4, anchor='w')
                            transfer = Button(next_win1, text='Transfer funds', style='W.TButton', command=transfer)
                            transfer.place(relx=0.5, rely=0.4, anchor='center')
                            back = Button(next_win1, text='back', style='W.TButton',command=lambda: [next_win1.destroy(), main_page()])
                            back.place(relx=0.5, rely=0.5, anchor='center')
                        def account_summary():
                            mainpage.destroy()
                            next_win5 = tk.Tk()
                            next_win5.title("Bank Management System")
                            next_win5.iconbitmap(r'C:\Users\shash\OneDrive\Desktop\School projects\bankicon.ico')
                            st1 = "SELECT Customer_name FROM Customer WHERE Customer_ID = %s"
                            value = (cid1,)
                            c.execute(st1, value)
                            name = c.fetchall()
                            # for fetching everything else
                            st2 = "SELECT * FROM Account_master WHERE Customer_ID = %s"
                            value1 = (cid1,)
                            c.execute(st2, value1)
                            result = c.fetchall()
                            columns = ('Cust Id','AcID','AccType','CreatedDate','Closdate','Bal','ACT')
                            tree = ttk.Treeview(columns=columns,height=len(result))
                            tree.column('#0', width=150, anchor='center')
                            tree.heading('#0', text='Name')
                            tree.column(columns[0],width=90,anchor='center')
                            tree.heading(columns[0], text = 'Customer ID')
                            tree.column(columns[1],width=90,anchor='center')
                            tree.heading(columns[1], text='Account ID')
                            tree.column(columns[2], width=90, anchor='center')
                            tree.heading(columns[2], text='Account Type')
                            tree.column(columns[3], width=150, anchor='center')
                            tree.heading(columns[3], text='Account Creation Date')
                            tree.column(columns[4], width=150, anchor='center')
                            tree.heading(columns[4], text='Account Closure Date')
                            tree.column(columns[5], width=90, anchor='center')
                            tree.heading(columns[5], text='Balance')
                            tree.column(columns[6], width=90, anchor='center')
                            tree.heading(columns[6], text='ACTIVE')
                            tree.pack()
                            for i in range(len(result)):
                                tree.insert('', tk.END, text=name[0][0],values=result[i][:])
                            back = Button(next_win5, text= 'back', style='W.TButton',command=lambda:[next_win5.destroy(),main_page()])
                            back.pack()
                            logout = Button(next_win5, text= 'Logout', style='W.TButton',command=lambda:[logoutsure(next_win5)])
                            logout.pack()

                        def close():
                            mainpage.destroy()
                            next_win8 = tk.Tk()
                            next_win8.title("Bank Management System")
                            next_win8.geometry('500x500')
                            next_win8.iconbitmap(r'C:\Users\shash\OneDrive\Desktop\School projects\bankicon.ico')
                            def check():
                                if len(accid.get())!=0:
                                    clos_acc = "SELECT Account_ID FROM Account_master WHERE Customer_ID = %s"
                                    c.execute(clos_acc, (cid1,))
                                    closing_acc = c.fetchall()
                                    alreadyclose = "SELECT ACTIVE FROM Account_master WHERE Account_ID = %s"
                                    c.execute(alreadyclose, (accid.get(),))
                                    closeornot = c.fetchall()
                                    if (accid.get(),) in closing_acc:
                                        if closeornot[0][0] == "YES":
                                            v = messagebox.askyesno('Account Closure','Are you sure you want to close account?')
                                            if v:
                                                leftamntaccm = "SELECT Opening_balace FROM Account_master WHERE Account_ID = %s"
                                                c.execute(leftamntaccm, (accid.get(),))
                                                left_amount = c.fetchall()
                                                msg = 'Amount withdrawn as a result of closing account is Rs.'+str(left_amount[0][0])
                                                messagebox.showinfo('Withdrawn Funds',msg)
                                                # updating accountmaster table
                                                closingaccountinam = "UPDATE Account_master SET Opening_balace = %s,Account_closed_date = %s,ACTIVE = %s WHERE Account_ID = %s"
                                                upvalue = (0, date, "NO", accid.get())
                                                c.execute(closingaccountinam, upvalue)
                                                mydb.commit()

                                                # for transaction record
                                                at = "SELECT Account_Type FROM Account_master WHERE Account_ID = %s"
                                                c.execute(at, (accid.get(),))
                                                account_type = c.fetchall()
                                                transaction_st = "INSERT INTO Account_transaction (Customer_ID, Account_ID, Account_Type, Transaction_date, Amount_Withdrawn, Balance) VALUES (%s,%s,%s,%s,%s,%s)"
                                                transaction_val = (cid1, accid.get(), account_type[0][0], date, left_amount[0][0], 0)
                                                c.execute(transaction_st, transaction_val)
                                                mydb.commit()
                                                msg1 = 'Account with Account ID '+accid.get()+' is successfully closed.'
                                                messagebox.showinfo('Confirmation of Closure',msg1)
                                                st = "SELECT * FROM Account_master WHERE Customer_ID=%s AND ACTIVE=%s"
                                                val = (cid1,'YES')
                                                c.execute(st,val)
                                                yesorno = c.fetchall()
                                                next_win8.destroy()
                                                if len(yesorno)==0:
                                                    master()
                                                else:
                                                    main_page()
                                        else:
                                            messagebox.showerror('Error','Account is already closed!')
                                    else:
                                        messagebox.showerror('Error', 'Account does not exist')
                                else:
                                    messagebox.showerror('Error','Please fill Account ID')

                            from datetime import date as date
                            today = date.today()
                            date = today.strftime("%Y-%m-%d")
                            accid_l = tk.Label(next_win8, text="Enter account ID:")
                            accid_l.place(relx=0.5, rely=0.1, anchor='e')
                            accid = tk.Entry(next_win8)
                            accid.place(relx=0.5, rely=0.1, anchor='w')
                            accid.focus_force()
                            clos = Button(next_win8,text='Close Account',command=check)
                            clos.place(relx=0.5,rely=0.2,anchor='center')
                            back = Button(next_win8,text='back',command=lambda: [next_win8.destroy(),main_page()])
                            back.place(relx=0.5,rely=0.35,anchor='center')
                            logout = Button(next_win8,text='Logout',command=lambda:[logoutsure(next_win8)])
                            logout.place(relx=0.5,rely=0.4,anchor='center')
                        def account_statement():
                            import datetime
                            format1 = "%Y-%m-%d"
                            def checkdate(d1,d2,win):
                                t=True
                                if len(accid.get())!=0:
                                    if len(startdate.get())!=0:
                                        if len(enddate.get())!=0:
                                            try:
                                                datetime.datetime.strptime(d1, format1)
                                            except ValueError:
                                                messagebox.showerror('Error','Invalid start date format. Correct format is YYYY-MM-DD.')
                                                t = False
                                            if t!=False:
                                                try:
                                                    datetime.datetime.strptime(d2, format1)
                                                except ValueError:
                                                    messagebox.showerror('Error','Invalid end date format. Correct format is YYYY-MM-DD.')
                                                    t = False
                                                if t!=False:
                                                    accstat = "SELECT * FROM Account_transaction WHERE Transaction_date >= %s AND Transaction_date <= %s AND Account_ID = %s"
                                                    value = (startdate.get(), enddate.get(), accid.get())
                                                    c.execute(accstat, value)
                                                    result = c.fetchall()
                                                    accidst = "SELECT Account_ID from account_master WHERE Customer_ID=%s"
                                                    c.execute(accidst,(cid1,))
                                                    result1 = c.fetchall()
                                                    if (accid.get(),) in result1:
                                                        if len(result) == 0:
                                                            messagebox.showinfo('No transaction history','No transactions made between the entered dates')
                                                        else:
                                                            win.destroy()
                                                            next_win7 = tk.Tk()
                                                            next_win7.title("Bank Management System")
                                                            next_win7.iconbitmap(r'C:\Users\shash\OneDrive\Desktop\School projects\bankicon.ico')
                                                            columns = ('AcID', 'AccType', 'TransactDate', 'Deposit', 'Withdraw','Bal')
                                                            tree = ttk.Treeview(columns=columns, height=len(result))
                                                            tree.column('#0', width=90,anchor='center')
                                                            tree.heading('#0',text='Customer ID')
                                                            tree.column(columns[0], width=90, anchor='center')
                                                            tree.heading(columns[0], text='Account ID')
                                                            tree.column(columns[1], width=90, anchor='center')
                                                            tree.heading(columns[1], text='Account Type')
                                                            tree.column(columns[2], width=100, anchor='center')
                                                            tree.heading(columns[2], text='Transaction Date')
                                                            tree.column(columns[3], width=100, anchor='center')
                                                            tree.heading(columns[3], text='Deposit amount')
                                                            tree.column(columns[4], width=110, anchor='center')
                                                            tree.heading(columns[4], text='Withdraw Amount')
                                                            tree.column(columns[5], width=90, anchor='center')
                                                            tree.heading(columns[5], text='Balance')
                                                            tree.pack()
                                                            for i in range(len(result)):
                                                                tree.insert('', tk.END, text=result[0][0], values=result[i][1:])
                                                            back = Button(next_win7, text='back', style='W.TButton',command=lambda: [next_win7.destroy(), main_page()])
                                                            back.pack()
                                                            logout = Button(next_win7, text='Logout', style='W.TButton',command=lambda: [logoutsure(next_win7)])
                                                            logout.pack()
                                                    else:
                                                        messagebox.showerror('Error', 'Account ID does not exist')
                                        else:
                                            messagebox.showerror('Error','Please fill in end date')
                                    else:
                                        messagebox.showerror('Error','Please fill in start date')
                                else:
                                    messagebox.showerror('Error', 'Please fill in account ID')

                            mainpage.destroy()
                            next_win6 = tk.Tk()
                            next_win6.title("Bank Management System")
                            next_win6.geometry('500x500')
                            next_win6.iconbitmap(r'C:\Users\shash\OneDrive\Desktop\School projects\bankicon.ico')
                            accid_l = tk.Label(next_win6, text="Enter account ID:")
                            accid_l.place(relx=0.5, rely=0.1, anchor='e')
                            accid = tk.Entry(next_win6)
                            accid.place(relx=0.5, rely=0.1, anchor='w')
                            accid.focus_force()
                            startdate_l = tk.Label(next_win6, text='Enter start date(YYYY-MM-DD):')
                            startdate = tk.Entry(next_win6)
                            enddate = tk.Entry(next_win6)
                            enddate_l = tk.Label(next_win6, text='Enter end date(YYYY-MM-DD):')
                            submit = Button(next_win6, text='Submit', style='W.TButton',command=lambda:[checkdate(startdate.get(),enddate.get(),next_win6)])
                            startdate.place(relx=0.5,rely=0.15, anchor='w')
                            startdate_l.place(relx=0.5,rely=0.15,anchor='e')
                            enddate.place(relx=0.5, rely=0.2, anchor='w')
                            enddate_l.place(relx=0.5, rely=0.2, anchor='e')
                            submit.place(relx=0.5,rely=0.3,anchor='center')
                            back = Button(next_win6, text='back', command=lambda:[next_win6.destroy(),main_page()])
                            back.place(relx=0.5, rely=0.45, anchor='center')
                            logout = Button(next_win6, text='Logout', command=lambda: [logoutsure(next_win6)])
                            logout.place(relx=0.5, rely=0.5, anchor='center')

                        s = "SELECT Customer_name FROM Customer WHERE Customer_ID=%s"
                        v = (cid1,)
                        c.execute(s,v)
                        r=c.fetchall()
                        m = 'Welcome '+str(r[0][0])+'!'
                        l = tk.Label(mainpage,text=m)
                        l.place(relx=0.5,rely=0.1,anchor='center')
                        acc_st = Button(mainpage, text='Account Statement', style='W.TButton', command=account_statement)
                        acc_st.place(relx=0.4, rely=0.2, anchor='e')
                        acc_sm = Button(mainpage, text='Account Summary', style='W.TButton', command=account_summary)
                        acc_sm.place(relx=0.6, rely=0.2, anchor='w')
                        trans = Button(mainpage, text='Transactions', style='W.TButton', command=transactions)
                        trans.place(relx=0.4, rely=0.3, anchor='e')
                        close = Button(mainpage, text='Close Account', style='W.TButton',command=close)
                        close.place(relx=0.6, rely=0.3, anchor='w')
                        logout = Button(mainpage, text='Logout', style='W.TButton', command=lambda:[logoutsure(mainpage)])
                        logout.place(relx=0.5, rely=0.4, anchor='center')
                    main_page()
                else:
                    messagebox.showerror('Error', 'Customer not found')

        forpwd = Button(next_win, text='Login',style = 'W.TButton', command=correct)
        forpwd.place(relx=0.5, rely=0.3, anchor='center')
        next_win.mainloop()
    def create():
        root.destroy()
        next_win = tk.Tk()
        next_win.geometry('500x500')
        next_win.title("Bank Management System")
        next_win.iconbitmap(r'C:\Users\shash\OneDrive\Desktop\School projects\bankicon.ico')
        oldornew = tk.Label(next_win, text="Are you an existing customer?")
        oldornew.place(relx=0.5,rely=0.05,anchor='center')
        def no():
            yes['state'] = 'disabled'
            no['state'] = 'disabled'
            from datetime import date as date
            today = date.today()
            date = today.strftime("%Y-%m-%d")
            choice = tk.Label(next_win,text='Choose your type of account:')
            choice.place(relx=0.5,rely=0.15,anchor='center')
            def savings_n():
                savings_b['state']='disabled'
                current_b['state']='disabled'
                def afterinfo_s():
                    if len(bal.get()) != 0:
                        if bal.get().isdigit() and int(bal.get()) >= 500:
                            condition = len(add.get()) != 0 and len(name.get()) != 0 and len(pwd.get()) != 0 and len(cont.get()) != 0
                            if condition:
                                if cont.get().isdigit() and len(str(cont.get())) == 10:
                                    # creating Customer id
                                    c.execute("SELECT Customer_ID FROM Customer")
                                    x = c.fetchall()
                                    r = random.randint(100000, 999999)
                                    while (r,) in x:
                                        r = random.randint(100000, 999999)
                                    st2 = "INSERT INTO Customer (Customer_ID, Branch_ID, Customer_name, Customer_Address, Contact_number, Password) VALUES (%s,%s,%s,%s,%s,%s)"
                                    values = (r, '0001', name.get(), add.get(), cont.get(), pwd.get())
                                    c.execute(st2, values)
                                    mydb.commit()

                                    # creating acc id
                                    c.execute("SELECT Account_ID FROM Account_master")
                                    y = c.fetchall()
                                    accid = random.randint(1000, 9999)
                                    while (accid,) in y:
                                        accid = random.randint(1000, 9999)
                                    st1 = "INSERT INTO Account_master (Customer_ID, Account_ID, Account_Type, Account_creation_date, Opening_balace, ACTIVE) VALUES(%s,%s,%s,%s,%s,%s)"
                                    values1 = (r, accid, 'savings', date, bal.get(), 'YES')
                                    c.execute(st1, values1)
                                    mydb.commit()
                                    transaction_st = "INSERT INTO Account_transaction (Customer_ID, Account_ID, Account_Type, Transaction_date, Amount_Deposited, Balance) VALUES (%s,%s,%s,%s,%s,%s)"
                                    transaction_values = (r, accid, 'savings', date, int(bal.get()), bal.get())
                                    c.execute(transaction_st, transaction_values)
                                    mydb.commit()
                                    accreated = "Your savings Account has been successfully created"
                                    newcid = "Your new customer ID for log in purposes is: " + str(r)
                                    newaccid = "Your new Account ID (savings account): " + str(accid)
                                    messagebox.showinfo('New Credentials', accreated+str('\n')+newcid+str('\n')+newaccid)
                                    enter['state']='disabled'
                                    close = Button(next_win, text='Home',style = 'W.TButton', command=lambda:[next_win.destroy(),master()])
                                    close.place(relx=0.5,rely=0.6,anchor='center')
                                    bal['state'] = 'disabled'
                                    name['state'] = 'disabled'
                                    add['state'] = 'disabled'
                                    pwd['state'] = 'disabled'
                                    cont['state'] = 'disabled'
                                else:
                                    messagebox.showerror('Error', 'Contact number must be 10 digits')
                            else:
                                messagebox.showerror('Error', 'Please fill your personal details')
                        else:
                            messagebox.showerror('Error', 'Incorrect balance amount. Balance must be in whole numbers (More than 500).')
                    else:
                        messagebox.showerror('Error', 'Enter Initial deposit.')


                bal_l = tk.Label(next_win, text="Enter initial deposit:")
                bal_l.place(relx=0.4,rely=0.3,anchor='e')
                bal = tk.Entry(next_win)
                bal.place(relx=0.4,rely=0.3,anchor='w')
                bal.focus_force()
                name_l = tk.Label(next_win, text="Enter name in full:")
                name_l.place(relx=0.4,rely=0.35,anchor='e')
                name = tk.Entry(next_win)
                name.place(relx=0.4,rely=0.35,anchor='w')
                add_l = tk.Label(next_win, text="Enter residential address:")
                add_l.place(relx=0.4,rely=0.4,anchor='e')
                add = tk.Entry(next_win)
                add.place(relx=0.4,rely=0.4,anchor='w')
                pwd_l = tk.Label(next_win, text="Enter a secure password:")
                pwd_l.place(relx=0.4,rely=0.45,anchor='e')
                pwd = tk.Entry(next_win,show='*')
                pwd.place(relx=0.4,rely=0.45,anchor='w')
                cont_l = tk.Label(next_win, text="Enter contact number:")
                cont_l.place(relx=0.4,rely=0.5,anchor='e')
                cont = tk.Entry(next_win)
                cont.place(relx=0.4,rely=0.5,anchor='w')
                enter = Button(next_win, text='Create',style = 'W.TButton', command=afterinfo_s)
                enter.place(relx=0.5,rely=0.55,anchor='center')
            def current_n():
                savings_b['state'] = 'disabled'
                current_b['state'] = 'disabled'
                def afterinfo_c():
                    if len(bal.get()) != 0:
                        if bal.get().isdigit() and int(bal.get()) >= 500:
                            condition = len(add.get()) != 0 and len(name.get()) != 0 and len(pwd.get()) != 0 and len(cont.get()) != 0
                            if condition:
                                if cont.get().isdigit() and len(str(cont.get())) == 10:
                                    # creating Customer id
                                    c.execute("SELECT Customer_ID FROM Customer")
                                    x = c.fetchall()
                                    r = random.randint(100000, 999999)
                                    while (r,) in x:
                                        r = random.randint(100000, 999999)
                                    st2 = "INSERT INTO Customer (Customer_ID, Branch_ID, Customer_name, Customer_Address, Contact_number, Password) VALUES (%s,%s,%s,%s,%s,%s)"
                                    values = (r, '0001', name.get(), add.get(), cont.get(), pwd.get())
                                    c.execute(st2, values)
                                    mydb.commit()

                                    # creating acc id
                                    c.execute("SELECT Account_ID FROM Account_master")
                                    y = c.fetchall()
                                    accid = random.randint(1000, 9999)
                                    while (accid,) in y:
                                        accid = random.randint(1000, 9999)
                                    st1 = "INSERT INTO Account_master (Customer_ID, Account_ID, Account_Type, Account_creation_date, Opening_balace, ACTIVE) VALUES(%s,%s,%s,%s,%s,%s)"
                                    values1 = (r, accid, 'current', date, bal.get(), 'YES')
                                    c.execute(st1, values1)
                                    mydb.commit()
                                    transaction_st = "INSERT INTO Account_transaction (Customer_ID, Account_ID, Account_Type, Transaction_date, Amount_Deposited, Balance) VALUES (%s,%s,%s,%s,%s,%s)"
                                    transaction_values = (r, accid, 'current', date, int(bal.get()), bal.get())
                                    c.execute(transaction_st, transaction_values)
                                    mydb.commit()
                                    accreated = "Your current Account has been successfully Created"
                                    newcid = "Your new customer ID for log in purposes is:" + str(r)
                                    newaccid = "Your new Account ID (current account):" + str(accid)
                                    messagebox.showinfo('New Credentials', accreated+str('\n') +newcid + str('\n') + newaccid)
                                    enter['state']='disabled'
                                    close = Button(next_win, text='Home', style='W.TButton',command=lambda: [next_win.destroy(), master()])
                                    close.place(relx=0.5, rely=0.6, anchor='center')
                                    bal['state'] = 'disabled'
                                    name['state'] = 'disabled'
                                    add['state'] = 'disabled'
                                    pwd['state'] = 'disabled'
                                    cont['state'] = 'disabled'
                                else:
                                    messagebox.showerror('Error', 'Contact number must be 10 digits')
                            else:
                                messagebox.showerror('Error', 'Please fill your personal details')
                        else:
                            messagebox.showerror('Error', 'Incorrect balance amount. Balance must be in whole numbers (more than 1000).')
                    else:
                        messagebox.showerror('Error', 'Enter Initial deposit.')
                bal_l = tk.Label(next_win, text="Enter initial deposit:")
                bal_l.place(relx=0.4, rely=0.3, anchor='e')
                bal = tk.Entry(next_win)
                bal.place(relx=0.4, rely=0.3, anchor='w')
                bal.focus_force()
                name_l = tk.Label(next_win, text="Enter name in full:")
                name_l.place(relx=0.4, rely=0.35, anchor='e')
                name = tk.Entry(next_win)
                name.place(relx=0.4, rely=0.35, anchor='w')
                add_l = tk.Label(next_win, text="Enter residential address:")
                add_l.place(relx=0.4, rely=0.4, anchor='e')
                add = tk.Entry(next_win)
                add.place(relx=0.4, rely=0.4, anchor='w')
                pwd_l = tk.Label(next_win, text="Enter a secure password:")
                pwd_l.place(relx=0.4, rely=0.45, anchor='e')
                pwd = tk.Entry(next_win, show='*')
                pwd.place(relx=0.4, rely=0.45, anchor='w')
                cont_l = tk.Label(next_win, text="Enter contact number:")
                cont_l.place(relx=0.4, rely=0.5, anchor='e')
                cont = tk.Entry(next_win)
                cont.place(relx=0.4, rely=0.5, anchor='w')
                enter = Button(next_win, text='Create',style = 'W.TButton', command=afterinfo_c)
                enter.place(relx=0.4, rely=0.55, anchor='w')

            savings_b = Button(next_win, text='Create savings Account',style = 'W.TButton', command=savings_n)
            savings_b.place(relx=0.2,rely=0.2,anchor='center')
            current_b = Button(next_win, text='Create current Account',style = 'W.TButton', command=current_n)
            current_b.place(relx=0.8,rely=0.2,anchor='center')
            saveinfo = tk.Label(next_win, text='Min balance for savings is Rs.500.')
            saveinfo.place(relx=0.2,rely=0.25,anchor='center')
            currentinfo = tk.Label(next_win, text='Min balance for current is Rs.1000.')
            currentinfo.place(relx=0.8,rely=0.25,anchor='center')

        def yes():
            yes['state'] = 'disabled'
            no['state'] = 'disabled'
            def info():
                cid['state']='disabled'
                pwd['state']='disabled'
                def savings():
                    savings_b['state'] = 'disabled'
                    current_b['state'] = 'disabled'
                    def valid_s():
                        if len(bal.get())!=0:
                            if bal.get().isdigit() and int(bal.get()) >= 500:
                                bal_b['state']='disabled'
                                c.execute("SELECT Account_ID FROM Account_master")
                                y = c.fetchall()
                                accid = random.randint(1000, 9999)
                                while (accid,) in y:
                                    accid = random.randint(1000, 9999)
                                st1 = "INSERT INTO Account_master (Customer_ID, Account_ID, Account_Type, Account_creation_date, Opening_balace, ACTIVE) VALUES(%s,%s,%s,%s,%s,%s)"
                                values1 = (cid.get(), accid, 'savings', date, bal.get(), 'YES')
                                c.execute(st1, values1)
                                mydb.commit()
                                transaction_st = "INSERT INTO Account_transaction (Customer_ID, Account_ID, Account_Type, Transaction_date, Amount_Deposited, Balance) VALUES (%s,%s,%s,%s,%s,%s)"
                                transaction_values = (cid.get(), accid, 'savings', date, int(bal.get()), bal.get())
                                c.execute(transaction_st, transaction_values)
                                mydb.commit()
                                text = "Your new account ID (savings account) is " + str(accid)
                                messagebox.showinfo('New Credentials', text)
                                close = Button(next_win, text='Home',style = 'W.TButton', command=lambda:[next_win.destroy(),master()])
                                close.place(relx=0.5,rely=0.6,anchor='center')
                                bal['state'] = 'disabled'
                            else:
                                messagebox.showerror('Error', 'Incorrect amount. Balance for savings account must be Rs.500 or more.')
                        else:
                            messagebox.showerror('Error', 'Enter initial deposit.')

                    bal_l = tk.Label(next_win, text="Enter initial deposit amount:")
                    bal_l.place(relx=0.5,rely=0.5,anchor='e')
                    bal = tk.Entry(next_win)
                    bal.place(relx=0.5,rely=0.5,anchor='w')
                    bal.focus_force()
                    bal_b = Button(next_win, text='Deposit',style = 'W.TButton', command=valid_s)
                    bal_b.place(relx=0.5,rely=0.55,anchor='center')


                def current():
                    savings_b['state'] = 'disabled'
                    current_b['state'] = 'disabled'
                    def valid_c():
                        if len(bal.get()) != 0:
                            if bal.get().isdigit() and int(bal.get()) >= 1000:
                                bal_b['state'] = 'disabled'
                                c.execute("SELECT Account_ID FROM Account_master")
                                y = c.fetchall()
                                accid = random.randint(1000, 9999)
                                while (accid,) in y:
                                    accid = random.randint(1000, 9999)
                                st1 = "INSERT INTO Account_master (Customer_ID, Account_ID, Account_Type, Account_creation_date, Opening_balace, ACTIVE) VALUES(%s,%s,%s,%s,%s,%s)"
                                values1 = (cid.get(), accid, 'current', date, bal.get(), 'YES')
                                c.execute(st1, values1)
                                mydb.commit()
                                transaction_st = "INSERT INTO Account_transaction (Customer_ID, Account_ID, Account_Type, Transaction_date, Amount_Deposited, Balance) VALUES (%s,%s,%s,%s,%s,%s)"
                                transaction_values = (cid.get(), accid, 'current', date, int(bal.get()), bal.get())
                                c.execute(transaction_st, transaction_values)
                                mydb.commit()
                                text = "Your new account ID (current account) is " + str(accid)
                                messagebox.showinfo('New Credentials', text)
                                close = Button(next_win, text='Home', style='W.TButton',command=lambda: [next_win.destroy(), master()])
                                close.place(relx=0.5, rely=0.6, anchor='center')
                                bal['state'] = 'disabled'
                            else:
                                messagebox.showerror('Error', 'Incorrect amount. Balance for current account must be Rs.1000 or more.')
                        else:
                            messagebox.showerror('Error', 'Enter initial deposit')


                    bal_l = tk.Label(next_win, text="Enter initial deposit amount:")
                    bal_l.place(relx=0.5, rely=0.5, anchor='e')
                    bal = tk.Entry(next_win)
                    bal.place(relx=0.5, rely=0.5, anchor='w')
                    bal.focus_force()
                    bal_b = Button(next_win, text='Deposit',style = 'W.TButton', command =valid_c)
                    bal_b.place(relx=0.5, rely=0.55, anchor='center')

                if len(cid.get()) == 0:
                    messagebox.showerror('Error','Customer ID field cannot be left empty')
                elif len(pwd.get()) == 0:
                    messagebox.showerror('Error', 'Password not entered')
                else:
                    c.execute("SELECT Customer_ID FROM Customer")
                    x = c.fetchall()
                    st1 = "SELECT Password FROM Customer WHERE Customer_ID = %s"
                    c.execute(st1, (cid.get(),))
                    p = c.fetchall()
                    if (cid.get(),) not in (x):
                        messagebox.showerror('Error', 'Customer not found')
                    elif (cid.get(),) in (x) and (pwd.get(),) not in (p):
                        messagebox.showerror('Error', 'Incorrect password')
                    elif (cid.get(),) in (x) and (pwd.get(),) in (p):
                        cid_b['state'] = 'disabled'
                        from datetime import date as date
                        today = date.today()
                        date = today.strftime("%Y-%m-%d")
                        savings_b = Button(next_win, text='Create savings Account',style = 'W.TButton',command = savings)
                        savings_b.place(relx=0.2,rely=0.35,anchor='center')
                        current_b = Button(next_win, text='Create current Account',style = 'W.TButton', command = current)
                        current_b.place(relx=0.8,rely=0.35,anchor='center')
                        saveinfo = tk.Label(next_win, text='Min balance for savings is Rs.500.')
                        saveinfo.place(relx=0.2, rely=0.4, anchor='center')
                        currentinfo = tk.Label(next_win, text='Min balance for current is Rs.1000.')
                        currentinfo.place(relx=0.8, rely=0.4, anchor='center')
                    else:
                        messagebox.showerror('Error', 'Customer not found')

            cid = tk.Entry(next_win)
            cid.place(relx=0.4,rely=0.2,anchor='w')
            cid.focus_force()
            cid_l = tk.Label(next_win,text="Enter customer ID:")
            cid_l.place(relx=0.4,rely=0.2,anchor='e')
            pwd_l = tk.Label(next_win,text="Enter password:")
            pwd_l.place(relx=0.4,rely=0.25,anchor='e')
            pwd = tk.Entry(next_win,show='*')
            pwd.place(relx=0.4,rely=0.25,anchor='w')
            cid_b = Button(next_win, text='Proceed',style = 'W.TButton',command = info)
            cid_b.place(relx=0.5,rely=0.3,anchor='center')
        yes = Button(next_win, text='Yes',style = 'W.TButton',command = yes)
        yes.place(relx=0.4,rely=0.1,anchor='center')
        no = Button(next_win, text='No',style = 'W.TButton',command=no)
        no.place(relx=0.6,rely=0.1,anchor='center')


    login_b = Button(root, text='Login',style = 'W.TButton', command=login,width=14)
    login_b.place(relx=0.4,rely=0.5,anchor='e')
    create_b = Button(root, text='Create Account',style = 'W.TButton', command=create,width=14)
    create_b.place(relx=0.6,rely=0.5,anchor='w')


    root.mainloop()

master()