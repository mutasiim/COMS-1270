# Mohammad Mu Tasim Chowdhury  11-22-2024
# Assignment 5

# This game is called 'Candy Realm!', a similar version to the classic board game 'Candy Land'

print("Candy Realm!")
print("By: Mohammad Mu Tasim Chowdhury")
print("[COM S 127 1]")

import random

def playgame():
    humanplayer = int(input("How Many Human Players [1] - [4]?: "))
    AI = 4 - humanplayer
    players = ['Human'] * humanplayer + ['Computer'] * AI
    cardcopy = int(input("How Many Copies Of Each Card [1] - [5]?: "))
    cardlist = ['M','R','B','C','G','Y']
    pathway = []
    print(players)
    for char in cardlist:
        for i in range(0, cardcopy):
            pathway.append(char)

    random.shuffle(pathway)  # creating the pathway
    print(f'START {pathway} GOAL!')
    cards = pathway.copy()
    random.shuffle(cards)  # creating the deck of cards
    print(f'CARDS {cards}')

    # starting positions for all players
    current_positions = [0] * len(players)

    for card in cards:
        for i in range(len(players)):
            if current_positions[i] >= len(pathway) - 1:
                print(f"Congratulations! {players[i]} {i + 1} has reached the end of the pathway!")
                return

            if players[i] == "Human":
                print(f"{players[i]} {i + 1}'s turn!")
                print(f'Would you like to [d]raw a {card} card, [s]huffle the deck, or [q]uit?: ')
                choice = input()
                if choice == 'd':
                    if card in pathway[current_positions[i]:]:
                        nextpos = pathway[current_positions[i]:].index(card)
                        current_positions[i] += nextpos
                        print(f"You have drawn {card}")
                        print(f"You move forward to position {current_positions[i] + 1}")
                        print(pathway)

                elif choice == 's':
                    random.shuffle(cards)
                    print("Human has shuffled the deck")
                    print(cards)

                elif choice == "q":
                    print("Goodbye!")
                    return

            elif players[i] == "Computer":
                print(f"{players[i]} {i + 1}'s turn!")
                choice = random.choice(['d', 's'])
                if choice == 'd':
                    if card in pathway[current_positions[i]:]:
                        nextpos = pathway[current_positions[i]:].index(card)
                        current_positions[i] += nextpos
                        print(f"Computer has drawn {card}")
                        print(f"Computer moved forward to position {current_positions[i] + 1}")
                        print(pathway)

                elif choice == 's':
                    random.shuffle(cards)
                    print("Computer has shuffled the deck")
                    print(cards)

def instruction():
    print("Here are the instructions for the game:")
    print("1. There are total 4 players in the game")
    print("2. You can choose how many human players can play the game, the rest will be AI")
    print("3. There will be a deck of cards")
    print("4. You can choose to shuffle or pick up a card")
    print("5. Move the character according to the card you receive")
    print("6. The first one to reach the candy castle wins!")
    print("ENJOY!")
    candy()

def candy():
    mode = input("MAIN MENU: [p]lay game, [i]nstructions, or [q]uit?: ")
    while (mode != 'p' and mode != 'i' and mode != 'q'):
        print("Please enter a valid input.")
        mode = input("MAIN MENU: [p]lay game, [i]nstructions, or [q]uit?: ")

    if mode == 'p':
        playgame()
    
    elif mode == 'i':
        instruction()
    
    elif mode == 'q':
        print("Goodbye!")

candy()