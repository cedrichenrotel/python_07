# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 16:46:43 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/30 19:35:15 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard


def main() -> None:
    try:
        player1 = EliteCard('Arcane Warrior', 1, "common", "adventurer", 5, 3,
                            10)
        goblin = CreatureCard('Goblin Warrior', 7, 'Common', 'Creature', 3, 3)
        dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 'Creature', 7, 5)
        fire_ball = SpellCard('Fire Ball', 3, 'Common', 'Spell',
                              'Deal 3 damage to target')
    except ValueError as e:
        print(f"ERROR: Initialion player [KO]: {e}")

    methode_card = [m for m in dir(Card) if not m.startswith('_')]
    methode_combatable = [m for m in dir(Combatable) if not m.startswith('_')]
    methode_magical = [m for m in dir(Magical) if not m.startswith('_')]

    print("=== DataDeck Ability System ===")
    print("\nEliteCard capabilities:")
    print(f"- Card: {methode_card}\n"
          f"- Combatable: {methode_combatable}\n"
          f"- Magical: {methode_magical}")

    print("\nPlaying Arcane Warrior (Elite Card):")

    print("\nCombat phase:")
    print(f"Attack result: {player1.attack(goblin.name)}")
    print(f"Defense result:{player1.defend(goblin.attack)}")

    print("\nMagic phase:")
    print(f"Spell cast: {player1.cast_spell(fire_ball.name,
                                            [goblin.name, dragon.name])}")
    print(f"Mana channel: {player1.channel_mana(2)}")
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
