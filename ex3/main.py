# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 14:54:34 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/31 11:52:51 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory


strategy = AggressiveStrategy()
factory = FantasyCardFactory()
engine = GameEngine()
engine.configure_engine(factory, strategy)
try:

    print("=== DataDeck Game Engine ===")

    print("\nConfiguring Fantasy Card Game...")
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.__class__.__name__}")
    try:
        print(f"Available types:\n {factory.get_supported_types()}")
        print(f"\nTurn execution:\n{engine.simulate_turn()}")
        print(f"\nGame Report:\n{engine.get_engine_status()}")
    except TypeError as e:
        print(f"[ERROR]: {e}")
    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility "
          "achieved!")

except (ValueError, AttributeError) as e:
    print(f"[KO] error: {e}")
