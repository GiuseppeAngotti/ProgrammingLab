class CSVFile: #definizione della classe

    def __init__(self, name): #inizializzo e setto attributo name
        self.name = name
        
        if not isinstance(self.name, str): #se il nome non è una stringa
            raise Exception("Eccezione con nome: '{}'".format(name)) #alzo l'eccezione
        
        
        self.can_read = True #variabile booleana che verifica si possa leggere
        
        try: #leggo una riga per verificare che il file non sia vuoto
            file = open(self.name, 'r')
            file.readline()
            
        except Exception as e: #a meno che non si possa leggere
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))

    def get_data(self, start=None, end=None): #definisco metodo get data
        
        if not self.can_read: #se il file non è leggibile
            print('Errore, file non aperto o illeggibile')
            return None #ritorno none ed esco da get data

        else: #altrimenti, se posso leggerlo
            data = [] #lista dove memorizzare i dati
            file = open(self.name, 'r') #apro file

            lines_in_file = open(file, 'r').readlines()

            if start>=end or end>len(lines_in_file) or start<0:
                raise Exception('Valori di start e/o end non validi')


            for line in file in range(start, end): #leggo linea per linea nell'intervallo
                
                elements = line.split(',') #divido dopo la virgola
                elements[-1] = elements[-1].strip() #elimino ultimo                        elemento
                
                #salto l'intestazione
                if elements[0] != 'Date':
                    data.append(elements) #aggiungo alla lista
            
            file.close() #chiudo il file
            
            return data #ritorno la lista dei dati


class NumericalCSVFile(CSVFile): #sottoclasse numericalCSVFile
    
    def get_data(self): #definisco metodo get data
        string_data = super().get_data() #estendo il metodo della classe             parent
        
        numerical_data = [] #lista per i dati
        
        for string_row in string_data: #leggo stringa per stringa
            
            numerical_row = [] #lista per gli elementi in formato numerico

            for i, element in enumerate(string_row): #contatore delle colonne
                
                if i == 0: #se sono nella colonna delle date
                    numerical_row.append(element)
                    
                else: #se siamo in un'altra riga qualsiasi
                    
                    try: #provo a convertire a float e aggiungere
                        numerical_row.append(float(element))
                        
                    except Exception as e: #a meno che non possa convertire
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break #esco dal for

            if len(numerical_row) == len(string_row): #vedo se ho                         processato tutti gli elementi
                numerical_data.append(numerical_row)

        return numerical_data


mio_file = CSVFile(name='shampoo_sales.csv')
print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: #"{}"'.format(mio_file.get_data(12, 26)))

mio_file_numerico = NumericalCSVFile(name='shampoo_sales.csv')
print('Nome del file: "{}"'.format(mio_file_numerico.name))
print('Dati contenuti nel file: "{}"'.format(mio_file_numerico.get_data()))