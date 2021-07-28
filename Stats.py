import statistics
import Graphs as grp
import KDE as kde
import Reader as rdr
import pickle as pk
import numpy as np
import Serializer as sr
#import MultiKDE as mkde

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

class Set():

    def __init__( self, setName = "None", filesNames = [], filesPath = "", savesPath = "", separator = "\n", real = None, distances = None, alphas = None, sameDist = None, sameAlpha = None ):

        self.setName = setName
        self.names = filesNames
        self.path = filesPath
        self.savesPath = savesPath
        self.separator = separator

        self.real = real
        self.dist = distances
        self.alpha = alphas
        self.sameDist = sameDist
        self.sameAlpha = sameAlpha

        self.samplesData = []
        self.samplesAnalysis = []

        self.loadGraphs = True
        self.sampleGraphs = []

        self.setChi2 = []
        self.setErr = []
        self.setErrPer = []
        self.setErrAr = []
        self.setErrRelative = []

    #--------------------------------------------------------------------------------------#
 
    def updateSamplesStatsWithProb( self ):

        for i in range ( len( self.samplesAnalysis ) ):

            sampleKDEX = self.sampleGraphs[i].kdeX
            samplePDFY = self.sampleGraphs[i].pdfY

            self.samplesAnalysis[i].ProbMean = linearInterpolation( self.samplesAnalysis[i].mean, sampleKDEX, samplePDFY )
            self.samplesAnalysis[i].ProbMeanAr = linearInterpolation( self.samplesAnalysis[i].meanAr, sampleKDEX, samplePDFY )

            if self.samplesAnalysis[i].real is not None:
                self.samplesAnalysis[i].ProbReal = linearInterpolation( self.samplesAnalysis[i].real, sampleKDEX, samplePDFY )

            self.samplesAnalysis[i].saveStats()

    #--------------------------------------------------------------------------------------#

    def areMeansUnderstimated( self, near ):

        temp = []
        
        for sample in self.samplesAnalysis:
            if sample.mean < self.real:
                temp.append(True)
            else:
                temp.append(False)
        
        return temp

    #--------------------------------------------------------------------------------------#
 
    def areMeansNearReal( self, near ):

        temp = []
        
        for sample in self.samplesAnalysis:
            if sample.mean >= ( self.real - near ) and sample.mean <= ( self.real + near ):
                temp.append(True)
            else:
                temp.append(False)
        
        return temp

    #--------------------------------------------------------------------------------------#
 
    def isRealInRange( self ):

        temp = []
        
        for sample in self.samplesAnalysis:
            if self.real >= sample.min and self.real <= sample.max:
                temp.append(True)
            else:
                temp.append(False)
        
        return temp

    #--------------------------------------------------------------------------------------#
 
    def printSetAnalysis( self, outputFolder, near = 0.0, show = False ):

        isInRange = self.isRealInRange()
        areNear = self.areMeansNearReal( near )
        areUnder = self.areMeansUnderstimated( near )

        perInRange = 0
        perNear = 0
        perUnder = 0

        inRangeString = []
        for varBool in isInRange:
            if varBool is True:
                perInRange += 1
                inRangeString.append("   Sì  ")
            else:
                inRangeString.append("   No  ")
        
        nearString = []
        for varBool in areNear:
            if varBool is True:
                perNear += 1
                nearString.append("   Sì  ")
            else:
                nearString.append("   No  ")

        underString = []
        for varBool in areUnder:
            if varBool is True:
                perUnder += 1
                underString.append("   Sì  ")
            else:
                underString.append("   No  ")
            
        txt = []

        #txt.append( " ╔═══════════════════════════════════════════════════════════════════════╗ " )
        #txt.append( " ║               SET " + str( self.setName ) + " - Campione                                ║ " )
        #txt.append( " ╠═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╣ " ) 
        #txt.append( " ║   1   ║   2   ║   3   ║   4   ║   5   ║   6   ║   7   ║   8   ║   9   ║ " )
        #txt.append( " ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣ " )  
        #txt.append( " ║" + str(inRangeString[0]) + "║" + str(inRangeString[1]) + "║" + str(inRangeString[2]) + "║" + str(inRangeString[3]) + "║" + str(inRangeString[4]) + "║" + str(inRangeString[5]) + "║" + str(inRangeString[6]) + "║" + str(inRangeString[7]) + "║" + str(inRangeString[8]) + "║ " )
        #txt.append( " ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣ " )  
        #txt.append( " ║" + str(nearString[0]) + "║" + str(nearString[1]) + "║" + str(nearString[2]) + "║" + str(nearString[3]) + "║" + str(nearString[4]) + "║" + str(nearString[5]) + "║" + str(nearString[6]) + "║" + str(nearString[7]) + "║" + str(nearString[8]) + "║ " )
        #txt.append( " ╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣ " )  
        #txt.append( " ║" + str(overString[0]) + "║" + str(overString[1]) + "║" + str(overString[2]) + "║" + str(overString[3]) + "║" + str(overString[4]) + "║" + str(overString[5]) + "║" + str(overString[6]) + "║" + str(overString[7]) + "║" + str(overString[8]) + "║ " )
        #txt.append( " ╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝ " ) 

        txt.append( " |               SET " + str( self.setName ) + " - Campione              | " )
        txt.append( " ------------------------------------------------------------------------- " ) 
        txt.append( " |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |   9   | " )
        txt.append( " |-------|-------|-------|-------|-------|-------|-------|-------|-------| " )  
        txt.append( " |" + str(inRangeString[0]) + "|" + str(inRangeString[1]) + "|" + str(inRangeString[2]) + "|" + str(inRangeString[3]) + "|" + str(inRangeString[4]) + "|" + str(inRangeString[5]) + "|" + str(inRangeString[6]) + "|" + str(inRangeString[7]) + "|" + str(inRangeString[8]) + "| Il valore reale è compreso tra la minima e massima misurazione?" )
        txt.append( " |-------|-------|-------|-------|-------|-------|-------|-------|-------| " )   
        txt.append( " |" + str(nearString[0]) + "|" + str(nearString[1]) + "|" + str(nearString[2]) + "|" + str(nearString[3]) + "|" + str(nearString[4]) + "|" + str(nearString[5]) + "|" + str(nearString[6]) + "|" + str(nearString[7]) + "|" + str(nearString[8]) + "| La media è vicina al valore reale?" )
        txt.append( " |-------|-------|-------|-------|-------|-------|-------|-------|-------| " )   
        txt.append( " |" + str(underString[0]) + "|" + str(underString[1]) + "|" + str(underString[2]) + "|" + str(underString[3]) + "|" + str(underString[4]) + "|" + str(underString[5]) + "|" + str(underString[6]) + "|" + str(underString[7]) + "|" + str(underString[8]) + "| La media è inferiore al valore reale?" )


        txt.append( "\n")

        txt.append( "Risultato:")
        txt.append( " - Il {}""%"" delle volte il valore reale di questo set ({}m) è compreso tra la minima e massima misurazione dei singoli campioni.".format( round( ( perInRange / 9 ) * 100, 2 ), self.real ) )
        txt.append( " - Il {}""%"" delle medie campionarie del set hanno un errore assoluto in metri minore di {}m.".format( round( ( perNear / 9 ) * 100, 2 ), near ) )
        txt.append( " - Il {}""%"" delle medie campionarie del set sono state sottostimata rispetto al valore valore reale di questo set ({}m).".format( round( ( perUnder / 9 ) * 100, 2 ), self.real ) )

        outputFile = open( outputFolder + "\\SET_" + self.setName + "_STATS.txt", "w" )

        for line in txt:

            if show is True:
                print( line )

            outputFile.write(line + "\n")
            
        outputFile.close()

    #--------------------------------------------------------------------------------------#

    def generateSamplesGraphs( self, histStep = 0.001, showHist = True, showAsciiHist = False, loadHist = True, kdeBinsNumber = 50, kdeCoeffBw = 0, kdeShow = True, loadKDE = True, outputImagesFolder = ""):

        if self.samplesData is not None and self.samplesAnalysis is not None and len( self.samplesAnalysis ) == len( self.samplesData ):

            for i in range( len( self.samplesData ) ):

                self.sampleGraphs.append(grp.GraphsInfo(self.names[i], self.samplesData[i].dataFinal, histStep, loadHist, kdeBinsNumber, kdeCoeffBw, loadKDE, self.savesPath))

                self.sampleGraphs[i].generateHistogram()
                self.sampleGraphs[i].generateKDE()

                self.sampleGraphs[i].displayHistogram(self.real, self.samplesAnalysis[i].mean, self.samplesAnalysis[i].meanAr, "default", outputImagesFolder, showHist)
                self.sampleGraphs[i].displayKDE("default", outputImagesFolder, kdeShow)
                self.sampleGraphs[i].displayKDE("pdf", outputImagesFolder, kdeShow)
            
            self.updateSamplesStatsWithProb()

    #--------------------------------------------------------------------------------------#

    def generateSetStats( self, load = True ):

        i = 0

        if self.names is not None:

            print( "\n*** Generazione dati statistici set " + str( self.setName ) + " ***" )

            for name in self.names:

                self.samplesData.append( rdr.TXT( name, self.path, self.separator ) )
                #self.samplesData[i].printData()

                #if load is True and sr.loadVariable( name + "_STATS_", True ) is not None:
                        
                        #self.samplesAnalysis.append( sr.loadVariable( name + "_STATS_" ) )

                        ###da cancellare
                        #toSave = [self.samplesAnalysis[i].n, self.samplesAnalysis[i].median, self.samplesAnalysis[i].mode, self.samplesAnalysis[i].mean, self.samplesAnalysis[i].meanAr, self.samplesAnalysis[i].var, self.samplesAnalysis[i].varAr, self.samplesAnalysis[i].std, self.samplesAnalysis[i].stdAr, self.samplesAnalysis[i].range, self.samplesAnalysis[i].coeff, self.samplesAnalysis[i].chi2, self.samplesAnalysis[i].ProbMean, self.samplesAnalysis[i].ProbMeanAr, self.samplesAnalysis[i].varReal, self.samplesAnalysis[i].stdReal, self.samplesAnalysis[i].ProbReal, self.samplesAnalysis[i].errMean, self.samplesAnalysis[i].errMeanAr]
                        #sr.saveVariable(self.names[i] + "_ALL_STATS_", toSave)

                #else:

                    #print( "\n      - Campione " + str( self.names[i] ) + " | Calcolo statistiche in corso\n" )

                self.samplesAnalysis.append( Sample( self.samplesData[ i ], self.savesPath, self.real) )
                self.samplesAnalysis[i].calculateStatistics()

                #sr.saveVariable( name + "_STATS_", self.samplesAnalysis[i] )

                self.setChi2.append( self.samplesAnalysis[i].chi2 )
                self.setErr.append( self.samplesAnalysis[i].errMean )

                self.setErrAr.append( self.samplesAnalysis[i].errMeanAr )

                self.setErrRelative.append( self.samplesAnalysis[i].errMeanRelative )

                #self.setErrPer.append( equivalentRange(x, rangeA, rangeB))

                i += 1

             

            for err in self.setErr:
                self.setErrPer.append( equivalentRange( self.real + np.abs( err ), [self.real, self.real + max( np.abs( self.setErr ) )], [0, 100] ))

            print( self.setErrPer )

    #--------------------------------------------------------------------------------------#

    def generateSetGraphs( self, show = True, outputFolder = "" ):

        print( "*** Generazione grafici set " + str( self.setName ) + " ***" )

        grp.displayErrDist( setX = self.dist, setY = self.setErr, name = self.setName, show = show, outputFolder = outputFolder, same = self.sameDist ) 
        grp.displayErrArDist( setX = self.dist, setY = self.setErrAr, name = self.setName, show = show, outputFolder = outputFolder, same = self.sameDist )

        grp.displayErrAlpha( setX = self.alpha, setY = self.setErr, name = self.setName, show = show, outputFolder = outputFolder, same = self.sameAlpha ) 
        grp.displayErrArAlpha( setX = self.alpha, setY = self.setErrAr, name = self.setName, show = show, outputFolder = outputFolder, same = self.sameAlpha )

        grp.displayErrChi2( setX = self.setChi2, setY = self.setErr, name = self.setName, show = show, outputFolder = outputFolder ) 
        grp.displayErrArChi2( setX = self.setChi2, setY = self.setErrAr, name = self.setName, show = show, outputFolder = outputFolder ) 

        grp.displayChi2Dist( setX = self.dist, setY = self.setChi2, name = self.setName, show = show, outputFolder = outputFolder ) 
        grp.displayChi2Alpha( setX = self.alpha, setY = self.setChi2, name = self.setName, show = show, outputFolder = outputFolder ) 

        grp.display3DErr( setX = self.alpha, setY = self.dist, setZ = self.setErr, setName = "SET_" + self.setName, show = show, outputFolder = outputFolder, zLabel = "Errore media campionaria (abs) [m]", fileDescription = "[Errore 3D]" )
        grp.display3DErr( setX = self.alpha, setY = self.dist, setZ = self.setErrAr, setName = "SET_" + self.setName, show = show, outputFolder = outputFolder, zLabel = "Errore media armonica (abs) [m]", fileDescription = "[Errore armonica 3D]" )
        grp.display3DErr( setX = self.alpha, setY = self.dist, setZ = self.setChi2, setName = "SET_" + self.setName, show = show, outputFolder = outputFolder, zLabel = "Risultato test chi2", fileDescription = "[Chi2 3D]", limXPer = 0.1, limYPer = 0.1, limZPer = 0.01)

        grp.display3DErr( setX = self.alpha, setY = self.dist, setZ = self.setErrPer, setName = "SET_" + self.setName, show = show, outputFolder = outputFolder, zLabel = "Errore percentuale media campionaria rispetto massimo valore modulo errore", fileDescription = "[Errore percentuale 3D]" )

        grp.display3DErr( setX = self.alpha, setY = self.dist, setZ = [errRel * 100 for errRel in self.setErrRelative], setName = "SET_" + self.setName, show = show, outputFolder = outputFolder, zLabel = "Errore relativo media campionaria rispetto all'altezza " + str( round( self.real, 3 ) ) + " m [%]", fileDescription = "[Errore relativo 3D]" )
    #--------------------------------------------------------------------------------------#            

    def printAllSet( self, outputPath, show = True ):

        if self.samplesAnalysis is not None:

            for analysis in self.samplesAnalysis:

                analysis.printAnalysis( outputPath, show )

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

class Sample(): # Classe che si occupa dell'analisi dei dati

    def chi2Gauss ( self ):
        obs = [ 0, 0, 0, 0 ]
        prob = [ 0.16, 0.34, 0.34, 0.16 ]

        for mis in self.data:

            if mis < ( self.mean - self.std ):
                obs[ 0 ] = obs[ 0 ] + 1

            elif ( self.mean - self.std ) <= mis and mis < self.mean:
                obs[ 1 ] = obs[ 1 ] + 1

            elif self.mean <= mis and mis < ( self.mean + self.std ):
                obs[ 2 ] = obs[ 2 ] + 1

            else:
                obs[ 3 ] = obs[ 3 ] + 1

        chi2 = 0.0

        for k in range(4):
            chi2 += pow( obs[k] - ( self.n * prob[ k ] ), 2) / ( self.n * prob[ k ] )

        return chi2

    #--------------------------------------------------------------------------------------#   

    def calculateStatistics( self, load = True ):
        if self.data is not None:

            if load is True and sr.loadVariable( self.name + "_STATS_", True ) is not None:

                toLoad = sr.loadVariable( self.name + "_STATS_")

                self.n = toLoad[0]
                self.median = toLoad[1]
                self.mode = toLoad[2]
                self.mean = toLoad[3]
                self.meanAr = toLoad[4]

                self.var = toLoad[5]
                self.varAr = toLoad[6]

                self.std = toLoad[7]
                self.stdAr = toLoad[8]

                self.range = toLoad[9]
                self.coeff = toLoad[10]
                self.chi2 = toLoad[11]

                self.ProbMean = toLoad[12]
                self.ProbMeanAr = toLoad[13]

                self.varReal = toLoad[14]
                self.stdReal = toLoad[15]
                self.ProbReal = toLoad[16]

                self.errMean = toLoad[17] 
                self.errMeanAr = toLoad[18]

                self.errMeanRelative = toLoad[19]

                self.min = toLoad[20]
                self.max = toLoad[21]

                
            else:
                
                self.n = len( self.data )
                self.median = statistics.median( self.data )
                self.mode = statistics.mode(self.data)
                self.mean = momentOrR( self.data, 1 )
                self.meanAr = armonicMean( self.data )

                self.var = momentCenR( self.data, self.mean, 2 )
                self.varAr = momentCenR( self.data, self.meanAr, 2 )

                self.std = np.sqrt( self.var )
                self.stdAr = np.sqrt( self.varAr )

                self.min = min( self.data )
                self.max = max( self.data )

                self.range = self.max - self.min
                self.coeff = self.std / self.mean
                self.chi2 = self.chi2Gauss()

                self.ProbMean = None
                self.ProbMeanAr = None

                if self.real is not None:
                    self.varReal = momentCenR( self.data, self.real, 2 )
                    self.stdReal = np.sqrt( self.varReal )
                    self.ProbReal = None

                    self.errMean = self.mean - self.real 
                    self.errMeanAr = self.meanAr - self.real

                    self.errMeanRelative = abs( self.errMean ) / self.real

            #self.saveStats()

    #--------------------------------------------------------------------------------------#   

    def printAnalysis( self, outputFolder, show = True ):

        txt = []

        txt.append( " Campione                           | " + str( self.name ) )
        txt.append( " Misurazioni                        | " + str( self.n )  )

        txt.append( "\n" ) 

        txt.append( " Moda (camp.)                       | " + str( self.mode )  )
        txt.append( " Mediana (camp.)                    | " + str( self.median ) ) 
        txt.append( " Media (camp.)                      | " + str( self.mean ) ) 
        txt.append( " PDF Media (camp.)                  | {:.2f}".format( self.ProbMean ) + "%") 
        txt.append( " Media armonica (camp.)             | " + str( self.meanAr ) ) 
        txt.append( " PDF Media armonica (camp.)         | {:.2f}".format( self.ProbMeanAr ) + "%") 

        if self.real is not None:
            txt.append( " Altezza reale                      | " + str( self.real ) ) 
            txt.append( " PDF altezza reale                  | {:.2f}".format( self.ProbReal ) + "%") 

            txt.append( "\n" ) 

            txt.append( " Errore (media) :                   | " + str( self.errMean ) + " m" )
            txt.append( " Errore relativo (media) :          | " + str( self.errMeanRelative * 100 ) + "%" ) 

            txt.append( "\n" ) 

            txt.append( " Errore (media armonica) :          | " + str( self.errMeanAr ) + " m" ) 

            txt.append( "\n" ) 

            txt.append( " Varianza (Val. reale)              | " + str( self.varReal ) ) 
            txt.append( " Deviazione standard (Val. reale)   | " + str( self.stdReal ) ) 

            txt.append( "\n" ) 

        txt.append( " Varianza (Media camp.)             | " + str( self.var ) ) 
        txt.append( " Deviazione standard (Media camp.)  | " + str( self.std ) ) 

        txt.append( "\n" ) 

        txt.append( " Varianza (Media arm.)              | " + str( self.varAr ) ) 
        txt.append( " Deviazione standard (Media arm.)   | " + str( self.stdAr ) ) 

        txt.append( "\n" ) 

        txt.append( " Ampiezza campo di variazione       | " + str( self.range ) + " m" ) 
        txt.append( " Coefficiente di variazione         | " + str( self.coeff ) ) 

        txt.append( "\n" ) 

        txt.append( " Test Chi^2                         | " + str( self.chi2 ) ) 

        outputFile = open( outputFolder + "\\" + self.name + "STATS.txt", "w" )

        
        for line in txt:

            if show is True:
                print( line )

            outputFile.write(line + "\n")
            
        outputFile.close()

    #--------------------------------------------------------------------------------------#    

    def __init__( self, data, savesPath = "", real = None):
        self.name = data.nameFile
        self.data = data.dataFinal
        self.savesPath = savesPath
        self.n = 0

        self.median = 0.0
        self.mode = 0.0
        self.real = real
        self.mean = 0.0
        self.meanAr = 0.0

        self.var = 0.0
        self.varAr = 0.0
        self.varReal = 0.0

        self.std = 0.0
        self.stdAr = 0.0
        self.stdReal = 0.0

        self.range = 0.0
        self.coeff = 0.0
        self.chi2 = 0.0

        self.ProbReal = 0.0
        self.ProbMean = 0.0
        self.ProbMeanAr = 0.0

        self.errMean = 0.0
        self.errMeanAr = 0.0

        self.varReal = 0.0
        self.varAr = 0.0

        self.errMeanRelative = 0.0

        self.min = 0.0
        self.max = 0.0

        #self.graphs = grp.GraphsInfo( self.name, self.data, self.histBinWidth)

        #self.pBW = perGaussBandwich

    #--------------------------------------------------------------------------------------# 

    def saveStats( self ):
        toSave = [self.n, self.median, self.mode, self.mean, self.meanAr, self.var, self.varAr, self.std, self.stdAr, self.range, self.coeff, self.chi2, self.ProbMean, self.ProbMeanAr, self.varReal, self.stdReal, self.ProbReal, self.errMean, self.errMeanAr, self.errMeanRelative, self.min, self.max]
        sr.saveVariable(self.name + "_STATS_", toSave, self.savesPath)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def armonicMean( inputVariables ):
    sum_inv = 0.0

    for variable in inputVariables:
        sum_inv += 1 / variable

    return len( inputVariables ) / sum_inv

#--------------------------------------------------------------------------------------#

def momentOrR( inputVariables, inputR ):  # Il MOMENTO ORDINARIO (O DALL’ORIGINE) DI ORDINE r corrisponde alla media dei valori della variabile elevati alla potenza r-esima. 

    summation = 0.0
    for variable in inputVariables:
        summation += pow( variable, inputR )

    return summation / len( inputVariables )

#--------------------------------------------------------------------------------------#

def momentCenR( inputVariables, inputEV, inputR ):   #Il MOMENTO CENTRALE DI ORDINE r corrisponde alla media degli scarti dalla media della variabile elevati alla potenza r-esima.

    summation = 0.0

    #print ("EV " + str(inputEV))

    for variable in inputVariables:
        summation += pow( ( variable - inputEV ), inputR )

    return summation / len( inputVariables )  

def linearInterpolation ( x, xArray, yArray ):

    if x < min( xArray ) or x > max( xArray ):
        return 0.0
    
    else:

        i = 0

        while x > xArray[ i ]:
            i += 1

        x1 = xArray[ i - 1 ]
        x2 = xArray[ i ]

        #print( "\n\n\n\n ********************** x1 =" + str(x1))
        #print( "\n\n\n\n ********************** x2 =" + str(x2))

        y1 = yArray[ i - 1 ]
        y2 = yArray[ i ]

        #print( "\n\n\n\n ********************** y1 =" + str(y1))
        #print( "\n\n\n\n ********************** y2 =" + str(y2))

        dX = ( x2 - x1 )
        dY = ( y2 - y1 )

        dXx = ( x - x1 )

        #print( "\n\n\n\n ********************** Y% =" + str(y))

        return y1 + ( ( dXx / dX ) * dY )

#--------------------------------------------------------------------------------------#

def equivalentRange ( x, rangeA, rangeB ):

    return ( ( rangeB[1] - rangeB[0] ) * ( x - rangeA[0] ) / ( rangeA[1] - rangeA[0] ) ) + rangeB[0]

#--------------------------------------------------------------------------------------#
