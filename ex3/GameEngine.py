# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  GameEngine.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 14:54:07 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/26 17:03:24 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine():
    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        main = self.factory.create_themed_deck(5)
        battlefield = self.factory.create_creature()
        return self.strategy.execute_turn(main['Creature cards'],
                                          [battlefield])

    def get_engine_status(self) -> dict:
        pass
