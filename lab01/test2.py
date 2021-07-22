class Person:
    pass
    #a simple class
    def _init_(self, name):
        self,name = name

    #a sample method
    def say_hi(self):
        print("Hello, my name is ", self.name )

p = Person()
p.say.hi()