#definizione dell'oggetto (categoria): files di tipo CSV;
#quindi creazione della classe CSVFile per indicare tale 
#categoria 
class CSVFile:
    
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
        #stato aperto o no
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

        #se non vanno quelle due istruzioni (che servivano a vedere se il file esiste) succede questo: 
        except Exception as e:
            
            #resetto il mio attributo a Falso (cioè non sono 
            #riuscito ad aprire il file) 
            self.can_read=False

            #continuo l'esecuzione del codice ma stampando a 
            #schermo l'errore che lo ha generato
            print('Errore in apertura del file: {}\n'.format(e))
            
    #(sapendo che il mio file è organizato in righe e colonne, 
    #dove ogni colonna ha un informazione) definisco un metodo 
    #che divide i dati e li memorizza, eliminando l'intestazione
    def get_data(self, start=None, end=None):
        self.start=start
        self.end=end

        if self.start==None:
            self.start=1
        if self.end==None:
            self.end=-1

        #In generale 'if' quando ha una condizione con un solo 
        #elemento verifica se questo elemento sia vero 
        #(elemento==True?). (Se l'elemento non è booleano è 
        #impostato a 'TRUE')
        #-------------------------------------------------------
        #not nega il significato booleano
        #-------------------------------------------------------
        #nel nostro caso chiedo se l'attributo del metodo 
        #costruttore durante l'istanzanziamento di un oggetto è 
        #uguale a 'False' cioè se il file si può aprire oppure 
        #no
        if not self.can_read:
            #il file non poteva essere aperto o era illeggibile
            print('Errore, file non aperto o illeggibile')
            return None

        else:
            #sono riuscito ad aprire il mio file e a leggerlo
            
            #riapro il file, lo converto a stringa e lo divido
            #in base alle informazioni. Le info le salvo in un 
            #array (nel mio caso a due elementi: data e 
            #acquisti) e i vari array che contengono le 
            #informazioni li salvo in un altro array che 
            #ritorno. Cioè creo così una lista di liste, dove i 
            #singoli elementi del mio array saranno array a due 
            #elementi.
            list_list=[]
            file=open(self.name,'r')
            for line in file:
                elements=line.strip('\n').split(',')
                #aggiungi alla mia lista di liste tutti gli 
                #array con valori eccetto l'intestazione
                list_list.append(elements)
            file.close()
            return(list_list)

#'NumericalCSVFile' estende la classe 'CSVFile' andando a 
#sovrascrivere il metodo 'get_data()' trasformando in float #alcuni valori
class NumericalCSVFile(CSVFile):   
    def get_data(self):
        
        #il metodo built-in 'super()' mi permette di utilizzare 
        #metodi della classe genitore.
        #Nel nostro caso passo alla mia liste di liste ciò che 
        #ritorna il metodo 'get_data() della mia classe 
        #genitore 'CSVFile'
        lista_lista=super().get_data()
        #print(lista_lista)
        for l in lista_lista:
            #'enumerate()' è un metodo che aggiunge un 
            #contatore a un ciclo, restituendo sia il valore 
            #del contatore 'i' sia l'elemento i-esimo e nei 
            #parametri richiede l'oggetto da ciclare
            for i,item in enumerate(l):
                #qui provo la conversione a float
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
        
            
#file_csv= NumericalCSVFile('shampoo_sales.csv')

#file_csv.get_data()