print("Welcome to Game of Decision !!!")

# Creating Variables
name = input("What is your name ? ")
age = int(input("How old are you ? "))  # Converting age into integer

print("Welcome "+name+" to Game of Decision. You are "+str(age)+" years old ...")

# Creating  age restriction condition
if age >= 18:
    print("You are old enough to play!")
    # Checking want to play or not
    want_to_play = input("Do you want to play (yes / no) ? ")
    if want_to_play == "yes":
        print("Let's play!")

        # Creating Decisions



    elif want_to_play == "no":
        exit()
    else:
        print("Invalid Input !!!")
else:
    print("Oh", name, ",you are not old enough to play!")
