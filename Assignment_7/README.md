# 🏦 Class 07 Assignment – April 27

Hi there! 👋🏻  
This is my submission for **Assignment 7** of the **GIAIC Q3** course.  
In this task, I applied **Object-Oriented Programming (OOP)** principles to create a fully functional **ATM CLI (Command Line Interface) Application** in Python. 🐍✨

## 🎯 Assignment Goal

- Build a **unique Python application** that utilizes **OOP concepts**.
- Create classes, objects, methods, and properly structure the codebase.
- Apply real-world scenarios into coding practice.

## 🛠️ Project Overview: ATM CLI Application

This project simulates an **Automated Teller Machine (ATM)** experience through the command line.  
Users can create accounts, login, deposit and withdraw money, check their balances, and even remove their accounts, all securely through PIN authentication.

## 🧩 Features & Functionalities

- **🏦 Create New Bank Account:**  
  Collects detailed user and account information with validation.
  
- **🔐 Secure Login System:**  
  Secure PIN input handling with hidden input characters (`*` masking).

- **💰 Check Account Balance:**  
  Instantly view the current balance with currency info.

- **➕ Deposit Money:**  
  Add funds to the account and update the balance in real-time.

- **➖ Withdraw Money:**  
  Withdraw funds while ensuring sufficient balance is available.

- **🗑️ Remove an Account:**  
  Securely delete an account after confirmation.

- **🚪 Logout:**  
  Safely exit the current session and return to the login screen.

## 🧱 Project Structure

The program is organized into **three main classes**:

| Class   | Responsibilities |
|---------|-------------------|
| **Bank** | Manages creation, storage, and removal of user accounts. |
| **ATM** | Handles login, user authentication, and menu-driven operations. |
| **Account** | Provides deposit, withdraw, and balance checking functionalities for an account. |

## 📋 ATM Main Menu

Upon logging in, users can access:

```
ATM Menu:
1. Check Balance
2. Deposit
3. Withdraw
4. Remove Account
5. Logout
```

## 🔒 Important Notes
 * **PIN Handling:**  
Users must create and input a 4-digit PIN securely (no PIN shown on screen).

 * **Error Handling:**  
Input validations are added for numbers, PIN creation, deposits, withdrawals, etc.

 * **Account Information:**  
Detailed personal information is gathered during account creation for a realistic banking simulation.

## 📱 My Socials
Let's connect and grow together in this learning journey! 🌐✨

🐦 Twitter (X): [@iamabdulrehman5](https://x.com/iamabdulrehman5)

💼 LinkedIn: [Abdul Rehman Jiwani](https://pk.linkedin.com/in/abdul-rehman-jiwani)

## 📚 Course Details

- **Course**: GIAIC (Governor Sindh Initiative of Artificial Intelligence and Computing)  
- **Instructor**: [Sir Asharib Ali](https://github.com/AsharibAli)

## 🛠️ How to Run the Code

You can run this assignment code locally by following the steps below:

### **Clone the Repo:**
```bash
git clone https://github.com/ProgrammerABDUL/GIAIC-Q3-Class-Assignments/tree/main/Assignment_7
```

### Run the Code:
Open a terminal and execute:

```bash
py main.py
```

Make sure you are running this on Windows because the code uses the msvcrt module for secure PIN entry.

Thanks for checking out my project! 🌹

Stay tuned for more amazing Python applications! 🚀

Happy Coding! ✨  

Thanks for Reading 😘