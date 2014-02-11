"""
Concrete table class with standard values/tiebreakers for the MLS.
"""

from modelfc.abstract.table import Table
from modelfc.concrete.team import Team


class MLSTable(Table):
    stats = {'w': 0, 'd': 0, 'l': 0, 'gf': 0, 'gd': 0, 'rgd': 0, 'rgf': 0,
             'hgd': 0, 'hgf': 0}

    def __init__(self):
        Table.__init__(self)

    def on_result(self, result):
        home = self.table.setdefault(result['home'],
                                     Team(result['home'], **MLSTable.stats))
        away = self.table.setdefault(result['away'],
                                     Team(result['away'], **MLSTable.stats))
        hscore, ascore = result['score'].split(' - ')
        hdict, adict = self.statsdict(hscore, ascore)

        if hscore == ascore:
            home.modify(1, **hdict)
            away.modify(1, **adict)
        else:
            home.modify(3 if hscore > ascore else 0, **hdict)
            away.modify(0 if hscore > ascore else 3, **adict)

    @staticmethod
    def statsdict(home_score, away_score):
        """
        Generates stats to be tracked for each team.
        """
        home_score = int(home_score)
        away_score = int(away_score)

        home = {'gf': home_score, 'gd': home_score - away_score,
                'hgf': home_score, 'hgd': home_score - away_score}
        away = {'gf': away_score, 'gd': away_score - home_score,
                'rgf': away_score, 'rgd': away_score - home_score}
        if home_score == away_score:
            home['d'] = away['d'] = 1
        else:
            home['w' if home_score > away_score else 'l'] = 1
            away['l' if home_score > away_score else 'w'] = 1

        return home, away

    @staticmethod
    def tiebreakers(team):
        return [team.value, team['w'], team['gf'], team['gd'], team['rgf'],
                team['rgd'], team['hgf'], team['hgd']]
