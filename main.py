print("Welcome to Game of Decision !!!")

# Creating Variables
name = input("What is your name ? ")
age = int(input("How old are you ? "))  # Converting age into integer
health = 0

print("Welcome "+name+" to Game of Decision. You are "+str(age)+" years old ...")

# Creating  age restriction condition
if age >= 18:
    print("You are old enough to play!")
    # Checking want to play or not
    want_to_play = input("Do you want to play (yes / no) ? ").lower()  # .lower() method converts any input into lower case
    if want_to_play == "yes":
        print("Let's play! Your health level is 10")

        # Creating Decisions
        print("First walk with me ... ")
        left_or_right = input("So, choose your direction (left / right): ").lower()
        if left_or_right == "left":
            print("You fall into the river ... Its so cold water\nYou have to came out from the river as soon as possible")
            health -= 1
            print("Your health is now "+str(health))
            bank_or_across_current = input("Now decide, swim across the flow current or towards the riverbank (bank / currect): ").lower()
            if bank_or_across_current == "bank":
                print("You swim towards the riverbank. It cost you some time.\nBut now you see bank is too high, you can't really make it.")
                print("Now you have no choise but swim across the flow current of the river\nAnd you loose some heath too")
                health -= 1
                print("Now your health is "+str(health))

            elif bank_or_across_current == "current":
                pass
            else:
                pass




        elif left_or_right == "right":
            health = 0
            print("You head towards the road and hit by truck while crossing the road .... \nHealth is "+str(health)+" now\nGAME OVER !!!")
        else:
            print("Invalid Input !!!")
    elif want_to_play == "no":
        print("That's okay, see you ...")
    else:
        print("Invalid Input !!!")
else:
    print("Oh", name, ",you are not old enough to play!")
