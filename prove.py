class CSVFile:
    def __init__(self,name):

        if isinstance(name, str):
            self.name=name
        else:
            raise Exception('Il nome del file non è una stringa')
            
        self.can_read=True
        
        try:
            file=open(self.name,'r')
            file.readline()
        except Exception as e:
            self.can_read=False
            print('Errore in apertura del file: {}\n'.format(e))

    def get_data(self, start=None, end=None):
        self.start=start
        self.end=end

        if self.start==None:
            self.start=1
        if self.end==None:
            self.end=-1
            
        if not self.can_read:
            raise Exception('Errore, file non aperto o illeggibile')
            return None
            
        else:
            list_list=[]
            file=open(self.name,'r')
            for line in file:
                elements=line.strip('\n').split(',')

                list_list.append(elements)
            file.close()
            if(len(list_list)==0):
                raise Exception('Il file è vuoto')
            return(list_list)

class NumericalCSVFile(CSVFile):   
    def get_data(self):
        lista_lista=super().get_data()
        #print(lista_lista)
        for l in lista_lista:
            for i,item in enumerate(l):
                if i!=0:
                    if item!='Sales':
                        try:
                                l[i]=float(item)
                                #print(isinstance(item[1],float))
                                #print('{}'.format(item[1]))
                        except ValueError:
                            print('Errore il dato che si presumeva float non lo è! Lo ha generato: {}'.format(l[i]))
                        except TypeError:
                            print('Errore hai sbagliato il tipo di dato!')
                        except Exception as e:
                            print('Errore generico: {}'.format(e))
                
        return lista_lista
        
            
file_csv= NumericalCSVFile('vuoto.csv')

print('{}'.format(file_csv.get_data()))