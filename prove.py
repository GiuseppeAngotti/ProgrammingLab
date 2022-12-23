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

        if not self.can_read:
            print('Errore, file non aperto o illeggibile')
            return None
            
        else:
            list_list=[]
            file=open(self.name,'r')

            if start == 1:
                list_list=[]
            
            elif start is None:
                start=1
                if end is None:
                    for line in file:
                        elements=line.strip('\n').split(',')
                        if elements[0]!='Date':
                            list_list.append(elements)
                else:
                    for i, line in enumerate(file):
                        if i in range(1,(1+end)):
                            elements=line.strip('\n').split(',')
                            if elements[0]!='Date':
                                list_list.append(elements)
                
            else:
                start=start-1
                if end is None:
                    for i, line in enumerate(file):
                        if i>=start:
                            elements=line.strip('\n').split(',')
                            list_list.append(elements)
                else:
                    for i, line in enumerate(file):
                        if i in range(start,(1+end)):
                            elements=line.strip('\n').split(',')
                            list_list.append(elements)
            
            print(list_list)
            #for line in file in range(self.start,self.end):
                #print('start={}'.format(self.start))
                #elements=line.strip('\n').split(',')
                #list_list.append(elements)
                #print('{}'.format(list_list))
            file.close()
            if(len(list_list)==0):
                return None
            return(list_list)

class NumericalCSVFile(CSVFile):   
    def get_data(self):#, *args, **kwargs
        lista_lista=super().get_data()#*args, **kwargs
        if lista_lista!=None:
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
        
            
#file_csv= CSVFile('shampoo_sales.csv')
#file_csv.get_data(5)#end esplicito esempio end=5
#print('{}'.format(file_csv.get_data(1,4)))