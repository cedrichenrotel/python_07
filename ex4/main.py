# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/30 13:42:25 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/30 19:08:42 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
from ex4.Rankable import Rankable
from ex2.Combatable import Combatable
from ex0.Card import Card


def main() -> None:
    platform = TournamentPlatform()
    dragon = TournamentCard("Fire Dragon", 5, "Legendary", "creature", 7, 5)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", "creature", 3, 4)

    try:
        card1 = platform.register_card(dragon)
        card2 = platform.register_card(wizard)
    except (AttributeError, ValueError) as e:
        print(f"[ERROR] register_card(): {e}")

    print("=== DataDeck Tournament Platform ===")

    print("\nRegistering Tournament Cards...")
    print(f"\n{dragon.name} ({card1}):")
    print(f"- Interfaces: [{Card.__name__}, {Combatable.__name__}, "
          f"{Rankable.__name__}]")
    print(f"- Rating: {dragon.calculate_rating()}")
    info = TournamentCard.get_rank_info(dragon)
    print(f"- Record: {info['wins']}-{info['losses']}")

    print(f"\n{wizard.name} ({card2}):")
    print(f"- Interfaces: [{Card.__name__}, {Combatable.__name__}, "
          f"{Rankable.__name__}]")
    print(f"- Rating: {wizard.calculate_rating()}")
    info = TournamentCard.get_rank_info(wizard)
    print(f"- Record: {info['wins']}-{info['losses']}")

    print("\nCreating tournament match...")

    try:
        result1 = platform.create_match(card1, card2)
        print(f"Match result: {result1}")
    except ValueError as e:
        print(f"[ERROR] create_match(): {e}")
        return

    print("Tournament Leaderboard:")
    for i, card in enumerate(platform.get_leaderboard(), 1):
        info = card.get_rank_info()
        print(f"{i}. {card.name} - Rating: {info['rating']} "
              f"({info['wins']}-{info['losses']})")

    print("\nPlatform Report:")
    try:
        print(f"{platform.generate_tournament_report()}")
    except ZeroDivisionError as e:
        print(f"[ERROR] generate_tournament_report(): {e}")
        return

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
