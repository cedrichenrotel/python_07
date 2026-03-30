# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentPlatform.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/27 15:02:41 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/30 13:34:06 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex4.TournamentCard import TournamentCard


class TournamentPlatform():
    def __init__(self) -> None:
        self.lst_matches = []
        self.cards = {}

    def register_card(self, card: TournamentCard) -> str:
        id = card.name + '_' + str(len(self.cards))
        self.cards[id] = card
        return id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.power > card2.power:
            winner = card1
            winner_id = card1_id
            loser = card2
            loser_id = card2_id
        else:
            winner = card2
            winner_id = card2_id
            loser = card1
            loser_id = card1_id

        winner.update_wins(1)
        loser.update_losses(1)

        result = {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner.calculate_rating(),
            'loser_rating': loser.calculate_rating()
        }
        self.lst_matches.append(result)
        return result

    def get_leaderboard(self) -> list:
        result = sorted(self.cards.values(), key=lambda x: x.rating,
                        reverse=True)
        return result

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)
        matches_played = len(self.lst_matches)
        total = 0
        for i in self.cards.values():
            total += i.rating
        avg_rating = total / total_cards
        result = {
            'total_cards': total_cards,
            'matches_played': matches_played,
            'avg_rating': avg_rating,
            'platform_status': 'active'
        }
        return result
