# password_manager.py
import random
import string
import json
from cryptography.fernet import Fernet
import os

def generate_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def save_password(service, password, key, filename="passwords.json"):
    f = Fernet(key)
    if os.path.exists(filename):
        with open(filename, 'r') as f_file:
            data = json.load(f_file)
    else:
        data = {}
    data[service] = f.encrypt(password.encode()).decode()
    with open(filename, 'w') as f_file:
        json.dump(data, f_file)
    print(f"Password for {service} saved.")

def load_password(service, key, filename="passwords.json"):
    f = Fernet(key)
    if not os.path.exists(filename):
        print("Password file does not exist.")
        return None
    with open(filename, 'r') as f_file:
        data = json.load(f_file)
    encrypted_pwd = data.get(service)
    if encrypted_pwd:
        return f.decrypt(encrypted_pwd.encode()).decode()
    else:
        return None

if __name__ == "__main__":
    choice = input("Do you want to (1) Generate and save a password or (2) Retrieve a password? Enter 1 or 2: ")
    if choice == '1':
        key = Fernet.generate_key()
        service = input("Enter the service name: ")
        pwd = generate_password()
        save_password(service, pwd, key)
        print(f"Generated password for {service}: {pwd}")
    elif choice == '2':
        key = input("Enter your encryption key: ").encode()
        service = input("Enter the service name: ")
        pwd = load_password(service, key)
        if pwd:
            print(f"Password for {service}: {pwd}")
        else:
            print("Service not found.")
    else:
        print("Invalid choice.")
