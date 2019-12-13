#General rules
#rock beats scissor
#scissor beat paper
#paper beats rock

def win_message(no):
    if no==1:
        print "Player wins"
    else:
        print "Computer wins"
import random
print "Welcome to rock_paper_scissors"
while True:
    print "Enter Choice"
    print "1 Rock"
    print "2 Paper"
    print "3 Scissors"
    player_input = input()
    computer_input = random.randrange(1, 4, 1)
    print "Computer entered ", computer_input
    # if player has rock and computer has scissors
    if (player_input == 1 and computer_input == 3) or (player_input == 3 and computer_input == 2) or (
            player_input == 2 and computer_input == 1):
        win_message(1)
        break
    elif (player_input == 3 and computer_input==1) or (player_input==2 and computer_input==3) or (player_input == 1 and computer_input == 2):
        win_message(2)
        break


