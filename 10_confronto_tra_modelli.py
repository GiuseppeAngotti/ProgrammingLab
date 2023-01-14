class Model():

    def __init__(self,finestra):
        if finestra is None or not isinstance(finestra,int) or finestra < 1:
            raise Exception('La lunghezza della finestra deve essere maggiore o uguale a 1.')
        self.finestra=finestra
 
    def fit(self,data):
        #Fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')
 
    def predict(self,data):
        #Predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')
 
#creo un oggetto IncrementModel che estende Model e implemento 
#la funzione predict()
class IncrementModel(Model):

    def controllo_data(self,data):
        if type(data) is not list:
            raise TypeError   
        if len(data)<=1:
            raise Exception('Errore la lunghezza del file deve essere >1')
        if data is None:
            raise  Exception("non c'è nessun input")
        for item in data:
            if type(item) is not int and type(item) is not float:
                raise TypeError


    def mean(self,data):
        self.controllo_data(data)
        sum_increments=0
        for i, item in enumerate(data):
            if i > 0:
                sum_increments += item - data[i-1]
        #incremento medio
        mean_increment = int(sum_increments / (len(data)-1))
        return mean_increment
    
    def predict(self,data):
        increm_med=self.mean(data)
        prediction = data[-1] + increm_med        
        return prediction

class FitIncrementModel(IncrementModel):
    
    def fit(self,data):
        super().controllo_data(data)
        self.global_avg_increment = super().mean(data)

    def predict(self,data):
        super().controllo_data(data)
        increm_med=super().mean(data)
        prediction = data[-1] + (increm_med + self.global_avg_increment) / 2
        return prediction
     
##per poter fare le PROVE
#values=[8, 19, 31, 41, 50, 52, 60]
##questo è un dizionario e non va bene 
#values={'1':1}
##istanzio l'oggetto 'modello'
#increment_model=IncrementModel()
#prediction=increment_model.predict(values[4:7])
#print(prediction)
#fitincrement_model=FitIncrementModel()
#fitincrement_model.fit(values[:4])
#fit_prediction=fitincrement_model.predict(values)
#print(fit_prediction)