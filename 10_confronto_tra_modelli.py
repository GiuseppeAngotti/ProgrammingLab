class Model():

    def fit(self,data):
        #Fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')
 
    def predict(self,data):
        #Predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')
 
#creo un oggetto IncrementModel che estende Model e implemento 
#la funzione predict()
class IncrementModel(Model):

    def __init__(self, finestra):
        #nel metodo costruttore della classe 
        #IncrementModel vado a sovrascrivere il metodo 
        #costruttore della classe Model
        super().__init__()
        self.finestra = finestra

    def controllo_data(self,data):
        if type(data) is not list:
            raise TypeError   
        if len(data)<=1:
            raise Exception('Errore la lunghezza del file deve essere >1')
        if data is None:
            #\' mi permette di stampare il carattere: '
            raise  Exception('non c\'è nessun input')
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
        mean_increment = sum_increments / (len(data)-1)
        return mean_increment
    
    def predict(self,data):
        increm_med=self.mean(data)
        prediction = data[-1] + increm_med        
        return prediction

    def evaluate(self, data):
        errors = []
        for i in range(len(data) - self.finestra):
            prediction = self.predict(data[i:i + self.finestra])
            #il meotodo abs() calcola il valore assoluto 
            #di un numero, elimina il segno negativo.
            error = abs(data[i + self.finestra] - prediction)
            #print(data[i + self.finestra])
            #print(prediction)
            #print(error)
            errors.append(error)
        return sum(errors) / len(errors)

class FitIncrementModel(IncrementModel):
    
    def fit(self,data):
        super().controllo_data(data)
        self.global_avg_increment = super().mean(data)

    def predict(self,data):
        super().controllo_data(data)
        increm_med=super().mean(data)
        prediction = data[-1] + (increm_med + self.global_avg_increment) / 2
        return prediction
     
##per poter fare le PROVE (in realtà non sono esatte)
values=[8, 19, 31, 41, 50, 52, 60, 67, 72, 72, 67, 72]
##questo è un dizionario e non va bene 
#values={'1':1}
##istanzio l'oggetto 'modello'
increment_model=IncrementModel(7)
#prediction=increment_model.predict(values[4:7])
#print(prediction)
valutazione_modello_senza_fit=increment_model.evaluate([ 67, 72, 72, 67, 72])
print(valutazione_modello_senza_fit)
print('-------------------------------------')
fitincrement_model=FitIncrementModel(7)
fitincrement_model.fit(values[:7])
#fit_prediction=fitincrement_model.predict(values)
#print(fit_prediction)
valutazione_modello_con_fit=fitincrement_model.evaluate([ 67, 72, 72, 67, 72])
print(valutazione_modello_con_fit)