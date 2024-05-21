from Root.Utilities.Rucksack import Rucksack
from Iterator import Iterator
class RucksackBruteForceSolver(Rucksack):
    def __init__(self, capacity: list):
        super().__init__(capacity)

    # Wypisujemy optymalny skład plecaka wyliczony przez algorytm wyczerpujący (brutalnej siły)
    # w postaci listy trójek [nr przedmiotu, size, value], jego całkowitą wartość i pojemność, liczbę
    # sprawdzonych zestawów oraz czas wykonania.
    def solve(self, dataset:dict, length:int) -> list:
        # dataset - a single dict of {number: {sizes:[...], vals:[...]}}
        iterator = Iterator(length, 2)
        feasible_solutions = [solution for solution in iterator.next() if self.check_solution_feasibility(solution, dataset["sizes"])]
        return max(feasible_solutions, key=lambda solution: self.check_solution_value(solution, dataset["vals"]))