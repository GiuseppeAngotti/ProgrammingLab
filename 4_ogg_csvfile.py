class CSVFile():
    def __init__(self,name):
        self.name=name

    def get_data(self):
        list_list=[]
        file=open(self.name,'r')
        for line in file:
            #.strip('qualcosa') toglie prima le robe che non mi piacciono 
            elements=line.strip('\n').split(',')
            if elements[0]!='Date':
                list_list.append(elements)
        file.close()
        return list_list

#file_csv= CSVFile('shampoo_sales.csv')

#print('{}'.format(file_csv.get_data()))