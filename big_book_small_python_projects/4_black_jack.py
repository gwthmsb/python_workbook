"""
Blackjack, also known as 21, is a card game
where players try to get as close to 21 points
as possible without going over. This program
uses images drawn with text characters, called
ASCII art. American Standard Code for Information
Interchange (ASCII) is a mapping of text characters
to numeric codes that computers used before Unicode
replaced it. The playing cards in this program are an
example of ASCII art:

Rules:
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    In case of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.


"""

from typing import List, Dict
from enum import Enum
from itertools import product, chain
import random

class Suites(Enum):
    HEART = "\u2665"
    DIAMOND = "\u2666"
    SPADE = "\u2660"
    CLUB = "\u2663"

RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

WIN_RATE = 2

def print_card(card: List, is_hole_card=False):
    """
    Print the card, if the hole_card is true, then print the card masked
    card = [Suites.HEART, "Q"]

    Output = 

         _____
        |Q    |
        |  S  |
        |____Q|

        or
         _____
        |##   |
        | ### |
        |___##|

    """

    card_matrix = [[" ", "_", "_", "_", "_", "_", " ",],
                   ["|", "#", "#", " ", " ", " ", "|",],
                   ["|", " ", "#", "#", "#", " ", "|",],
                   ["|", "_", "_", "_", "#", "#", "|",],
                   ]

    def _card(card_matrix):
        for i in card_matrix:
            for j in i:
                print(j, end="")
            print("\n")
    
    if not is_hole_card:
        card_matrix[1][1] = card[1]
        card_matrix[1][2] = " "

        card_matrix[2][2] = " "
        card_matrix[2][3] = card[0].value
        card_matrix[2][4] = " "

        card_matrix[3][4] = "_"
        card_matrix[3][5] = card[1]

    _card(card_matrix)

def card_sum(initial_sum, card):
    if card == 'A':
        initial_sum+=11
    elif card in ['J', 'Q', 'K']:
        initial_sum+=10
    else:
        initial_sum+=card
    return initial_sum

class Player():
    def __init__(self, player_num, bet) -> None:
        self.id = player_num
        self._cards = []
        self._stand_down = False
        self._bust = False
        self.count_21 = 0
        self.bet = bet

    def add_card(self, card):
        if not self._stand_down:
            self._cards.append(card)
            self.count_21 = card_sum(self.count_21, card[1])

            if self.count_21> 21:
                self._bust = True
        
    def down(self):
        self._stand_down = True
    
    def bust(self):
        self._bust = True

    def is_bust(self):
        return self._bust
    
    def is_eligible_to_play(self):
        return not (self._bust or self._stand_down)

    def get_count(self):
        return self.count_21
    
    def check_for_black_jack(self):
        sum = 0
        for c in self._cards:
            card_sum(sum, c[1])

        if sum == 21:
            return True
    
    def double_the_bet(self):
        self.bet *= 2
        self.down()


class Dealer(Player):
    def __init__(self, player_num) -> None:
        super().__init__(player_num, 0)
        self.hole_card = True

    def add_card(self, card):
        if self.count_21 < 17:
            super().add_card(card)
        if self.count_21 >= 17 and self.count_21 <= 21:
            self.down()
        if self.count_21 > 21:
            self.bust()
        
    def reveal_card(self):
        self.hole_card = False
    
    def double_the_bet(self):
        print("Dealer can't double the bet")


class BlackJack():
    def __init__(self, num_of_players=1, bets: Dict= dict()) -> None:
        self.cards_in_the_deck =[c for c in product([Suites.CLUB, Suites.SPADE, Suites.DIAMOND, Suites.HEART], RANKS)]
        self.dealer =  Dealer("Dealer")
        self.players = set(Player(p+1, bets.get(p+1, 10)) for p in range(num_of_players))
        self.total_num_of_players = num_of_players
        self.winners = []
        self._initiate_the_game()
        self.print_the_cards()


    def _deal_a_card(self):
        card = random.choice(self.cards_in_the_deck)
        self.cards_in_the_deck.remove(card)
        return card
    
    def _initiate_the_game(self):
        for _ in [1, 2]:
            for i in chain([self.dealer,], self.players):
                card = self._deal_a_card()
                i.add_card(card)
        for i in self.players:
            if i.check_for_black_jack():
                print(f"Player {i.id} has won the black jack")
                print("Cards are:")
                print_card(i._cards)
                self.winners.append(i)
                exit(0)

    def print_the_cards_for_the_dealer(self, show_hole_card=False):
        print("Cards of the Dealer")
        print_card(self.dealer._cards[0], is_hole_card=not(show_hole_card))
        for c in self.dealer._cards[1:]:
            print_card(c)

    def print_the_cards(self, is_showdown=False):
        if is_showdown:
            self.print_the_cards_for_the_dealer(show_hole_card=True)
        else:
            self.print_the_cards_for_the_dealer()
        print("Cards of the Players")
        for p in self.players:
            print(f"Player{p.id}")
            for c in p._cards:
                print_card(c)
            

    def play_a_round(self) -> bool:
        """
        Return whether round resulted in show down or not
        """

        busted_players = set()
        eligible_players_count = 0
        for player in self.players:
            if player.is_eligible_to_play():
                print(f"(H)it, (S)tand, (D)ouble down for player {player.id}")
                player_input = input()
                if player_input not in ["H", "S", "D", "h", "s", "d", ]:
                    print(f"Invalid input {player_input}. Standing you down")
                    player.down()
                else:
                    if player_input.lower() == "s":
                        player.down()
                    elif player_input.lower() == "h":
                        drawn_card = self._deal_a_card()
                        player.add_card(drawn_card)
                    else:
                        drawn_card = self._deal_a_card()
                        player.add_card(drawn_card)
                        player.double_the_bet()
                if player.is_eligible_to_play():
                    eligible_players_count += 1
                if player.is_bust(): 
                    busted_players.add(player)

        print("Following players lost in this round")
        print([p.id for p in busted_players])
            
        self.players = self.players ^ busted_players
        
        if self.dealer.is_eligible_to_play():
            drawn_card = self._deal_a_card()
            self.dealer.add_card(drawn_card)

        print(f"Eligible player count: {eligible_players_count}")
        return False if eligible_players_count else True
    
    def show_down(self):
        print("Showdown commenced")
        print("Dealer cards are: ") 
               
        self.print_the_cards(is_showdown=True)

        push_back_player = [p for p in self.players if not p.is_bust() and p.get_count() == self.dealer.get_count()]

        if self.dealer.is_bust():
            self.winners.extend([p for p in self.players if not p.is_bust()])
        else:    
            self.winners.extend([p for p in self.players if not p.is_bust() and p.get_count() >= self.dealer.get_count()])
        
        print("Winner of the game are:")

        if push_back_player:
            print("Pushed back players are: ")
            print([p.id for p in push_back_player])


        if not len(self.winners):
            if push_back_player:
                print("No winners, but pushed back")
            else:
                if self.dealer.is_bust():
                    print("Dealer is bust and all the players are bust. Bets pushed back")
                else:
                    print("House take it all")
        else:
            for p in self.players:
                print(f"Player {p.id} has won the amount {p.bet * WIN_RATE}")

            if len(self.players) < self.total_num_of_players:
                print("House also has won")


        exit(0)


def main():
    print("Enter number of players")
    num_of_players = int(input())
    
    bets = {}

    for i in range(1, num_of_players+1):
        print("Enter the bet value for player {}".format(i))
        bet = input()
        bets[i] = int(bet)

    black_jack = BlackJack(num_of_players=num_of_players, bets=bets)
    while(True):
        end_of_the_game = black_jack.play_a_round()
        if end_of_the_game:
            black_jack.show_down()
        else:
            black_jack.print_the_cards()


if __name__ == "__main__":
    main()