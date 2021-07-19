#functions/variable
def cars():
    print("I love cars. They are great!!")
    

cars()
#functions with arguments
def cars(first_car, second_car):
    print(f"My whole fleet includes a {first_car} and a {second_car}.")


cars("BMW", "Merc")

#function with a loop

def cars(model):
    for x in model:
        print(x)

german = ["BMW","Merc","Opel Astra","VW"]

cars(german)
