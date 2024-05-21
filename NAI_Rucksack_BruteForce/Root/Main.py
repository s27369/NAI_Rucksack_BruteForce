from BruteForce.Iterator import Iterator
from Heuristics.RucksackDensitySolver import RucksackDensitySolver
from Utilities.Util import *
data_filepath = "./Data/plecak.txt"
num_of_times_item_can_be_taken = 1
if __name__=="__main__":

    file = read_file(data_filepath)
    # print(*handle_data_str(file), sep="\n")
    try:
        length, capacity, data = handle_data_str(file)
    except ValueError:
        print("Data incorrect")
        quit()


    iterator = Iterator(length, num_of_times_item_can_be_taken+1)
    #
    # for solution in iterator.next():