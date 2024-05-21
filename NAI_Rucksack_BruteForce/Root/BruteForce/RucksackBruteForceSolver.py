from Root.Utilities.Rucksack import Rucksack
from Iterator import Iterator
class RucksackBruteForceSolver(Rucksack):
    def __init__(self, capacity: list, iterator: Iterator):
        super().__init__(capacity)
        self.iterator = iterator

    def solve(self, dataset:dict):
        pass