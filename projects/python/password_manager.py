master_pwd = input("Enter password: ")

def view():
 with open('password.txt', 'r') as f:
   for line in f.readlines():
     print(line.rstrip())
   

def add():
  name=input("Account Name: ")
  pwd = input("Password: ")

  with open('password.txt', 'a') as f:
    f.write("Account Name: "+name+"|"+"Password: "+pwd+"\n")


while True:
 mode=input("if you want to add the password or view eixsiting password (view,add)?: ")
 if mode =="q":
   break
 
 if mode =="view":
   view()
 
 elif mode == "add":
  add()
 else:
   print("Invalid mode")
   continue
 print("Password saved successfully")
 print("hi")
 
