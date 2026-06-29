def best_hands(hands):
    """Return the best hand(s) from a list of poker hands."""
    if not hands:
        return []
    
    # Parse all hands and rank them
    ranked_hands = [(hand, _rank_hand(hand)) for hand in hands]
    
    # Find the highest rank
    best_rank = max(ranked_hands, key=lambda x: x[1])[1]
    
    # Return all hands with the best rank (in case of ties)
    return [hand for hand, rank in ranked_hands if rank == best_rank]


def _rank_hand(hand):
    """Return a numeric rank for a hand (higher is better)."""
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    
    cards = hand.split()
    ranks = sorted([values[card[:-1]] for card in cards], reverse=True)
    suits = [card[-1] for card in cards]
    
    # Check for flush
    is_flush = len(set(suits)) == 1
    
    # Check for straight
    unique_ranks = sorted(set(ranks), reverse=True)
    is_straight = False
    if len(unique_ranks) == 5:
        if unique_ranks[0] - unique_ranks[4] == 4:
            is_straight = True
        # Ace-low straight (A, 2, 3, 4, 5)
        elif unique_ranks == [14, 5, 4, 3, 2]:
            is_straight = True
            ranks = [5, 4, 3, 2, 1]  # Adjust for ace-low
    
    # Count rank frequencies
    rank_counts = {}
    for rank in ranks:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    
    counts = sorted(rank_counts.values(), reverse=True)
    
    # Determine hand rank
    # Royal Flush: 10, J, Q, K, A all same suit
    if is_flush and is_straight and ranks == [14, 13, 12, 11, 10]:
        return (9, ranks)
    
    # Straight Flush
    if is_flush and is_straight:
        return (8, ranks)
    
    # Four of a kind
    if counts == [4, 1]:
        four_rank = [r for r, c in rank_counts.items() if c == 4][0]
        kicker = [r for r, c in rank_counts.items() if c == 1][0]
        return (7, [four_rank, kicker])
    
    # Full House
    if counts == [3, 2]:
        three_rank = [r for r, c in rank_counts.items() if c == 3][0]
        two_rank = [r for r, c in rank_counts.items() if c == 2][0]
        return (6, [three_rank, two_rank])
    
    # Flush
    if is_flush:
        return (5, ranks)
    
    # Straight
    if is_straight:
        return (4, ranks)
    
    # Three of a kind
    if counts == [3, 1, 1]:
        three_rank = [r for r, c in rank_counts.items() if c == 3][0]
        kickers = sorted([r for r, c in rank_counts.items() if c == 1], reverse=True)
        return (3, [three_rank] + kickers)
    
    # Two pair
    if counts == [2, 2, 1]:
        pairs = sorted([r for r, c in rank_counts.items() if c == 2], reverse=True)
        kicker = [r for r, c in rank_counts.items() if c == 1][0]
        return (2, pairs + [kicker])
    
    # One pair
    if counts == [2, 1, 1, 1]:
        pair_rank = [r for r, c in rank_counts.items() if c == 2][0]
        kickers = sorted([r for r, c in rank_counts.items() if c == 1], reverse=True)
        return (1, [pair_rank] + kickers)
    
    # High card
    return (0, ranks)


def _compare_hands(hand1, hand2):
    """Compare two hands, return 1 if hand1 wins, -1 if hand2 wins, 0 if tie."""
    rank1, values1 = _rank_hand(hand1)
    rank2, values2 = _rank_hand(hand2)
    
    if rank1 > rank2:
        return 1
    if rank1 < rank2:
        return -1
    
    # Same rank, compare values
    for v1, v2 in zip(values1, values2):
        if v1 > v2:
            return 1
        if v1 < v2:
            return -1
    
    return 0  # Tie