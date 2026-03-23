#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  CreatureCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/20 13:12:10 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/23 13:26:32 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, type: str,
                 attack: int, health: int) -> None:

        if isinstance(attack, int) is False:
            raise AttributeError(f"Class CreatureCard -> {attack}")
        elif attack <= 0:
            raise ValueError(f"Class CreatureCard -> {attack}")

        if isinstance(health, int) is False:
            raise AttributeError(f"Class CreatureCard -> {health}")
        elif health <= 0:
            raise ValueError(f"Class CreatureCard -> {health}")

        super().__init__(name, cost, rarity)
        self.type = type
        self.attack = attack
        self.health = health

    def get_card_info(self) -> dict:
        card_info = {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'type': self.type,
            'attack': self.attack,
            'health': self.health
            }
        return card_info

    def play(self, game_state: dict) -> dict:
        game_state = {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
            }
        return game_state

    def attack_target(self, target: str) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True
            }
