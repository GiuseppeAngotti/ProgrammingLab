class Diff():

    def __init__(self, ratio=1):     
        if ratio is None:
            raise ExamException("Errore: ratio è None.")
        if type(ratio) is not int and type(ratio) is not float:
            raise ExamException("Errre: ratio deve essere un intero o un float.")
        if ratio < 1:
            raise ExamException("Errore: ratio deve essere maggiore o uguale a 1.")
        else:
            self.ratio = ratio        

    def compute(self, serie):
        # conrolli sull'input
        if type(serie) is not list:
            raise ExamException(f'Errore: l\'input di compute deve essere una lista e non {type(serie)}.')
        elif len(serie) <= 1:
            raise ExamException(f'Errore: la serie deve avere almeno due valori.')
        else:
            for valore in serie:
                if type(valore) is str and valore.isnumeric() is False:
                    raise ExamException(f"Errore: la serie contiene il valore non numerico {valore}.")

        # calcolo media mobile
        lista_differenze = []
        for i in range(len(serie)-1):
            differenza = (serie[i+1] - serie[i]) / self.ratio
            lista_differenze.append(differenza)
        return lista_differenze

class ExamException(Exception):
    pass