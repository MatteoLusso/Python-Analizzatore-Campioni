import Reader as rdr
import Stats as sts
import Sets as sets

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

class CamInfo():

    def __init__( self ):

        self.inputFolder_Cam4_A = "Input\\CAM4\\Distanze\\Set_A"
        self.inputFolder_Cam4_M = "Input\\CAM4\\Distanze\\Set_M"
        self.inputFolder_Cam4_C = "Input\\CAM4\\Distanze\\Set_C"
        self.inputFolder_Cam4_T = "Input\\CAM4\\Distanze\\Set_T"

        self.Cam4_A = rdr.getAllFilesNamesInFolder( self.inputFolder_Cam4_A, ".txt" )
        self.Cam4_M = rdr.getAllFilesNamesInFolder( self.inputFolder_Cam4_M, ".txt" )
        self.Cam4_C = rdr.getAllFilesNamesInFolder( self.inputFolder_Cam4_C, ".txt" )
        self.Cam4_T = rdr.getAllFilesNamesInFolder( self.inputFolder_Cam4_T, ".txt" )

        self.outputText_Cam4_A = "Output\\CAM_4\\Distanze\\Set_A\\Text"
        self.outputText_Cam4_M = "Output\\CAM_4\\Distanze\\Set_M\\Text"
        self.outputText_Cam4_C = "Output\\CAM_4\\Distanze\\Set_C\\Text"
        self.outputText_Cam4_T = "Output\\CAM_4\\Distanze\\Set_T\\Text"

        self.outputImages_Cam4_A = "Output\\CAM_4\\Distanze\\Set_A\\Images"
        self.outputImages_Cam4_M = "Output\\CAM_4\\Distanze\\Set_M\\Images"
        self.outputImages_Cam4_C = "Output\\CAM_4\\Distanze\\Set_C\\Images"
        self.outputImages_Cam4_T = "Output\\CAM_4\\Distanze\\Set_T\\Images"

        self.outputImages_Sets = "Output\\CAM_4\\Distanze\\Images"

        self.dataSavePath_CAM4 = "D:\\Varie\\TesiOff\\Temp\\CAM4\\Dist"

        self.separator = "\n"

        #--------------------------------------------------------------------------------------#

        self.real_Cam4_A = 1.427
        self.real_Cam4_M = 1.633
        self.real_Cam4_C = 1.778
        self.real_Cam4_T = 1.940

        self.distances = [ 11.862, 11.884, 11.939, 8.973, 8.895, 9.004, 5.971, 6.013, 5.993 ]
        self.alphas = [ -16.7, 0.0, 18.6, -16.701, 0.001, 18.601, -16.702, 0.002, 18.602 ]

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

        self.set_Cam4_A = sts.Set( "CAM_4 - A", self.Cam4_A, self.inputFolder_Cam4_A, self.dataSavePath_CAM4, self.separator, self.real_Cam4_A, self.distances, self.alphas, self.sameDist, self.sameAlpha )
        self.set_Cam4_A.generateSetStats( True )
        self.set_Cam4_A.generateSamplesGraphs( self.hBin, self.hShow, self.hAsciiShow, True, self.kdeBinsNumb, self.kdeBWPer, self.kdeShow, self.kdeLoad, self.outputImages_Cam4_A )
        self.set_Cam4_A.generateSetGraphs( False, self.outputImages_Cam4_A )
        self.set_Cam4_A.printAllSet( self.outputText_Cam4_A, False )
        self.set_Cam4_A.printSetAnalysis( self.outputText_Cam4_A, 0.005, False )

        self.set_Cam4_M = sts.Set( "CAM_4 - M", self.Cam4_M, self.inputFolder_Cam4_M, self.dataSavePath_CAM4, self.separator, self.real_Cam4_M, self.distances, self.alphas, self.sameDist, self.sameAlpha )
        self.set_Cam4_M.generateSetStats( True )
        self.set_Cam4_M.generateSamplesGraphs( self.hBin, self.hShow, self.hAsciiShow, True, self.kdeBinsNumb, self.kdeBWPer, self.kdeShow, self.kdeLoad, self.outputImages_Cam4_M )
        self.set_Cam4_M.generateSetGraphs( False, self.outputImages_Cam4_M )
        self.set_Cam4_M.printAllSet( self.outputText_Cam4_M, False )
        self.set_Cam4_M.printSetAnalysis( self.outputText_Cam4_M, 0.005, False )

        self.set_Cam4_C = sts.Set( "CAM_4 - C", self.Cam4_C, self.inputFolder_Cam4_C, self.dataSavePath_CAM4, self.separator, self.real_Cam4_C, self.distances, self.alphas, self.sameDist, self.sameAlpha )
        self.set_Cam4_C.generateSetStats( True )
        self.set_Cam4_C.generateSamplesGraphs( self.hBin, self.hShow, self.hAsciiShow, True, self.kdeBinsNumb, self.kdeBWPer, self.kdeShow, self.kdeLoad, self.outputImages_Cam4_C )
        self.set_Cam4_C.generateSetGraphs( False, self.outputImages_Cam4_C )
        self.set_Cam4_C.printAllSet( self.outputText_Cam4_C, False )
        self.set_Cam4_C.printSetAnalysis( self.outputText_Cam4_C, 0.005, False )

        self.set_Cam4_T = sts.Set( "CAM_4 - T", self.Cam4_T, self.inputFolder_Cam4_T, self.dataSavePath_CAM4, self.separator, self.real_Cam4_T, self.distances, self.alphas, self.sameDist, self.sameAlpha )
        self.set_Cam4_T.generateSetStats( True )
        self.set_Cam4_T.generateSamplesGraphs( self.hBin, self.hShow, self.hAsciiShow, True, self.kdeBinsNumb, self.kdeBWPer, self.kdeShow, self.kdeLoad, self.outputImages_Cam4_T )
        self.set_Cam4_T.generateSetGraphs( False, self.outputImages_Cam4_T )
        self.set_Cam4_T.printAllSet( self.outputText_Cam4_T, False )
        self.set_Cam4_T.printSetAnalysis( self.outputText_Cam4_T, 0.005, False )

        for i in range(0, 9):
            sets.displayErrKDE( [ self.set_Cam4_A, self.set_Cam4_M, self.set_Cam4_C, self.set_Cam4_T ], i, False, "Campione " + str( i + 1 ) + " - CAM_4", "Errore [m]", self.outputImages_Sets, self.setShow, "[DISTRIBUZIONE ERRORI]" )
            sets.displayErrKDE( [ self.set_Cam4_A, self.set_Cam4_M, self.set_Cam4_C, self.set_Cam4_T ], i, True, "Campione " + str( i + 1 ) + " - CAM_4", "Errore relativo [%]", self.outputImages_Sets, self.setShow, "[DISTRIBUZIONE ERRORI RELATIVI]" )

        sets.displaySetsErrorsPercent( [ self.set_Cam4_A, self.set_Cam4_M, self.set_Cam4_C, self.set_Cam4_T ], self.outputImages_Sets, self.setShow )
        sets.displaySetsErrorsRelative( [ self.set_Cam4_A, self.set_Cam4_M, self.set_Cam4_C, self.set_Cam4_T ], [ self.real_Cam4_A, self.real_Cam4_M, self.real_Cam4_C, self.real_Cam4_T ], [ "A [1.427 m]", "M [1.633 m]", "C [1.778 m]", "T [1.940 m]" ], "CAM4_SET_A_M_C_T", "Altezza [m]", "Errore relativo [%]", self.outputImages_Sets, self.setsShow, "[Errori relativi per campione]" )