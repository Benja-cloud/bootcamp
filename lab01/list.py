# below is a list in python
#they are indexed. meaning the first item has the place zero
#and the last is indexed n-1
shopping_list = ['apples', 'pen' , 'oatmeal cookies' , 'notepad' ]
# to replace an item check the example below

shopping_list[2] = 'candy'
print(shopping_list)

#the output should be ['apples', 'pen', 'candy', 'notepad']
#note that oatmeal has been replaced 
#the list has 4 items. if you access a fifth item whch does not exist 

print(shopping_list[5])

#you get an error ie INdexError: list index out of range
# note that negative indexing is also possible
# the last element is indexed -1

print(shopping_list[-1])

#this should give the last item: notepad
