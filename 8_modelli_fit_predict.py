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
        i=0
        val_prec=None
        for item in data:
            if(val_prec!=None):
                succ=item-val_prec
                sum_suc+=succ
            val_prec=item
            i+=1
        
        prediction=val_prec+sum_suc/i
        return prediction