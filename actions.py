import time 
import sys
import subprocess

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

def rest(vitals): 
    vitals["health"] = vitals["health"] + 1 
    print """
     //////////////
               ///
             ///
           ///
         ///
       ///
     ///
    //////////////
    """
    time.sleep(1)
    subprocess.call("clear")

    print """ 
    /////////////
              //
            //
          //
        //
      //
    //
    ////////////
    """
    time.sleep(1)
    subprocess.call("clear")

    print """ 
    //////////
           //
         //
       //
     //
    ////////// 
    """
    time.sleep(1)
    subprocess.call("clear")

    print """ 
        ///////
            //
          //
        //
        ////// """ 

    time.sleep(1)
    subprocess.call("clear")

    print """ 
        /////
           /
          /
         /
        /////
    """ 
    time.sleep(1)
    subprocess.call("clear")


    print """ 
        /////
           /
          /
        /////
    """ 

    time.sleep(1)
    subprocess.call("clear")

    print """ 
        Z
    """ 
    
    time.sleep(1)
    subprocess.call("clear")

def poop(vitals): 
    vitals["poop_load"] = vitals["poop_load"] - 1

def eat(vitals):
    vitals["health"] = vitals["health"] + 1 
    vitals["poop_load"] = vitals["poop_load"] + 1

