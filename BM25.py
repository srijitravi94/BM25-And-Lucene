# importing necessary libraries
import os
from math import log


# Declaring global variables
k1 = 1.2
k2 = 100
b = 0.75
R = 0.0
r = 0
N = 1000
QUERY = "query.txt"
BM_25_SCORE_LIST = "BM_25_SCORE_LIST"
INPUT_DIRECTORY = "CORPUS"
INPUT_FOLDER = os.getcwd() + "/" + INPUT_DIRECTORY


# Function to generate Inverted Index from the given corpus files 
def generateInvertedIndex():
    invertedIndex = {}
    tokenDict = {}
    files = os.listdir(INPUT_FOLDER)
    for file in files:
        contents = open(INPUT_DIRECTORY + "/" + file, "r").read()
        words = contents.split()
        length = len(words)
        file = file[:-4]
        tokenDict[file] = length
        for i in range(length):
            word = words[i]
            if word not in invertedIndex.keys():
                docIDCount = {file : 1}
                invertedIndex[word] = docIDCount
            elif file in invertedIndex[word].keys():
                invertedIndex[word][file] += 1
            else:
                docIDCount = {file : 1}
                invertedIndex[word].update(docIDCount)
    return invertedIndex


# Function to parse the queries
def queryParser(query):
    file = open(query,'r').read().splitlines()
    queries = []
    for query in file:
        queries.append(query.split())
    return queries


# Function that returns a dictionary of term and its frequency in a query
def queryFrequency(query):
    queryFreq = {}
    for term in query:
        if term in queryFreq.keys():
            queryFreq[term] += 1
        else:
            queryFreq[term] = 1
    return queryFreq


# Function to calculate the length of each document in the corpus 
def calculateLength():
    fileLengths = {}
    files = os.listdir("CORPUS")
    for file in files:
        doc = open("CORPUS/" + file,'r').read()
        file = file[:-4]
        fileLengths[file] = len(doc.split())
    return fileLengths


# Function to calculate average length of all the documents in the corpus
def calculateAverageLength(fileLengths):
    avgLength = 0
    for file in fileLengths.keys():
        avgLength += fileLengths[file]
    return avgLength/N


# Function to calculate BM25 score
def calculateBM25(n, f, qf, r, N, dl, avdl):
    K = k1 * ((1 - b) + b * (float(dl) / float(avdl)))
    Q1 = log(((r + 0.5) / (R - r + 0.5)) / ((n - r + 0.5) / (N - n - R + r + 0.5)))
    Q2 = ((k1 + 1) * f) / (K + f)
    Q3 = ((k2 + 1) * qf) / (k2 + qf)
    return Q1 * Q2 * Q3


# Function to score the documents based on the given query
def findDocumentsForQuery(query, invertedIndex, fileLengths):
    queryFreq = queryFrequency(query)
    avdl = calculateAverageLength(fileLengths)
    BM25ScoreList = {}
    for term in query:
        if term in invertedIndex.keys():
            qf = queryFreq[term]
            docDict = invertedIndex[term]
            for doc in docDict:
                n = len(docDict)
                f = docDict[doc]
                dl = fileLengths[doc]
                BM25 = calculateBM25(n, f, qf, r, N, dl, avdl)
                if doc in BM25ScoreList.keys():
                    BM25ScoreList[doc] += BM25
                else:
                    BM25ScoreList[doc] = BM25
    return BM25ScoreList


# Function to write top 100 ranked documents for each query 
def writeToFile(queries, invertedIndex, fileLengths):
    queryID = 1
    queryNames = open(QUERY, 'r').read().splitlines()
    for query in queries:
        BM25ScoreList = findDocumentsForQuery(query, invertedIndex, fileLengths)
        sortedScoreList = sorted(BM25ScoreList.items(), key=lambda x:x[1], reverse=True)
        if not os.path.exists(BM_25_SCORE_LIST):
            os.makedirs(BM_25_SCORE_LIST)
        file = open( BM_25_SCORE_LIST + "/BM_25_SCORE_LIST_" + str(queryNames[queryID-1]) + ".txt", "w")
        for rank in range(100):
            text = str(queryID) +  "   " + "Q0" +  "   " + str(sortedScoreList[rank][0]) + "   " + str(rank+1) +  "   " + str(sortedScoreList[rank][1]) +  "   " + "BM25" +"\n"
            file.write(text)
        queryID += 1


# Main function
def main():
    queries = queryParser(QUERY)
    invertedIndex = generateInvertedIndex()
    fileLengths = calculateLength()
    writeToFile(queries, invertedIndex, fileLengths)
main()
