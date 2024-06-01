# hash_generator.py
import bcrypt

def generate_hash(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

if __name__ == "__main__":
    pwd = input("Enter password to hash: ")
    hashed_pwd = generate_hash(pwd)
    print(f"Hashed password: {hashed_pwd.decode()}")
