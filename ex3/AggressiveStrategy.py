# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  AggressiveStrategy.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 14:53:22 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/26 09:35:36 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        total_cost = 9
        cost_used = 0
        damage_dealt = 0
        card = []
        hand_sorted = sorted(hand, key=lambda x: x.cost)
        for item in hand_sorted:
            if total_cost >= item.cost:
                card.append(item)
                total_cost -= item.cost
                cost_used += item.cost
                if hasattr(item, 'attack'):
                    damage_dealt += item.attack

        result = {
            'cards_played': [x.name for x in card],
            'mana_used': cost_used,
            'targets_attacked': [x.name for x in battlefield],
            'damage_dealt': damage_dealt
        }
        return result

    def get_strategy_name(self) -> str:
        return 'AggressiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets
