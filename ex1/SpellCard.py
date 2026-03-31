#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  SpellCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/23 13:59:51 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/31 09:33:45 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex0.Card import Rarity


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity,
                 type: str, effect_type: str) -> None:

        if not isinstance(effect_type, str) or effect_type == "":
            raise ValueError(f"Class SpellCard -> effect_type: {effect_type}")

        super().__init__(name, cost, rarity, type)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        game_state = {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect_type
        }
        return game_state

    def resolve_effect(self, targets: list) -> dict:
        if not isinstance(targets, list) or targets == []:
            raise ValueError(f"resolve_effect: {targets}")

        attack_result = {
            'attack': self.name,
            'target': targets,
            'damage': self.effect_type
        }
        return attack_result
