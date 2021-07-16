#what is the value of j after each of the following code fragments is executed
j = 0
for i in range(0,10): 
    j += i
    print(j)

#Answer: the result is = 0,1,3,6,10,15,21,28,36,45

j = 1
for i in range(0,10): 
    j += j
    print(j)

#Answer: the result is = 2,8,16,32,64,128,256,512,1024

for j in range(0,10): 
    j += j
    print(j)

#Answer: 0,2,4,6,8,10,12,14,16,18