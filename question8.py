balance = 1000

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print(f"Deposited {amount}. New balance: {balance}")
        
    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"Withdrawn {amount}. New balance: {balance}")
            
    elif choice == '3':
        print(f"Current balance: {balance}")
        
    elif choice == '4':
        print("Exiting...")
        break
        
    else:
        print("Invalid option. Try again.")
        