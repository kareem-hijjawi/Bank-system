import tkinter as tk
from tkinter import messagebox, simpledialog
import os

ACCOUNT_FILE = 'accounts.txt'

if not os.path.exists(ACCOUNT_FILE):
    with open(ACCOUNT_FILE, 'w') as file:
        pass

def load_accounts():
    accounts = {}
    with open(ACCOUNT_FILE, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split('|')
            if len(parts) == 6:
                acc_id, first_name, last_name, password, balance, marital_status = parts
                accounts[acc_id] = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'password': password,
                    'balance': float(balance),
                    'marital_status': marital_status
                }
    return accounts

def save_accounts(accounts):
    with open(ACCOUNT_FILE, 'w') as file:
        for acc_id, info in accounts.items():
            file.write(f"{acc_id}|{info['first_name']}|{info['last_name']}|{info['password']}|{info['balance']}|{info['marital_status']}\n")

def create_account(first_name, last_name, password, marital_status):
    accounts = load_accounts()
    new_id = str(len(accounts) + 1)
    accounts[new_id] = {
        'first_name': first_name,
        'last_name': last_name,
        'password': password,
        'balance': 0.0,
        'marital_status': marital_status
    }
    save_accounts(accounts)
    return new_id

def validate_login(acc_id, password):
    accounts = load_accounts()
    if acc_id in accounts and accounts[acc_id]['password'] == password:
        return True
    return False

def deposit(acc_id, amount):
    accounts = load_accounts()
    if acc_id in accounts:
        accounts[acc_id]['balance'] += amount
        save_accounts(accounts)
        return True
    return False

def withdraw(acc_id, amount):
    accounts = load_accounts()
    if acc_id in accounts and accounts[acc_id]['balance'] >= amount:
        accounts[acc_id]['balance'] -= amount
        save_accounts(accounts)
        return True
    return False

def check_balance(acc_id):
    accounts = load_accounts()
    if acc_id in accounts:
        return accounts[acc_id]['balance']
    return None

def apply_for_loan(acc_id, salary):
    accounts = load_accounts()
    if acc_id in accounts:
        balance = accounts[acc_id]['balance']
        marital_status = accounts[acc_id]['marital_status']
        if marital_status == "Single" and salary >= 5000 and balance >= 10000:
            return True
        elif marital_status == "Married" and salary >= 15000 and balance >= 20000:
            return True
    return False

def main_menu(acc_id):
    accounts = load_accounts()
    user_info = accounts.get(acc_id, {})
    
    def deposit_gui():
        def submit():
            amount = float(entry_amount.get())
            if deposit(acc_id, amount):
                messagebox.showinfo("Success", "Deposit successful.")
                window_deposit.destroy()
            else:
                messagebox.showerror("Error", "Invalid account ID.")
        
        window_deposit = tk.Toplevel(root)
        window_deposit.title("Deposit")
        
        tk.Label(window_deposit, text="Amount:").pack()
        entry_amount = tk.Entry(window_deposit)
        entry_amount.pack()
        
        tk.Button(window_deposit, text="Submit", command=submit).pack()

    def withdraw_gui():
        def submit():
            amount = float(entry_amount.get())
            if withdraw(acc_id, amount):
                messagebox.showinfo("Success", "Withdrawal successful.")
                window_withdraw.destroy()
            else:
                messagebox.showerror("Error", "Invalid account ID or insufficient funds.")
        
        window_withdraw = tk.Toplevel(root)
        window_withdraw.title("Withdraw")
        
        tk.Label(window_withdraw, text="Amount:").pack()
        entry_amount = tk.Entry(window_withdraw)
        entry_amount.pack()
        
        tk.Button(window_withdraw, text="Submit", command=submit).pack()

    def check_balance_gui():
        balance = check_balance(acc_id)
        if balance is not None:
            messagebox.showinfo("Balance", f"Your balance is ${balance:.2f}.")
        else:
            messagebox.showerror("Error", "Invalid account ID.")
    
    def apply_for_loan_gui():
        def submit():
            salary = float(entry_salary.get())
            if apply_for_loan(acc_id, salary):
                messagebox.showinfo("Success", "Loan application approved.")
            else:
                messagebox.showerror("Error", "Loan application denied.")
            window_loan.destroy()
        
        window_loan = tk.Toplevel(root)
        window_loan.title("Apply for Loan")
        
        tk.Label(window_loan, text="Salary:").pack()
        entry_salary = tk.Entry(window_loan)
        entry_salary.pack()
        
        tk.Button(window_loan, text="Submit", command=submit).pack()

    def sign_out():
        start_screen()

    for widget in root.winfo_children():
        widget.destroy()

    # Display the user's first and last name at the top
    tk.Label(root, text=f"Welcome, {user_info['first_name']} {user_info['last_name']}", font=("Helvetica", 16)).pack(pady=20)
    
    tk.Button(root, text="Deposit", command=deposit_gui, width=20, height=2).pack(pady=10)
    tk.Button(root, text="Withdraw", command=withdraw_gui, width=20, height=2).pack(pady=10)
    tk.Button(root, text="Check Balance", command=check_balance_gui, width=20, height=2).pack(pady=10)
    tk.Button(root, text="Apply for Loan", command=apply_for_loan_gui, width=20, height=2).pack(pady=10)
    
    # Add a "Sign Out" button at the bottom
    tk.Button(root, text="Sign Out", command=sign_out, width=20, height=2, fg="red").pack(pady=20)

def register():
    def submit():
        first_name = entry_first_name.get()
        last_name = entry_last_name.get()
        password = entry_password.get()
        marital_status = var_marital_status.get()
        if first_name and last_name and password and marital_status:
            acc_id = create_account(first_name, last_name, password, marital_status)
            messagebox.showinfo("Success", f"Account created! Your ID is {acc_id}.")
            window_register.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
    
    window_register = tk.Toplevel(root)
    window_register.title("Register")
    
    tk.Label(window_register, text="First Name:").pack()
    entry_first_name = tk.Entry(window_register)
    entry_first_name.pack()
    
    tk.Label(window_register, text="Last Name:").pack()
    entry_last_name = tk.Entry(window_register)
    entry_last_name.pack()
    
    tk.Label(window_register, text="Password:").pack()
    entry_password = tk.Entry(window_register, show='*')
    entry_password.pack()
    
    tk.Label(window_register, text="Marital Status:").pack()
    var_marital_status = tk.StringVar(value="Single")
    tk.Radiobutton(window_register, text="Single", variable=var_marital_status, value="Single").pack()
    tk.Radiobutton(window_register, text="Married", variable=var_marital_status, value="Married").pack()
    
    tk.Button(window_register, text="Submit", command=submit).pack()

def login():
    def submit():
        acc_id = entry_id.get()
        password = entry_password.get()
        if validate_login(acc_id, password):
            messagebox.showinfo("Success", "Login successful.")
            window_login.destroy()
            main_menu(acc_id)
        else:
            messagebox.showerror("Error", "Invalid ID or password.")
    
    window_login = tk.Toplevel(root)
    window_login.title("Login")
    
    tk.Label(window_login, text="Account ID:").pack()
    entry_id = tk.Entry(window_login)
    entry_id.pack()
    
    tk.Label(window_login, text="Password:").pack()
    entry_password = tk.Entry(window_login, show='*')
    entry_password.pack()
    
    tk.Button(window_login, text="Submit", command=submit).pack()

def start_screen():
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Button(root, text="Register", command=register, width=20, height=2).pack(pady=10)
    tk.Button(root, text="Sign In", command=login, width=20, height=2).pack(pady=10)

root = tk.Tk()
root.title("Bank Account System")
root.geometry("450x600")

start_screen()

root.mainloop()