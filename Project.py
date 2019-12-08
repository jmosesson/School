import random

print("How's it going fella? We're gonna play the game 'Guess the Number', where you try to guess a number I am thinking. What can I call you?") #introduces the game and asks for the player's name

playersname=input() #gives the player's name a variable to be used next in referencing the player by the name provided

print("\nOkie Dokie " + playersname + ", I am thinking of a number from 1 to 100. Get ready to take your first shot!! \n") #begins the game for the user



answer=random.randint(1,101) #randomly selects an integer from 1 to 100
guesses = 0
while guesses < 10:
    print("Take a shot. ")
    guess=input()
    
    guess=int(guess) #this is to establish that the input with be an integer and not a string
    if guess > answer: #case where the player's guess it higher than the answer
        guesses+=1 #Counts the number of guesses
        print("Nope, you're too high")
    elif guess < answer: #case where the player's guess it loweer than the answer
        print ("You're too low")
        guesses+=1 #Counts the number of guesses
    elif guess == answer: #case where the player guesses a number that is the same as the answer
        print(f"DING DING DING DING DING \nCongrats " + playersname + f" You guessed correctly in {guesses} tries!") #Winning message
        break #end of program
if guesses > 10:
    print(f"Sorry. You have run out of tries. The correct answer was {answer}")
