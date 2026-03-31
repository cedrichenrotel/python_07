# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 16:46:43 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/31 11:36:34 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard


def main() -> None:
    try:
        player1 = EliteCard('Arcane Warrior', 1, Rarity.COMMON, "adventurer",
                            5, 3,
                            10)
        goblin = CreatureCard('Goblin Warrior', 7, Rarity.COMMON, 'Creature',
                              3, 3)
        dragon = CreatureCard('Fire Dragon', 5, Rarity.LEGENDARY, 'Creature',
                              7, 5)
        fire_ball = SpellCard('Fire Ball', 3, Rarity.COMMON, 'Spell',
                              'Deal 3 damage to target')
    except ValueError as e:
        print(f"ERROR: Initialion player [KO]: {e}")
        return

    methode_card = [m for m in dir(Card) if not m.startswith('_')]
    methode_combatable = [m for m in dir(Combatable) if not m.startswith('_')]
    methode_magical = [m for m in dir(Magical) if not m.startswith('_')]

    print("=== DataDeck Ability System ===")
    print("\nEliteCard capabilities:")
    print(f"- Card: {methode_card}\n"
          f"- Combatable: {methode_combatable}\n"
          f"- Magical: {methode_magical}")

    print("\nPlaying Arcane Warrior (Elite Card):")

    try:
        print("\nCombat phase:")
        print(f"Attack result: {player1.attack(goblin.name)}")
        print(f"Defense result:{player1.defend(goblin.attack)}")
    except (KeyError, ValueError, TypeError) as e:
        print(f"[ERROR]: {e}")
        return

    print("\nMagic phase:")
    try:
        spell = player1.cast_spell(fire_ball.name, [goblin.name, dragon.name])
        print(f"Spell cast: {spell}")
        print(f"Mana channel: {player1.channel_mana(2)}")
        print("\nMultiple interface implementation successful!")
    except (ValueError, TypeError) as e:
        print(f"[ERROR]: {e}")
        return


if __name__ == "__main__":
    main()
