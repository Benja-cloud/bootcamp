#python code to demo
#instantiation of a class
class Dog:
    pass
    #a simple class
    attr1 = "mammal"
    attr2 = "dog"

    #a sample method
    def fun(self):
        print("I'm a" ,self.attr1)
        print("I'm a",self.attr2)

#driver Code 
#object instantiation
Rodger = Dog()
#Accessing class attributes
#and method through objects
print(Rodger.attr1)
Rodger.fun()