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
        succ=None
        sum_suc=0
        
        #il valore corrente (t) non deve essere contato:
        #se osservo l'esempio n=3 ma divide per 2
        i=-1
        val_prec=None
        for item in data:
            if(val_prec!=None):
                succ=item-val_prec
                sum_suc+=succ
            val_prec=item
            i+=1

        if i==0:
            prediction=val_prec
            #raise Exception('Errore non posso fare una divisione per 0')
        else:
            prediction=val_prec+int(sum_suc/i)
            
        return prediction
