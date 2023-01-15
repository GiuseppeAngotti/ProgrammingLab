class ExamException(Exception):
    pass


class Diff():

    def __init__(self,ratio=1):
        if type(ratio) is not int and type(ratio) is not float:
            raise ExamException("Errre: ratio deve essere un intero o un float.")
        if ratio < 1:
            raise ExamException("Errore: ratio deve essere maggiore o uguale a 1.")
        if ratio is None:
            raise ExamException("Errore: ratio è None.")
        self.ratio=ratio
        
    def compute(self, data):
        if data is None:
            raise ExamException('No input data')
        if type(data) is not list:
            raise ExamException('Input type is not a list')

        if len(data) <= 1:
            raise ExamException('The list is empty or formed by a singol element')
            
        for valore in data:
            if type(valore) is str and valore.isnumeric() is False:
                #mettendo una f davanti alla stringa 
                #posso stampare il valore "formattare" i 
                #valori dentro {}
                raise ExamException(f"Errore: la serie contiene il valore non numerico {valore}.")

        lista_differenze = []
        for i in range(len(data) - 1):
                res = (data[i+1] - data[i])/self.ratio
                lista_differenze.append(res) 
                
        return lista_differenze
