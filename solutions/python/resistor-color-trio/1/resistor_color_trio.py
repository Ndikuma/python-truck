COLOR_MAP = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def label(colors: list[str]) -> str:
    first = COLOR_MAP[colors[0]]
    second = COLOR_MAP[colors[1]]
    zeros = COLOR_MAP[colors[2]]

    value = (first * 10 + second) * (10 ** zeros)

    # convert to engineering units
    units = [
        (10**9, "gigaohms"),
        (10**6, "megaohms"),
        (10**3, "kiloohms"),
        (1, "ohms"),
    ]

    for factor, name in units:
        if value >= factor:
            if factor == 1:
                return f"{value} {name}"
            return f"{value // factor} {name}"

    return f"{value} ohms"