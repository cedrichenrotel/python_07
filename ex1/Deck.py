#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Deck.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/23 14:00:55 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/31 09:57:01 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
import random
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck():
    def __init__(self) -> None:
        self.lst_deck: list[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("add_card typing error")
        self.lst_deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        if not isinstance(card_name, str) or card_name == "":
            raise ValueError("remove_card error")
        for item in self.lst_deck:
            if item.name == card_name:
                self.lst_deck.remove(item)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.lst_deck)

    def draw_card(self) -> Card:
        if len(self.lst_deck) <= 0:
            raise ValueError(f"draw_card -> {len(self.lst_deck)}")
        return self.lst_deck.pop(0)

    def get_deck_stats(self) -> dict:
        card_total = len(self.lst_deck)
        creature, spell, artifact, total_cost = 0, 0, 0, 0

        if card_total == 0:
            raise ZeroDivisionError("get_deck_stats: total_cost <= 0")

        for item in self.lst_deck:
            if isinstance(item, CreatureCard):
                creature += 1
            elif isinstance(item, SpellCard):
                spell += 1
            elif isinstance(item, ArtifactCard):
                artifact += 1
            total_cost += item.cost
        avg_cost = float(total_cost / card_total)

        deck_stats = {
            'total_cards': card_total,
            'creatures': creature,
            'spells': spell,
            'artifacts': artifact,
            'avg_cost': avg_cost
        }
        return deck_stats
