import Reader as rdr
import Stats as sts
import Sets as sets

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

inputFolder_Cam3_A = "Input\\CAM3\\Quadranti\\Set_A"
inputFolder_Cam3_M = "Input\\CAM3\\Quadranti\\Set_M"
inputFolder_Cam3_S = "Input\\CAM3\\Quadranti\\Set_S"
inputFolder_Cam3_T = "Input\\CAM3\\Quadranti\\Set_T"

Cam3_A = rdr.getAllFilesNamesInFolder( inputFolder_Cam3_A, ".txt" )
Cam3_M = rdr.getAllFilesNamesInFolder( inputFolder_Cam3_M, ".txt" )
Cam3_S = rdr.getAllFilesNamesInFolder( inputFolder_Cam3_S, ".txt" )
Cam3_T = rdr.getAllFilesNamesInFolder( inputFolder_Cam3_T, ".txt" )

outputText_Cam3_A = "Output\\CAM_3\\Quadranti\\Set_A\\Text"
outputText_Cam3_M = "Output\\CAM_3\\Quadranti\\Set_M\\Text"
outputText_Cam3_S = "Output\\CAM_3\\Quadranti\\Set_S\\Text"
outputText_Cam3_T = "Output\\CAM_3\\Quadranti\\Set_T\\Text"

outputImages_Cam3_A = "Output\\CAM_3\\Quadranti\\Set_A\\Images"
outputImages_Cam3_M = "Output\\CAM_3\\Quadranti\\Set_M\\Images"
outputImages_Cam3_S = "Output\\CAM_3\\Quadranti\\Set_S\\Images"
outputImages_Cam3_T = "Output\\CAM_3\\Quadranti\\Set_T\\Images"

outputImages_Sets = "Output\\CAM_3\\Quadranti\\Images"

separator = "\n"

#--------------------------------------------------------------------------------------#

real_Cam3_A = 1.427
real_Cam3_M = 1.633
real_Cam3_S = 1.758
real_Cam3_T = 1.940

distances = [ 11.953, 11.660, 11.775, 8.973, 8.790, 8.875, 5.951, 5.864, 3.206 ]
alphas = [ -26.6, 0.0, 30.9, -26.601, 0.001, 30.91, -26.602, 0.002, 30.901 ]

#sameDist = [ [ 1, 4, 7 ], [ 2, 5, 8 ], [ 3, 6, 9 ] ]
#sameAlpha = [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]

hBin = 0.0005
hShow = False
hAsciiShow = False

kdeShow = False
kdeBinsNumb = 50
kdeLoad = True

kdeBWPer = 0

setShow = False
setsShow = False

#set_Cam3_A = sts.Set( "CAM_3 - A", Cam3_A, inputFolder_Cam3_A, separator, real_Cam3_A, distances, alphas)
#set_Cam3_A.generateSetStats( True )
#set_Cam3_A.generateSamplesGraphs( hBin, hShow, hAsciiShow, True, kdeBinsNumb, kdeBWPer, kdeShow, kdeLoad, outputImages_Cam3_A )
#set_Cam3_A.generateSetGraphs( False, outputImages_Cam3_A )
#set_Cam3_A.printAllSet( outputText_Cam3_A, False )
#set_Cam3_A.printSetAnalysis( outputText_Cam3_A, 0.005, False )

set_Cam3_M = sts.Set( "CAM_3 - M [Quad]", Cam3_M, inputFolder_Cam3_M, separator, real_Cam3_M, distances, alphas)
set_Cam3_M.generateSetStats( True )
set_Cam3_M.generateSamplesGraphs( hBin, hShow, hAsciiShow, True, kdeBinsNumb, kdeBWPer, kdeShow, kdeLoad, outputImages_Cam3_M )
set_Cam3_M.generateSetGraphs( False, outputImages_Cam3_M )
set_Cam3_M.printAllSet( outputText_Cam3_M, False )
set_Cam3_M.printSetAnalysis( outputText_Cam3_M, 0.005, False )

#set_Cam3_S = sts.Set( "CAM_3 - S", Cam3_S, inputFolder_Cam3_S, separator, real_Cam3_S, distances, alphas)
#set_Cam3_S.generateSetStats( True )
#set_Cam3_S.generateSamplesGraphs( hBin, hShow, hAsciiShow, True, kdeBinsNumb, kdeBWPer, kdeShow, kdeLoad, outputImages_Cam3_S )
#set_Cam3_S.generateSetGraphs( False, outputImages_Cam3_S )
#set_Cam3_S.printAllSet( outputText_Cam3_S, False )
#set_Cam3_S.printSetAnalysis( outputText_Cam3_S, 0.005, False )

#set_Cam3_T = sts.Set( "CAM_3 - T", Cam3_T, inputFolder_Cam3_T, separator, real_Cam3_T, distances, alphas)
#set_Cam3_T.generateSetStats( True )
#set_Cam3_T.generateSamplesGraphs( hBin, hShow, hAsciiShow, True, kdeBinsNumb, kdeBWPer, kdeShow, kdeLoad, outputImages_Cam3_T )
#set_Cam3_T.generateSetGraphs( False, outputImages_Cam3_T )
#set_Cam3_T.printAllSet( outputText_Cam3_T, False )
#set_Cam3_T.printSetAnalysis( outputText_Cam3_T, 0.005, False )

#sets.displaySetsErrorsPercent( [ set_Cam3_A, set_Cam3_M, set_Cam3_S, set_Cam3_T ], outputImages_Sets, setsShow )
#sets.displaySetsErrorsRelative( [ set_Cam3_A, set_Cam3_M, set_Cam3_S, set_Cam3_T ], [ real_Cam3_A, real_Cam3_M, real_Cam3_S, real_Cam3_T ], [ "A [1.427 m]", "M [1.633 m]", "S [1.758 m]", "T [1.940 m]" ], "CAM3_SET_A_M_S_T", "Altezza [m]", "Errore relativo [%]", outputImages_Sets, setsShow, "[Errori relativi per campione]" )