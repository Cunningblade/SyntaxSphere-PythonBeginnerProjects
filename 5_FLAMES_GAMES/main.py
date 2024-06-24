def remove_common_char(name1,name2):
    name1 = list(name1)
    name2 = list(name2)

    for char in name1:
        if char in name2:
            name1.remove(char)
            name2.remove(char)

    return (len(name1) + len(name2))

def flames_game(counts):
    FLAMES = ['F','L','A','M','E','S'] 
    
    while len(FLAMES) > 1:
        index = (counts % len(FLAMES)) - 1
        if index >= 0:
            right = FLAMES[index+1:]
            left = FLAMES[:index]
            FLAMES = right + left
        else:
            FLAMES = FLAMES[:len(FLAMES)-1]
        

    return FLAMES[0]
        
def flame():
    # name1 = input("Enter the 1st person Name: ")
    # name2 = input("Enter the 2nd person Name: ") 

    name1 = name1.replace(" ","")
    name2 = name2.replace(" ","")
    character_count = remove_common_char(name1,name2)
    relation = flames_game(character_count)

    flames_relation = {
        'F' : 'Friends',
        'L' : 'Lovers',
        'A' : 'Affectionate',
        'M' : 'Marriage',
        'E' : 'Enemies',
        'S' : ' Sibling '
    }
    print(f"The RelationShip between {name1} and {name2} is {flames_relation[relation]}.")
    


def char_to_value(char):
    return ord(char.lower()) - 96

def love():
    name1 = input("Enter the 1st person Name: ")
    name2 = input("Enter the 2nd person Name: ") 
    
    name1 = name1.replace(" ","")
    name2 = name2.replace(" ","")

    sum1 = 0
    sum2 = 0

    for char in name1:
        sum1 = sum1 + char_to_value(char)
    for char in name2:
        sum2 = sum2 + char_to_value(char)

    love_percentage = (sum1 + sum2)% 101 

    print(f"The Love Between {name1} and {name2} is {love_percentage}% .")


def main():
    print("You Can calulate your RealtionShips status or Your LOve for someone:\n1) YOUR REALTIONSHIP\n2)YOUR LOVE FOR SOMEONE")
    start = input("Choose Any One of the two : ")
    if start == '1':
        flame()
    elif start == '2':
        love()
    else:
        print("You Pressed the Wrong Button.")
        exit()


if __name__ == "__main__":
    main()