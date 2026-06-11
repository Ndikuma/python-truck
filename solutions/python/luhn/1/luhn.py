class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        number = self.card_num.replace(" ", "")

        if len(number) <= 1:
            return False

        if not number.isdigit():
            return False

        total = 0

        for i, digit in enumerate(reversed(number)):
            n = int(digit)

            if i % 2 == 1:  # every second digit from the right
                n *= 2
                if n > 9:
                    n -= 9

            total += n

        return total % 10 == 0