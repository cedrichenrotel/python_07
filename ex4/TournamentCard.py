# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentCard.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/27 13:54:29 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/27 17:40:53 by cehenrot        ###   ########.fr        #
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

    def attack(self, target: dict) -> dict:
        result = {
            'attacker': self.name,
            'target': target['name'],
            'damage_dealt': self.power,
            'combat_resolved': True
        }
        return result

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = min(self.health, incoming_damage)

        result = {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': damage_blocked,
            'still_alive': self.health > incoming_damage
        }
        return result

    def get_combat_stats(self) -> dict:
        result = {
            'card_player': self.name,
            'health': self.health,
            'power': self.power,
            'mana': self.cost
        }
        return result

    def calculate_rating(self) -> int:
        self.rating = 1200 + (self.wins * 16) - (self.losses * 16)
        return self.rating

    def get_tournament_stats(self) -> dict:
        result = {
            'name': self.name,
            'wins': self.wins,
            'losses': self.losses,
            'rating': self.rating
        }
        return result

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        result = {
            'wins': self.wins,
            'losses': self.losses,
            'rating': self.rating
        }
        return result
