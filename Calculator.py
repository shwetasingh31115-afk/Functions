def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("Please select a operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.division")
choice=int(input("Enter your choice number:"))
num1=int(input("Enter your first number:"))
num2=int(input("Enter your second number:"))
if choice==1:
    print(num1,"+",num2,"=",add(num1,num2))
elif choice==2:
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice==3:
    print(num1,"x",num2,"=",multiply(num1,num2))
elif choice==4:
    print(num1,"%",num2,"=",divide(num1,num2))
else:
    print("Invalid input")