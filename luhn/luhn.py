import re

class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        num = re.sub(r'\s', "", self.card_num)
        if len(num) <= 1:
            return False

        if re.match(r'^(?:[0-9]|\s)*$', num) == None:
            return False        
        
        list_num = list(num)
        list_num.reverse()
        sum = 0
        for i, d in enumerate(list_num):
            if (i+1) % 2 == 0:
                doubled = 2*int(d)
                if doubled > 9:
                    doubled -= 9
                sum += doubled
            else:
                sum += int(d)
        
        return sum % 10 == 0
