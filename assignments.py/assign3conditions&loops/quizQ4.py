#compose a program that takes three integer command-line arguments and
#writes 'equal' if all three are equal and 'not equal', otherwise.
num1 = int(input('Enter the first number:  '))
num2 = int(input('Enter the second number:  '))
num3 = int(input('Enter the third number:  '))

if num1 == num2 == num3:
    print('Equal')
else:
    print('Not Equal')