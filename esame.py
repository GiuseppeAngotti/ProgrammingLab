class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self,lung):
        if lung < 1:
            raise ExamException('La lunghezza della finestra deve essere maggiore o uguale a 1.')
        self.lung=lung
        

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
        n_volte=lunghezza_lista-self.lung+1
        j=0
        for item in data:
            if n_volte!=j:
                i=0
                somma = 0
                while i<self.lung:
                    somma+=data[j+i]
                    i+=1
                elemento=somma/self.lung
                average_list.append(elemento)
                j+=1
        
        return average_list

moving_average = MovingAverage(4)
result = moving_average.compute([2,4,8,16,32])
print(result) # Deve stampare a schermo [3,6,12]