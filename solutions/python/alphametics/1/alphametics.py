import itertools
import re


def solve(puzzle):
    # Remove spaces and normalize
    puzzle = puzzle.replace(" ", "")

    left, right = puzzle.split("==")
    words = left.split("+")

    # all unique letters
    letters = sorted(set(re.findall(r"[A-Z]", puzzle)))

    if len(letters) > 10:
        return None

    # leading letters cannot be 0
    leading = set(word[0] for word in words + [right])

    # convert word to expression
    def word_value(word):
        return sum(
            10 ** i * (10 ** 0)  # placeholder (we rebuild later)
            for i, _ in enumerate(word)
        )

    # precompute positional weights
    def build_weights(words, result):
        weights = {c: 0 for c in letters}

        for w in words:
            for i, c in enumerate(reversed(w)):
                weights[c] += 10 ** i

        for i, c in enumerate(reversed(result)):
            weights[c] -= 10 ** i

        return weights

    weights = build_weights(words, right)

    # backtracking with pruning
    def backtrack(assignments, used_digits):
        if len(assignments) == len(letters):
            if sum(weights[c] * d for c, d in assignments.items()) == 0:
                return assignments.copy()
            return None

        letter = letters[len(assignments)]

        for digit in range(10):
            if digit in used_digits:
                continue

            if digit == 0 and letter in leading:
                continue

            assignments[letter] = digit
            used_digits.add(digit)

            result = backtrack(assignments, used_digits)
            if result:
                return result

            used_digits.remove(digit)
            del assignments[letter]

        return None

    return backtrack({}, set())