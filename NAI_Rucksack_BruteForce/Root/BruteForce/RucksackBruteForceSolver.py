from Root.Utilities.Rucksack import Rucksack
from Root.BruteForce.Iterator import Iterator
import time
class RucksackBruteForceSolver(Rucksack):
    def __init__(self, capacity: int):
        super().__init__(capacity)

    # Wypisujemy optymalny skład plecaka wyliczony przez algorytm wyczerpujący (brutalnej siły)
    # w postaci listy trójek [nr przedmiotu, size, value], jego całkowitą wartość i pojemność, liczbę
    # sprawdzonych zestawów oraz czas wykonania.
    def solve(self, dataset:dict, length:int):
        # dataset - a single dict of {number: {sizes:[...], vals:[...]}}
        iterator = Iterator(length, 2)
        feasible_solutions = []
        counter = 0
        start_time = time.time()
        for solution in iterator.next():
            # print(solution)
            if self.check_solution_feasibility(solution, dataset["sizes"]):
                feasible_solutions.append(solution)
            counter+=1

        best_solution = max(feasible_solutions, key=lambda solution: self.check_solution_value(solution, dataset["vals"]))
        exec_time = time.time()-start_time
        value = self.check_solution_value(best_solution, dataset["vals"])
        weight = self.check_solution_weight(best_solution, dataset["sizes"])
        result = [(x, dataset["sizes"][x], dataset["vals"][x]) for x in range(len(best_solution)) if best_solution[x]==1]
        self.print_info("Brute Force", result, value, weight, exec_time, counter)
        return result, value, weight, counter, exec_time