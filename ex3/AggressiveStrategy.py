# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  AggressiveStrategy.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 14:53:22 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/25 19:05:21 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        total_cost = 9
        cost_used = 0
        card = []
        hand_sorted = sorted(hand, key=lambda x: x.cost)
        for item in hand_sorted:
            if total_cost >= item.cost:
                card.append(item)
                total_cost -= item.cost
                cost_used += item.cost


        result = {
            'cards_played': card.name,
            'mana_used': cost_used,
            'targets_attacked':
        }
        return result

    def get_strategy_name(self) -> str:
        return 'AggressiveStrategy'
    
    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets