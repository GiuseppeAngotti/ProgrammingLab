class ExamException(Exception):
    pass


class CSVTimeSeriesFile:

    def __init__(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise ExamException('Il nome del file non è una stringa')
    def check_open_file(self):
        try:
            file = open(self.name, 'r')
            file.readline()
        except ExamException as e:
            raise ExamException('Errore in apertura del file: {}\n'.format(e))                
    def get_data(self):
        list_list=[]
        c=0
        self.check_open_file()
        file = open(self.name, 'r')
        if file is None:
            raise ExamException('Il file è vuoto')
        for line in file:
            elements=line.strip('\n').split(',')
            try:
                elements[1]=int(elements[1])
            except Exception:
                continue
            if elements[1]<0:
                continue
            try:
                date=elements[0].split('-')
            except Exception:
                continue
            if not date[0].isdigit() or not date[1].isdigit():
                continue
                
            date[0]=int(date[0])
            date[1]=int(date[1])
            real_month=range(1,13)
            if (date[1] not in real_month):
                raise ExamException('I mesi vanno da da 01 a 12')
            if c==0:
                current_year = date[0]
                current_month = date[1]
                c+=1
            else:
                if date[0] == current_year:
                    if date[1] <= current_month:
                        raise ExamException('I mesi non sono ordinati o sono presenti duplicati')
                    else:
                        current_month = date[1]
                else:
                    if date[0] - current_year != 1:
                        raise ExamException('Le date non sono ordinate o sono presenti duplicati')
                    else:
                        current_year = date[0]
                        current_month = date[1]
                        
            list_list.append(elements[0:2])
        print(list_list)    
        
        return list_list


def detect_similar_monthly_variations(time_series, years):
    if type(years) is not list:
        raise ExamException('Cio che si è passato non è  una lista')
    if len(years)!=2:
        raise Exception("La lunghezza della lista deve essere uguale a 2")
    for i,item in enumerate(years):
        if not isinstance(item, int):
            raise ExamException("I valori all'interno della lista non sono di tipo intero")
        if i==0:
            f_year=item
        else:
            s_year=item
            
    list_check_year=[]
    for elements in time_series:
        date=elements[0].split('-')
        date[0]=int(date[0])
        list_check_year.append(date[0])
    if f_year not in list_check_year or s_year not in list_check_year:
        raise ExamException('Gli anni da controllare non sono presenti nel file')
    if s_year-f_year!=1:
        raise ExamException('I due anni non sono consecutivi')
        
    f_year_variation_list = []
    s_year_variation_list = []

    i=1
    y=1
    for elements in time_series:
        date=elements[0].split('-')
        date[0]=int(date[0])
        date[1]=int(date[1])
        if f_year == date[0]:
            while(i!=date[1]):
                f_year_variation_list.append(None)
                i+=1
            f_year_variation_list.append(elements[1])
            i+=1
            
        if s_year == date[0]:
            while(i<13):
                f_year_variation_list.append(None)
                i+=1
            while(y!=date[1]):
                s_year_variation_list.append(None)
                y+=1
            s_year_variation_list.append(elements[1])
            y+=1
    while(y<13):
            s_year_variation_list.append(None)
            y+=1
    f_y_sub=[]
    s_y_sub=[]
    for i in range(13):
        if i== 0:   
            first_y_subtracting = f_year_variation_list[i]
            second_y_subtracting = s_year_variation_list[i]
        elif i<12:
            try:
                x=f_year_variation_list[i]-first_y_subtracting
                f_y_sub.append(x)
                first_y_subtracting = f_year_variation_list[i]
            except Exception:
                f_y_sub.append(None)
                first_y_subtracting = f_year_variation_list[i]
                    
            try:
                y=s_year_variation_list[i]-second_y_subtracting
                s_y_sub.append(y)
                second_y_subtracting = s_year_variation_list[i]
            except Exception:
                s_y_sub.append(None)
                second_y_subtracting = s_year_variation_list[i]
    var=[]
    for k in range(12):
        if k == 0:   
            var_subtracting = f_y_sub[k]

        elif k<12:
            try:
                v=s_y_sub[k-1]-var_subtracting
                if v in range(-2,3):
                    var.append(True)
                else:
                    var.append(False)
                if k!=11:
                    var_subtracting = f_y_sub[k]
            except Exception:
                var.append(False)
                if k!=11:
                    var_subtracting = f_y_sub[k] 
                
        

    print(f_year_variation_list)
    print(s_year_variation_list)

    print(f_y_sub)
    print(s_y_sub)

    print(var)
    return var


time_series_file = CSVTimeSeriesFile(name='ordine_duplicati.csv')
time_series = time_series_file.get_data()

years = [1949,1950]
detect_similar_monthly_variations(time_series, years)