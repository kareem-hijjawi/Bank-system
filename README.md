# Bank-system
### Screenshot
![Alt Text](https://raw.githubusercontent.com/kareem-hijjawi/portfoliomedia/main/bankaccount.gif)

This is a simple bank account management system built using Python and Tkinter. The system allows users to register, log in, deposit money, withdraw money, check their balance, and apply for loans based on their marital status and salary.

## Features

- **Account Registration**: Create a new bank account by providing your first name, last name, password, and marital status.
- **User Login**: Log in using your account ID and password.
- **Deposit**: Add money to your account.
- **Withdraw**: Withdraw money from your account, ensuring you have sufficient funds.
- **Check Balance**: View the current balance in your account.
- **Apply for Loan**: Apply for a loan based on your marital status, balance, and salary.

## File Structure

- `projectpy.py`: The main Python script containing all the functionality of the bank account management system.
- `accounts.txt`: A text file that stores user account information in the format `account_id|first_name|last_name|password|balance|marital_status`.

## How to Run

1. **Install Python**: Make sure you have Python installed on your machine. You can download it from [here](https://www.python.org/downloads/).

2. **Install Tkinter**: Tkinter comes pre-installed with Python, but if not, you can install it using the following command:
    ```bash
    pip install tk
    ```

3. **Clone the Repository**:
    ```bash
    git clone <repository_url>
    ```

4. **Run the Application**:
    Navigate to the directory where `projectpy.py` is located and run the script:
    ```bash
    python projectpy.py
    ```

5. **Interact with the Application**:
    - Upon launching, you will be greeted with a start screen where you can either register a new account or log in to an existing one.
    - After logging in, you can deposit money, withdraw money, check your balance, or apply for a loan.

## Loan Criteria

- **Single**: Must have a salary of at least $5,000 and a balance of at least $10,000.
- **Married**: Must have a salary of at least $15,000 and a balance of at least $20,000.

## Notes

- The account data is stored in `accounts.txt` in the root directory. Make sure this file is in the same directory as `projectpy.py` when running the application.
- The system currently supports basic operations. Future enhancements can include more complex financial services and a more secure way of storing passwords.

