# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1, 2)
    print("Human plays first={0},  winner={1} "
          .format(human_plays_first, result))
    return result

def play_many(human_score,computer_score,draws,counter):
    result = play_once(counter)
    if counter == True:         # Players take turns to play first
        counter = False
    else:
        counter = True
    if result == -1:            # Check if human wins, add score
        print("I win!")
        human_score += 1
    elif result == 1:           # Check if computer wins, add score
        print("You win!")
        computer_score += 1
    else:                       # Draw, add score
        print("Game drawn!")
        draws += 1
    print("Human wins: ", human_score)          #
    print("Computer wins: ", computer_score)    # Display scores
    print("Draws: ", draws)                     #
    print("Percentage of human wins:",human_score/(human_score+computer_score+draws)*100, "%")
    response = input("Do you want to play again?")      # Ask if player wants to play again
    if response == "yes":
        play_many(human_score,computer_score,draws,counter)
    else:
        print("Goodbye")


play_many(0,0,0,True)


