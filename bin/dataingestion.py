import os
import flask
from flask import Flask, request
import json

app = Flask(__name__)


class Ingest:

    def findAllClass(self, basePath):
        """To find the class names.

        Input:
            path: A string for path of data
        Output:
            classArr: An array of String(class names)"""

        classArr = os.listdir(basePath)
        return classArr

    def readContentFromDir(self, basePath, className):

        classDir = os.path.join(basePath, className)
        files = os.listdir(classDir)
        contentList = []
        for file in files:
            with open(os.path.join(classDir, file)) as fl:
                content = fl.read()
            contentList.append(content)
        return contentList

    def collectData(self, basePath):

        classNames = self.findAllClass(basePath)
        finalData = {}
        for className in classNames:
            contentList = self.readContentFromDir(basePath, className)
            finalData[className] = contentList
        return finalData


@app.route('/fetch')
def getData():
    ingestObj = Ingest()
    basePath = r'/Users/prathameshgarge/Desktop/Grey-Atom/GADeployment1/data/20news-18828'
    finalData = ingestObj.collectData(basePath)
    return json.dumps(finalData)


app.run('localhost', 5000)





