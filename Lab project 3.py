#oregon trial game

import random 
#setting stuff up
name =(input("what is your name" ))
print(f"my name is {name}")
miles_left = 2000
days_left = 305
print("I must travel the Oregon Trail and I have 305 days to do it, 5 health, 500lbs of food, and have 2000 miles to go. I wish you good luck on your adventure and hope for your safe return! ")
current_miles = 0
current_health = 5
current_food = 500
current_days = 1
days = 0
turn = 0

#use
#fuctions
def health():
    global current_health
    current_health += 1
    
def eat():
    global current_food, current_days
    
def travel():
    global current_days, current_miles , miles_left, days_left, current_food
    current_days += random.randint(3,7)
    current_miles += random.randint(30,60)
    print (f"you Have traveled {current_miles} miles")
    miles_left -= current_miles
    days_left -= current_days
    current_food -= current_days * 5
    
def status():
    print(f"you have {miles_left} miles, have {days_left}days left, have {current_health} health, and have {current_food}lbs of food.")

def hunt():
    
    global current_food, current_days
    current_food += 100
    current_days += random.randint(2,5)
    current_food -= current_days * 5
    print(f"you now have {current_food} lbs of food and {current_days} days travled")
def rest():
    global current_days, current_food
    current_days += random.randint(2,5)
    print(f"you have gained 1 health and are now on {current_days} days travled")
    current_food -= current_days * 5
    health()
def quit():
    global game_over
    print("You could not endure the trail better luck next time! ")
    game_over = True






# if current_days += 1:
#     print("another day has past which consumed 5 lbs of food")
#     current_food -= 5
game_over = False
while not game_over:
    
#player decisions
    
    player_choices = input("what would you like to do? (travel, hunt, rest, status, help, quit ")
    print(player_choices)
    if player_choices == 'status':
        status()
    
    elif player_choices == 'help':
        print(player_choices)

    elif player_choices == 'quit':
        quit()

    elif player_choices == 'travel':
        travel()
    elif player_choices == 'hunt':
        hunt()
    elif player_choices == 'rest':
        rest()

    elif current_miles == miles_left:
        print("Congradulations you made it through the Oregon Trial and beat the game!")
        game_over = True
    
    elif current_days == days_left:
        print("You have run out of days and lost the game :( ")
        game_over = True
    
    elif current_food == 0:
        print("You have starved to death game over! ")
        game_over = True

    else:
        print("This is not one of the options")


