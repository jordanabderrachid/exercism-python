from typing import List


class Team:
    def __init__(self, name):
        self.name = name
        self.game_played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0

    def __getattr__(self, name):
        if name == "score":
            return self._score()

        return super().__getattr__(name)

    def record_result(self, result):
        self.game_played += 1
        if result == "win":
            self.wins += 1

        if result == "draw":
            self.draws += 1

        if result == "loss":
            self.losses += 1

    def _score(self):
        return self.wins * 3 + self.draws

    def to_table(self):
        score = str(self._score())
        return f"{self.name.ljust(31)}|  {self.game_played} |  {self.wins} |  {self.draws} |  {self.losses} | {score.rjust(2)}"


def tally(rows: List[str]):
    teams_map = {}
    res = ["Team                           | MP |  W |  D |  L |  P"]
    for row in rows:
        home_team_name, visitor_team_name, result, *_ = row.split(";")
        record_result(teams_map, home_team_name, result)
        record_result(teams_map, visitor_team_name, convert_result_to_visitor(result))

    teams_list = list()
    for _, t in teams_map.items():
        teams_list.append(t)

    teams_list.sort(key=lambda t: (-t.score, t.name))

    for t in teams_list:
        res.append(t.to_table())

    return res


def record_result(teams_map, team_name, result):
    t = teams_map.get(team_name)
    if t is None:
        t = Team(team_name)

    t.record_result(result)
    teams_map[team_name] = t


def convert_result_to_visitor(result):
    if result == "win":
        return "loss"

    if result == "loss":
        return "win"

    return result
