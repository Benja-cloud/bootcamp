#this is a program that takes input (marks)
#And then grades the user
num =int(input('Please enter your mark: \n'))
if num<100 and num >80:
    print("you got grade A")
elif num<80 and num >84:
    print("you got grade B+")
elif num<84 and num >80:
    print("you got grade B")
elif num<79 and num >75:
    print("you got grade B-")
elif num<74 and num >70:
    print("you got grade C+")
elif num<69 and num >65:
    print("you got grade C")
elif num<64 and num >60:
    print("you got grade C-")
elif num<59 and num >55:
    print("you got grade D")
else: 
    print("you FAILED")


