class Model():

    def fit(self, data):
        raise NotImplementedError("Metodo non implementato.")

    def predict(self, data):
        raise NotImplementedError("Metodo non implementato.")


class IncrementModel(Model):

    def __init__(self, finestra):
        super().__init__()
        self.finestra = finestra

    def _check_input_data(self, data):
        if type(data) is not list:
            raise TypeError
        if len(data) <= 1:
            raise Exception("La lunghezza del file deve essere > 1.")

    def _compute_mean_increment(self, data):
        sum_increments = 0
        for i, item in enumerate(data):
            if i > 0:
                sum_increments += item - data[i-1]
        mean_increment = sum_increments / (len(data)-1)
        return mean_increment

    def predict(self, data):
        self._check_input_data(data)
        mean_increment = self._compute_mean_increment(data)
        prediction = data[-1] + mean_increment
        return prediction

    def evaluate(self, data):
        errors = []
        for i in range(len(data)-self.finestra):
            prediction = self.predict(data[i:i+self.finestra])
            error = abs(data[i+self.finestra] - prediction)
            errors.append(error)
        return sum(errors) / len(errors)      

 
class FitIncrementModel(IncrementModel):

    def __init__(self, finestra):
        super().__init__(finestra)
        self.global_avg_increment = None

    def predict(self, data):
        super()._check_input_data(data)
        mean_increment = super()._compute_mean_increment(data)
        prediction = data[-1] + (mean_increment + self.global_avg_increment) / 2
        return prediction

    def fit(self, data):
        super()._check_input_data(data)
        self.global_avg_increment = super()._compute_mean_increment(data)

##per poter fare le PROVE (in realtà non sono esatte)
values=[8, 19, 31, 41, 50, 52, 60, 67, 72, 72, 67, 72]
##questo è un dizionario e non va bene 
#values={'1':1}
##istanzio l'oggetto 'modello'
increment_model=IncrementModel(7)
#prediction=increment_model.predict(values[4:7])
#print(prediction)
valutazione_modello_senza_fit=increment_model.evaluate([8, 19, 31, 41, 50, 52, 60, 67, 72, 72, 67, 72])
print(valutazione_modello_senza_fit)
print('-------------------------------------')
fitincrement_model=FitIncrementModel(7)
fitincrement_model.fit(values[:7])
#fit_prediction=fitincrement_model.predict(values)
#print(fit_prediction)
valutazione_modello_con_fit=fitincrement_model.evaluate([8, 19, 31, 41, 50, 52, 60, 67, 72, 72, 67, 72])
print(valutazione_modello_con_fit)