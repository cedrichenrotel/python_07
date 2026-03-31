#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ArtifactCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/23 14:00:20 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/31 09:14:36 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex0.Card import Rarity


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity, type: str,
                 durability: int, effect: str) -> None:

        if not isinstance(durability, int) or durability <= 0:
            raise ValueError(f"Class ArtifactCard -> durability: {durability}")
        elif not isinstance(effect, str) or effect == "":
            raise ValueError(f"Class ArtifactCard -> effect: {effect}")

        super().__init__(name, cost, rarity, type)
        self.dura = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
            raise TypeError(f"{game_state} is not 'dict'")
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
