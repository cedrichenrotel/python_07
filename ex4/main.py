# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/30 13:42:25 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/30 15:00:48 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", "creature", 7, 5)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", "creature", 3, 4)

    print("=== DataDeck Tournament Platform ===")
    print("\nRegistering Tournament Cards...")
    print(f"\n{dragon.name} ({platform.register_card(dragon)}):")
    print(f"\n{wizard.name} ({platform.register_card(wizard)}):")
    print(f"Rating: {wizard.calculate_rating()}")


if __name__ == "__main__":
    main()
