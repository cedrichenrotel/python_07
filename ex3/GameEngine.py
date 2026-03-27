# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  GameEngine.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 14:54:07 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/27 11:35:47 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine():
    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.turn = 0
        self.len_card_creature = 0
        self.total_dommage = 0

    def simulate_turn(self, pioche: dict) -> dict:
        if not isinstance(pioche, dict):
            raise AttributeError("simulate_turn: pioche is not dict")
        main = pioche
        battlefield = pioche['Creature cards']

        self.len_card_creature = (len(pioche['Creature cards']) +
                                  len(pioche['Spell cards']) +
                                  len(pioche['Artifact cards']))
        self.turn += 1
        result = self.strategy.execute_turn(main['Creature cards'],
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
