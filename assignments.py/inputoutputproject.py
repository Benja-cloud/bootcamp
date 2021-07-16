#the project determines if an individual knows the house
#he or he is headed to in the estate

visit = int(input("Hallo, welcome to jacaranda Estate. Which house are you headed?: "))
if visit >= 1 and visit <=45:
    print("you are headed to M-soma court")

elif visit >= 46 and visit <= 90:
    print("You are headed to Projects court")

elif visit >= 91 and visit <= 150:
    print("You are headed to Assignments court")
else:
    print("You must be in the wrong estate")