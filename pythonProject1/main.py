try:
    with open("/Users/shukurullomeliboyev2004/Desktop/python_functions.-/pythonProject/Untitledt.txt") as file:
        print(file.read())
except FileNotFoundError as e:
    print("file is not avilable")
