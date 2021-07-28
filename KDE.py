import numpy as np

def gaussianKernel(x):
    return ( 1 / np.sqrt( 2 * np.pi ) ) * np.exp ( -0.5 * ( x**2 ) )    # gauss(x) = ( 1 / √( 2 * π ) ) * e^( -0.5 * x^2 )

def getPoint(x, data_array, N = None, bw = None, bwCoeff = 0.0):

        if bw is None:
            bw = 1.05 * np.std( data_array ) * ( len( data_array )**( -1 / 5 ) )   # Regola del pollice di Scott per determinare la banda ottimale h del filtro gaussiano.
        
        bw += bw * ( bwCoeff / 100 )  # La banda h può essere modificata aumentandola o diminuendola in percentuale.

        if N is None:
            N = len( data_array )

        res = 0

        if N > 0:
            for i in range( N ):
                res += gaussianKernel( ( x - data_array[i] ) / bw )
            #res /= ( N * bw )

        return res #res = ( 1 / ( N * h ) ) * Ʃ( gauss( ( x( i ) - data( i ) ) / h ) )

#def getPoint2(x, data, h, dev, var):    # dev = deviazione standard = σ | var = varianza = σ^2 | h = banda filtro gaussiano
                                        # dev = √var <=> σ = √( σ^2 )
    #N = len( data )                         

    #temp = 0.0

    #for value in data:
        #temp += ( 1 / ( np.sqrt( 2 * np.pi ) * dev ) ) * np.exp( ( -1 / ( 2 * np.power( h, 2 ) ) ) * ( np.power( x - value, 2 ) / var ) )

    #return  temp / ( N * h )  # ( 1 / ( N * h ) ) * Ʃ( ( -1 / ( √(2 * π) * σ ) ) * e^( ( -1 / ( 2 * h^2 ) ) * ( ( x( i ) - data( i ) )^2 ) / σ^2 ) )