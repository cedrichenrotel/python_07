# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 14:54:34 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/26 17:09:21 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory


strategy = AggressiveStrategy()
fantasy = FantasyCardFactory()
engine = GameEngine()

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
engine.configure_engine(fantasy, strategy)
print(f"tour enemy: {engine.simulate_turn()}")
