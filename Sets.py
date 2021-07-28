import Graphs as grp
import Stats as sts

def displayErrKDE( sets, sampleNumber, relativeErr, graphTitle = "", xLabel = "", outputFolder = "", show = True, graphDescription = ""):

    arrays1 = []
    arrays2 = []
    names = []

    for singleSet in sets:
        sample = singleSet.samplesData[sampleNumber].dataFinal
        names.append( singleSet.setName + " [" + str( singleSet.real ) + " m]" )

        if relativeErr is True:
            arrays2.append( [ ( ( value - singleSet.real ) / singleSet.real ) * 100 for value in sample ] )
        else:
            arrays1.append( [ value - singleSet.real for value in sample ] )
    
    if relativeErr is True:
        grp.displayErrsDistributions( arrays2, names, graphTitle, xLabel, outputFolder, show, graphDescription )
    else:
        grp.displayErrsDistributions( arrays1, names, graphTitle, xLabel, outputFolder, show, graphDescription )

    #mkde.errsDist([value - self.real for value in self.samplesData[i].dataFinal])


def displaySetsErrorsRelative( sets, setsOrder, setsNames = None, graphTitle = "", xLabel = "", yLabel = "", outputFolder = "", show = True, graphDescription = "" ):

    names = []
    finalString = ""
    temp1 = []

    for singleSet in sets:
        temp1.append( singleSet.setErrPer )

        finalString += " SET_"
        finalString += str( singleSet.setName )

        if singleSet != sets[ -1 ]:
            finalString += " -"

    print( "\n*** Generazione grafici comuni dei set in corso" + str( finalString ) + " ***" )

    samplesErrRel = []
    empty = []

    #for i in range( len ( setsOrder ) ):
        #empty.append( i )

    samplesErrRel = [ [ 1,2,3,4 ], [ 5,6,7,8 ], [ 9,10,11,12 ], [ 13,14,15,16 ], [ 17,18,19,20 ], [ 21,22,23,23 ], [ 24,26, 27,28 ], [ 29,30,31,32 ], [ 33,34,35,36 ] ]

    #for i in range( len( sets[ 0 ].setErrRelative ) ):
        #samplesErrRel.append( empty )

    h = 0

    for singleSet in sets:

        k = 0

        for relErr in singleSet.setErrRelative:

            samplesErrRel[ k ][ h ] = relErr * 100
            k += 1

        h += 1

    grp.displaySubPlots(samplesErrRel, setsOrder, setsNames, graphTitle, xLabel, yLabel, show, outputFolder, graphDescription)

    pass

def displaySetsErrorsPercent( sets, outputFolder, show = False ):

    names = []
    finalString = ""
    temp1 = []

    for singleSet in sets:
        temp1.append( singleSet.setErrPer )

        finalString += " SET_"
        finalString += str( singleSet.setName )

        if singleSet != sets[ -1 ]:
            finalString += " -"

    print( "\n*** Generazione grafici comuni dei set in corso" + str( finalString ) + " ***" )

    temp2 = ( [ sum( x ) for x in zip( * temp1 ) ] )

    for i in range( len( temp2 ) ):
        temp2[ i ] = temp2[ i ] / len( temp1 )

    grp.display3DErr( setX = sets[0].alpha, setY = sets[0].dist, setZ = temp2, setName = str( finalString ) , show = show, outputFolder = outputFolder, zLabel = "Media errore percentuale set [%]", fileDescription = "[Media errore percentuale set 3D ]" )