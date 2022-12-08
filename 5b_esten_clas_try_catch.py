class CSVFile:
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
    def get_data(self):
        lista_lista=super().get_data()
        #print(lista_lista)
        for l in lista_lista:
            for i,item in enumerate(l):
                try:
                    if i!=0:
                        l[i]=float(item)
                        #print(isinstance(item[1],float))
                        #print('{}'.format(item[1]))
                except ValueError:
                    print('Errore il dato che si presumeva float non lo è! Lo ha generato: {}'.format(item))
                    #al posto di 'item' potevo mettere l[i] o l[1]
                except TypeError:
                    print('Errore hai sbagliato il tipo di dato!')
                except Exception as e:
                    print('Errore generico: {}'.format(e))
                
        return lista_lista
        
            
#file_csv= NumericalCSVFile('shampoo_sales.csv')

#file_csv.get_data()
