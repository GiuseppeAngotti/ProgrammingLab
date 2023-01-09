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
        if len(data)<=1:
            raise Exception('Errore non posso prevedere dei dati avendo solo un valore')
            
        succ=None
        sum_suc=0
        prediction=None
        
        #il valore corrente (t) non deve essere contato:
        #se osservo l'esempio n=3 ma divide per 2
        i=0
        val_prec=None
        for item in data:
            if type(item)!=int:
                raise TypeError('Il tipo di dati inserito non va bene')
            if(val_prec!=None):
                succ=item-val_prec
                sum_suc+=succ
            val_prec=item
            i+=1

            #raise Exception('Errore non posso fare una divisione per 0')
        prediction=val_prec+int(sum_suc/i)
            
        return prediction
