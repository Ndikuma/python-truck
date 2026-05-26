"""Functions to help play and score a game of blackjack.

How to play blackjack:
https://bicyclecards.com/how-to-play/blackjack/

"Standard" playing cards:
https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card."""

    if card in ["J", "Q", "K"]:
        return 10
    elif card == "A":
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""

    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card."""

    total = 0

    # Existing ace counts as 11
    if card_one == "A":
        total += 11
    else:
        total += value_of_card(card_one)

    if card_two == "A":
        total += 11
    else:
        total += value_of_card(card_two)

    # Upcoming ace should be 11 if it doesn't bust
    if total + 11 <= 21:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a blackjack."""

    total = 0

    if card_one == "A":
        total += 11
    else:
        total += value_of_card(card_one)

    if card_two == "A":
        total += 11
    else:
        total += value_of_card(card_two)

    return total == 21


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""

    def get_split_value(card):
        if card in ["J", "Q", "K"]:
            return 10
        elif card == "A":
            return 1
        else:
            return int(card)

    return get_split_value(card_one) == get_split_value(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet."""

    total = value_of_card(card_one) + value_of_card(card_two)

    return total in [9, 10, 11]