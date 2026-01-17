import random

print("\t \t \t \t Welcome to the Random Password generator \t \t \t \t")

# Variables for creating passwords

symbols = ['!','@', '#' ,'$' , '%','^' ,'&','*','(',')','=','+','}','{',']','[','~','?','<','>',':']
alphabets_min = ['a','b','c','d','d','e','f','g','h','i','j','k','l','m','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabets_max = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']

#Level Logic

hard = symbols + alphabets_min + alphabets_max + numbers
medium = alphabets_min + alphabets_max + numbers
easy = alphabets_min + numbers

#Function For generating Passcode

def making_():

    #Input for Difficulty Level

    choice = input("""
                   
    Choose a Difficulty level from 1 to 3 : """)

    #Conditions For each Difficulty level

    if choice == '1':
        level = easy
        passcode_len = random.randint(6,8)
    elif choice == '2':
        level = medium
        passcode_len = random.randint(10,15)
    elif choice == '3':
        level = hard
        passcode_len = random.randint(15,20)
    
    # Condition For Invalid Input for Difficulty level

    else:
        print("Invalid Input")
        making_()
    
    # Loop For generaing Required passcode
    
    print("""
          The Passcode is : """, end = " ")
    for i in range(passcode_len):
        char = random.choice(level)
        print(char, end = "")
    
    #Function For Continuing or Discontinuing generating Passcode
    def condition():
        continue_ = input("""
        
          Do you Want To Continue ? (Yes or No) : """)

        if continue_.lower() == "yes":
            making_()
        elif continue_.lower() == "no":
            exit()
        else:
            print("invalid Input")
            condition()

    condition()

making_()