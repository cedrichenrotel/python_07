# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 14:54:34 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/30 19:48:02 by cehenrot        ###   ########.fr        #
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
    print(f"Available types:\n {factory.get_supported_types()}")
    print(f"\nTurn execution:\n{engine.simulate_turn()}")
    print(f"\nGame Report:\n{engine.get_engine_status()}")
    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility "
          "achieved!")

except (ValueError, AttributeError) as e:
    print(f"[KO] error: {e}")
