"""
Cho-han is a dice game played in gambling
houses of feudal Japan. Two six-sided dice
are rolled in a cup, and gamblers must guess
if the sum is even (cho) or odd (han). The
house takes a small cut of all winnings.

"""

import random


def roll_a_dice():
    return random.randint(1, 6)


def main():
    print("How much money you want to play with for tonight")
    purse = int(input("> "))
    
    house_fee = 0
    house_bet = 0
    while(purse>0):
        print("Enter the bet amount")
        bet = int(input("> "))

        if (purse - bet) < 0:
            print("You dont have enough money to bet")
            break
        
        print("Rolling dices in a cup")
        dice1 = roll_a_dice()
        dice2 = roll_a_dice()
        sum = dice1 + dice2

        print("CHO (even) or HAN (odd)?")
        cho_han = input("> ")

        if cho_han.lower() not in ("cho", "han"):
            print("Input should be CHO or HAN. {} is bad input, you lost the bet".format(cho_han))
            exit(1)
        else:
            even_or_odd = sum % 2
            if (cho_han.lower()=="cho" and not even_or_odd) or (cho_han.lower()=="han" and even_or_odd) :
                print("Dice values are: {} and {}".format(dice1, dice2))
                print("You have won, your price money: {}".format(bet*2))
                print("House fee is: {:.2f}".format(0.1 * bet))
                house_fee += 0.1 * bet
                purse += bet - 0.1 * bet
                house_bet -= bet
            else:
                print("Dice values are: {} and {}".format(dice1, dice2))
                print("You have lost")
                purse -= bet
                house_bet += bet
        
        if purse:
            print("Do you want to continue? ")
            print("Amount in the purse: {:.2f}".format(purse))
            cnt = input("> y/n :")
            if cnt.lower() == "y":
                continue
            else: 
                break
        
        
    print("Game ended")
    print("Your left out amount is: {:.2f}".format(purse))
    print("House has won: {:.2f}".format(house_bet))
    print("House fee: {}".format(house_fee))

if __name__ == "__main__":
    main()