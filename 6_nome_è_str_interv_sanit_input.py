#definizione dell'oggetto (categoria): files di tipo CSV;
#quindi creazione della classe CSVFile per indicare tale 
#categoria 
class CSVFile():

    #creazione del metodo costruttore: 
    #    gli passo come argomento il nome del mio file su cui 
    #    devo lavorare
    def __init__(self,name):

        #verifico che il nome del file che passo sia una stringa
        if isinstance(name, str):
            #VERO:  creo un nuovo attributo per salvare il nome
            #       del file
            self.name=name
        else:
            #FALSO: alzo un eccezione in cui termina  
            #       l'esecuzione del mio codice e stampa a 
            #       schermo 'Errore'
            raise Exception('Il nome del file non è una stringa')
            
        #creo un attributo booleano per memorizzare il successo 
        #o meno dell'apertura di un file, soprattutto per sapere 
        #nelle classi estese o in altri metodi se il mio file è 
        #stato: aperto o non aperto    
        self.can_read=True

        #provo ad aprire il file e leggere una linea
        try:
            #creo un oggetto di nome 'file' che nel caso in cui 
            #il file esiste contiene tutto il contenuto del file 
            #in formato stringa
            file=open(self.name,'r')

            #chiamo un metodo built-in che legge una linea del
            #file (anche nel caso in cui il file è vuoto)
            file.readline()

        #se non vanno quelle due istruzioni (che servivano a 
        #vedere se il file esiste) succede questo:
        except Exception as e:

            #resetto il mio attributo a Falso (cioè non sono 
            #riuscito ad aprire il file) 
            self.can_read=False

            #continuo l'esecuzione del codice ma stampando a 
            #schermo l'errore che lo ha generato
            print('Errore in apertura del file: {}\n'.format(e))

    #(sapendo che il mio file è organizato in righe e       
    #colonne, dove ogni colonna ha un informazione) definisco     #un metodo che divide i dati e li memorizza, eliminando       #l'intestazione. Opzionalmente si può selezionare da che      #riga iniziare o finire per memorizzare i dati
    def get_data(self, start=None, end=None):

       #In generale 'if' quando ha una condizione con un solo 
        #elemento, verifica se questo elemento sia vero 
        #(elemento==True?). (Se l'elemento non è booleano è 
        #impostato a 'TRUE')
        #-----------------------------------------------------
        #not nega il significato booleano
        #-----------------------------------------------------
        #nel nostro caso chiedo se l'attributo del metodo 
        #costruttore durante l'istanzanziamento di un oggetto 
        #è uguale a 'False' cioè se il file si può aprire             #oppure no
        if not self.can_read:

            #il file non poteva essere aperto o era 
            #illeggibile e quindi stampo un errore e 
            #restituisco None
            print('Errore, file non aperto o illeggibile')
            return None
            
        else:
            #sono riuscito ad aprire il mio file e a leggerlo;
            #quindi riapro il file, lo converto a stringa e 
            #lo divido dalla prima all'ultima riga o in base 
            #alle righe:  riga di partenza e/o riga finale e
            #salvo tutte queste informazioni. Le info le 
            #salvo in un array di array (nel mio caso                     #l'elemento array ha due elementi: data e 
            #acquisti). Cioè creo così una lista di liste.   
            
            file=open(self.name,'r')
            list_list=[]

            #questa variabile conterrà il numero massimo di               #righe quindi di elementi che ho all'interno del              #mio file; quindi potrò confrontarla con il 
            #valore, se passato, dell'ultima riga alla quale
            #si vuole arrivare.
            n_max=0

            #conto tutte le righe attraverso un ciclo
            for line in file:
                    n_max=n_max+1

            #qui faccio un po' di sanitizazzione del mio input
            #e dove posso convertirlo a stringa lo faccio

            #isdigit() è un metodo built-in che verifica se               #una stringa contiene una cifra; restituisce TRUE             #se tutti caratteri sono cifre, FALSE altrimenti.             #ATTENZIONE PERO' se la stringa è così composta:              #'5.5' NON E' CONSIDERATA COME VALORE FLOAT e                 #pertanto restituisce FALSE.
            #---------------------------------------------
            #qui verifico che se l'input inserito per start è 
            #stringa ed è una cifra lo converto a intero
            if type(start) is str and start.isdigit():
                start = int(start)

            #qui verifico che se l'input inserito per start è 
            #intero o di tipo float lo converto a intero
            elif type(start) is int or type(start) is float:
                start = int(start)

            #qui verifico che se l'input inserito per start 
            #non è nemmeno None (end e start sono impostati a 
            #None di default nel caso non fossero inseriti) 
            #alzo un'eccezione
            elif start is not None:
                raise Exception("Non riesco a contertire start in intero")

            #qui verifico che se l'input inserito per end è 
            #stringa ed è una cifra lo converto a intero
            if type(end) is str and end.isdigit():
                end = int(end)

            #qui verifico che se l'input inserito per end è 
            #intero o di tipo float lo converto a intero    
            elif type(end) is int or type(end) is float:
                end = int(end)

            #qui verifico che se l'input inserito per end 
            #non è nemmeno None alzo un'eccezione
            elif end is not None:
                raise Exception("Non riesco a contertire end in intero")

            #qui verifico che se l'input inserito per end e 
            #start non è None e il valore di end è minore di 
            #start alzo un'eccezione
            if start is not None and end is not None and start>end:
                raise Exception('Errore: start è maggiore di end')

            #Le righe per traccia e/o per logica vanno al più 
            #da 1 (intestazione) al massimo fino all'ultima
            #(n_max).
            #-------------------------------------------------
            #qui verifico che se l'input inserito per start 
            #non è None e il valore di start è minore o uguale
            #a zero alzo un'eccezione.
            if start is not None and start<=0:
                raise Exception('Il parametro start "{}" non ha un indice accettabile; è sotto il minimo(1) '.format(start))

            #qui verifico che se l'input inserito per start 
            #non è None e il valore di start è maggiore al 
            #massimo numero di righe alzo un'eccezione.
            if start is not None and start>n_max:
                raise Exception('Il parametro start "{}" non ha un indice accettabile; va oltre il massimo ({})'.format(start,n_max))

            #qui verifico che se l'input inserito per start 
            #non è None e il valore di start è maggiore al 
            #massimo numero di righe alzo un'eccezione.
            if end is not None and end>n_max:
                raise Exception('Il parametro end "{}" non ha un indice accettabile; va oltre il massimo ({})'.format(end,n_max))

            #qui verifico che se l'input inserito per end 
            #non è None e il valore di start è minore o uguale
            #a zero alzo un'eccezione.
            if end is not None and end<=0:
                raise Exception('Il parametro end "{}" non ha un indice accettabile; è sotto il minimo(1)'.format(end))

            #ora distinguo i vari casi
            if start is None:
                file=open(self.name,'r')
                if end is None:
                    #qui stampo tutto
                    for line in file:
                        elements=line.strip('\n').split(',')
                        if elements[0]!='Date':
                            list_list.append(elements)
                else:
                    
                    #qui stampo l'array vuoto perché 
                    #l'intestazione non va stampata per 
                    #traccia
                    if end==1:
                        list_list=[]
                    else:

                        #stampo dalla prima riga alla riga 
                        #indicata
                        for i, line in enumerate(file):
                            if i<end:
                                elements=line.strip('\n').split(',')
                                if elements[0]!='Date':
                                    list_list.append(elements)
            else:

                file=open(self.name,'r')

                #qui verifico se sia start che end abbiano 
                #valore uguale a 1 e stampo quindi niente 
                #(per via dell'intestazione)
                if start==1:
                    if end==1:
                        file.close()
                        return(list_list)
                    else:
                        
                        #se l'comunque start è 1 e end non è                          #uguale a 1, salto l'intestazione     
                        #sommando 1
                        start=start+1
                
                if end is None:
                    
                    #se start non è 1 stampo dal valore di 
                    #start fino alla fine
                    for i, line in enumerate(file):
                        if i>=start-1:
                            elements=line.strip('\n').split(',')
                            if elements[0]!='Date':
                                list_list.append(elements)
                else:

                    #qui stampo dal valore di start al valore 
                    #di end
                    for i, line in enumerate(file):
                        if i>=start-1 and i<end:
                            elements=line.strip('\n').split(',')
                            if elements[0]!='Date':
                                list_list.append(elements)

            file.close()
            return(list_list)
            
#essendo NumericalCSVFile una classe estesa dalla classe 
#CSVFile essa eredita soltanto la milioria del controllo del 
#nome del file se è una stringa solamente perché è dichiarata 
#nel metodo costruttore; quindi non funziona il controllo di 
#start ed end. Se si vuole inserire questa miglioria o la si 
#mette 'manualmente', passando come argomenti end e start e 
#passandoli quando si chiama nella super oppure c'è un modo 
#più generico di fare le cose che eredità tutto ciò che stato 
#fatto in un metodo costruito in una classe:
#
#      *ARGS
#La sintassi speciale *args nelle definizioni delle funzioni 
#in python viene utilizzata per passare un numero variabile 
#di argomenti a una funzione. Viene utilizzato per passare un 
#elenco di argomenti di lunghezza variabile senza parole 
#chiave.
#
#      *KWARGS
#La sintassi speciale **kwargs nelle definizioni delle 
#funzioni in Python viene utilizzata per passare un elenco di 
#argomenti di lunghezza variabile con parole chiave. Usiamo 
#il nome kwargs con la doppia stella. Il motivo è che la 
#doppia stella ci consente di passare attraverso argomenti di 
#parole chiave (e qualsiasi numero di essi).
#Si può pensare ai kwargs come a un dizionario che associa 
#ogni parola chiave al valore che le passiamo accanto. Questo 
#è il motivo per cui quando iteriamo sui kwargs non sembra 
#esserci alcun ordine in cui sono stati stampati.
#
#vedi meglio dal sito:
#         https://www.geeksforgeeks.org/args-kwargs-python/
            
class NumericalCSVFile(CSVFile):   
    def get_data(self, *args, **kwargs):
        lista_lista=super().get_data(*args, **kwargs)
        if lista_lista!=None:
            for l in lista_lista:
                for i,item in enumerate(l):
                    if i!=0:
                        if item!='Sales':
                            try:
                                    l[i]=float(item)
                            except ValueError:
                                print('Errore il dato che si presumeva float non lo è! Lo ha generato: {}'.format(l[i]))
                            except TypeError:
                                print('Errore hai sbagliato il tipo di dato!')
                            except Exception as e:
                                print('Errore generico: {}'.format(e))
                
        return lista_lista
        
            
#file_csv= CSVFile('shampoo_sales.csv')
#file_csv.get_data()#end esplicito esempio end=5
#print('{}'.format(file_csv.get_data(8,9)))