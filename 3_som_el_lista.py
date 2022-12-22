def isfloat(num):
    
    #il 'try' prova, riga per riga, tutte le istruzioni 
    #indentate. Nel nostro caso prova un casting, cioè la 
    #conversione a float del parametro generico 'num' e in 
    #seguito prova a restiturlo.
    #Se il 'try' va bene,cioè tutti i comandi indentati vengono 
    #eseguiti con esito positivo, si eseguono e si passa oltre, 
    #cioè si eseguono le istruzioni oltre l''except' e tutti i 
    #comandi indentati dentro l''except' (cioè si passa 'QUI')
    try:
        float(num)
        return num

        
    #L''except' viene eseguito nel caso il try non vada a buon 
    #fine e si esegue tutto quello che sta sotto ogni except.
    # 'except' può essere affiancato da una classe che comprende 
    #tutti gli errori; ovviamente ci sono delle sottoclassi per 
    #rientrare in una categoria di errori più specifica e 
    #aiutare il debug.
    #--------------------------------------------Nel nostro caso:
    #se non è andato tutto il codice indentato sotto il try, 
    #prova a vedere che non si tratti di un errore della classe 
    #'ValueError' (va controllare che un metodo riceva un 
    #argomento di tipo dati corretto ma con un valore 
    #inappropriato):
    #se è così ritornami 'None'
    except ValueError:
        return None

    #se non è andato ancora niente a buon fine, vado nella 
    #classe più generica (la quale contiene le altri 
    #sottoclassi) per capire di che errore (eccezione), si 
    #tratta: 
    #con 'as e' istanzio la mia classe Exception con il tipo di 
    #eccezione/errore che mi restituisce provando a eseguire il 
    #codice try. Quindi stampo l'ogetto 'e' (contenente 
    #l'eccezione) e ritorno 'None'
    except Exception as e:
        print('Ho avuto il seguente problema: {}'.format(e))
        return None

#QUI
def sum_csv(nome_file):

    #dichiarazione di un array
    values=[]

    #'open()' è un metodo built-in per aprire un file e si mette 
    #nome del file.estensione (in questo caso nome_file è un 
    #file generico, cioè il file vero è proprio è passato al 
    #metodo come parametro), la modalità in cui slo si vuole 
    #aprire (nel nostro caso è 'r' cioè read=lettura)
    file=open(nome_file,'r')  
    for line in file:

        #'split()' è un metodo built-in che serve a dividere 
        #delle robe in base a dove si vuol dividere. Esempio con         #la riga di codice sottostante:
        #30-08-2022,10000 
        #Dopo lo split(',')  avrò: 
        #30-08-2022                e                   10000
        #--------------------------------------------------------
        #'elements' è un array a due elementi (questo dipende 
        #dal file) in cui vado a inserire i valori splittati
        elements=line.split(',')

        #converto il mio valore a float, se possibile, con il 
        #mio metodo 
        v_f=isfloat(elements[1])
        if(v_f!= None):
            
            #'float()' è un metodo che casta gli argomenti 
            #all'interno SE POSSIBILE a float
            values.append(float(elements[1]))

    #'close()' è una funzione built-in che chiude il file che 
    #avevo aperto
    file.close()
    if(len(values)==0):
        return None

    #'sum()' è una funzione built-in che permette di sommare tutti gli elementi di una lista (in questo caso dell'array)
    return sum(values)

#risultato=sum_csv('shampoo_sales.csv')

#print('La somma degli elementi è uguale a: {}'.format(risultato))