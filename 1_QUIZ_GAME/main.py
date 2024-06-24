print("Welcome TO Quizzzessss")
name = input("What is your Name?\n")
print("Welcome",name,",Let the Game Begin!!!")

score = 0
print("\nYou will be awarded 1 point for a correct answer and No points for any Wrong Answer")

q = 0 #this will keep track of the no. of questions 
#Question
print("Question",q+1,":")
answer = input("Who is known as the Father of Geometry?\n")
q += 1
if answer.lower() == "euclid":#here .lower() will convert all the charaters of the string into lower case
    print("Correct Answer !! \nYour Score is increased By 1\n")
    score += 1
else:
    print("Wrong Answer! Its Okay try The next question\n")

#Question
print("Question",q+1,":")
answer = input("Which is the biggest animal on earth?\n")
q += 1
if answer.lower() == "blue whale":
    print("Correct Answer !! \nYour Score is increased By 1\n")
    score += 1
else:
    print("Wrong Answer! Its Okay try The next question\n")

#Question
print("Question",q,":")
answer = input("How many days does a leap year have?\n")
q += 1
if answer == "366":
    print("Correct Answer !! \nYour Score is increased By 1\n")
    score += 1
else:
    print("Wrong Answer! Its Okay try The next question\n")

#Question
print("Question",q+1,":")
answer = input("Who wrote the Mahabharata?\n")
q += 1
if answer.lower() == "ved vyasa":
    print("Correct Answer !! \nYour Score is increased By 1\n")
    score += 1
else:
    print("Wrong Answer! Its Okay try The next question\n")

#Question
print("Question",q+1,":")
answer = input("Which is the smallest ocean?\n")
q += 1
if answer.lower() == "artic":
    print("Correct Answer !! \nYour Score is increased By 1\n")
    score += 1
else:
    print("Wrong Answer! Its Okay try The next question\n")

#Question
print("Question",q,":")
answer = input("Which organ is responsible for the purification of blood in the human body?\n")
q += 1
if answer.lower() == "kidney":
    print("Correct Answer !! \nYour Score is increased By 1\n")
    score += 1
else:
    print("Wrong Answer! Its Okay try The next question\n")

#Question
print("Question",q+1,":")
answer = input("Which part of the human body has the smallest bone?\n")
q += 1
if answer.lower() == "ear":
    print("Correct Answer !! \nYour Score is increased By 1\n")
    score += 1
else:
    print("Wrong Answer! Its Okay try The next question\n")

#Question
print("Question",q,":")
answer = input("Which is the most sensitive organ in the human body?\n")
q += 1
if answer.lower() == "skin":
    print("Correct Answer !! \nYour Score is increased By 1\n")
    score += 1
else:
    print("Wrong Answer! Its Okay try The next question\n")

#Question
print("Question",q+1,":")
answer = input("Which animal is known as the ship of the desert?\n")
q += 1
if answer.lower() == "camel":
    print("Correct Answer !! \nYour Score is increased By 1\n")
    score += 1
else:
    print("Wrong Answer! Its Okay try The next question\n")

#Display Score
print("You Have Scored:",score,"Points")
print("Your correct answer percentage is:",((score/q)*100),"%")
