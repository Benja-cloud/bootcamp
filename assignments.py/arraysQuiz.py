#compose a program that creates a one-dimensional array 'a"
#containing exactly 1000 integers, and then attempt to access a[1000]
#What happens when you run the program?
a = list(range(1000))
print(a[1000])

#Answer: Indexing error
#What is wrong with he following code fragment
a = []
for i in range(10):
    a[i] = i + i

#Answer: there is no instruction on what to do with the list

#what does the following code fragment write?

a = stdarray.createID(10,0)
for i in range(10):
    a[i] = 9 - i
for i in range(10):
    a[i] = a[a[i]]
for v in a:
    stdio.writeIn(v)

#Answer:Pythn does not accomodate

#what is a[] after executing the following code fragment
n = 10
a = [0, 1]
for i in range(2,n):
    a += [a[i-1]+a[i-2]]
print(a)

#compose a program that takes an integer command-line argument n
#and writes n poker hands(five cards each) from a shuffle deck separated 
# by blank lines
