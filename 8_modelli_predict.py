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
    def predict(self,data):
        if type(data) is not list:
            raise TypeError
      
        if len(data)<=1:
            raise Exception('Errore la lunghezza del file deve assere >1')
         
        succ=None
        sum_suc=0
        prediction=None
        #il valore corrente (t) non deve essere contato:
        #se osservo l'esempio n=3 ma divide per 2
        i=-1
        val_prec=None
        for item in data:
            if type(item) is not int and type(item) is not float:
                raise TypeError
            if(val_prec!=None):
                succ=item-val_prec
                sum_suc+=succ
            val_prec=item
            i+=1
        prediction=val_prec+int(sum_suc/i)
        
        return prediction
        
##per poter fare le PROVE
#values=[50,52,60]
##questo è un dizionario e non va bene 
#values={'1':1}
##istanzio l'oggetto 'modello'
#increment_model=IncrementModel()
#prediction=increment_model.predict(values)
#print(prediction)
