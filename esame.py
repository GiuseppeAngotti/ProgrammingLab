class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self,finestra=None):
        if finestra is None or not isinstance(finestra,int) or finestra < 1:
            raise ExamException('La lunghezza della finestra deve essere maggiore o uguale a 1.')
        self.finestra=finestra
        

    def controllo_input(self, data):
        if type(data) is not list:
            raise ExamException('Errore, in input non è stata inserita una lista')
        if len(data) < 1:
            raise ExamException('La lunghezza della lista deve essere maggiore o uguale a 1.')
        
    def compute(self,data):
        self.controllo_input(data)

        lunghezza_lista=len(data)
        average_list=[]
        elemento=None
        n_volte=lunghezza_lista-self.finestra+1
        j=0
        for item in data:
            if n_volte!=j:
                i=0
                somma = 0
                while i<self.finestra:
                    if type(data[j+i]) is not float and type(data[j+i]) is not int:
                        raise ExamException('Gli elementi della lista devono essere o float o intero')
                    somma+=data[j+i]
                    i+=1
                elemento=somma/self.finestra
                average_list.append(elemento)
                j+=1
        
        return average_list

moving_average = MovingAverage(3)
result = moving_average.compute([2,4,8,16,32])
print(result) # Deve stampare a schermo [3,6,12]
