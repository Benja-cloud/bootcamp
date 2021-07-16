#function to add two numbers
def add(num1, num2):
    return num1 + num2

#function to subtract two numbers
def subtract(num1,num2):
    return num1 - num2

#function to multiply two numbers
def multiply(num1,num2):
    return num1*num2

#fucntion to divide two numbers
def divide(num1,num2):
    return num1/num2

print("Please select an operation\n" \
        "1.Addition\n" \
        "2.Subtraction\n" \
        "3.Multiplication\n" \
        "4.Division\n")
select = int(input("Enter the selected operation: "))
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
if select == 1:
    print(number_1, " + ", number_2, " = ", add(number_1, number_2))

elif select == 2:
    print(number_1, " - ", number_2, " = ", subtract(number_1, number_2))

elif select == 3:
    print(number_1, " * ", number_2, " = ", multiply(number_1, number_2))

elif select == 4:
    print(number_1, " / ", number_2, " = ", divide(number_1, number_2))

else:
    print("Thats an invalid operation!!")