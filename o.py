def sum_csv(nome_file):
    somma=0.0 
    file=open(nome_file,'r') 
    for line in file:
        elements=line.split(',')
        if elements[0]=='Date':
            continue
        else:
            try:    
                somma=somma+float(elements[1])
            except ValueError:
                return None
    if(somma==0.0):
        return None
    return somma


#risultato=sum_csv('shampoo_sales.csv')

#print('La somma degli elementi è uguale a: {}'.format(risultato))