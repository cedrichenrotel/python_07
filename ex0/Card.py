#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Card.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/20 13:04:01 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/31 08:45:36 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    COMMON = 'Common'
    RARE = 'Rare'
    LEGENDARY = 'Legendary'


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: Rarity,
                 type: str) -> None:
        if not isinstance(name, str) or name == "":
            raise ValueError(f"Class Card -> name: {name}")
        if not isinstance(cost, int) or cost <= 0:
            raise ValueError(f"Class Card -> cost: {cost}")
        if not isinstance(rarity, Rarity):
            raise ValueError("rarity must be a Rarity enum value")

        self.name = name
        self.cost = cost
        self.rarity = rarity.value
        self.type = type

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
            }

    def is_playable(self, available_mana: int) -> bool:
        if isinstance(available_mana, int) is False or available_mana < 0:
            raise ValueError("init mana cannot be a negative value")
        return available_mana >= self.cost
