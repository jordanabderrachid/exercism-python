import re

class PhoneNumber:
    def __init__(self, number):
        if re.search(r'[a-z]+', number) != None:
            raise ValueError("letters not permitted")

        if re.search(r'(?:\@|\:|\!)', number) != None:
            raise ValueError("punctuations not permitted")
        
        cleaned = re.sub(r'\D', "", number)
        if len(cleaned) < 10:
            raise ValueError("must not be fewer than 10 digits")
        
        if len(cleaned) == 11:
            if cleaned[0] != "1":
                raise ValueError("11 digits must start with 1")

            cleaned = cleaned[1:]

        if len(cleaned) > 11:
            raise ValueError("must not be greater than 11 digits")

        self.number = cleaned
        self.area_code = cleaned[0:3]
        self.exchange_code = cleaned[3:6]
        self.subscriber = cleaned[6:]

        if self.area_code.startswith("0"):
            raise ValueError("area code cannot start with zero")
        
        if self.area_code.startswith("1"):
            raise ValueError("area code cannot start with one")
        
        if self.exchange_code.startswith("0"):
            raise ValueError("exchange code cannot start with zero")
        
        if self.exchange_code.startswith("1"):
            raise ValueError("exchange code cannot start with one")
        
    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber}"