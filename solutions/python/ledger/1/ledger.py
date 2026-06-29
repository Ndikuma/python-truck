from datetime import datetime


class LedgerEntry:
    def __init__(self):
        self.date = None
        self.description = None
        self.change = None


def create_entry(date, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, "%Y-%m-%d")
    entry.description = description
    entry.change = change
    return entry


def format_entries(currency, locale, entries):
    if locale == "en_US":
        header = "Date       | Description               | Change       "
    else:
        header = "Datum      | Omschrijving              | Verandering  "
    
    sorted_entries = sorted(entries, key=lambda e: (e.date, e.change, e.description))
    
    lines = [header]
    for entry in sorted_entries:
        date_str = format_date(entry.date, locale)
        desc_str = format_description(entry.description)
        money_str = format_money(currency, locale, entry.change)
        lines.append(f"{date_str} | {desc_str} | {money_str}")
    
    return "\n".join(lines)


def format_date(date, locale):
    if locale == "en_US":
        return date.strftime("%m/%d/%Y")
    return date.strftime("%d-%m-%Y")


def format_description(description):
    if len(description) > 25:
        return description[:22] + "..."
    return description.ljust(25)


def format_money(currency, locale, amount):
    is_negative = amount < 0
    amount = abs(amount)
    
    whole = amount // 100
    cents = amount % 100
    
    if locale == "nl_NL":
        thousands_sep = "."
        decimal_sep = ","
        symbol = "€" if currency == "EUR" else "$"
    else:
        thousands_sep = ","
        decimal_sep = "."
        symbol = "$" if currency == "USD" else "€"
    
    whole_str = f"{whole:,}".replace(",", thousands_sep)
    number_part = f"{whole_str}{decimal_sep}{cents:02d}"
    
    if is_negative:
        if locale == "nl_NL":
            # Dutch negative: $ -123,45 (with trailing space)
            formatted = f"{symbol} -{number_part} "
        else:
            # US negative: ($123.45) (no trailing space)
            formatted = f"({symbol}{number_part})"
    else:
        if locale == "nl_NL":
            # Dutch positive: $ 123,45 (with trailing space)
            formatted = f"{symbol} {number_part} "
        else:
            # US positive: $123.45 (with trailing space)
            formatted = f"{symbol}{number_part} "
    
    # Pad to exactly 13 characters
    return formatted.rjust(13)