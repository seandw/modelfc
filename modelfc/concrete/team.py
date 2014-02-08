"""
Concrete classes used in the model.
"""

class Team(object):
    """
    A team representation with modifiable value and metadata.
    """

    def __init__(self, name, *, value=0, **stats):
        self.name = name
        self.value = value
        self.stats = dict(stats)

    def modify(self, value, **stats):
        """
        A catchall method to add value and statistics.
        """
        self.value += value
        for (key, value) in stats.items():
            self.stats[key] += value

    def __getitem__(self, key):
        return self.stats[key]

    def __repr__(self):
        stats_str = ' '.join('{0:s}={1:d}'.format(key, value)
                             for (key, value) in self.stats.items())
        return '[Team {0:s}: {1:d}, {2:s}]'.format(self.name,
                                                   self.value, stats_str)
