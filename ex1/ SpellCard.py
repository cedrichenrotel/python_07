#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#   SpellCard.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/23 13:59:51 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/23 14:24:45 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from abc import ABC, abstractmethod

def __init__(self, name: str, cost: int, rarity: str, 
             effect_type: str) -> None: