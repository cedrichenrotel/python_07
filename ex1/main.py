#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/23 14:02:06 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/23 19:10:29 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard


def main() -> None:

    print("=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")

    try:
        lightning = SpellCard('Lightning Bol', 3, 'Common', 'Spell',
                              'Deal 3 damage to target')
        crystal = SpellCard('Mana Crystal', 2, 'Rarity', 'Artifact',
                            'Permanent: +1 mana per turn')
        dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 'Creature', 7, 5)
    except (AttributeError, ValueError) as e:
        print(f"SpellCard [KO]: {e}")
        return
    print("\nDrawing and playing cards:")
    print(f"\nDrew: {lightning.name} ({lightning.type})")
    print(f"Play result: {lightning.play({})}")

    print(f"\nDrew: {crystal.name} ({crystal.type})")
    print(f"Play result: {crystal.play({})}")

    print(f"\nDrew: {dragon.name} ({dragon.type})")
    print(f"Play result: {dragon.play({})}")


if __name__ == "__main__":
    main()
