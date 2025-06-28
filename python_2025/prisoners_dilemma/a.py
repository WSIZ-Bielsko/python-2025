from pydantic import BaseModel


class Score(BaseModel):
    player1: float
    player2: float


class Game:
    def __init__(self, payoff: dict[str, tuple[float, float]]):
        self.payoff = payoff

    def post_player1_move(self, move: str):
        # record move; if both players have made a move, compute score and update scores
        # and reset moves
        pass

    def post_player2_move(self, move: str):
        pass

    def _update_scores(self):
        pass

    def reset_game(self):
        pass

    def get_scores(self) -> Score:
        pass


def compute_updated_score(decisions: str, current_score: Score, payoff: dict[str, tuple[float, float]]) -> Score:
    """
    Assume decisions are keys in payoff dict.
    Update score and return it.

    :param decisions:
    :param score:
    :param payoff:
    :return: updated score
    """

    d = current_score.model_copy()
    d.player1 += 10

    return d


def test_update_score():
    score = Score(player1=0, player2=0)
    po = {'DD': (0, 0.5), 'CD': (-1, 2), 'DC': (1, -1), 'CC': (0.5, 1)}
    assert compute_updated_score('DD', score, payoff=po) == Score(player1=0, player2=0.5)
    assert compute_updated_score('DC', score, payoff=po) == Score(player1=1, player2=-1)
    assert compute_updated_score('CC', score, payoff=po) == Score(player1=0.5, player2=1)
    assert compute_updated_score('CD', score, payoff=po) == Score(player1=-1, player2=2)


def test_update_score2():
    score = Score(player1=0, player2=0)
    po = {'DD': (0, 0), 'CD': (1, 1), 'DC': (1, 1), 'CC': (2, 2)}
    assert compute_updated_score('DD', score, payoff=po) == Score(player1=0, player2=0)
    assert compute_updated_score('DC', score, payoff=po) == Score(player1=1, player2=1)
    assert compute_updated_score('CC', score, payoff=po) == Score(player1=2, player2=2)
    assert compute_updated_score('CD', score, payoff=po) == Score(player1=1, player2=1)


if __name__ == '__main__':
    payoff = {'DD': (0, 0.5), 'CD': (-1, 2), 'DC': (1, -1), 'CC': (0.5, 1)}

    print(payoff['DD'])  # (0,0.5)

    scores = Score(player1=0, player2=0)  # tworzymy instancje klasy
    print(scores)
    scores.player1 = 2  # zmieniamy instancje klasy
    print(scores)

    new_scores = compute_updated_score('DD', scores, payoff)
    print(scores)
