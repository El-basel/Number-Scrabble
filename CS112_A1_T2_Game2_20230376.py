# File: CS112_A1_T2_Game2_20230376
# purpose: The game starts with a list of numbers form 1 to 9 and there are two players,
# each player chooses a number from the list and try to make a sum of three numbers to equal 15 to win
# Author: Mahmoud Mohamed El-Basel
# ID: 20230376

# the main area of selection
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# inventory for each player
p1_picked = []
p2_picked = []


# sum of every combination of three numbers
def sumOfThree(player):
    for i in range(0, len(player)):
        for j in range(i+1, len(player)):
            for k in range(j+1, len(player)):
                if player[i] + player[j] + player[k] == 15:
                    return True
    return False


def getNumber(turn):
    # check whose turn to print a different text based on the player turn
    if turn == 1:
        num = input("Player 1 turns: ")
        # validate that the entered number contains digits only
        while not num.isdigit():
            print("please enter a number between 1 and 9")
            num = input("Player 1 turns: ")
    else:
        num = input("Player 2 turns: ")
        # validate that the entered number contains digits only
        while not num.isdigit():
            print("please enter a number between 1 and 9")
            num = input("Player 2 turns: ")

    return int(num)


# control of player 1
def player1():
    num = getNumber(1)
    # remove the chosen number form the selection area and add it to the player inventory
    while True:
        if num in numbers:
            numbers.remove(num)
            p1_picked.append(num)
            break
        elif num == 0:
            print("please enter a number between 1 and 9")
            num = getNumber(1)
        else:
            # if the number has been picked before ask for another number
            print("this number has been picked, please select another number")
            num = getNumber(1)
    # start the summation when the inventory reaches 3 elements
    if len(p1_picked) >= 3:
        if sumOfThree(p1_picked):
            print("Player 1 wins!")
            return True
    return False


# control of player 2
def player2():
    num = getNumber(2)
    # remove the chosen number form the selection area and add it to the player inventory
    while True:
        if num in numbers:
            numbers.remove(num)
            p2_picked.append(num)
            break
        elif num == 0:
            print("please enter a number between 1 and 9")
            num = getNumber(2)
        else:
            # if the number has been picked before ask for another number
            print("this number has been picked, please select another number")
            num = getNumber(2)
    # start the summation when the inventory reaches 3 elements
    if len(p2_picked) >= 3:
        if sumOfThree(p2_picked):
            print("Player 2 wins!")
            return True
    return False


def main():
    print("Welcome to the ** Number Scrabble **")
    print("each player will choose a number between 1 and 9")
    print("if a player has picked three numbers that add up to 15, that player wins the game")

    while True:
        winner = player1()
        if winner:
            break
        # check if the main selection area reached 0 and no player won then declare draw
        if len(numbers) == 0:
            print("draw")
            return
        winner = player2()
        if winner:
            break
        # check if the main selection area reached 0 and no player won then declare draw
        if len(numbers) == 0:
            print("draw")
            return


main()
