class ExamException(Exception):
    pass


class Diff():

    def __init__(self, window=1,ratio=1):
        if type(window) != int:
            raise ExamException('The value of the window is not a integer')

        if window <= 0 or window > 2:
            raise ExamException('The window is negative')
        self.window = window
        if type(ratio) != int:
            raise ExamException('The value of the ratio is not a integer')
        if ratio == 0:
            raise ExamException("The ratio can't be 0")
        self.ratio=ratio
        
    def compute(self, data):
        if data is None:
            raise ExamException('No input data')

        if type(data) is not list:
            raise ExamException('Input type is not a list')

        if len(data) <= 1:
            raise ExamException('The list is empty or formed by a singol element')

        for i in data:
            if type(i) is str:
                raise ExamException('Values are not int or float')

        result = []
        for i in range(len(data) - 3):
                res = int((data[i+1] - data[i])/self.ratio)
                result.append(res) 
                
        return result

diff = Diff(2,2)
result = diff.compute([2,4,8,16])
print(result)
