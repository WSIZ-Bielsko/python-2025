class Game:

    def __init__(self, payoff: dict[str, tuple[float, float]]):
        # constructor method
        self.payoff = payoff
        self.history = []
        self.score = [0, 0]
        self.moves = ['N', 'N']

    def post_move(self, move: str, player: int):
        # method
        player -= 1
        self.moves[player] = move
        if self.moves[0] != 'N' and self.moves[1] != 'N':
            self._update_scores()

    def _update_scores(self):
        # method
        move = self.moves[0] + self.moves[1]
        payoff = self.payoff[move]
        self.score[0] += payoff[0]
        self.score[1] += payoff[1]
        self.history.append(move)
        self.moves = ['N', 'N']


def test_game1():
    po = {'DD': (0, 0), 'CD': (3, 0), 'DC': (0, 3), 'CC': (2, 2)}
    g = Game(po)
    g.post_move('D', 1)
    g.post_move('C', 2)
    print(g.score)
    print(g.history)
    g.post_move('C', 1)
    g.post_move('C', 2)
    print(g.score)
    print(g.history)


if __name__ == '__main__':
    pass
