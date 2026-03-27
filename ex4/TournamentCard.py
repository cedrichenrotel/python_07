# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentCard.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/27 13:54:29 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/27 15:23:56 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, type: str,
                 power: int, health: int) -> None:
        if not isinstance(name, str) or name == "":
            raise ValueError(f"Class Card -> name: {name}")
        elif not isinstance(cost, int) or cost <= 0:
            raise ValueError(f"Class Card -> cost: {cost}")

        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.type = type
        self.power = power
        self.health = health
        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def play(self, game_state: dict) -> dict:
        game_state = {'available_mana': 6}
        if self.cost <= game_state['available_mana']:
            result = {
                'Card_player': self.name,
                'Cost': self.cost,
                'Rarity': self.rarity,
                'Type': self.type,
                'Attack': self.power,
                'Health': self.health
            }
            return result
        else:
            return {'Echec': 'Insufficient mana '}

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            'type': self.type,
            'attack': self.power,
            'health': self.health
            }

    def is_playable(self, available_mana: int) -> bool:
        if isinstance(available_mana, int) is False or available_mana < 0:
            raise ValueError("init mana cannot be a negative value")
        return available_mana >= self.cost

    def attack(self, target) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass

    def calculate_rating(self) -> int:
        pass

    def get_tournament_stats(self) -> dict:
        pass

    def update_wins(self, wins: int) -> None:
        pass

    def update_losses(self, losses: int) -> None:
        pass

    def get_rank_info(self) -> dict:
        pass
