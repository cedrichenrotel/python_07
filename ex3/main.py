# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 14:54:34 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/26 15:23:37 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# from ex0.CreatureCard import CreatureCard
# from ex1.ArtifactCard import ArtifactCard
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory


strategy = AggressiveStrategy()
fantasy = FantasyCardFactory()

lst_player = [
    fantasy.create_spell('fire'),
    fantasy.create_spell(1),
    fantasy.create_spell()
]

lst_enemy = [
    fantasy.create_creature(),
    fantasy.create_creature(),
    fantasy.create_creature()
]

print("=== DataDeck Game Engine ===")
# print("\nTurn execution:")
# print(f"Strategy: {strategy.get_strategy_name()}:")
# print(f"Action: {strategy.execute_turn(lst_player, lst_enemy)}")
packet = fantasy.create_themed_deck(10)

for key, cards in packet.items():
    print(f"\n{key}:")
    for card in cards:
        print(card.get_card_info())
