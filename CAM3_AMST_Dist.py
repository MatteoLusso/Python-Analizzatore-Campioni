import Reader as rdr
import Stats as sts
import Sets as sets

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

class CamInfo():

    def __init__( self ):

        self.inputFolder_Cam3_A = "Input\\CAM3\\Distanze\\Set_A"
        self.inputFolder_Cam3_M = "Input\\CAM3\\Distanze\\Set_M"
        self.inputFolder_Cam3_S = "Input\\CAM3\\Distanze\\Set_S"
        self.inputFolder_Cam3_T = "Input\\CAM3\\Distanze\\Set_T"

        self.Cam3_A = rdr.getAllFilesNamesInFolder( self.inputFolder_Cam3_A, ".txt" )
        self.Cam3_M = rdr.getAllFilesNamesInFolder( self.inputFolder_Cam3_M, ".txt" )
        self.Cam3_S = rdr.getAllFilesNamesInFolder( self.inputFolder_Cam3_S, ".txt" )
        self.Cam3_T = rdr.getAllFilesNamesInFolder( self.inputFolder_Cam3_T, ".txt" )

        self.outputText_Cam3_A = "Output\\CAM_3\\Distanze\\Set_A\\Text"
        self.outputText_Cam3_M = "Output\\CAM_3\\Distanze\\Set_M\\Text"
        self.outputText_Cam3_S = "Output\\CAM_3\\Distanze\\Set_S\\Text"
        self.outputText_Cam3_T = "Output\\CAM_3\\Distanze\\Set_T\\Text"

        self.outputImages_Cam3_A = "Output\\CAM_3\\Distanze\\Set_A\\Images"
        self.outputImages_Cam3_M = "Output\\CAM_3\\Distanze\\Set_M\\Images"
        self.outputImages_Cam3_S = "Output\\CAM_3\\Distanze\\Set_S\\Images"
        self.outputImages_Cam3_T = "Output\\CAM_3\\Distanze\\Set_T\\Images"

        self.outputImages_Sets = "Output\\CAM_3\\Distanze\\Images"

        self.dataSavePath_CAM3 = "D:\\Varie\\TesiOff\\Temp\\CAM3\\Dist"

        self.separator = "\n"

        #--------------------------------------------------------------------------------------#

        self.real_Cam3_A = 1.427
        self.real_Cam3_M = 1.633
        self.real_Cam3_S = 1.758
        self.real_Cam3_T = 1.940

        self.distances = [ 11.953, 11.660, 11.775, 8.973, 8.790, 8.875, 5.951, 5.864, 5.857 ]
        self.alphas = [ -26.6, 0.0, 24.2, -26.601, 0.001, 24.201, -26.602, 0.002, 24.202 ]

        self.sameDist = [ [ 1, 4, 7 ], [ 2, 5, 8 ], [ 3, 6, 9 ] ]
        self.sameAlpha = [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]

        self.hBin = 0.0005
        self.hShow = False
        self.hAsciiShow = False

        self.kdeShow = False
        self.kdeBinsNumb = 50
        self.kdeLoad = True

        self.kdeBWPer = 0

        self.setShow = False
        self.setsShow = False

        self.set_Cam3_A = sts.Set( "CAM_3 - A", self.Cam3_A, self.inputFolder_Cam3_A, self.dataSavePath_CAM3, self.separator, self.real_Cam3_A, self.distances, self.alphas, self.sameDist, self.sameAlpha )
        self.set_Cam3_A.generateSetStats( True )
        self.set_Cam3_A.generateSamplesGraphs( self.hBin, self.hShow, self.hAsciiShow, True, self.kdeBinsNumb, self.kdeBWPer, self.kdeShow, self.kdeLoad, self.outputImages_Cam3_A )
        self.set_Cam3_A.generateSetGraphs( False, self.outputImages_Cam3_A )
        self.set_Cam3_A.printAllSet( self.outputText_Cam3_A, False )
        self.set_Cam3_A.printSetAnalysis( self.outputText_Cam3_A, 0.005, False )

        self.set_Cam3_M = sts.Set( "CAM_3 - M", self.Cam3_M, self.inputFolder_Cam3_M, self.dataSavePath_CAM3, self.separator, self.real_Cam3_M, self.distances, self.alphas, self.sameDist, self.sameAlpha )
        self.set_Cam3_M.generateSetStats( True )
        self.set_Cam3_M.generateSamplesGraphs( self.hBin, self.hShow, self.hAsciiShow, True, self.kdeBinsNumb, self.kdeBWPer, self.kdeShow, self.kdeLoad, self.outputImages_Cam3_M )
        self.set_Cam3_M.generateSetGraphs( False, self.outputImages_Cam3_M )
        self.set_Cam3_M.printAllSet( self.outputText_Cam3_M, False )
        self.set_Cam3_M.printSetAnalysis( self.outputText_Cam3_M, 0.005, False )

        self.set_Cam3_S = sts.Set( "CAM_3 - S", self.Cam3_S, self.inputFolder_Cam3_S, self.dataSavePath_CAM3, self.separator, self.real_Cam3_S, self.distances, self.alphas, self.sameDist, self.sameAlpha )
        self.set_Cam3_S.generateSetStats( True )
        self.set_Cam3_S.generateSamplesGraphs( self.hBin, self.hShow, self.hAsciiShow, True, self.kdeBinsNumb, self.kdeBWPer, self.kdeShow, self.kdeLoad, self.outputImages_Cam3_S )
        self.set_Cam3_S.generateSetGraphs( False, self.outputImages_Cam3_S )
        self.set_Cam3_S.printAllSet( self.outputText_Cam3_S, False )
        self.set_Cam3_S.printSetAnalysis( self.outputText_Cam3_S, 0.005, False )

        self.set_Cam3_T = sts.Set( "CAM_3 - T", self.Cam3_T, self.inputFolder_Cam3_T, self.dataSavePath_CAM3, self.separator, self.real_Cam3_T, self.distances, self.alphas, self.sameDist, self.sameAlpha )
        self.set_Cam3_T.generateSetStats( True )
        self.set_Cam3_T.generateSamplesGraphs( self.hBin, self.hShow, self.hAsciiShow, True, self.kdeBinsNumb, self.kdeBWPer, self.kdeShow, self.kdeLoad, self.outputImages_Cam3_T )
        self.set_Cam3_T.generateSetGraphs( False, self.outputImages_Cam3_T )
        self.set_Cam3_T.printAllSet( self.outputText_Cam3_T, False )
        self.set_Cam3_T.printSetAnalysis( self.outputText_Cam3_T, 0.005, False )

        for i in range(0, 9):
            sets.displayErrKDE( [ self.set_Cam3_A, self.set_Cam3_M, self.set_Cam3_S, self.set_Cam3_T ], i, False, "Campione " + str( i + 1 ) + " - CAM_3", "Errore [m]", self.outputImages_Sets, self.setShow, "[DISTRIBUZIONE ERRORI]" )
            sets.displayErrKDE( [ self.set_Cam3_A, self.set_Cam3_M, self.set_Cam3_S, self.set_Cam3_T ], i, True, "Campione " + str( i + 1 ) + " - CAM_3", "Errore relativo [%]", self.outputImages_Sets, self.setShow, "[DISTRIBUZIONE ERRORI RELATIVI]" )

        sets.displaySetsErrorsPercent( [ self.set_Cam3_A, self.set_Cam3_M, self.set_Cam3_S, self.set_Cam3_T ], self.outputImages_Sets, self.setShow )
        sets.displaySetsErrorsRelative( [ self.set_Cam3_A, self.set_Cam3_M, self.set_Cam3_S, self.set_Cam3_T ], [ self.real_Cam3_A, self.real_Cam3_M, self.real_Cam3_S, self.real_Cam3_T ], [ "A [1.427 m]", "M [1.633 m]", "S [1.758 m]", "T [1.940 m]" ], "CAM3_SET_A_M_S_T", "Altezza [m]", "Errore relativo [%]", self.outputImages_Sets, self.setsShow, "[Errori relativi per campione]" )

import Reader as rdr
import Stats as sts
import Sets as sets

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def StartAnalysis():

    inputFolder_Cam3_A = "Input\\CAM3\\Distanze\\Set_A"
    inputFolder_Cam3_M = "Input\\CAM3\\Distanze\\Set_M"
    inputFolder_Cam3_S = "Input\\CAM3\\Distanze\\Set_S"
    inputFolder_Cam3_T = "Input\\CAM3\\Distanze\\Set_T"

    Cam3_A = rdr.getAllFilesNamesInFolder( inputFolder_Cam3_A, ".txt" )
    Cam3_M = rdr.getAllFilesNamesInFolder( inputFolder_Cam3_M, ".txt" )
    Cam3_S = rdr.getAllFilesNamesInFolder( inputFolder_Cam3_S, ".txt" )
    Cam3_T = rdr.getAllFilesNamesInFolder( inputFolder_Cam3_T, ".txt" )

    outputText_Cam3_A = "Output\\CAM_3\\Distanze\\Set_A\\Text"
    outputText_Cam3_M = "Output\\CAM_3\\Distanze\\Set_M\\Text"
    outputText_Cam3_S = "Output\\CAM_3\\Distanze\\Set_S\\Text"
    outputText_Cam3_T = "Output\\CAM_3\\Distanze\\Set_T\\Text"

    outputImages_Cam3_A = "Output\\CAM_3\\Distanze\\Set_A\\Images"
    outputImages_Cam3_M = "Output\\CAM_3\\Distanze\\Set_M\\Images"
    outputImages_Cam3_S = "Output\\CAM_3\\Distanze\\Set_S\\Images"
    outputImages_Cam3_T = "Output\\CAM_3\\Distanze\\Set_T\\Images"

    outputImages_Sets = "Output\\CAM_3\\Distanze\\Images"

    dataSavePath_CAM3 = "D:\\Varie\\TesiOff\\Temp\\CAM3\\Dist"

    separator = "\n"

    #--------------------------------------------------------------------------------------#

    real_Cam3_A = 1.427
    real_Cam3_M = 1.633
    real_Cam3_S = 1.758
    real_Cam3_T = 1.940

    distances = [ 11.953, 11.660, 11.775, 8.973, 8.790, 8.875, 5.951, 5.864, 5.857 ]
    alphas = [ -26.6, 0.0, 24.2, -26.601, 0.001, 24.201, -26.602, 0.002, 24.202 ]

    sameDist = [ [ 1, 4, 7 ], [ 2, 5, 8 ], [ 3, 6, 9 ] ]
    sameAlpha = [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]

    hBin = 0.0005
    hShow = False
    hAsciiShow = False

    kdeShow = False
    kdeBinsNumb = 50
    kdeLoad = True

    kdeBWPer = 0

    setShow = False
    setsShow = False

    set_Cam3_A = sts.Set( "CAM_3 - A", Cam3_A, inputFolder_Cam3_A, dataSavePath_CAM3, separator, real_Cam3_A, distances, alphas, sameDist, sameAlpha )
    set_Cam3_A.generateSetStats( True )
    set_Cam3_A.generateSamplesGraphs( hBin, hShow, hAsciiShow, True, kdeBinsNumb, kdeBWPer, kdeShow, kdeLoad, outputImages_Cam3_A )
    set_Cam3_A.generateSetGraphs( False, outputImages_Cam3_A )
    set_Cam3_A.printAllSet( outputText_Cam3_A, False )
    set_Cam3_A.printSetAnalysis( outputText_Cam3_A, 0.005, False )

    set_Cam3_M = sts.Set( "CAM_3 - M", Cam3_M, inputFolder_Cam3_M, dataSavePath_CAM3, separator, real_Cam3_M, distances, alphas, sameDist, sameAlpha )
    set_Cam3_M.generateSetStats( True )
    set_Cam3_M.generateSamplesGraphs( hBin, hShow, hAsciiShow, True, kdeBinsNumb, kdeBWPer, kdeShow, kdeLoad, outputImages_Cam3_M )
    set_Cam3_M.generateSetGraphs( False, outputImages_Cam3_M )
    set_Cam3_M.printAllSet( outputText_Cam3_M, False )
    set_Cam3_M.printSetAnalysis( outputText_Cam3_M, 0.005, False )

    set_Cam3_S = sts.Set( "CAM_3 - S", Cam3_S, inputFolder_Cam3_S, dataSavePath_CAM3, separator, real_Cam3_S, distances, alphas, sameDist, sameAlpha )
    set_Cam3_S.generateSetStats( True )
    set_Cam3_S.generateSamplesGraphs( hBin, hShow, hAsciiShow, True, kdeBinsNumb, kdeBWPer, kdeShow, kdeLoad, outputImages_Cam3_S )
    set_Cam3_S.generateSetGraphs( False, outputImages_Cam3_S )
    set_Cam3_S.printAllSet( outputText_Cam3_S, False )
    set_Cam3_S.printSetAnalysis( outputText_Cam3_S, 0.005, False )

    set_Cam3_T = sts.Set( "CAM_3 - T", Cam3_T, inputFolder_Cam3_T, dataSavePath_CAM3, separator, real_Cam3_T, distances, alphas, sameDist, sameAlpha )
    set_Cam3_T.generateSetStats( True )
    set_Cam3_T.generateSamplesGraphs( hBin, hShow, hAsciiShow, True, kdeBinsNumb, kdeBWPer, kdeShow, kdeLoad, outputImages_Cam3_T )
    set_Cam3_T.generateSetGraphs( False, outputImages_Cam3_T )
    set_Cam3_T.printAllSet( outputText_Cam3_T, False )
    set_Cam3_T.printSetAnalysis( outputText_Cam3_T, 0.005, False )

    sets.displaySetsErrorsPercent( [ set_Cam3_A, set_Cam3_M, set_Cam3_S, set_Cam3_T ], outputImages_Sets, setsShow )
    sets.displaySetsErrorsRelative( [ set_Cam3_A, set_Cam3_M, set_Cam3_S, set_Cam3_T ], [ real_Cam3_A, real_Cam3_M, real_Cam3_S, real_Cam3_T ], [ "A [1.427 m]", "M [1.633 m]", "S [1.758 m]", "T [1.940 m]" ], "CAM3_SET_A_M_S_T", "Altezza [m]", "Errore relativo [%]", outputImages_Sets, setsShow, "[Errori relativi per campione]" )