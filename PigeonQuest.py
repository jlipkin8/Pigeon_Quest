
import time 
import sys
import subprocess
import actions

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
# story_intro() 

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
            print """
                 ___  __   __ _   ___  ____   __  ____  ____  _   
                / __)/  \ (  ( \ / __)(  _ \ / _\(_  _)/ ___)/ \  
               ( (__(  O )/    /( (_ \ )   //    \ )(  \___ \\_/  
                \___)\__/ \_)__) \___/(__\_)\_/\_/(__) (____/(_)  
            """

            time.sleep(.5)
            print "you've made it to Point B!"
            break
        elif vitals["poop_load"] > 4: 
            print "I recommend you poop"
        elif vitals["health"] < 3: 
            print "I recommend you eat or rest"
               
        pigeon_input = raw_input(pigeon_options) 
        subprocess.call("clear")
        
        if (pigeon_input == "1") and vitals["health"] >= 3: 
            # print "fly"
            actions.fly(vitals)
        elif pigeon_input == "2": 
            # print "rest"
            actions.rest(vitals)
        elif pigeon_input == "3": 
            # print "Poop"
            actions.poop(vitals)
        elif pigeon_input == "4": 
            # print "Eat"
            actions.eat(vitals)
        elif pigeon_input == "5": 
            break 
        else: 
            print "invalid option, please enter 1, 2, 3, 4, or 5"


vitals = {
    "health": 5,
    "distance": 0, 
    "poop_load": 3
}

display_main_menu(vitals)



# for i in range(10):
#     print '\r',         # print is Ok, and comma is needed.
#     time.sleep(0.3)
#     print i,
#     sys.stdout.flush()  # fl

