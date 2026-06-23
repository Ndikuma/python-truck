from collections import Counter

# Score categories.
YACHT = "yacht"
ONES = "ones"
TWOS = "twos"
THREES = "threes"
FOURS = "fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "full house"
FOUR_OF_A_KIND = "four of a kind"
LITTLE_STRAIGHT = "little straight"
BIG_STRAIGHT = "big straight"
CHOICE = "choice"


def score(dice, category):
    counts = Counter(dice)

    if category == YACHT:
        return 50 if len(counts) == 1 else 0

    if category == ONES:
        return counts[1] * 1

    if category == TWOS:
        return counts[2] * 2

    if category == THREES:
        return counts[3] * 3

    if category == FOURS:
        return counts[4] * 4

    if category == FIVES:
        return counts[5] * 5

    if category == SIXES:
        return counts[6] * 6

    if category == FULL_HOUSE:
        values = sorted(counts.values())
        return sum(dice) if values == [2, 3] else 0

    if category == FOUR_OF_A_KIND:
        for num, c in counts.items():
            if c >= 4:
                return num * 4
        return 0

    if category == LITTLE_STRAIGHT:
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0

    if category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0

    if category == CHOICE:
        return sum(dice)

    return 0