from cryptography.fernet import Fernet

master_pwd = input("enter master password: ")

def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_files:
        


def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user: ",user , ", password: ",passw)
    
def add():
    name = input("account name: ")
    pwd = input("password : ")

    with open('password.txt','a') as f:
        f.write(name + "|" + pwd + "\n")

    
while True:
    mode = input("would you like to add or view pass?(add/view/q to quit): ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode")
        continue