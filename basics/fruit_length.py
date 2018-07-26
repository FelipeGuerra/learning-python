myfile = open("fruits.txt")
fruits = myfile.read()
myfile.close()
fruits = fruits.splitlines()

for fruit in fruits:
    print(len(fruit))