from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt


class CharCounter(Bolt):
    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        char = tup.values[0]
        self.counts[char] += 1
        self.emit([char, self.counts[char]])
        self.log('%s: %d' % (char, self.counts[char]))
