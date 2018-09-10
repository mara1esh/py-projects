#class Buffer, which will accumulate the elements of the sequence and output the sum of the five consecutive elements as they accumulate

class Buffer:
    def __init__(self):
        self.container = []
        self.part = []

    def add(self, *a):
        SUM_FOR_APPEND = 5
        for i in a:
            self.container.append(i)
            if len(self.container) is SUM_FOR_APPEND:
                self.part.append(sum(self.container))
                sum_part = self.part[0]
                print(sum_part)
                self.part = []
                self.container = []

    def get_current_part(self):
        return self.container
