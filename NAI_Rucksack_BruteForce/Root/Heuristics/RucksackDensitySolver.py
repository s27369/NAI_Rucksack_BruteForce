from Root.Utilities.Rucksack import Rucksack
import time
#remove and return key



class RucksackDensitySolver(Rucksack):
    def __init__(self, capacity: int):
        super().__init__(capacity)

    def solve(self, data, length):

        density = {i:data["vals"][i]/data["sizes"][i] for i in range(length)}
        load = 0
        solution=[0 for _ in range(length)]

        start_time = time.time()
        while (load<self.capacity) and len(density.items())>0:
            selected = max(density.items(), key=lambda pair: pair[1])[0]
            if data["sizes"][selected] <= (self.capacity-load):
                solution[selected]=1
                load+=data["sizes"][selected]
            density.pop(selected)

        exec_time = time.time() - start_time
        value = self.check_solution_value(solution, data["vals"])
        result = [(x, data["sizes"][x], data["vals"][x]) for x in range(len(solution)) if
                  solution[x] == 1]
        self.print_info("Heuristic method (density)", result, value, load, exec_time)
        return result, value, load, exec_time