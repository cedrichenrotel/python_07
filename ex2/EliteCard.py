# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  EliteCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 16:43:05 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/31 11:36:23 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex0.Card import Rarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: Rarity, type: str,
                 health: int, power: int, mana: int) -> None:

        if not isinstance(power, int) or power <= 0:
            raise ValueError(f"EliteCard -> power: {power}")
        elif not isinstance(health, int) or health <= 0:
            raise ValueError(f"EliteCard -> defense: {health}")
        elif not isinstance(mana, int) or mana <= 0:
            raise ValueError(f"EliteCard -> mana: {mana}")

        super().__init__(name, cost, rarity, type)
        self.health = health
        self.power = power
        self.mana = mana

    def get_combat_stats(self) -> dict:
        result = {
            'card_player': self.name,
            'health': self.health,
            'power': self.power,
            'mana': self.cost
        }
        return result

    def attack(self, target: str) -> dict:
        if not isinstance(target, str):
            raise TypeError(f"attack: target: {target} is not Card")
        result = {
            'attacker': self.name,
            'target': target,
            'damage': self.power,
            'combat_type': 'melee'
        }
        return result

    def defend(self, incoming_damage: int) -> dict:
        if not isinstance(incoming_damage, int):
            raise TypeError(f"defend: incoming_damage is not int -> "
                            f"{incoming_damage}")
        damage_blocked = min(self.health, incoming_damage)

        result = {
            'defender': self.name,
            'damage_blocked': damage_blocked,
            'damage_taken': incoming_damage,
            'still_alive': self.health > incoming_damage
        }
        return result

    def get_magic_stats(self) -> dict:
        result = {
            'total_mana': self.mana
        }
        return result

    def channel_mana(self, amount: int) -> dict:
        if self.mana + amount > 10:
            self.mana = 10
        else:
            self.mana += amount

        result = {
            'channeled': amount,
            "total_mana": self.mana
        }
        return result

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if not isinstance(spell_name, str) or spell_name == "":
            raise TypeError(f"cast_spell: {spell_name}")
        if not isinstance(targets, list) or targets == []:
            raise TypeError(f"cast_spell: {targets}")

        mana_used = 4
        if self.mana - mana_used < 0:
            spell_name = "[Echec] - insufficient mana points"
            mana_used = 0
        else:
            self.mana -= mana_used

        result = {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': mana_used
        }
        return result

    def play(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
            raise TypeError(f"play: {game_state} is not dict")
        good_key = [
            'target',
            'incoming_damage',
            'spell_name',
            'targets'
        ]
        for key in good_key:
            if key not in game_state:
                raise KeyError(f"play: {key} wrong keys")
        result = {
            'attack': self.attack(game_state['target']),
            'defense': self.defend(game_state['incoming_damage']),
            'spell': self.cast_spell(game_state['spell_name'],
                                     game_state['targets'])
        }
        return result

    def is_playable(self, available_mana: int) -> bool:
        if isinstance(available_mana, int) is False or available_mana < 0:
            raise ValueError("init mana cannot be a negative value")
        return available_mana >= self.cost

    def get_card_info(self) -> dict:
        info_base = super().get_card_info()
        info_elite = {
            'health': self.health,
            'power': self.power,
            'defense': self.health,
            'mana': self.mana
        }
        return {**info_base, **info_elite}
