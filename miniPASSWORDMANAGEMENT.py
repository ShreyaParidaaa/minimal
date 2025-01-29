#!/usr/bin/env python
# coding: utf-8

# # Simple Password Manager

# Features:
# ✅ Store passwords for different accounts
# ✅ Retrieve stored passwords
# ✅ Encrypt passwords using base64
# ✅ Save data in a JSON file

# In[ ]:


import json
import base64
import os

PASSWORD_FILE = "passwords.json"

def load_passwords():
    """Load passwords from the JSON file."""
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    return {}

def save_passwords(passwords):
    """Save passwords to the JSON file."""
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file, indent=4)

def encrypt_password(password):
    """Encrypt password using base64 encoding."""
    return base64.b64encode(password.encode()).decode()

def decrypt_password(encrypted_password):
    """Decrypt password using base64 decoding."""
    return base64.b64decode(encrypted_password.encode()).decode()

def add_password(account, password):
    """Add a new password to the storage."""
    passwords = load_passwords()
    passwords[account] = encrypt_password(password)
    save_passwords(passwords)
    print(f"Password saved for {account}!")

def get_password(account):
    """Retrieve and decrypt the password for an account."""
    passwords = load_passwords()
    if account in passwords:
        print(f"Password for {account}: {decrypt_password(passwords[account])}")
    else:
        print("Account not found!")

def main():
    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            account = input("Enter account name: ")
            password = input("Enter password: ")
            add_password(account, password)
        elif choice == "2":
            account = input("Enter account name: ")
            get_password(account)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()

