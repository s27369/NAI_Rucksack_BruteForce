from BruteForce.RucksackBruteForceSolver import RucksackBruteForceSolver
from Heuristics.RucksackDensitySolver import RucksackDensitySolver
from Utilities.Util import *
import random
data_filepath = "./Data/plecak.txt"
num_of_times_item_can_be_taken = 1

def interface(data, rbf, rds, length):
    r = input("1 - Random dataset\nq - quit\n>>>")
    while r.lower()!="q":
        if r=="1":
            i = random.randint(min(data.keys()), max(data.keys()))
            print(f"Dataset {i}")
            rds.solve(data[i], length)
            rbf.solve(data[i], length)
        else:
            print("Incorrect input")
            r = input("1 - Random dataset\nq - quit\n>>>")

if __name__=="__main__":

    file = read_file(data_filepath)
    # print(*handle_data_str(file), sep="\n")
    try:
        length, capacity, data = handle_data_str(file)
    except ValueError:
        print("Data incorrect")
        quit()

    rbf = RucksackBruteForceSolver(capacity)
    rds = RucksackDensitySolver(capacity)
    # test_data = {
    # "sizes": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    # "vals": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # }
    # rds.solve(test_data, len(test_data["vals"]))
    # rbf.solve(test_data, len(test_data["vals"]))

    interface(data, rbf, rds, length)