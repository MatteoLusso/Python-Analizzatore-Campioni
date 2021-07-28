import Graphs as grp
import CAM3_AMST_Dist
import CAM4_AMCT_Dist

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def CamsErrRelConfrontation( camsSets, camsNames, imageName = "", imageDescription = "", zLabel = "", outputImageFolder = "", outputTextFolder = "", show = False ):

    txt = []

    txt.append( str( imageName ) )
    txt.append( "Differenza di errore relativo percentuale = ErrRel%(" + str( camsSets[1].setName ) + ") - ErrRel%(" + str( camsSets[0].setName ) + ") per campione\n" )

    for i in range( len( camsSets[0].setErrRelative ) ):

        txt.append( "Campione " + str( i + 1 ) + ": " + str( ( camsSets[ 1 ].setErrRelative[ i ] - camsSets[ 0 ].setErrRelative[ i ] ) * 100 ) + "%" )

        grp.display3DErr( [ camsSets[ 0 ].alpha[ i ], camsSets[ 1 ].alpha[ i ] ], [ camsSets[ 0 ].dist[ i ], camsSets[ 1 ].dist[ i ] ], [ camsSets[ 0 ].setErrRelative[ i ], camsSets[ 1 ].setErrRelative[ i ] ], imageName, show, outputImageFolder, zLabel, imageDescription + str( i + 1 ), customScatterText = camsNames )

    outputFile = open( outputTextFolder + "\\" + imageName + "_DELTA_ERR_REL.txt", "w" )

    for line in txt:

        if show is True:
            print( line )

        outputFile.write(line + "\n")
        
    outputFile.close()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

outputImagesFolder = "D:\\Varie\\OneDrive\\MatteoLusso\\OneDrive\\Tesi\\Python\\Analizzatore_Campioni\\Output\\Images"
outputTextFolder = "D:\\Varie\\OneDrive\\MatteoLusso\\OneDrive\\Tesi\\Python\\Analizzatore_Campioni\\Output\\Text"
show = False

D3_AMST_1 = CAM3_AMST_Dist.CamInfo()
D4_AMCT_1 = CAM4_AMCT_Dist.CamInfo()

CamsErrRelConfrontation( [ D3_AMST_1.set_Cam3_A, D4_AMCT_1.set_Cam4_A ], [ "CAM3", "CAM4" ], "Set A (Dist)", "Campione ", "Errore relativo [%]", outputImagesFolder, outputTextFolder, show )
CamsErrRelConfrontation( [ D3_AMST_1.set_Cam3_M, D4_AMCT_1.set_Cam4_M ], [ "CAM3", "CAM4" ], "Set M (Dist)", "Campione ", "Errore relativo [%]", outputImagesFolder, outputTextFolder, show )
CamsErrRelConfrontation( [ D3_AMST_1.set_Cam3_T, D4_AMCT_1.set_Cam4_T ], [ "CAM3", "CAM4" ], "Set T (Dist)", "Campione ", "Errore relativo [%]", outputImagesFolder, outputTextFolder, show )


