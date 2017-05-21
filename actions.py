import time 
import sys
import subprocess

# I got this ascii art from this website  http://www.ascii-art.com 
# They are NOT mine, they are by Joan Stark 


def map_progress(scalar): 
    path = " -->" * scalar 
    # print '{:#<20}'.format('')
    print "A *",
    print '{:20}'.format(path),
    print "* B"

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
    map_progress(vitals["distance"])
    time.sleep(1)
    subprocess.call("clear")


def sleep_cycles(): 
    print """
                 .-"-.
                / _ _ \\ 
                \_ v _/
                //   \\      
               ((     ))
         =======""===""=======
                  |||
                  '|'
      """
    time.sleep(.2)
    subprocess.call("clear")

    print """
                 .-"-.
                / _ _ \\ 
                \_ v _/ z
                //   \\      
               ((     ))
         =======""===""=======
                  |||
                  '|'
    """
    time.sleep(.2)
    subprocess.call("clear")

    print """
                 .-"-.
                / _ _ \\ Z
                \_ v _/ z
                //   \\      
               ((     ))
         =======""===""=======
                  |||
                  '|'
    """
    time.sleep(.2)
    subprocess.call("clear")

    print """
                 .-"-.    Z
                / _ _ \\ z
                \_ v _/ z
                //   \\      
               ((     ))
         =======""===""=======
                  |||
                  '|'
    """
    time.sleep(.2)
    subprocess.call("clear")

    print """
                 .-"-.    Z
                / _ _ \\ z
                \_ v _/ 
                //   \\      
               ((     ))
         =======""===""=======
                  |||
                  '|'
    """

    time.sleep(.2)
    subprocess.call("clear")

    print """
                 .-"-.    Z
                / _ _ \\ 
                \_ v _/ 
                //   \\      
               ((     ))
         =======""===""=======
                  |||
                  '|'
    """
    time.sleep(.2)
    subprocess.call("clear")

    print """
                 .-"-.    
                / _ _ \\ 
                \_ v _/ 
                //   \\      
               ((     ))
         =======""===""=======
                  |||
                  '|'
    """
    time.sleep(.2)
    subprocess.call("clear")


def rest(vitals): 
    vitals["health"] = vitals["health"] + 1 
    sleep_cycles()
    sleep_cycles()
    sleep_cycles()

    

def poop(vitals): 
    vitals["poop_load"] = vitals["poop_load"] - 1
    print """
                 .-"-.
                / . . \\
                \_ v _/
                //   \\      
               ((     ))
         =======""===""=======
                  |||
                  '|'
                   8 

    """

    time.sleep(.3)
    subprocess.call("clear")

    print """
                 .-"-.
                / . . \\
                \_ v _/
                //   \\      
               ((     ))
         =======""===""=======
                  |||
                  '|'

                   8 

    """

    time.sleep(.2)
    subprocess.call("clear")

    print """
                 .-"-.
                / . . \\
                \_ v _/
                //   \\      
               ((     ))
         =======""===""=======
                  |||
                  '|'


                   8 

    """

    time.sleep(.1)
    subprocess.call("clear")

    print """
                 .-"-.
                / . . \\
                \_ v _/
                //   \\      
               ((     ))
         =======""===""=======
                  |||
                  '|'


                   
                   8 

    """

    time.sleep(.05)
    subprocess.call("clear")

    print """
                 .-"-.
                / 0 0 \\
                \_ v _/
                //   \\      
               ((     ))
         =======""===""=======
                  |||
                  '|'


                   
                  '_' 

    """

    time.sleep(1)
    subprocess.call("clear")



def eat(vitals):
    vitals["health"] = vitals["health"] + 1 
    vitals["poop_load"] = vitals["poop_load"] + 1

