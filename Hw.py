d1 = {}

while True:
    print("Menu:")
    print("1. Add item")
    print("2. Delete item")
    print("3. Display dictionary")
    print("4. Access value by key")
    print("5. Print all values")
    print("6. Print all keys")
    print("7. Exit")

    ch = input("Choose an option: ")

    if ch == '1':
        key = input("Enter key: ")
        value = input("Enter value: ")
        d1[key] = value
        print("Item added.")
    
    elif ch == '2':
        key = input("Enter key to delete: ")
        if key in d1:
            del d1[key]
            print("Item deleted.")
        else:
            print("Key not found.")
    
    elif ch == '3':
        print("Dictionary:")
        for key in d1:
            print(key, ":", d1[key])
    
    elif ch == '4':
        key = input("Enter key: ")
        if key in d1:
            print("Value:", d1[key])
        else:
            print("Key not found.")
    
    elif ch == '5':
        print("All values:")
        for value in d1.values():
            print(value)
    
    elif ch == '6':
        print("All keys:")
        for key in d1.keys():
            print(key)
    
    elif ch == '7':
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Try again.")
