import os.path


class HighScores:

    def __init__(self):
        self.high_scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.read_scores()
        self.save_scores()

    def save_scores(self):
        self.sort()
        file = open("high_scores.txt", "w")
        for x in self.high_scores:
            file.write(str(x) + "\n")
        file.close()

    def update_scores(self, stats):
        for x in self.high_scores:
            if stats.score > x:
                self.high_scores[9] = stats.score
                break

    def sort(self):
        for x in range(10):
            for y in range(9):
                if self.high_scores[y] < self.high_scores[y + 1]:
                    self.high_scores[y], self.high_scores[y + 1] = \
                        self.high_scores[y + 1], self.high_scores[y]

    def read_scores(self):
        if os.path.isfile('high_scores.txt'):
            file = open("high_scores.txt")
            for x in range(10):
                self.high_scores[x] = int(file.readline())
            file.close()
