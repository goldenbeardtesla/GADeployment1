import os

class Ingest:

    def findAllClass(path):

        """to find the class names.

        Input:
            path:A String for path of data
        Output:
            classArr:An Array of Strings(classnames)

        """
        classArr = os.listdir(path)

        return classArr

    def readContentFromDir():
        pass

    def collectData():
        pass
