# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  FantasyCardFactory.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 14:53:45 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/26 15:16:08 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard
from ex3.CardFactory import CardFactory
from random import randint, choice


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            return CreatureCard(
                name_or_power,
                randint(1, 10),
                choice(['Common', 'Rare', 'Legendary']),
                'Creature',
                randint(1, 10),
                randint(1, 10)
                )
        elif isinstance(name_or_power, int):
            return CreatureCard(
                choice(["Fire Dragon",
                        "Goblin Warrior",
                        "Ice Wizard",
                        "Lightning Elemental",
                        "Stone Golem",
                        "Shadow Assassin",
                        "Healing Angel",
                        "Forest Sprite"]),
                name_or_power,
                choice(['Common', 'Rare', 'Legendary']),
                'Creature',
                randint(1, 10),
                randint(1, 10)
                )
        else:
            return CreatureCard(
                choice(["Fire Dragon",
                        "Goblin Warrior",
                        "Ice Wizard",
                        "Lightning Elemental",
                        "Stone Golem",
                        "Shadow Assassin",
                        "Healing Angel",
                        "Forest Sprite"]),
                randint(1, 10),
                choice(['Common', 'Rare', 'Legendary']),
                'Creature',
                randint(1, 10),
                randint(1, 10)
                )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            return SpellCard(
                name_or_power,
                randint(1, 10),
                choice(['Common', 'Rare', 'Legendary']),
                'Spell',
                choice(["damage", "heal"])
                )
        elif isinstance(name_or_power, int):
            return SpellCard(
                choice(["Lightning Bolt",
                        "Healing Potion",
                        "Fireball",
                        "Shield Spell",
                        "Meteor",
                        "Ice Shard",
                        "Divine Light",
                        "Magic Missile"]),
                name_or_power,
                choice(['Common', 'Rare', 'Legendary']),
                'Spell',
                choice(["damage", "heal"])
                )
        else:
            return SpellCard(
                choice(["Lightning Bolt",
                        "Healing Potion",
                        "Fireball",
                        "Shield Spell",
                        "Meteor",
                        "Ice Shard",
                        "Divine Light",
                        "Magic Missile"]),
                randint(1, 10),
                choice(['Common', 'Rare', 'Legendary']),
                'Spell',
                choice(["damage", "heal"])
                )

    def create_artifact(self, name_or_power: str | int |
                        None = None) -> Card:
        if isinstance(name_or_power, str):
            return ArtifactCard(
                name_or_power,
                randint(1, 10),
                choice(['Common', 'Rare', 'Legendary']),
                'Artifact',
                randint(1, 3),
                choice([
                    "Permanent: +1 mana per turn",
                    "Permanent: +2 attack to equipped creature",
                    "Permanent: Draw an extra card each turn",
                    "Permanent: +3 health to all friendly creatures",
                    "Permanent: +1 cost reduction to all cards"
                    "Permanent: Cards cost 1 less mana",
                    "Permanent: Creatures have stealth",
                    "Permanent: +1 spell damage"])
                )
        elif isinstance(name_or_power, int):
            return ArtifactCard(
                choice(["Mana Crystal",
                        "Sword of Power",
                        "Ring of Wisdom",
                        "Shield of Defense",
                        "Crown of Kings",
                        "Boots of Speed",
                        "Cloak of Shadows",
                        "Staff of Elements"]),
                name_or_power,
                choice(['Common', 'Rare', 'Legendary']),
                'Artifact',
                randint(1, 3),
                choice([
                    "Permanent: +1 mana per turn",
                    "Permanent: +2 attack to equipped creature",
                    "Permanent: Draw an extra card each turn",
                    "Permanent: +3 health to all friendly creatures",
                    "Permanent: +1 cost reduction to all cards"
                    "Permanent: Cards cost 1 less mana",
                    "Permanent: Creatures have stealth",
                    "Permanent: +1 spell damage"])
                )
        else:
            return ArtifactCard(
                choice(["Mana Crystal",
                        "Sword of Power",
                        "Ring of Wisdom",
                        "Shield of Defense",
                        "Crown of Kings",
                        "Boots of Speed",
                        "Cloak of Shadows",
                        "Staff of Elements"]),
                randint(1, 10),
                choice(['Common', 'Rare', 'Legendary']),
                'Artifact',
                randint(1, 3),
                choice([
                    "Permanent: +1 mana per turn",
                    "Permanent: +2 attack to equipped creature",
                    "Permanent: Draw an extra card each turn",
                    "Permanent: +3 health to all friendly creatures",
                    "Permanent: +1 cost reduction to all cards"
                    "Permanent: Cards cost 1 less mana",
                    "Permanent: Creatures have stealth",
                    "Permanent: +1 spell damage"])
                )

    def create_themed_deck(self, size: int) -> dict:
        base = size // 3
        reste = size % 3

        pack_c = [self.create_creature() for _ in range(base)]
        pack_a = [self.create_artifact() for _ in range(base)]
        pack_s = [self.create_spell() for _ in range(base)]
        for _ in range(reste):
            lst_choice = (choice([pack_c, pack_a, pack_s]))
            lst_choice.append(choice([
                self.create_creature(),
                self.create_artifact(),
                self.create_spell()
            ]))
        result = {
            'Creature cards': pack_c,
            'Spell cards': pack_s,
            'Artifact cards': pack_a
        }
        return result

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['goblin', 'dragon', 'golem', 'assassin'],
            'spells': ['lightning'],
            'artifacts': ['crystal']
        }
