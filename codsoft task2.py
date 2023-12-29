
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
oper = input("Choose operator:")
if(oper == "+"):
    print("addition:",num1+num2)
elif(oper == "-"):
    print("subtraction:",num1-num2)
elif(oper == "*"):
    print("Multiplication:",num1*num2)
elif(oper == "/"):
    print("divison:",num1/num2)
else:
    print("Invalid operation...please enter correct operator")
