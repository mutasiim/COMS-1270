import random

def playgame():
    # Input: Number of human players
    humanplayer = int(input("How Many Human Players [1] - [4]?: "))
    total_players = 4  # Total number of players (some human, some AI)
    cardcopy = int(input("How Many Copies Of Each Card [1] - [5]?: "))

    # Initialize the pathway and deck
    cardlist = ['M', 'R', 'B', 'C', 'G', 'Y']
    pathway = []
    for char in cardlist:
        for _ in range(cardcopy):
            pathway.append(char)

    random.shuffle(pathway)
    print(f"\nSTART {pathway} GOAL!")

    cards = pathway.copy()
    random.shuffle(cards)
    print(f"\nCARDS {cards}\n")

    # Track each player's position
    player_positions = {f'Player {i+1}': 0 for i in range(total_players)}

    # Game loop
    current_card_index = 0
    while current_card_index < len(cards):
        for i in range(total_players):
            player_name = f'Player {i+1}'
            currentpos = player_positions[player_name]

            # Check if the player has already reached the goal
            if currentpos >= len(pathway) - 1:
                print(f"\n{player_name} has reached the end of the pathway and wins!")
                return

            card = cards[current_card_index]

            # Determine if the current player is human or AI
            is_human = i < humanplayer
            if is_human:
                # Human player's turn
                print(f"\n{player_name}'s turn!")
                print(f"Would you like to [d]raw a {card} card, [s]huffle the deck, or [q]uit?: ")
                choice = input().lower()

                if choice == 'd':  # Draw a card
                    if card in pathway[currentpos:]:
                        move_forward = pathway[currentpos:].index(card)
                        player_positions[player_name] += move_forward
                        print(f"\n{player_name} has drawn {card}")
                        print(f"{player_name} moves forward to position {player_positions[player_name] + 1}")
                    else:
                        print("\nThe drawn card does not match any position ahead.")
                elif choice == 's':  # Shuffle the deck
                    random.shuffle(cards)
                    print("\nThe deck has been shuffled.")
                    print(f"New deck: {cards}")
                elif choice == 'q':  # Quit the game
                    print(f"\n{player_name} has quit the game.")
                    return
                else:
                    print("\nInvalid choice. Please choose again.")
            else:
                # AI player's turn
                print(f"\n{player_name}'s turn! (AI-controlled)")
                if card in pathway[currentpos:]:
                    move_forward = pathway[currentpos:].index(card)
                    player_positions[player_name] += move_forward
                    print(f"{player_name} has drawn {card}")
                    print(f"{player_name} moves forward to position {player_positions[player_name]}")
                else:
                    print(f"{player_name} skips the turn as the card does not match any position ahead.")

            # Move to the next card
            current_card_index += 1

            # Check if the card deck is exhausted
            if current_card_index >= len(cards):
                print("\nThe deck of cards is exhausted. The game ends in a draw!")
                return

# Instructions
def instruction():
    print("Here are the instructions for the game:")
    print("1. There are 4 players in total (some human, some AI).")
    print("2. You can choose how many human players participate; the rest will be computers.")
    print("3. Each player takes turns drawing cards or shuffling the deck.")
    print("4. Move forward according to the card you draw.")
    print("5. The first player to reach the end of the pathway wins!")
    print("ENJOY!")
    candy()

# Main Menu
def candy():
    mode = input("MAIN MENU: [p]lay game, [i]nstructions, or [q]uit?: ").lower()
    while mode not in ('p', 'i', 'q'):
        print("Please enter a valid input.")
        mode = input("MAIN MENU: [p]lay game, [i]nstructions, or [q]uit?: ").lower()

    if mode == 'p':
        playgame()
    elif mode == 'i':
        instruction()
    elif mode == 'q':
        print("Goodbye!")

# Run the game
candy()