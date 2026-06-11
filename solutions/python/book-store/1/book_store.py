from functools import lru_cache

PRICE = 800  # cents

DISCOUNTS = {
    1: 1.00,
    2: 0.95,
    3: 0.90,
    4: 0.80,
    5: 0.75,
}


def total(basket):
    counts = [basket.count(book) for book in range(1, 6)]

    @lru_cache(maxsize=None)
    def best(state):
        if sum(state) == 0:
            return 0

        state = list(state)
        result = float("inf")

        available = [i for i, count in enumerate(state) if count > 0]

        for mask in range(1, 1 << len(available)):
            new_state = state[:]
            size = 0

            for bit, idx in enumerate(available):
                if mask & (1 << bit):
                    new_state[idx] -= 1
                    size += 1

            cost = int(size * PRICE * DISCOUNTS[size])
            result = min(result, cost + best(tuple(new_state)))

        return result

    return best(tuple(counts))