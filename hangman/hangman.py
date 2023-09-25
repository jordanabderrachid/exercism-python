# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.letters = [(letter, False) for letter in word]

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")

        success = False
        for i, (letter, found) in enumerate(self.letters):
            if char == letter and not found:
                success = True
                self.letters[i] = (letter, True)

        if not success:
            self.remaining_guesses -= 1

        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE

        if all(map(lambda l: l[1], self.letters)):
            self.status = STATUS_WIN

    def get_masked_word(self):
        return "".join([letter if found else "_" for (letter, found) in self.letters])

    def get_status(self):
        return self.status
