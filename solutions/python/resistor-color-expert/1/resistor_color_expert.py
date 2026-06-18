def resistor_label(colors):
    COLOR_DIGIT = {
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

    TOLERANCE = {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%",
    }

    # 1-band resistor
    if len(colors) == 1:
        return "0 ohms"

    # 4-band resistor
    if len(colors) == 4:
        value = COLOR_DIGIT[colors[0]] * 10 + COLOR_DIGIT[colors[1]]
        multiplier = COLOR_DIGIT[colors[2]]
        tolerance = TOLERANCE[colors[3]]

    # 5-band resistor
    elif len(colors) == 5:
        value = (
            COLOR_DIGIT[colors[0]] * 100 +
            COLOR_DIGIT[colors[1]] * 10 +
            COLOR_DIGIT[colors[2]]
        )
        multiplier = COLOR_DIGIT[colors[3]]
        tolerance = TOLERANCE[colors[4]]

    else:
        raise ValueError("invalid input")

    value *= 10 ** multiplier

    # format units
    if value >= 1_000_000:
        if value % 1_000_000 == 0:
            value_str = str(value // 1_000_000)
        else:
            mega_value = value / 1_000_000
            # Remove trailing zeros and decimal point if needed
            value_str = f"{mega_value:.3f}".rstrip('0').rstrip('.')
            # If it ends up like "2.5", keep it
            if value_str.endswith('.0'):
                value_str = value_str[:-2]
        unit = "megaohms"
    elif value >= 1_000:
        if value % 1_000 == 0:
            value_str = str(value // 1_000)
        else:
            kilo_value = value / 1_000
            value_str = f"{kilo_value:.3f}".rstrip('0').rstrip('.')
            if value_str.endswith('.0'):
                value_str = value_str[:-2]
        unit = "kiloohms"
    else:
        value_str = str(value)
        unit = "ohms"

    return f"{value_str} {unit} ±{tolerance}"