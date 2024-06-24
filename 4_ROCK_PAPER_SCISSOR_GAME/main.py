import random 
def rules():
    print("You will be playing against the Computer\n")
    print("Paper X Rock -> Paper wins")
    print("Scissor X Rock -> Rock wins")
    print("Paper X Scissor -> Scissor")

def user_inputs():
    print("1.Press 'r' or 'R' or '1' for Rock")
    print("2.Press 'p' or 'P' or '2' for Paper")
    print("3.Press 's' or 'S' or '3' for Scissor")
    us_input = input("Choose one one of the above: ").lower()
    if us_input == 'r' or us_input == '1':
        return 1 # Rock
    elif us_input == 'p' or us_input == '2':
        return 2 # Paper
    elif us_input == 's' or us_input == '3':
        return 3 # Scissor
    else:
        print("Wrong Input! Select Again")
        return user_inputs()

def game():
    user_choice = user_inputs()
    ob = ["ROCK","PAPER","SCISSOR"]
    comp_input = random.randrange(0,2) 
    print(f"The computer selected :{ob[comp_input]}")
    comp_input += 1 
    print("You Selected :",end="")
    if user_choice == 1:
        print(ob[0])
    elif user_choice == 2:
        print(ob[1])
    elif user_choice == 3:
        print(ob[2])
    # Game decision 
    if user_choice == comp_input:
        print("Draw")
    elif user_choice == 1:
        if comp_input == 3:
            print("YOU WON")
    elif user_choice == 2:
        if comp_input == 1:
            print("YOU WON")
    elif user_choice == 3:
        if comp_input == 2:
            print("YOU WON")
    else:
        print("YOU LOSE")



def main():
    print("Choose any of the one option below:\n"+"Select 1 for the RULES\n"+"SELECT 2 for PLaying the GAME\n"+"Select 3 For EXITING the GAME\n")

    start = input("Choose any One of the Following: ")
    if start == '1':
        rules()
    elif start == '2':
        game()
    else:
        exit()

if __name__ == "__main__":
    main()