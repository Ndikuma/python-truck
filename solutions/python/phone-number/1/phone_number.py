import re

class PhoneNumber:
    def __init__(self, number):
        if re.search(r"[A-Za-z]", number):
            raise ValueError("letters not permitted")

        if re.search(r"[^0-9\s\+\-\.\(\)]", number):
            raise ValueError("punctuations not permitted")

        digits = re.sub(r"\D", "", number)

        if len(digits) == 11:
            if digits[0] != "1":
                raise ValueError("11 digits must start with 1")
            digits = digits[1:]
        elif len(digits) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(digits) > 11:
            raise ValueError("must not be greater than 11 digits")

        if digits[0] == "0":
            raise ValueError("area code cannot start with zero")
        if digits[0] == "1":
            raise ValueError("area code cannot start with one")
        if digits[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if digits[3] == "1":
            raise ValueError("exchange code cannot start with one")

        self.number = digits
        self.area_code = digits[:3]
        self.exchange_code = digits[3:6]
        self.subscriber_number = digits[6:]

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"