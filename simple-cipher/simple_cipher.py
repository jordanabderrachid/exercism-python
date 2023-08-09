import random

# ord("a") = 97
# ord("z") = 122

class Cipher:
    def __init__(self, key=None):
        if key == None:
            self._set_random_key()
        else:
            self.key = key
            self.key_len = len(key)

    def _set_random_key(self):
        self.key_len = 100
        self.key = "".join([chr(random.randint(97, 122)) for _ in range(self.key_len)])

    def encode(self, text):
        encoded = ""
        for i, l in enumerate(text):
            k = self.key[i % self.key_len]
            d = ord(k) - 97
            ord_l = ord(l)
            if ord_l + d > 122:
                encoded += chr(ord_l + d - 26)
            else:
                encoded += chr(ord_l + d)

        return encoded

    def decode(self, text):
        decoded = ""
        for i, l in enumerate(text):
            k = self.key[i % self.key_len]
            d = ord(k) - 97
            ord_l = ord(l)
            if ord_l - d < 97:
                decoded += chr(ord_l - d + 26)
            else:
                decoded += chr(ord_l - d)

        return decoded
