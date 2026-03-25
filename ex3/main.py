# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 14:54:34 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/25 17:43:59 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex3.AggressiveStrategy import AggressiveStrategy


try:
    goblin = CreatureCard('Goblin Warrior', 2, 'Common', 'Creature', 3, 3)
    dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 'Creature', 7, 5)
    lightning = SpellCard('Lightning Bolt', 3, 'rarity', 'Spell',
                          'Deal 3 damage to target')
except ValueError as e:
    print(f"Ex3: [ERROR]-> initialisation card [KO]: {e}")

print("=== DataDeck Game Engine ===")
print("\nTurn execution:")
print(f"")
print(f"Strategy: {AggressiveStrategy.get_strategy_name}:")