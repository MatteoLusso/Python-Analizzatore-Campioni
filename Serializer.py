import pickle as pk

def saveVariable( name, var, path ):

    with open( path + "\\" + name + "SAVE.pkl", "wb" ) as saveFile:

        print( "\n      +++ Salvataggio file " + name + "SAVE.pkl in corso +++" )

        pk.dump(var, saveFile)
        saveFile.close()

def loadVariable( name, path, checkOnly = False ):

    try:

        with open( path + "\\" + name + "SAVE.pkl", "rb" ) as reloaded:

            if checkOnly is False:

                print( "\n      +++ Caricamento da file " + name + "SAVE.pkl in corso +++" )

                var =  pk.load( reloaded )
                reloaded.close()

                return var

            else:

                print( "\n      +++ Il file " + name + "SAVE.pkl esiste +++" )

                return "Not empty"

    except:

        print( "\n      +++ Il file " + name + "SAVE.pkl non esiste +++" )

        return None

    finally:

        pass