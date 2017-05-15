
import time 

def story_intro(): 
    # let the user know they are playing a pigeon 
    # they are tasked with transporting a message from point A to point B
    print """
     ____  _                           ____                  __ 
    / __ \(_)___ ____  ____  ____     / __ \__  _____  _____/ /_
   / /_/ / / __ `/ _ \/ __ \/ __ \   / / / / / / / _ \/ ___/ __/
  / ____/ / /_/ /  __/ /_/ / / / /  / /_/ / /_/ /  __(__  ) /_  
 /_/   /_/\__, /\___/\____/_/ /_/   \___\_\__,_/\___/____/\__/  
         /____/                                                 
"""
    time.sleep(.5)
    print "Welcome to PIGEON QUEST"
    print "YOU are a pigeon" 
    time.sleep(.5)
    print "You must transport a very important message from Point A to Point B."
    time.sleep(.5)
    print "Are you ready?!!!!"

#testing out the story_intro 
story_intro() 

def display_main_menu(vitals): 
    # asks user for input 
    # fly 
    # rest 
    # poop 
    # eat 
    time.sleep(1)
    pigeon_options = "\n\n\nDear Pigeon, \n\
    Would you like to: \n\
    1. Fly \n\
    2. Rest \n\
    3. Poop \n\
    4. Eat \n\
    5. Quit this Mission \n\
    Enter 1, 2, 3, 4, or 5: "

    while True: 
        if vitals["distance"] == 5: 
            print "Congratulations you've made it to Point B!"
            break
        elif vitals["poop_capacity"] > 4: 
            print "I recommend you poop"
        elif vitals["health"] < 3: 
            print "I recommend you eat or rest"

        pigeon_input = raw_input(pigeon_options)
        if (pigeon_input == "1") and vitals["health"] >= 3: 
            print "fly"
            fly(vitals)
        elif pigeon_input == "2": 
            print "rest"
            rest(vitals)
        elif pigeon_input == "3": 
            print "Poop"
            poop(vitals)
        elif pigeon_input == "4": 
            print "Eat"
            eat(vitals)
        elif pigeon_input == "5": 
            break 
        else: 
            print "invalid option, please enter 1, 2, 3, 4, or 5"


def fly(vitals): 
    print """
                    ,-' ______
                    '  .-'  ____7
                /   /   ___7
              _|   /  ___7
            >(')\ | ___7     
              \\/     \_______
                '        _======>
                `'----\\`        
    """
    vitals["health"] = vitals["health"] - 1
    vitals["distance"] = vitals["distance"] + 1 


def rest(vitals): 
    vitals["health"] = vitals["health"] + 1 

def poop(vitals): 
    vitals["poop_capacity"] = vitals["poop_capacity"] - 1

def eat(vitals):
    vitals["health"] = vitals["health"] + 1 
    vitals["poop_capacity"] = vitals["poop_capacity"] + 1


vitals = {
    "health": 5,
    "distance": 0, 
    "poop_capacity": 3
}
display_main_menu(vitals)
