from abc import abstractmethod


class Rucksack:
    def __init__(self, capacity):
        self.capacity = capacity

    def check_solution_for_feasibility(self, solution:list, sizes:list) -> bool:
        if len(solution)!= len(sizes):
            raise ValueError("Length does not match")
        load = 0
        for i in range(len(solution)):
            if solution[i]==1:
                load+=sizes[i]
        if load>self.capacity:
            return False
        return True

    @abstractmethod
    def solve(self, data):
        pass