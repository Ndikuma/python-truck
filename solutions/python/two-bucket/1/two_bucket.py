from collections import deque


def measure(bucket1, bucket2, goal, start_bucket):
    if goal > max(bucket1, bucket2):
        raise ValueError("Goal impossible with given buckets")

    start = 0 if start_bucket == "one" else 1

    # state = (a, b, last_action_bucket)
    # last_action_bucket prevents invalid rule:
    # "starting bucket empty AND other full after action"
    initial = (0, 0)

    queue = deque([(initial, 0)])
    visited = set([(0, 0)])

    def valid(a, b):
        return (a, b) not in visited

    while queue:
        (a, b), steps = queue.popleft()

        if a == goal:
            return steps, "one", b
        if b == goal:
            return steps, "two", a

        next_states = []

        # fill bucket 1
        next_states.append((bucket1, b))

        # fill bucket 2
        next_states.append((a, bucket2))

        # empty bucket 1
        next_states.append((0, b))

        # empty bucket 2
        next_states.append((a, 0))

        # pour 1 -> 2
        transfer = min(a, bucket2 - b)
        next_states.append((a - transfer, b + transfer))

        # pour 2 -> 1
        transfer = min(b, bucket1 - a)
        next_states.append((a + transfer, b - transfer))

        for na, nb in next_states:
            # RULE 3 constraint:
            # don't allow (start empty AND other full)
            if start == 0:
                if na == 0 and nb == bucket2:
                    continue
            else:
                if nb == 0 and na == bucket1:
                    continue

            if (na, nb) not in visited:
                visited.add((na, nb))
                queue.append(((na, nb), steps + 1))

    raise ValueError("No solution found")