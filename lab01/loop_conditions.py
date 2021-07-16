a = 330
b = 200
if b > a:
	print("b is greater than a")
else:
	print("a is greater than b")
#if test whether the condition is true(executes before run time)
# while executes during run time
# if there are only two conditions use if ...... else
#else tells the programmes that its comes to the end

#the code below prints even numbers
for num in range(1,100):

#this part checks the condition is met
	if num%2==0:
		print(num)
		num=num+1

#using the while loop

while num < 100:
	if num % 2 == 0:
		print(num)
		break
		num += 1

#the following code prints prime numbers

 