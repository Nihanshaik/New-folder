master_pwd = input("Enter master password: ")

def view():
    # Open the file in read mode to view the saved passwords
    try:
        with open('password.txt', 'r') as f:
            for line in f.readlines():
                # Split the account name and password for better formatting
                data = line.strip()  # Removes leading/trailing whitespace including \n
                account, pwd = data.split(" ")
                print(f"Account: {account}, Password: {pwd}")
    except FileNotFoundError:
        print("No passwords saved yet.")

def add():
    # Taking account name and password as input from the user
    name = input("Account Name: ")
    pwd = input("Password: ")

    # Appending the new account and password to the file
    with open('password.txt', 'a') as f:
        f.write(name + " " + pwd + "\n")
    print("Password added successfully.")

while True:
    # Taking mode input from the user to either add or view passwords
    mode = input("Do you want to add a password or view existing passwords (view, add)? Type 'q' to quit: ")

    # Quit the program if the user enters 'q'
    if mode == "q":
        break

    # Call view function if user chooses 'view'
    elif mode == "view":
        view()

    # Call add function if user chooses 'add'
    elif mode == "add":
        add()

    # If the mode is invalid, prompt the user again
    else:
        print("Invalid mode, please choose 'view', 'add', or 'q' to quit.")
