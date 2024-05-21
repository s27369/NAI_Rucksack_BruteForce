def next_number(digits, base):
    next_digits = digits.copy()
    if (pointer := len(next_digits) - 1) <1:#albo zero>??
        return [0]
    while(next_digits[pointer] == base-1):
        next_digits[pointer] = 0
        pointer-=1
    if pointer>=0: next_digits[pointer]+=1
    return next_digits


# ----------------------------------------------------------

class Iterator:

    def __init__(self, num_digits, num_base):
        self.size = num_digits
        self.num_base = num_base
        self.digits = [0 for x in range(num_digits)]

    def next(self):
        yield self.digits
        self.digits = next_number(self.digits, self.num_base)
        while not all(element == 0 for element in self.digits):
            yield self.digits
            self.digits = next_number(self.digits, self.num_base)
        return