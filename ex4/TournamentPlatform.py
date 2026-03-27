# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentPlatform.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/27 15:02:41 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/27 15:03:34 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def play(self, game_state: dict) -> dict:
        result = {
            'winner': game_state['winner_card'], #state du combats
            'loser': game_state['loser_card'],
            'winner_rating': game_state['winner_rathing'],
            'loser_rating': game_state['loser_rating']
        }
        return result