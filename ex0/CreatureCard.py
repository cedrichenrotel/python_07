# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  CreatureCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/20 13:12:10 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/31 09:02:38 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex0.Card import Rarity


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity, type: str,
                 attack: int, health: int) -> None:

        if not isinstance(attack, int) or attack <= 0:
            raise ValueError(f"Class CreatureCard -> {attack}")

        if not isinstance(health, int) or health <= 0:
            raise ValueError(f"Class CreatureCard -> {health}")

        super().__init__(name, cost, rarity, type)
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
        if target is None:
            raise ValueError(f"target is {target}")
        elif not isinstance(target, str) or target == "":
            raise ValueError(f"target is not string: {target}")
        result = {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True
            }
        return result
