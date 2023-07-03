# let's say:
# choice 1=addition
# choice 2=subtraction
# choice 3=multiplication
# choice 4=division

choice = input("Enter your choice : ")

num = float(input("Enter Number 1 : "))
num1 = float(input("Enter Number 2 : "))
if choice == "1":
    print(num, "+", num1, "=", (num + num1))
elif choice == "2":
    print(num, "-", num1, "=", (num - num1))
elif choice == "3":
    print(num, num1, "*", "=", (num * num1))
elif choice == "4":
    if num == 0.0 or num1 == 0.0:
        print("Divided by 0 is error")
    else:
        print(num, "/", num1, "=", (num / num1))

else:
    print("invalid choice")
