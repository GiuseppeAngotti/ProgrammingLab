def sum_csv(shampoo_sales):
    #creo una lista vuota per poter aggiungere di volta in volta i valori che mi servono dal file
    values=[] 
    #apro il file su cui voglio lavorare in lettura e lo assegno all'oggetto file
    file=open('shampoo_sales.csv','r') 

    sum=0
    
    #eseguo un ciclo linea per linea del mio file, poichè è considerato come una stringa 
    for line in file:
        #avendo disposto gli elementi del file in due colonne (data e shampii venduti) divido le informazioni e le assegno alla lista elements)
        elements=line.split(',')
        #se il primo elemento della lista non è la mia intestazione della colonna salvo in una variabile d'appoggio (value) il valore delle vendite contenuto come info nella seconda colonna del file e quindi nel secondo elemento della lista elements (ecco il perché dell'indice 1 di elements)
        if elements[0]!='Date':
            value=elements[1]
            #aggiungo il valore che mi interessa e lo casto a tipo float (altrimenti sarebbe considerato come stringa) nella mia lista values
            values.append(float(value))
    file.close()
    if(len(values)==0):
        return None
    for item in values:
        sum+=item
    return sum


risultato=sum_csv('shampoo_sales.csv')

print('La somma degli elementi è uguale a: {}'.format(risultato))