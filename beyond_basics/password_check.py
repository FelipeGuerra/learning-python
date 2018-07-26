correct_password = "python123"
name = input("Enter name: ")
surname = input("Enter surname: ")
password = input("Enter password: ")

while correct_password != password:
    password = input("Wroang password! Enter Again: ")

message = "Hi %s %s, you are logged in" % (name,surname)
print(message)