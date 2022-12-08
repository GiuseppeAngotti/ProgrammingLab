#'class'+ 'nome della classe' + ':' permette di creare una classe
class CSVFile:
    #self è usato come collegamento a ciascuna istanza della 
    #classe. Esempio:
    #ho creato l'istanza della classe, file_csv
    #-----------------------------------------------------------
    #__init__() è il metodo costruttore di una classe, cioè 
    #contiene tutti gli attributi e metodi fondamentali alla 
    #classe
    #----------------------------------------------------------
    #In generale tutti quei metodi __nome del metodo__ sono dei 
    #metodi built-in. Un altro esempio è __string__
    def __init__(self,name):
        self.name=name

    def get_data(self):
        list_list=[]
        file=open(self.name,'r')
        for line in file:
            #'strip()' è un metodo built-in che toglie quello 
            #che è indicato tra le parentesi. In questo caso 
            #tutti gli 'a capo' che vengono visualizzati a 
            #schermo come '\n'
            elements=line.strip('\n').split(',')
            if elements[0]!='Date':

                #'append()' è un metodo built-in che permette di 
                #aggiungere un elemento in coda alla lista
                list_list.append(elements)
        file.close()
        return list_list

#file_csv= CSVFile('shampoo_sales.csv')

#print('{}'.format(file_csv.get_data()))