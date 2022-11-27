class CSVFile():
    def __init__(self,name):
        self.name=name

    def get_data(self):
        list_list=[]
        try:
            file=open(self.name,'r')
            for line in file:
                elements=line.strip('\n').split(',')
                if elements[0]!='Date':
                    list_list.append(elements)
            file.close()
            return(list_list)
        except:
            print('Errore il file che stavi cercando non esiste')

class NumericalCSVFile(CSVFile):   
    def conv_float(self):
        lista_lista=super().get_data()
        for i in lista_lista:
            try:
                i[1]=float(i[1])
                #print(isinstance(i[1],float))
                print('{}'.format(i[1]))
            except ValueError:
                print('Errore 1il dato che si presumeva float non lo è!')
            except TypeError:
                print('Errore 2il dato che si presumeva float non lo è!')
            
file_csv= NumericalCSVFile('shampoo_sales.csv')

file_csv.conv_float()
