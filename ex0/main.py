#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/20 13:12:47 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/31 08:41:02 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity


def main() -> None:
    print("=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")
    print("\nCreatureCard Info:")
    try:
        goblin = CreatureCard('Goblin Warrior', 7, Rarity.COMMON,
                              'Creature', 3, 3)
        dragon = CreatureCard('Fire Dragon', 5, Rarity.LEGENDARY,
                              'Creature', 7, 5)
    except (AttributeError, ValueError) as e:
        print(f"[ERROR] CreateCard: {e}")
        return

    print(dragon.get_card_info())

    try:
        mana = 6
        print(f"\nPlaying {dragon.name} with {mana} mana available:")
        if dragon.is_playable(mana) is False:
            print(f"Playable: {dragon.is_playable(mana)}")
        else:
            print(f"Playable: {dragon.is_playable(mana)}")
            print(f"Play result: {dragon.play({})}")
    except (AttributeError, ValueError) as e:
        print(f"[KO] mana:{mana} -> {e}")
        return

    print(f"\n{dragon.name} attacks {goblin.name}:")
    try:
        print(f"Attack result: {dragon.attack_target(goblin.name)}")
    except ValueError as e:
        print(f"[ERROR] attack_target: {e}")

    print("\nTesting insufficient mana (3 available):")
    try:
        mana = 3
        if dragon.is_playable(mana) is False:
            print(f"Playable: {dragon.is_playable(mana)}")
        else:
            print(f"Playable: {dragon.is_playable(mana)}")
            print(f"Play result: {dragon.play({})}")
    except (AttributeError, ValueError) as e:
        print(f"[KO] mana:{mana} -> {e}")
        return

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
