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
