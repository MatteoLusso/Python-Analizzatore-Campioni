import re
import csv
import os

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

class CSV(): # Classe che si occupa della gestione dell'input via .csv.

    def load( self ): # Lettura del file .csv
        csvFile = open( self.pathFile + "\\" + self.nameFile, "r" )
        csvLines = csv.reader( csvFile, delimiter = self.fieldDelimiter )


        lines = []
        for row in csvLines:
            line = self.fieldDelimiter.join( row )
            lines.append( line )

        string = self.fieldDelimiter.join( lines )
        string = keepOnlyNumbers( string, self.fieldDelimiter )  # Eliminazione di tutti i caratteri che non siano numeri, punti e \n.

        words = string.split( "\n" )   # Separazione dei caratteri della stringa completa in più elementi ogni volta che si va a capo ("\n").
        words[ : ] = [ word for word in words if word != "" ]   # Rimozione delle righe vuote.

        return words

    #--------------------------------------------------------------------------------------#

    def convert( self ):

        floats = []
        floats = wordsToFloat( self.dataRaw )   # Conversione delle singole parole in una lista di float.
        self.dataErrors = len( self.dataRaw ) - len( floats )

        return floats
    
    #--------------------------------------------------------------------------------------#

    def printData( self ):
        print(" \nPercorso file:   {}".format( self.pathFile ) )
        print(" Nome file:       {}\n".format( self.nameFile ) )
        print(" Input grezzi:    {}".format( self.dataRaw ) )
        print(" Input elaborati: {}".format( self.dataFinal ) )
        print(" Input non letti: {}".format( self.dataErrors ) )

    #--------------------------------------------------------------------------------------#

    def __init__(self, fileName, filePath, fieldDelimiter):
        self.nameFile = fileName
        self.pathFile = filePath
        self.fieldDelimiter = fieldDelimiter
        self.dataRaw = self.load()  # Array di stringhe come vengono lette dal file (sono compresi eventuali errori di formattazione)
        self.dataFinal = self.convert() # Array di float con i dati convertiti in numeri decimali.
        self.dataErrors # Il numero di eventuali dati non letti è salvato in questa variabile.

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

class TXT(): # Classe che si occupa della gestione dell'input via testo.

    def load(self): # Lettura del file di testo
        file = open( self.pathFile + "\\" + self.nameFile, "r" ) 

        lines = []  # Conversione del testo in una lista di stringhe.
        for line in file.readlines():
            lines.append( line)

        string = "".join( lines ) # Unione delle singole stringhe in un'unica stringa
        string = keepOnlyNumbers( string, self.separator )  # Eliminazione di tutti i caratteri che non siano numeri, punti e \n.

        words = string.split( "\n" )   # Separazione dei caratteri della stringa completa in più elementi ogni volta che si va a capo ("\n").
        words[ : ] = [ word for word in words if word != "" ]   # Rimozione delle righe vuote.

        return words

    #--------------------------------------------------------------------------------------#

    def convert( self ):

        floats = []
        floats = wordsToFloat( self.dataRaw )   # Conversione delle singole parole in una lista di float.
        self.dataErrors = len( self.dataRaw ) - len( floats )

        return floats
    
    #--------------------------------------------------------------------------------------#

    def printData( self ):
        print("\nPercorso file:   {}".format( self.pathFile ) )
        print("Nome file:       {}\n".format( self.nameFile ) )
        print("Input grezzi:    {}".format( self.dataRaw ) )
        print("Input elaborati: {}".format( self.dataFinal ) )
        print("Input non letti: {}".format( self.dataErrors ) )

    #--------------------------------------------------------------------------------------#

    def __init__( self, fileName, filePath, separator ):
        self.nameFile = fileName
        self.pathFile = filePath
        self.separator = separator
        self.dataRaw = self.load()  # Array di stringhe come vengono lette dal file (sono compresi eventuali errori di formattazione)
        self.dataFinal = self.convert() # Array di float con i dati convertiti in numeri decimali.
        self.dataErrors # Il numero di eventuali dati non letti è salvato in questa variabile.

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def keepOnlyNumbers( string, separator ):   # Elimina tutti i caratteri da un testo che non siano numeri "0-9", punti "." o "\n". Inoltre sostituisce il carattere separatore dei dati con "\n".

    string = string.replace( ",", "." )
    string = string.replace( separator, "\n" )
    string = re.sub( "0123456789.-\n", "", string )

    return string

#--------------------------------------------------------------------------------------#     

def wordsToFloat( words ):   # Converte una lista di parole fatta di soli numeri, con un punto che separa i decimali, in una lista di float.

    floats = []

    for word in words:
        if checkFormat( word ):
            floats.append( float( word ) )

    return floats

#--------------------------------------------------------------------------------------#

def getAllFilesNamesInFolder( folder, extension ):

    nameList = []

    for file in os.listdir( folder ):
        if file.endswith( extension ):
            nameList.append( file )

    return nameList

#--------------------------------------------------------------------------------------# 

def checkFormat( word ): # Controlla che la stringa sia nel formato giusto per essere convertita in float.

    dotCounter = 0
    reCounter = 0   # Contatore cifre intere
    deCounter = 0   # Contatore cifre decimali 

    for char in word:
        if char == ".":
            dotCounter += 1

        else:
            if char not in "-0123456789":
                return False

            else:
                if dotCounter == 0 and char != "-":
                    reCounter += 1

                else:
                    deCounter += 1
    
    if dotCounter == 1 and reCounter > 0 and deCounter > 0:
        return True

    else:
        return False