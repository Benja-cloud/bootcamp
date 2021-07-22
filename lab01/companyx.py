#creating a class
class Employee():
    def __init__(self,first, last, shift,email,machine ):
        self.first = first
        self.last = last
        self.shift = shift
        self.email = email
        self.machine = machine

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Polycarp','Odhiambo','A','KT-2')
emp_2 = Employee('Benjamin','Otieno','B','FBD')

print(emp_2.fullname())

