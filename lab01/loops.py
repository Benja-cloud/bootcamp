#for loops is used in python to iterate over a list
#coolection based data structures like list, tuples and dictionaries
#basic syntax is for value in lst_of_values
list_of_tuples = [(1,2),(3,4)]
for a, b in list_of_tuples:
    print("a:", a, "b:", b)

#for loops can be used to
#,1-iterate over the range() function

for i in range(7):
    print(i)

#ne can add the bounds as below
for i in range(3,7,1):
    print(i)
#above code prints 3 4 5 6 
#2-iterate over values in a tuple
A = ["hello",1,65,"thank you",[2,3]]
for value in A:
    print(value)

#3- iterate over keys in a dictionary(aka hashmap)
fruits_to_colors = {"apple": "red",
                     "lemon": "green",
                     "orange": "orange"}  
for key in fruits_to_colors:
    print(key, fruits_to_colors[key])