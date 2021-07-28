import matplotlib.pyplot as plt
import KDE as kde
import numpy as np
from collections import OrderedDict
import Serializer as sr
from scipy import integrate
import seaborn as sns

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

class GraphsInfo():

    def __init__( self, campName, dataArray, histBinWidth = 0.001, histLoad = True, kdeBins = 50, kdeCoeffBW = 0, kdeLoad = True, savesPath = "" ):

        self.data = dataArray
        self.n = len( dataArray )
        self.name = campName
        self.savesPath = savesPath

        self.start = min( dataArray )
        self.end = max( dataArray )

        print ( str(self.start ) + " ... " + str(self.end ))

        self.range = self.end - self.start
        self.histBinW = histBinWidth
        self.histBins =  ( max( dataArray ) - min( dataArray ) ) / self.histBinW
        self.histLoad = histLoad

        fltString = getExpandedScientificNotation( self.histBinW )
        self.decimals = str(fltString)[::-1].find('.')

        self.hist = {}
        self.histNorm = {}

        self.kdeBins = kdeBins
        self.kdePerBW = kdeCoeffBW
        self.kdeLoad = kdeLoad

        self.kdeX = []
        self.kdeY = []
        self.kdeH = 0.0

        self.pdfY = []
        #self.kdeYErrs = []
        #self.kdeErrsH = 0.0

    #--------------------------------------------------------------------------------------#

    def generateKDE( self ):#, real = None ):

        print( "\n*** Campione " + self.name + " | Generazione KDE ***" )

        self.kdeH = 1.05 * np.std( self.data ) * ( self.n**( -1 / 5 ) )

        #--------------------------------------------------------------------------------------#

        print( "\n   - Calcolo ascisse KDE (" + str( self.kdeBins ) + ") in corso -" )

        if self.kdeLoad is True and sr.loadVariable( self.name + "_KDE_X_ARRAY_", self.savesPath, True ) is not None:

            self.kdeX = sr.loadVariable( self.name + "_KDE_X_ARRAY_", self.savesPath )

        else:

            self.kdeX = np.linspace( self.start, self.end, self.kdeBins)
            
            sr.saveVariable(self.name + "_KDE_X_ARRAY_", self.kdeX, self.savesPath)

        #--------------------------------------------------------------------------------------#

        print( "\n   - Calcolo ordinate KDE (" + str( self.kdeBins ) + ") in corso -\n" )

        if self.kdeLoad is True and sr.loadVariable( self.name + "_KDE_Y_ARRAY_", self.savesPath, True ) is not None:

            self.kdeY = sr.loadVariable( self.name + "_KDE_Y_ARRAY_", self.savesPath )

        else:

            for i in range( self.kdeBins ):

                self.kdeY.append( kde.getPoint( self.kdeX[i], self.data, self.n, self.kdeH, self.kdePerBW) )

                print( "      - " + str( i + 1 ) + "/" + str( self.kdeBins ) + " -" )

            sr.saveVariable(self.name + "_KDE_Y_ARRAY_", self.kdeY, self.savesPath)

        #--------------------------------------------------------------------------------------#

        print( "\n   - Normalizzazione KDE in corso -\n" )

        if self.kdeLoad is True and sr.loadVariable( self.name + "_PDF_Y_ARRAY_", self.savesPath, True ) is not None:

            self.pdfY = sr.loadVariable( self.name + "_PDF_Y_ARRAY_", self.savesPath )

        else:

            kdeInt = integrate.simps( self.kdeY ) # Regola di Cavalieri-Simpson per il calcolo di un integrale definito 

            for y in self.kdeY:
                self.pdfY.append( ( y / kdeInt ) * 100 )
                #print( "+++++++++++++++++++++++++++++++++++++++++++++++" + str(( y / kdeInt ) * 100) )

            sr.saveVariable( self.name + "_PDF_Y_ARRAY_", self.pdfY, self.savesPath )

        #--------------------------------------------------------------------------------------#

        #if real is not None:

            #print( "\n   - Calcolo ordinate KDE degli errori (" + str( self.kdeBins ) + ") in corso -\n" )

            #if self.kdeLoad is True and sr.loadVariable( self.name + "_KDE_Y_ERRS_ARRAY_", self.savesPath, True ) is not None:

                #self.kdeYErrs = sr.loadVariable( self.name + "_KDE_Y_ERRS_ARRAY_", self.savesPath )

            #else:

                #errs = []

                #for data in self.data:
                    #errs.append(abs(data - real))

                #self.kdeErrsH = 1.05 * np.std( errs ) * ( self.n**( -1 / 5 ) )

                #for i in range( self.kdeBins ):

                    #self.kdeYErrs.append( kde.getPoint( self.kdeX[i], errs, self.n, self.kdeErrsH, self.kdePerBW) )

                    #print( "      - " + str( i + 1 ) + "/" + str( self.kdeBins ) + " -" )

                #sr.saveVariable(self.name + "_KDE_Y_ERRS_ARRAY_", self.kdeYErrs, self.savesPath)

    #--------------------------------------------------------------------------------------#

    def generateHistogram( self ):

        print( "\n*** Campione " + self.name + " | Generazione istogramma ***" )

        save = False

        if self.histLoad is True and sr.loadVariable( self.name + "_HIST_ARRAY_", self.savesPath, True ) is not None:

            self.hist = sr.loadVariable( self.name + "_HIST_ARRAY_", self.savesPath )

        else:

            print( "\n   - Calcolo istogramma in corso -" )

            save = True

            temp = {}

            for variable in self.data:

                low = round(int( variable / self.histBinW ) * self.histBinW, self.decimals)

                if low in temp.keys():
                    temp[low] += 1

                else:
                    temp[low] = 1

            self.hist = OrderedDict(sorted(temp.items()))

        area = 0.0

        for k, v in self.hist.items():
            self.histNorm[k] = (v / self.n) * ( 1 / self.histBinW )
            area += self.histNorm[k] * self.histBinW

        if save is True:
            sr.saveVariable(self.name + "_HIST_ARRAY_", self.hist, self.savesPath)

    #--------------------------------------------------------------------------------------#

    def printAsciiHistogram( self ):
        print("\n")
        for occurence in self.hist:
            i = 0
            symbols = ""
            while i < self.hist[occurence]:
                i += 1
                symbols += "+"

            print(str(occurence) + " - " + str( round( occurence + self.range - ( 1 / pow( 10, ( self.decimals + 1 ) ) ), self.decimals + 1 ) ) + " | [" + str(len(symbols)) + "] " + symbols)

    #--------------------------------------------------------------------------------------#

    def displayKDE( self, kdeType = "default", outputFolder = "", show = True):
        
        plt.clf()

        plt.gcf().set_size_inches(20, 11.25)

        plt.axvspan( self.start, self.end, alpha = 0.25, color = "k")

        plt.xlabel("Altezza [m]", fontsize = 25)

        if "default" == kdeType:

            plt.suptitle( "KDE del campione " + str( self.name ) + "\n Banda gaussiana: " + str( self.kdeH ), fontsize = 40 )

            plt.plot( np.array( self.kdeX ), np.array( self.kdeY ), color='red', linestyle='-' )
            plt.ylabel("KDE", fontsize = 25)

            plt.draw()

            plt.savefig( outputFolder + "\\" + str( self.name ) + " [KDE].png" )

        elif "pdf" == kdeType:

            plt.suptitle( "PDF del campione " + str( self.name ) + "\n Banda gaussiana: " + str( self.kdeH ), fontsize = 25 )

            plt.plot( np.array( self.kdeX ), np.array( self.pdfY ), color='orange', linestyle='-' )
            plt.ylabel("PDF [%]", fontsize = 18)

            plt.draw()

            plt.savefig( outputFolder + "\\" + str( self.name ) + " [PDF].png" )

            #print("Integrale pdf: " + str( integrate.simps( pdfY ) ) )

        #elif "errs" == kdeType:

            #plt.suptitle( "KDE errori " + str( self.name ) + "\n Banda gaussiana: " + str( self.kdeH ), fontsize = 25 )

            #plt.plot( np.array( self.kdeX ), np.array( self.kdeYErrs ), color='green', linestyle='-' )
            #plt.ylabel("Errore [m]", fontsize = 18)

            #plt.draw()

            #plt.savefig( outputFolder + "\\" + str( self.name ) + " [ERRS].png" )

        #if show is True:
            #plt.show()

        #plt.clf()

    #--------------------------------------------------------------------------------------#
    
    def displayHistogram( self, real, mean, meanAr, histType = "default", outputFolder = "", show = True):

        plt.clf()

        plt.gcf().set_size_inches(20, 11.25)

        plt.axvspan( self.start, self.end, alpha = 0.25, color = "k")

        if "default" == histType:
            plt.bar( list( self.hist.keys() ), self.hist.values(), width = self.histBinW, align = 'edge', color = 'g', edgecolor = 'k', linewidth = 1)

        plt.suptitle( str( self.name ), fontsize = 40 )
        plt.xlabel("Altezza [m]", fontsize = 25)
        plt.ylabel("Occorenze / [" + str( self.histBinW ) + " m]", fontsize = 25)

        plt.draw()
        plt.savefig( outputFolder + "\\" + str( self.name ) + " [Distribuzione].png" )

        xCoords = [meanAr, mean, real]
        xNames = ["Media Armonica", "Media", "Valore reale"]
        xStyles = [':', '-.', '--']
        xColors = ['orange','r','c']
        for xC, xN, xCol, xS in zip(xCoords, xNames, xColors, xStyles):
            if(xC != None):
                plt.axvline( x = xC, label = str( xN ) + ": {:.4f}".format(xC), c = xCol, ls = xS, alpha = 0.75 )
        plt.legend( ( str( xNames[ 0 ] ) + ": " + str( round( xCoords[ 0 ], 3 ) ) + " m", str( xNames[ 1 ] ) + ": " + str( round( xCoords[ 1 ], 3 ) ) + " m", str( xNames[ 2 ] ) + ": " + str( round( xCoords[ 2 ], 3 ) ) + " m"), fontsize = 'xx-large' )

        halfHist = max( list( self.hist.values() ) ) / 2

        x1 = min( real, mean )
        x2 = max( real, mean )

        plt.plot([x1, x2], [halfHist, halfHist], color = "blue", linestyle= (0, (5, 1)), alpha = 0.75)
        errText = plt.text( x1 + ( ( x2 - x1 ) / 2 ), halfHist + ( 0.08 * halfHist), str( round( ( mean - real ) * 1000, 2 ) ) + " mm", color = "blue", size = 25 )
        errText.set_bbox(dict(facecolor = 'white', alpha = 0.5, edgecolor = 'grey'))

        plt.draw()
        plt.savefig( outputFolder + "\\" + str( self.name ) + " [Confronto valori].png" )

        #self.histKDEFig.append(plt.gcf())

        if show is True:
            plt.show()

        return plt.gcf()
            
        #plt.clf()

    #def displayMultiImage( self, outputFolder = "", show = True):

        #fig, axs = plt.subplots(3, 3)

        #k = 0

        #for i in range(0, 2):
            #for j in range(0, 2):
                #axs.plot(self.histKDEFig(k))
                #k += 1

        #plt.draw()
        #plt.savefig( outputFolder + "\\" + str( self.name ) + " [Multi].png" )

        #if show is True:
            #plt.show()
            
        #plt.clf()

        #pass

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def displayErrsDistributions( arrays, legends, title = "", xLabel = "", outputFolder = "", show = True, fileDescription = ""):

    fig, ax = plt.subplots()

    plt.clf()

    fig.set_size_inches(20, 11.25)

    plt.axvline(x = 0, color = 'k', linestyle='--', alpha = 0.75)

    i = 0

    for array in arrays:
        ax = sns.distplot(array, hist = False, kde = True, label = str( legends[i] ) )
        i += 1

    ax.set( xlabel = xLabel )

    fig.legend()

    fig.suptitle( str( title ) + "\n" + str( fileDescription ), fontsize = 25 )

    plt.gcf()

    plt.draw()
    
    plt.savefig( outputFolder + "\\" + title + " " + fileDescription + ".png", bbox_inches = 'tight', dpi = 300 )

    if show is True:
        plt.show()
            
    plt.clf()

def displayChi2Dist( setX, setY, name = "", show = True, outputFolder = "", same = None ):

    plotErr( setX, setY, same )

    plt.suptitle( "SET_" + str( name ) + "\n[Chi2 dei campioni rispetto alla distanza dalla telecamera]", fontsize = 40 )
    plt.ylabel("Chi2", fontsize = 25)
    plt.xlabel("Distanza dalla telecamera [m]", fontsize = 25)

    fig = plt.gcf()
    fig.set_size_inches(20, 11.25)

    plt.draw()
    plt.savefig( outputFolder + "\\SET_" + str( name ) + " [Chi2 - distanza].png" )

    if show is True:
        plt.show()
            
    plt.clf()

#--------------------------------------------------------------------------------------#

def displayChi2Alpha( setX, setY, name = "", show = True, outputFolder = "", same = None ):

    plotErr( setX, setY, same )

    plt.suptitle( "SET_" + str( name ) + "\n[Chi2 dei campioni rispetto all'angolo alpha]", fontsize = 40 )
    plt.ylabel("Chi2", fontsize = 25)
    plt.xlabel("Angolo alpha rispetto alla telecamera [deg]", fontsize = 25)

    fig = plt.gcf()
    fig.set_size_inches(20, 11.25)

    plt.draw()
    plt.savefig( outputFolder + "\\SET_" + str( name ) + " [Chi2 - angolo alpha].png" )

    if show is True:
        plt.show()
            
    plt.clf()

#--------------------------------------------------------------------------------------#

def displayErrDist( setX, setY, name = "", show = True, outputFolder = "", same = None ):

    plotErr( setX, setY, same )

    plt.suptitle( "SET_" + str( name ) + "\n[Errore delle medie dei campioni rispetto alla distanza dalla telecamera]", fontsize = 40 )
    plt.ylabel("Errore [m]", fontsize = 25)
    plt.xlabel("Distanza dalla telecamera [m]", fontsize = 25)

    fig = plt.gcf()
    fig.set_size_inches(20, 11.25)

    plt.draw()
    plt.savefig( outputFolder + "\\SET_" + str( name ) + " [Errore media - distanza].png" )

    if show is True:
        plt.show()
            
    plt.clf()

#--------------------------------------------------------------------------------------#

def displayErrArDist( setX, setY, name = "", show = True, outputFolder = "", same = None ):

    plotErr( setX, setY, same )

    plt.suptitle( "SET_" + str( name ) + "\n[Errore delle medie armoniche dei campioni rispetto alla distanza dalla telecamera]", fontsize = 40 )
    plt.ylabel("Errore [m]", fontsize = 25)
    plt.xlabel("Distanza dalla telecamera [m]", fontsize = 25)

    fig = plt.gcf()
    fig.set_size_inches(20, 11.25)

    plt.draw()
    plt.savefig( outputFolder + "\\SET_" + str( name ) + " [Errore media armonica - distanza].png" )

    if show is True:
        plt.show()
            
    plt.clf()

#--------------------------------------------------------------------------------------#

def displayErrChi2( setX, setY, name = "", show = True, outputFolder = "", same = None ):

    plotErr( setX, setY, same )

    plt.suptitle( "SET_" + str( name ) + "\n[Errore delle medie dei campioni rispetto al punteggio del test chi2]", fontsize = 40 )
    plt.ylabel("Errore [m]", fontsize = 25)
    plt.xlabel("Punteggio test chi2", fontsize = 25)

    fig = plt.gcf()
    fig.set_size_inches(20, 11.25)

    plt.draw()
    plt.savefig( outputFolder + "\\SET_" + str( name ) + " [Errore media - chi2].png" )

    if show is True:
        plt.show()
            
    plt.clf()

#--------------------------------------------------------------------------------------#

def displayErrArChi2( setX, setY, name = "", show = True, outputFolder = "", same = None ):

    plotErr( setX, setY, same )

    plt.suptitle( "SET_" + str( name ) + "\n[Errore delle medie armoniche dei campioni rispetto al punteggio del test chi2]", fontsize = 40 )
    plt.ylabel("Errore [m]", fontsize = 25)
    plt.xlabel("Punteggio test chi2", fontsize = 25)

    fig = plt.gcf()
    fig.set_size_inches(20, 11.25)

    plt.draw()
    plt.savefig( outputFolder + "\\SET_" + str( name ) + " [Errore media armonica - chi2].png" )

    if show is True:
        plt.show()
            
    plt.clf()

#--------------------------------------------------------------------------------------#

def displayErrAlpha( setX, setY, name = "", show = True, outputFolder = "", same = None ):

    plotErr( setX, setY, same )

    plt.suptitle( "SET_" + str( name ) + "\n[Errore delle medie dei campioni rispetto all'angolo alpha]", fontsize = 40 )
    plt.ylabel("Errore [m]", fontsize = 25)
    plt.xlabel("Angolo alpha rispetto alla telecamera [deg]", fontsize = 25)

    fig = plt.gcf()
    fig.set_size_inches(20, 11.25)

    plt.draw()
    plt.savefig( outputFolder + "\\SET_" + str( name ) + " [Errore media - angolo alpha].png" )

    if show is True:
        plt.show()
            
    plt.clf()

#--------------------------------------------------------------------------------------#

def displayErrArAlpha( setX, setY, name = "", show = True, outputFolder = "", same = None ):

    plotErr( setX, setY, same )

    plt.suptitle( "SET_" + str( name ) + "\n[Errore delle medie armoniche dei campioni rispetto all'angolo alpha]", fontsize = 40 )
    plt.ylabel("Errore [m]", fontsize = 25)
    plt.xlabel("Angolo alpha rispetto alla telecamera [deg]", fontsize = 25)

    fig = plt.gcf()
    fig.set_size_inches(20, 11.25)

    plt.draw()
    plt.savefig( outputFolder + "\\SET_" + str( name ) + " [Errore media armonica - angolo alpha].png" )

    if show is True:
        plt.show()
            
    plt.clf()

#--------------------------------------------------------------------------------------#

def plotErr ( setX, setY, same = None ):

    temp1 = dict( zip( setX, np.absolute( setY ) ) )
    temp1 = dict( sorted( temp1.items() ) )

    temp2 = dict( zip( setX, list( range( 1, len( setX ) + 1 ) ) ) )
    temp2 = dict( sorted( temp2.items() ) )

    #print(temp2)
    #print(temp1)

    order = list( temp2.values() )

    x = np.array( list( temp1.keys() ) )
    y = np.array( list( temp1.values() ) )

    #m, b1 = np.polyfit(x, y, 1)

    #fit = np.polyfit(x, y, 2)
    #a = fit[0]
    #b = fit[1]
    #c = fit[2]
    #fitEquation = a * np.square(x) + b * x + c

    plt.clf()
    plt.grid()

    if same is not None:

        k = 0

        for array in same:

            index = []

            for el in array:
                index.append( order.index( el ) )

            index = sorted( index )

            secondaryX = []
            secondaryY = []

            for i in index:
                secondaryX.append( x[ i ] )
                secondaryY.append( y[ i ] )

            secR1 = regression( secondaryX, secondaryY, 1 )

            plt.plot( secondaryX, secR1, color = "green", alpha = 0.5, linestyle='-.' )

            if (k % 2) == 0:
                secText = plt.text( secondaryX[ 0 ] + ( ( plt.xlim()[ 1 ] - plt.xlim()[ 0 ] ) * 0.05), secR1[ 0 ] + ( ( plt.ylim()[ 1 ] - plt.ylim()[ 0 ] ) * 0.08), array, fontsize = 20, color = "green")
            else:
                secText = plt.text( secondaryX[ 2 ] - ( ( plt.xlim()[ 1 ] - plt.xlim()[ 0 ] ) * 0.1), secR1[ 2 ] - ( ( plt.ylim()[ 1 ] - plt.ylim()[ 0 ] ) * 0.02), array, fontsize = 20, color = "green")

            secText.set_bbox( dict( facecolor = 'white', alpha = 0.5, edgecolor = 'grey' ) )

            k += 1

    #plt.plot( x, y, linestyle='--', alpha = 0.25 )

    r1 = regression( x, y, 1 )
    r2 = regression( x, y, 2 )
    
    plt.plot( x, r1, color = "red", linestyle='-.', alpha = 0.5, label = "Regressione 1° ordine" )
    plt.plot( x, r2, color = "red", linestyle='-', alpha = 0.75, label = "Regressione 2° ordine" )

    plt.scatter(x, y)

    #ax = plt.axes()

    txtDX = ( max( setX ) - min( setX ) ) * 0.01
    txtDY = ( max( setY ) - min( setY ) ) * 0.01

    for i in range( len ( setX ) ):
        plt.text(x[i] + txtDX, y[i] + txtDY, order[i], color='blue', size = 25, wrap = True)

    plt.legend()

#--------------------------------------------------------------------------------------#

def regression( x, y, order ):

    if order == 1:

        m, b1 = np.polyfit( x, y, 1 )

        r1 = np.asarray( ( m * np.asarray( x ) ) + b1 )

        return r1

    elif order == 2:

        fit = np.polyfit( x, y, 2 )
        
        a = fit[0]
        b = fit[1]
        c = fit[2]

        r2 = np.asarray( ( a * np.square( np.asarray( x ) ) ) + ( b * np.asarray( x ) ) + c )

        return r2

def display3DErr( setX, setY, setZ, setName = "", show = True, outputFolder = "", zLabel = "", fileDescription = "", limXPer = 0.1, limYPer = 0.1, limZPer = 0.2, customScatterText = None ):

    plt.clf()

    #print("************X : " + str(len(setX)) + " Y : " + str(len(setY)) + " Z : " + str(len(setZ)))

    ax = plt.axes( projection = '3d', proj_type = 'ortho' )
    ax.set_xlabel( "Angolo α\n[deg]", fontsize = 25 )
    ax.set_ylabel( "Distanza\n[m]", fontsize = 25 )
    ax.set_zlabel( zLabel )

    setZ = np.absolute( setZ )

    rangeX = max( setX ) - min( setX )
    rangeY = max( setY ) - min( setY )
    rangeZ = max( setZ ) - min( setZ )

    limX = [ min( setX ) - ( rangeX * limXPer ), max( setX ) + ( rangeX * limXPer ) ]
    limY = [ min( setY ) - ( rangeY * limYPer ), max( setY ) + ( rangeY * limYPer ) ]
    limZ = [ min( setZ ) - ( rangeZ * limZPer ), max( setZ ) + ( rangeZ * limZPer ) ]

    ax.set_xlim( limX )
    ax.set_ylim( limY )
    ax.set_zlim( limZ )

    ax.plot(setX, setZ, 'r+', zdir='y', zs = limY[1], alpha = 0.5 )
    ax.plot(setY, setZ, 'g+', zdir='x', zs = limX[0], alpha = 0.5 )
    ax.plot(setX, setY, 'b+', zdir='z', zs = limZ[0], alpha = 0.5 )

    for i in range( len ( setX ) ):

        ax.plot3D(np.array([ setX[ i ], setX[ i ] ]), np.array( [ setY[ i ], limY[ 1 ] ] ), np.array( [ setZ[ i ], setZ[ i ] ] ), color = "r", alpha = 0.2, linestyle = (0, (3, 5, 1, 5)) )
        ax.plot3D(np.array([ setX[ i ], limX[ 0 ] ]), np.array( [ setY[ i ], setY[ i ] ] ), np.array( [ setZ[ i ], setZ[ i ] ] ), color = "g", alpha = 0.2, linestyle = (0, (3, 5, 1, 5)) )
        ax.plot3D(np.array([ setX[ i ], setX[ i ] ]), np.array( [ setY[ i ], setY[ i ] ] ), np.array( [ setZ[ i ], limZ[ 0 ] ] ), color = "b", alpha = 0.5, linestyle = "solid", linewidth = 2 )

        if customScatterText is None:
            scatterName = ax.text(setX[i] + (rangeX * 0.05), setY[i] + (rangeY * 0.05), setZ[i], str( i + 1 ), color='b', size = 10)
        else:
            scatterName = ax.text(setX[i] + (rangeX * 0.05), setY[i] + (rangeY * 0.05), setZ[i], customScatterText[i], color='b', size = 10)
        
        scatterName.set_bbox(dict(facecolor = 'white', alpha = 0.5, edgecolor = 'grey'))
        #ax.text(setX[i] + 0.2, limY[1] - 0.2, setZ[i], str( i + 1 ), color='red')
        #ax.text(limX[0] + 0.2, setY[i] - 0.2, setZ[i], str( i + 1 ), color='green')
        #ax.text(setX[i] + 0.2, setY[i] - 0.2, limZ[0], str( i + 1 ), color='black')

    ax.scatter( np.array( setX ), np.array( setY), np.array( setZ ), depthshade = False, color = "k" )
    
    plt.suptitle( str( setName ) + "\n" + str( fileDescription ), fontsize = 40 )

    fig = plt.gcf()
    fig.set_size_inches(20, 11.25)

    plt.draw()
    
    plt.savefig( outputFolder + "\\" + str( setName ) + " " + str( fileDescription ) + ".png", bbox_inches = 'tight', dpi = 100 )

    if show is True:
        plt.show()
            
    plt.clf()

#--------------------------------------------------------------------------------------#

def displaySubPlots( multiY, commonAxis, commonAxisLabels = None,  title = "", xLabel = "", yLabel = "", show = True, outputFolder = "", fileDescription = ""):

    fig, axs = plt.subplots( 3, 3 )
    fig.set_size_inches(20, 11.25)

    k = 0

    for row in range( 3 ):
        for col in range( 3 ):

            axs[ row, col ].grid()
            axs[ row, col ].scatter( commonAxis, multiY[ k ] )

            axs[ row, col ].set_title( "Campione " + str( ( row * 3 ) + ( col + 1 ) ) )

            r1 = regression( commonAxis, multiY[ k ], 1 )
            axs[ row, col ].plot( commonAxis, r1, color = "red", linestyle='-.', alpha = 0.5)

            r2 = regression( commonAxis, multiY[ k ], 2 )
            axs[ row, col ].plot( commonAxis, r2, color = "red", linestyle='-', alpha = 0.75)

            if commonAxisLabels is None:
                axs[ row, col ].set_xticks( commonAxis )
            else:
                plt.sca(axs[ row, col ])
                plt.xticks(commonAxis, commonAxisLabels )
                #axs[ row, col ].set_xticks( commonAxis, labels )

            k += 1

    fig.suptitle( str( title ) + "\n" + str( fileDescription ), fontsize = 25 )
    fig.text( 0.5, 0.04, str( xLabel ), ha = 'center', fontsize = 20 )
    fig.text( 0.04, 0.5, str( yLabel ), va = 'center', rotation = 'vertical', fontsize = 20 )

    plt.gcf()

    plt.draw()
    
    plt.savefig( outputFolder + "\\" + str( title ) + " " + str( fileDescription ) + ".png", bbox_inches = 'tight', dpi = 300 )

    if show is True:
        plt.show()
            
    plt.clf()

#--------------------------------------------------------------------------------------#

def getExpandedScientificNotation( flt ):

    was_neg = False

    if not ("e" in str(flt)):
        return flt

    if str(flt).startswith('-'):
        flt = flt[1:]
        was_neg = True

    str_vals = str(flt).split('e')
    coef = float(str_vals[0])
    exp = int(str_vals[1])
    return_val = ''

    if int(exp) > 0:
        return_val += str(coef).replace('.', '')
        return_val += ''.join(['0' for _ in range(0, abs(exp - len(str(coef).split('.')[1])))])

    elif int(exp) < 0:
        return_val += '0.'
        return_val += ''.join(['0' for _ in range(0, abs(exp) - 1)])
        return_val += str(coef).replace('.', '')

    if was_neg:
        return_val='-'+return_val

    return return_val