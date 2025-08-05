def calculator(): 
    while True:
        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 2nd number: "))
        print(" \nChoose operation:")
        print("1) Addition")
        print("2) Subtraction")
        print("3) Multiplication")
        print("4) Division")
        print("5) exit")
        ch=input("Enter your choice: ")
        if ch=="1":
            print(num1+num2)
        elif ch=="2":
            print(num1-num2)
        elif ch=="3":
            print(num1*num2) 
        elif ch=="4":
            if num2!=0:
                print(num1/num2)
            else:
                print("can not Divide by zero")
        elif ch=="5":
            print("thank you for using calculator")
            break
        else:
            print("invalid choice")
        
calculator()
