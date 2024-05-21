from abc import abstractmethod


class Rucksack:
    def __init__(self, capacity):
        self.capacity = capacity

    def check_solution_feasibility(self, solution:list, sizes:list) -> bool:
        if len(solution)!= len(sizes):
            raise ValueError("Length does not match")
        load = sum([sizes[x] for x in range(len(solution)) if solution[x]==1])
        return load<=self.capacity

    def check_solution_value(self, solution:list, vals:list):
        if len(solution)!= len(vals):
            raise ValueError("Length does not match")
        return [vals[x] for x in range(len(vals)) if solution[x]==1]

    @abstractmethod
    def solve(self, data):
        pass