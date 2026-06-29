def can_chain(dominoes):
    if not dominoes:
        return []

    used = [False] * len(dominoes)

    def backtrack(path):
        if len(path) == len(dominoes):
            # check chain is valid loop
            if path[0][0] == path[-1][1]:
                return path
            return None

        last = path[-1][1] if path else None

        for i, (a, b) in enumerate(dominoes):
            if used[i]:
                continue

            # try a -> b
            if not path or a == last:
                used[i] = True
                result = backtrack(path + [(a, b)])
                if result:
                    return result
                used[i] = False

            # try b -> a (flip)
            if not path or b == last:
                used[i] = True
                result = backtrack(path + [(b, a)])
                if result:
                    return result
                used[i] = False

        return None

    for i, (a, b) in enumerate(dominoes):
        used[i] = True
        result = backtrack([(a, b)])
        if result:
            return result
        used[i] = False

    return None