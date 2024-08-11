a=int(input("Enter the value of first number:"))
b=int(input("Enter the value of second number:"))
choice=0
while choice<4:
    print("Simple Calculator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice = int(input("Enter your choice"))
    if choice==1:
            c=a+b
            print("Addition is:",c)
    elif choice==2:
            c=a-b
            print("Subtraction is:",c)
    elif choice==3:
            c=a*b
            print("Multiplication is:",c)
    elif choice==4:
            c=a/b
            print("Division is:",c)
    else:
            print("Invalid Choice")
