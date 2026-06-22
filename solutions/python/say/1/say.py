def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
             "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]

    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    def under_100(n):
        if n < 20:
            return ones[n]
        if n < 100:
            return tens[n // 10] + ("" if n % 10 == 0 else "-" + ones[n % 10])

    def under_1000(n):
        if n < 100:
            return under_100(n)
        return ones[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + under_100(n % 100))

    def chunk(n, unit):
        if n == 0:
            return ""
        return under_1000(n) + " " + unit

    billion = number // 1_000_000_000
    million = (number // 1_000_000) % 1000
    thousand = (number // 1000) % 1000
    rest = number % 1000

    parts = []
    if billion:
        parts.append(chunk(billion, "billion"))
    if million:
        parts.append(chunk(million, "million"))
    if thousand:
        parts.append(chunk(thousand, "thousand"))
    if rest:
        parts.append(under_1000(rest))

    return " ".join(parts).strip()