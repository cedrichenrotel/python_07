# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentPlatform.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/27 15:02:41 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/27 17:50:09 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from TournamentCard import TournamentCard


class TournamentPlatform():
    def __init__(self, name: str, cost: int, rarity: str, type: str,
                 power: int, health: int) -> None:
        if not isinstance(name, str) or name == "":
            raise ValueError(f"Class Card -> name: {name}")
        elif not isinstance(cost, int) or cost <= 0:
            raise ValueError(f"Class Card -> cost: {cost}")
        
    def register_card(self, card: TournamentCard) -> str:
        pass

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        pass

    def get_leaderboard(self) -> list:
        pass

    def generate_tournament_report(self) -> dict:




# def play(self, game_state: dict) -> dict:
#         result = {
#             'winner': game_state['winner_card'], #state du combats
#             'loser': game_state['loser_card'],
#             'winner_rating': game_state['winner_rathing'],
#             'loser_rating': game_state['loser_rating']
#         }
#         return result