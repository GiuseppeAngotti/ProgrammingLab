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
            return None
            
#file_csv= CSVFile('shampoo_sales.csv')

#file_csv.get_data()
