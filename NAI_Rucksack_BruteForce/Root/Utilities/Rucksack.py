from abc import abstractmethod


class Rucksack:
    def __init__(self, capacity:int):
        self.capacity = int(capacity)

    def check_solution_weight(self, solution:list, sizes:list):
        if len(solution)!= len(sizes):
            raise ValueError("Length does not match")
        return sum([sizes[x] for x in range(len(solution)) if solution[x]==1])
    def check_solution_feasibility(self, solution:list, sizes:list) -> bool:
        return self.check_solution_weight(solution, sizes)<=self.capacity

    def check_solution_value(self, solution: list, vals: list):
        if len(solution) != len(vals):
            raise ValueError("Length does not match")
        return sum([vals[x] for x in range(len(vals)) if solution[x] == 1])

    def print_info(self, type, result, value, load, exec_time, counter=None):
        print(f"Method: {type}")
        print(f"Solution value: {value}")
        print(f"Solution load: {load}")
        print(f"Execution time: {exec_time}")
        if counter: print(f"Possible solutions checked : {counter}")
        print("Result (item_nr, size, value):")
        for element in result:
            print(element)
    @abstractmethod
    def solve(self, data):
        pass