class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]
    
    def personal_best(self):
        return sorted(self.scores)[-1]
    
    def personal_top_three(self):
        top_three = sorted(self.scores)[-3:]
        top_three.reverse()
        return top_three