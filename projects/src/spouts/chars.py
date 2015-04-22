from __future__ import absolute_import, print_function, unicode_literals

import itertools
from streamparse.spout import Spout


class CharSpout(Spout):

    def initialize(self, stormconf, context):
        self.words = itertools.cycle(['dog', 'cat',
                                      'zebra', 'elephant'])

    def next_tuple(self):
        word = next(self.words)
        for c in word:
            self.emit([c])
