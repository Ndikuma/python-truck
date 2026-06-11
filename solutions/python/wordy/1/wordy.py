def answer(question):
    if not question.startswith("What is ") or not question.endswith("?"):
        raise ValueError("syntax error")

    tokens = question[8:-1].strip().split()

    if not tokens:
        raise ValueError("syntax error")

    def to_int(x):
        try:
            return int(x)
        except:
            raise ValueError("syntax error")

    # first token must be number
    try:
        result = to_int(tokens[0])
    except:
        raise ValueError("syntax error")

    i = 1

    while i < len(tokens):
        op = tokens[i]

        # handle operations
        if op in ("plus", "minus", "multiplied", "divided"):

            if op == "plus":
                func = lambda a, b: a + b
                i += 1

            elif op == "minus":
                func = lambda a, b: a - b
                i += 1

            elif op == "multiplied":
                if i + 1 >= len(tokens) or tokens[i + 1] != "by":
                    raise ValueError("syntax error")
                func = lambda a, b: a * b
                i += 2

            elif op == "divided":
                if i + 1 >= len(tokens) or tokens[i + 1] != "by":
                    raise ValueError("syntax error")
                func = lambda a, b: a // b
                i += 2

        else:
            # IMPORTANT FIX:
            # If it's not a number AND not a known operation → unknown operation
            try:
                raise ValueError("unknown operation")
            except ValueError as e:
                if op.lstrip("-").isdigit():
                    raise ValueError("syntax error")
                raise

        # must have number next
        if i >= len(tokens):
            raise ValueError("syntax error")

        try:
            num = to_int(tokens[i])
        except:
            raise ValueError("syntax error")

        result = func(result, num)
        i += 1

    return result