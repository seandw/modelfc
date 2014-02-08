"""
A module with the abstract classes used in the model.
"""
from abc import ABCMeta, abstractmethod

class Table(metaclass=ABCMeta):
    """
    An abstract table, responsible for collecting all teams and
    modifying their point values based off of results.
    """

    def __init__(self):
        self.table = dict()

    def __iter__(self):
        """
        Returns an iterator of sorted teams based off of tiebreakers.
        """
        return sorted(self.table.values(), key=self.tiebreakers,
                      reverse=True).__iter__()

    @abstractmethod
    def on_result(self, result):
        """
        Abstract method that modifies the table based off the result input.
        """
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def tiebreakers(team):
        """
        Abstract method that orders team stats for sorted() to sort with.
        """
        raise NotImplementedError()

    def __str__(self):
        return '\n'.join(str(team) for team in self)

    def __repr__(self):
        return '[Table {0:d} teams]'.format(len(self.table))
