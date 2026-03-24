#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ArtifactCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/23 14:00:20 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/24 09:54:20 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, type: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity, type)
        self.dura = durability
        self.effect = effect

    def play(self, game_state) -> dict:
        game_state = {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect
        }
        return game_state

    def activate_ability(self) -> dict:
        effect_art = {
            'card_played': self.name,
            'effect': self.effect,
            'durability': self.dura
        }
        return effect_art
