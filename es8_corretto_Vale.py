class Model():
    def fit(self, data):
        raise NotImplementedError("Metodo non implementato.")

    def predict(self, data):
        raise NotImplementedError("Metodo non implementato.")

class IncrementModel(Model):

    def _check_input_data(self, data):
        if type(data) is not list:
            raise TypeError
        if len(data) <= 1:
            raise Exception("La lunghezza del file deve essere > 1.")

    def predict(self, data):
        self._check_input_data(data)
        sum_increments = 0
        for i, item in enumerate(data):
            if i > 0:
                sum_increments += item - data[i-1]
        mean_increment = sum_increments / (len(data)-1)
        prediction = data[-1] + mean_increment
        return prediction

# # PROVE
# values = [50, 52, 60]
# # values = {'1': 1}
# increment_model = IncrementModel()
# print(increment_model.predict(values))