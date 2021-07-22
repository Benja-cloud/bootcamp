import random
number = random.randint(1, 10)

guess_party = input("Hi, kindly state your name?")
number_of_guesses = 0
print('Hey! '+ guess_party + ' Kindly engage for a few. Guess a number between 1 and 10:')
print()

def game():
    number = random.randint(1, 10)
    print("You don't have forever. Just 5 chances to guess the number. Have the Go!!")
    i = 1
    r = 1
    while i<5:  
        guess_digit = int(input('Enter your number: ')) 
        if guess_digit < number:
            print("Your guess is too low")
            print()
            print("You are at " + str(5-i)+ " chances to go" )
            i = i+1
        elif guess_digit > number:
            print("Your guess is too high")
            print()
            print("You are at " + str(5-i)+ " chances to go" )
            i = i+1
        elif guess_digit == number:
            print("\n You gave the right guess, Yay!!. BINGO!!")
            
            r = 0;
            break
        else:
            print("This number is invalid. You need to give it another try")
            print("You are at " + str(5-i)+ " chances to go" )
            continue
    if r==1:
        print("Ooooh!!! Sooo bad you lost the game!!")
        print()
        print("I was holding = " + str(number))
        print("Put in your best foot next time!!")

def main():
    game()
    while True:
        another_game = input("Do you wish to play again?(Y/N): ")
        if another_game == "Y":
            game()
        else:
            break
main()
print("\n This is THE END! You did great.Thanks!")