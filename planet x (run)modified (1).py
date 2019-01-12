import time


def ship2():
    time.sleep(3)
    print ("\n-----------------------Ship-----------------------")
    time.sleep(2)
    print ("\nThank you for come back to the ship to repair it.")
    time.sleep(2)
    print ("Did you bring sapphire that has a magical power to renew all the things?")
    print("\n1. Y")
    print("2. N")
    choice18=(str(input("\nUser: ")).lower())
    if choice18=="1" or choice18=="y":
        print("Now you can go back to the earth!")
        time.sleep(1)
        print("BUT you don't want to leave without people who live in Planet X.")
        print("Will you leave the Planet X or decide to stay with people in Planet X?")
        time.sleep(1)
        print("\n1. Go back to the earth")
        print("2. Stay in Planet X")
        choice19=(str(input("\nUser: ")).lower())
        if choice19=="1":
            time.sleep(1)
            print("CONGRATULATION! Now you can go back to your family")
            time.sleep(1)
            print("CCC  O   N  N  GGGG  RRRR     A   TTTTT  SSSS")
            time.sleep(1)
            print("C   O O  NN N  G     R  R   A   A   T    S")
            time.sleep(1)
            print("C   O O  N NN  G GG  RRRR   A A A   T    SSSS")
            time.sleep(1)
            print("CCC  O   N  N  GGGG  R   R  A   A   T       S")
            time.sleep(1)
            print(" 		     R    R	         SSSS")
            exit(0)
        elif choice19=="2":
            print("Monster attacked again!")
            exit()
        else:
            print("nInvalid Input")
            time.sleep(1)
            choice19 = input("User: ")
    elif choice18=="2" or choice18=="n":
        time.sleep(1)
        print("You need to bring sapphire to repair the ship.")
        return cave()
    else:
        print("\nInvalid Input")
        time.sleep(1)
        choice18 = input("User: ")
                

def cave2():
    time.sleep(1)
    print("\nThere are 3 tunnels fork in the cave")
    time.sleep(1)
    print("Choose one to find the sapphire")
    time.sleep(1)
    print("\n1.Tunnel 1")
    print("2. Tunnel 2")
    print("3. Tunnel 3")
    choice16 = (str(input("\nUser: ")).lower())
    if choice16=="1":
        print("You leaped off the cliff.")
        print("GAME OVER")
        time.sleep(1)
        print("\n1. Exit")
        print("2. Restart the game")
        choice0 = (str(input("\nUser: ")).lower())
        if choice0==1 or choice0==exit:
            exit(0)
        elif choice0=="2" or choice0=="restart the game":
            return main()
        else:
            print("nInvalid Input")
            time.sleep(1)
            choice16 = input("User: ")
    elif choice16=="2":
        print("There is small light in the tunnel 2.")
        time.sleep(1)
        print("\n1. Follow the light")
        print("2. Go back to the fork")
        choice17 = (str(input("\nUser: ")).lower())
        if choice17=="1" or choice17=="follow the light":
            time.sleep(1)
            print("You found the sapphire. Go back to ship and repair it.")
            ship2()
        elif choice17=="2" or choice17=="go back to the fork":
            return cave2()
        else:
            print("\nInvalid Input")
            time.sleep(1)
            choice17 = input("User: ")
    elif choice16=="3":
        time.sleep(1)
        print("One monster is sleeping in Tunnel 3.")
        time.sleep(1)
        print("\n1. Go back to the fork to go other tunnel.")
        print("2. Try to kill the monster incase it has the sapphire.")
        choice18 = (str(input("\nUser: ")).lower())
        
        if choice18=="1":
            return cave2()
        
        elif choice18=="2":
            time.sleep(1)
            print("You've got serious injury by the monster.")
            time.sleep(1)
            print("You need to go back to the ship to get the first aid.")
            alcohol()
        else:
            print("\nInvalid Input")
            time.sleep(1)
            choice18 = input("User: ")
    else:
        print("\nInvalid Input")
        time.sleep(1)
        choice16 = input("User: ")

        
def cave():
    time.sleep(2)
    print ("There’s a special gemstone in this cave. It is a crystal clear sapphire that has been transmitted from generation to generation.")
    time.sleep(1)
    print ("This sapphire has a magical power to renew all the things. But six years ago, a monster lived in and took over the sapphire.")
    time.sleep(1)
    print ("Some people tried to drive him away.")
    time.sleep(1)
    print ("Unfortunately, they all got very serious injury because of the trap set by the monster. From that time, some people started to get sick.")
    time.sleep(2)
    print ("\n--------------------------------------------------")
    time.sleep(1)
    print ("\nThe sapphire is control by the monster. It must be the reason that these people get sick in this planet.")
    time.sleep(1)
    print ("\n1. Find a way to get the sapphire to launch the ship.")
    print ("2. Try to fix the ship again with the materials.")
    choice12 = (str(input("\nUser: ")).lower())
    if choice12 == "1" or choice12=="find a way to get the sapphire to launch the ship":
        sapphire()
    else:
        print("You try it again and again, but still cannot fix the ship. So you think you should find a way to get the sapphire to launch the ship")
        time.sleep(1)
        print ("\n1. Find a way to get the sapphire to launch the ship.")
        print ("2. Quit")
        choice13 = (str(input("\nUser: ")).lower())
        if choice13 == "1" or choice13=="find a way to get the sapphire to launch the ship":
            sapphire()
        else:
                exit(0)
        


def sapphire():
    time.sleep(2)
    print("\n1. Put on the space suit, with guns and knife in hand, go into the cave to kill it.")
    print("2. Collect the dry firewood and weeds, and burn them in the entrance of the cave.")
    choice10 = (str(input("\nUser: ")).lower())
    while (choice10 != "1" or choice10 != "2"):
        if choice10 == "1" or choice10 == "put on the space":
            time.sleep(2)
            print ("OMG! It’s huge and strong! It just kicks you with its foot, you died!")
            time.sleep(1)
            print("\n1. Restart the game.")
            print("2. Quit.")
            choice11 = (str(input("\nUser: ")).lower())
            if choice11 == "quit" or choice11=="2":
                exit(0)
                break
            else:
                return main()
        elif choice10=="2":
            print("Prepare a super large net to catch it when it goes out.")
            time.sleep(1)
            print ("1.Catch it")
            print ("2. Kill it")
            choice14 = (str(input("\nUser: ")).lower())
            if choice14 == "1" or choice14=="2" or choice14=="catch it" or choice14=="kill it":
                time.sleep(1)
                print("Monster died. Go into the cave to get the saaphire")
                print("\n1. Go into the cave to get the sapphire.")
                print("2. Quit")
                choice20 = (str(input("\nUser: ")).lower())
                if choice20=="1":
                    cave2()
                elif choice20=="2":
                    exit(0)
                else:
                    print("\nInvalid Input")
                    time.sleep(1)
                    choice20 = input("User: ")
            else:
                exit(0)
        
        
                      
                

def observe():
    time.sleep(2)
    print ("Get materials and back to fix the ship")
    time.sleep(1)
    print ("\n--------------------------------------------------")
    time.sleep(1)
    print ("The materials only can fix some parts of the ship, and it seems to need more power to launch")
    time.sleep(1)
    print ("--------------------------------------------------")
    time.sleep(1)
    print ("You think there are some other materials in the cave.")
    time.sleep(1)
    print("So you ask the people what is in the cave")
    cave()

    
def materials():
    time.sleep(2)
    print ("On the way to get materials, you find people are afraid of the cave which is not far away.")
    time.sleep(2)
    print("\n1. Observe and keep moving forward")
    print("2. Ask them what is in the cave")
    choice9 = (str(input("\nUser: ")).lower())
    while (choice9 != "1" or choice9 != "2"):
        if choice9 == "1" or choice9 == "observe and keep moving forward":
            observe()
        else:
            cave()
           
                
           
        
            
def repairShip():
    time.sleep(3)
    print ("\n-----------------------Ship-----------------------")
    time.sleep(2)
    print ("\nThank you for come to the ship to repair it.")
    time.sleep(2)
    print ("\nWhen you start repairing the ship you find out that you don’t have the material you need.")
    time.sleep(2)
    print("\nSo you need to go talk to the people.")
    time.sleep(2)
    print("\nAsk them to bring the materials you need.")
    time.sleep(2)
    print("\nDo you think people will come back with materials?")
    time.sleep(2)
    print("1.Follow people to get materials.")
    print("2.Stay until they come back and look for materials.")
    choice8 = (str(input("\nUser: ")).lower())
    while (choice8 != "1" or choice8 != "2"):
        if choice8 == "1" or choice8 == "follow people to get materials":
            materials()
        elif choice8=="2":
            print ("You've got attacked from aliens.")
            print("GAME OVER")
            time.sleep(1)
            print("\n1. Exit")
            print("2. Restart the game")
            choice0 = (str(input("\nUser: ")).lower())
            if choice0==1 or choice0==exit:
                exit(0)
            elif choice0=="2" or choice0=="restart the game":
                return main()
            else:
                print("\nInvalid Input")
                time.sleep(1)
                choice0 = input("User: ")
        else:
            print("\nInvalid Input")
            time.sleep(1)
            choice20 = input("User: ")
                  
        

def alcohol():
    time.sleep(2)
    print ("\nPut emergency mask on your face and put on gloves on your hands.")
    time.sleep(2)
    print ("Rubb alcohol pad to people's dark patches.")
    time.sleep(2)
    print ("Tell people to go repair ship together with you.")
    time.sleep(2)

    repairShip()
    

def firstAid():
    time.sleep(2)
    choice7 = (str(input("\nUser: ")).lower())
    while(choice7 != "y" or choice7 != "n"):
        if choice7 == "n" or choice7=="2":
            time.sleep(2)
            print ("\nThey don't know what the first aid kit is.")
            print ("\nExplain them while you cure people.")
            break
        elif choice7=="1" or choice7=="y":
            time.sleep(2)
            print("\nIf they nod then they have many too")
            time.sleep(2)
            print("\nTell them to bring more first aid kit.")
            break
        else:
            print("\nInvalid Input")
            time.sleep(1)
            choice3 = input("User: ")
    alcohol()
        
    
def cure():
    time.sleep(2)
    print("\n1. Find first aid kit.")
    print ("2. Ignore them.")
          
    choice6 = (str(input("\nUser: ")).lower())
    time.sleep(2)
    while (choice6 != "1" or choice6 != "2"): 
        if choice6 == "1" or choice6 == "find first aid kit":
           print ("Show the first aid kit to people. Do they know it?")
           time.sleep(1)
           print ("\n1.Y")
           print("2. N")
           firstAid()
        elif choice6=="2" or choice6=="ignore them":
            time.sleep(2)
            choice6 = input("\nToo bad. You need to cure people. \n1. Find first aid kit. \n2. Quit \n\nUser: ")
            if choice6 == "quit" or choice6 == "2" or choice6=="ignore them":
                exit(0)
        else:
            print("\nInvalid Input")
            time.sleep(1)
            choice6 = input("User: ")

    
def darkPatch():
    time.sleep(2)
    print ("Are those dark patches on people's face?")
    time.sleep(1)
    print ("\n1.Y")
    print ("2. N")
    
    choice4 = (str(input("\nUser: ")).lower())

    while (choice4 != "y" or choice4 != "n"):    
        if choice4 == "y" or choice4 == "1":
            print ("\nThey have a disease")
            time.sleep(2)
            print ("You need to cure the people first")
            cure()
        elif choice4=="n" or choice4=="2":
            print ("\nThey are good and can help.")
            time.sleep(2)
            print ("Can people help us repair the ship?")
            time.sleep(1)
            print ("\n1.Y")
            print ("2. N")
            
            choice5= (str(input("\nUser: ")).lower())
                                      
            if choice5 == "y" or choice5=="1":
                break

            else:
                print ("\nWe must repair the ship to cure the citizens of Planet X on Planet Earth.")
                print ("Please come to ship to repair and bring resources in exchange we will heal the citizens of Planet X.")
        else:
            print("\nInvalid Input")
            time.sleep(1)
            choice4 = input("User: ")
        repairShip()
    

def outside():
    time.sleep(2)
    print ("\nThere are people outside of the ship.")
    time.sleep(1)
    print("\n1.Picks to speak to people to find out what happened")
    print("2. Start repairing the ship")
    
    choice3 = (str(input("\nUser: ")).lower())
    
    while (choice3 != "1" or choice3 != "2"):
        if (choice3 == "1" or choice3 == "picks to speak to people to find out what happened"):
            time.sleep(2)
            print("\nYou find out that they have resources that are needed, also find out that they are sick.")
            time.sleep(2)
            print ("\nAtmosphere is interacting with their health.")

            darkPatch()

        elif choice3=="2" or choice3=="start repairing the ship":
            time.sleep(1)
            print ("\nYou chose to repair the ship first.")
            time.sleep(1)
            print ("\nBut you need people's help to repair the ship.")
            time.sleep(1)
            print("\n1.Picks to speak to people to find out what happened")
            print("2. Start repairing the ship")
            
            choice3 = (str(input("\nUser: ")).lower())
        else:
            print("\nInvalid Input")
            time.sleep(1)
            choice3 = input("User: ")
            
    
def ship():
    time.sleep(2)
    print ("\nYou wake up. But the only thing you remember last was leaving earth.")
    time.sleep(2)
    print ("\nYou look outside the rocket ship window, and see that you have arrived in a unknown planet in your journey to planet Mars.")
    time.sleep(2)
    print ("\nAre you ready for what’s next? Do you want to go outside to investigate or check what’s wrong with the ship?")
    time.sleep(2)
    print ("\n1. Go outside")
    print ("2. Check ship")

    choice2 = (str(input("\nUser: ")).lower())

    while (choice2 != "1" or choice2 != "2"):            
        if choice2 == "1" or choice2 == "go outside":
            time.sleep(2)
            print("\nChoose what will you do outside.")
            break            
        elif choice2 == "2" or choice2 == "check ship":
            time.sleep(1)
            print("\nThere is nothing in the ship.")
            time.sleep(2)
            choice2 = input("\nYou need to go outside to find out something more. \n1. Go outside \n2. Quit \n\nUser: ")
            if choice2 == "1" or choice2 == "go outside":
                outside()
            elif choice2 == "2" or choice2 == "quit":
                quit(0)
            else:
                choice2 = input ("Invalid input")
        else:
            print("\nInvalid Input")
            time.sleep(1)
            choice2 = input("User: ")
    outside()
            

def start(inv):
    time.sleep(1)
    print ("\nSpaceX has sent you on a mission to go to Mars.")
    time.sleep(1)
    print ('Are you ready?')
    time.sleep(1)
    print ("\n1. Y")
    print ("2. N")


    choice =(str(input("\nUser: ")).lower())
    time.sleep(1)
    while (choice != "1" or choice != "y" or choice != "2" or choice != "n"):
        if choice == "1" or choice == "y":
            print ("\nYou prepare through intense training, it is May 1st, the mission is ON.")
            break
        elif choice == "2" or choice == "n":
            choice = input ("\nYou end up having cancer and die in planet earth. \n1.Restart \n2.Quit \n\nUser: ")
            if choice == "quit" or choice=="2":
                exit(0)
                break
            else:
                start(inv)
        else:
            print ("Invalid input")
            return start(inv)
    ship()
    
def name():
    time.sleep(1)
    print ("------------------------------------------------------------------------------------------------------------")
    time.sleep(1)
    print ("Title: Planet X")
    time.sleep(1)
    print ("Author: Christina G., Yoonju H., Miaodan X.")
    time.sleep(1)
    print ("------------------------------------------------------------------------------------------------------------")
    time.sleep(1)
    print ("\n *WRITE ALL ANSWERS IN NUMBER*")
    

def main():
    name()
    inv=[' ']
    start(inv)
main()
