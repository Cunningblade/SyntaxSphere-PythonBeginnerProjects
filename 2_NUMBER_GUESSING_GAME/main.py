# So for this we will require a random number to be guessed , so for this we will import random module which is an inbult module in python
##****Try to declare all the module at the top of the program , it enhances readability
import random #This will generate a random no. for us
import math 

# Defining the game function now
def game(number,chances,lower_bound,upper_bound):

    while(chances != 0):
        
        # Asking the User to Guess the Number
        guess = int(input("Choose a Number: "))

        # Checking if the Guess is in Bound or Not
        if guess > upper_bound:
            print("Duffer! You Guessed the value higher than the Upper Bound.\nTry Again\n")
        elif guess < lower_bound:
            print("Idiot! You Guessed the Value Lower than the Lower Bound.\nTry Again\n")
        else:#If guess is the Proper Bound
            if guess > number :#If the guess Is Greater than the NUmber
                if guess - number < 5:
                    print("You are Too Close\nGuess a little bit Lower\n")
                elif guess - number < 15:
                    print("You Can TRY Better \nGuess Lower\n")
                else:
                    print("YOUR GUESS IS TOO HIGH \n")
            if guess < number : # If the guess is lower tha the number
                if number - guess < 5:
                    print("You are Too Close\nGuess a little bit Higher\n")
                elif number - guess < 15:
                    print("You Can TRY Better \nGuess Higher\n")
                else:
                    print("YOUR GUESS IS TOO LOW \n")
            else:
                print("YOU GUESSED IT RIGHT!!\n You Won THE GAME\n")
                break
        chances -= 1
        print("The NO. of tries Reamining",chances)
        if(chances == 0):
            print("\nYou have exhausted your chances of guessing. YOU LOST!!! LOSER\n ")
            print("\nThe Correct Number to be guessed was:",chances)
        
            
# Now we will start our main program 
def main():#THis is the starting of the program
    #Firstly we will bw taking a Range in which we want to guess a no.
    lower_bound = int(input("Enter The lower Range: "))
    print("")
    upper_bound = int(input("Enter The Upper Range: "))
    print("")
    print("You Have to Guess the No. in between",lower_bound,"-",upper_bound,"")

    #Now we need to chances in which the user can guess the no. so For this we need a Math Module as log function is defined in it  
    chances = math.ceil(math.log(upper_bound - lower_bound , 2)) + 1 # This many chances will the user get to guess the number

    # Lets Show the user How many chances will they be getting to guess the correct no.
    print("You will be getting",chances,"to guess the correct no.")
    
    #Now Lets genrate a random no. by using random module which we have imported earlier
    number = random.randint(lower_bound,upper_bound)

    #now we will call the game function which we are going to CODE NOW
    game(number,chances,lower_bound,upper_bound)


# Now this is the Normal synatax which i will right just now so dont panic
# This means the program exection will start from now
if __name__ == "__main__":
    main()

# Now lets Try to run our code
# So the output does now look nice so i will just do it in such a way that it is readable
# Now try to Code it yourself and see how much you learned 


                                