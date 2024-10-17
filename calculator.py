def addition(x,y):
    return round(x+y,2)

def subtraction(x,y):
    return round(x-y,2)

def multiplication(x,y):
    return round(x*y,2)

def division(x,y):
    if y==0:
        return "Division by Zero Error"
    return round(x/y,2)


print("Welcome to Simple Calculator")
print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Quit")

while True:
    choice=int(input("Enter your Choice(1/2/3/4/5):"))

    if choice==5:
            print("You Quit")
            break
            
    if choice in(1,2,3,4):
        num1=float(input("Enter the first number:"))
        num2=float(input("Enter the second number:"))

        if choice==1:
            result=addition(num1,num2)
            print(f"Result for Addition:{result}")
        elif choice==2:
            result=subtraction(num1,num2)
            print(f"Result for Subtraction:{result}")
        elif choice==3:
            result=multiplication(num1,num2)
            print(f"Result for Multiplication:{result}")
        elif choice==4:
            result=division(num1,num2)
            print(f"Result for Division:{result}")
        
    else:
        print("Invalid Input")


