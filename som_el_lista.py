def isfloat(num):
    try:
        float(num)
        return num
    except ValueError:
        return None
def sum_csv(nome_file):
    values=[]
    file=open(nome_file,'r')  
    for line in file:
        elements=line.split(',')
        v_f=isfloat(elements[1])
        if(v_f!= None):
            values.append(float(elements[1]))
    file.close()
    if(len(values)==0):
        return None
    return sum(values)


#risultato=sum_csv('vuoto.csv')

#print('La somma degli elementi è uguale a: {}'.format(risultato))