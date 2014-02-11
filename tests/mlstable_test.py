import unittest

from mlstable import MLSTable


class MLSTableTest(unittest.TestCase):
    def setUp(self):
        self.table = MLSTable()

    def tearDown(self):
        self.table = None

    def test_tiebreakers(self):
        self.table.on_result(
            {'home': 'FC Test', 'away': 'Test United', 'score': '1 - 0'})
        self.table.on_result(
            {'home': 'Test United', 'away': 'FC Test', 'score': '2 - 1'})
        self.assertEqual(['FC Test', 'Test United'],
                         [team.name for team in self.table])


if __name__ == '__main__':
    unittest.main()
