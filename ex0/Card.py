#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Card.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/20 13:04:01 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/23 13:40:03 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if isinstance(cost, int) is False:
            raise AttributeError(f"Class Card -> {cost}")
        elif cost <= 0:
            raise ValueError(f"Class Card -> {cost}")
        self.name = name
        self.cost = cost
        self.rarity = rarity

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
