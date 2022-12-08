#'def' serve per creare una funzione, meglio chiamata metodo. 
#Dopo il nome del metodo e gli eventuali argomenti ci vanno i 
#due punti ':'
def sum_list(my_list):
    sum=0
    
    #dopo la condizione di un 'if' o di un 'elif' o 
    #semplicemente dopo l' 'else' ci vanno sempre i due punti ':'
    #'elif' è l'equivalente di else if
    #'len()' è una funzione 'built-in' che permette di avere la 
    #lunghezza di una lista
    if(len(my_list)==0):
        return None
        
    #il 'for' cicla ogni elemento ('item') nella ('in') mia lista
    #'in' è un operatore che permette di controllare se qualcosa 
    #sta in qualcos'altro
    for item in my_list:
        sum+=item
    return sum

list=[2,3,5]

risultato=sum_list(list)

#Il metodo format() formatta i valori specificati e li inserisce #all'interno del segnaposto della stringa.
#Il segnaposto è definito utilizzando parentesi graffe: {}. 
#Il metodo format() restituisce la stringa formattata.
#ESEMPIO_1:
#txt = "For only {price:.2f} dollars!"
#print(txt.format(price = 49))
#--------------------OUTPUT--------------------------------------
#For only 49.00 dollars!
#
#
#I segnaposto possono essere identificati utilizzando indici con nome {nome}, indici numerati {0} o anche segnaposti vuoti {}.
#ESEMPIO_2:
#indici con nome:
#txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#indici numerati:
#txt2 = "My name is {0}, I'm {1}".format("John",36)
#segnaposti vuoti:
#txt3 = "My name is {}, I'm {}".format("John",36)
#
#print(txt1)
#print(txt2)
#print(txt3)
#--------------------OUTPUT--------------------------------------
#My name is John, I'm 36
#My name is John, I'm 36
#My name is John, I'm 36

#In questo caso stampa quindi il contenuto dell'oggetto
#risultato 
print('La somma degli elementi è uguale a: {}'.format(risultato))