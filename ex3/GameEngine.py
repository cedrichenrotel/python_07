# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  GameEngine.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 14:54:07 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/31 11:53:31 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine():
    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        if not isinstance(factory, CardFactory):
            raise TypeError(f"configure_engine: factory invalid: {factory}")
        if not isinstance(strategy, GameStrategy):
            raise TypeError(f"configure_engine: strategy invalid: {strategy}")
        self.factory = factory
        self.strategy = strategy
        self.turn = 0
        self.len_card_creature = 0
        self.total_dommage = 0

    def simulate_turn(self) -> dict:
        pioche = self.factory.create_themed_deck(9)
        lst_pioche = (
            pioche['Creature cards'] +
            pioche['Spell cards'] +
            pioche['Artifact cards']
        )
        half = len(lst_pioche) // 2
        main = lst_pioche[half:]
        battlefield = lst_pioche[:half]

        self.len_card_creature = len(lst_pioche)
        self.turn += 1
        result = self.strategy.execute_turn(main,
                                            battlefield)
        self.total_dommage = result['damage_dealt']
        return result

    def get_engine_status(self) -> dict:
        result = {
            'turns_simulated': self.turn,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.total_dommage,
            'cards_created': self.len_card_creature
        }
        return result
