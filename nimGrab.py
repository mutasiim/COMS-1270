# Mohammad Mu Tasim Chowdhury              10-11-2024
# Assignment #3
# This game is called NIMGRAB, a classic game of NIM with 2 players

global action
def Game():
    
    print("NIMGRAB!")
    print(" ")
    print("By: Mohammad Mu Tasim Chowdhury")
    print("[COM S 127 1]")

    global action
    import random 

    count = 0
    global itemtotal 
    itemtotal = random.randrange(20, 25)

    def rules():
        print(" ")
        print("NIMGRAB is a 2 player game or can be played against computer.")
        print("There are 20 - 25 number of items placed in a row.")
        print("Each player takes turn and removes a number of items from 1 - 3.")
        print("The player who takes the last time loses.")
        print("HAVE FUN PLAYING!")

    def AIPlay():
        global itemtotal
        itemtotal = random.randrange(20, 25) 
        print(f"Items left: {itemtotal}")
        print("|" * itemtotal)
        while itemtotal > 0:
            playertake = int(input("How many items do you want to take [1-3]?: "))
            while (playertake < 1) or (playertake > 3):
                print("ERROR: Invalid choice. Please choose again.")
                playertake = int(input("How many items do you want to take [1-3]?: "))

            itemtotal = itemtotal - playertake
            if itemtotal == 0:
                print("Human took the last item. Computer wins!")
                break

            if itemtotal > 3:
                comptake = random.randrange(1, 4)
            else:
                if itemtotal == 3:
                    comptake = 2
                elif itemtotal == 2:
                    comptake = 1
                elif itemtotal == 1:
                    comptake = 1

            print(f"Computer takes: {comptake}")
            itemtotal = itemtotal - comptake
            if itemtotal == 0:
                print("Computer took the last item. Human wins!")
                break

            print(f"Items left: {itemtotal}")
            print("|" * itemtotal)

    def Humanplay():
        global itemtotal
        itemtotal = random.randrange(20, 25)  
        playerturn = 1
        print(f"Items left: {itemtotal}")
        print("|" * itemtotal)
        while itemtotal > 0:
            if playerturn == 1:
                playerinput = int(input("Player 1, How many items do you want to take [1-3]?: "))
            else:
                playerinput = int(input("Player 2, How many items do you want to take [1-3]?: "))

            while playerinput < 1 or playerinput > 3:
                print("ERROR: Invalid choice. Please choose again.")
                playerinput = int(input(f"Player {playerturn}, How many items do you want to take [1-3]?: "))

            itemtotal = itemtotal - playerinput
            if itemtotal == 0:
                print(f"Player {playerturn} took the last item. Player {3 - playerturn} wins.")
                break

            print(f"Items left: {itemtotal}")
            print("|" * itemtotal)

            playerturn = 3 - playerturn  

    while True:  
        action = input("Do you want to [p]lay, read the [r]ules, or [q]uit?: ")

        while (action != "p") and (action != "r") and (action != "q"):
            action = input("Do you want to [p]lay, read the [r]ules, or [q]uit?: ")

        if action == "p":
            player = input("Do you want to play against [h]uman or [c]omputer?: ")
            while (player != "h") and (player != "c"):
                player = input("Do you want to play against [h]uman or [c]omputer?: ")
            
            if player == "h":
                Humanplay()

            elif player == "c":
                AIPlay()
        
        elif action == "r":
            rules()

        elif action == "q":
            print("Goodbye!")
            break  
        
Game()