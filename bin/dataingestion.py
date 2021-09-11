import os

class Ingest:

    def findAllClass(basePath):

        """to find the class names.

        Input:
            path:A String for path of data
        Output:
            classArr:An Array of Strings(classnames)

        """
        classArr = os.listdir(self,basePath)

        return classArr

    def readContentFromDir(self,basePath,className):

        classDir = os.path.join(basePath,className)
        files = os.listdir(classDir)
        contentList = []
        for file in files:
            with open(os.path.join(classDir,file)) as fl:
                content = fl.read()
            contentList.append(content)

        return contentList:

    def collectData(self):

        classNames = self.findAllClass(basePath)
        finalData = {}
        for className in classNames:
            contentList = self.readContentFromDir(basePath,className)
            finalData[className] = contentList
        return finalData

