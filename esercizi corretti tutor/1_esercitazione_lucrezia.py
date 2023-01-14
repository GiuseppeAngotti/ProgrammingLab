class ExamException(Exception):
    pass


class MovingAverage():

    def __init__(self, window):
        if type(window) != int:
            raise ExamException('The value of the window is not a integer')

        if window <= 0:
            raise ExamException('The window is negative')

        self.window = window

    def compute(self, data):
        if data is None:
            raise ExamException('No input data')

        if type(data) is not list:
            raise ExamException('Input type is not a list')

        if len(data) == 0:
            raise ExamException('The list is empty')

        for i in data:
            if type(i) is str:
                raise ExamException('Values are not int or float')

        if len(data) < self.window:
            raise ExamException('The input data is shorter than the window')

        result = []
        for i in range(len(data) - self.window + 1):
            res = sum(data[i:i + self.window]) / self.window
            result.append(res)
        return result

#moving_average = MovingAverage(6)
#result = moving_average.compute([2,3,5,6,7,54,34])
#print(result)