CS 6200 INFORMATION RETRIEVAL Fall '17'
Assignment 4

Submitted By : Srijit Ravishankar
NUID : 001282238

SUMMARY :
		** The given instructions contains software installations and running the program that is suitable in MAC environment ** 


GENERAL INSTRUCTIONS :
1. Install Python v.3.6.1
2. Install Java JDK
3. Install Lucene from https://lucene.apache.org/


INSTRUCTIONS TO RUN THE PROGRAM :

Create a text file "query.txt" document that has all the queries in the same directory where the program is. 

TASK 1 :

1. Open Terminal
2. Navigate to the desired directory
3. Add the required JAR files provided
4. Enter the command "java HW4.java"
5. Under the prompt to enter the file path, provide the path to the CORPUS which has the documents to be indexed and ranked.

TASK 2 :

1. Open Terminal
2. Navigate to the desired directory
3. Enter the command "python BM25.py"


OTHER INSTRUCTIONS :

1. HW4.java creates the FOLDER "LUCENE_SCORE_LIST" that has all the top 100 documents for each of the query from the Lucene model.
2. BM25.py creates the FOLDER "BM_25_SCORE_LIST" that has all the top 100 documents for each of the query from the BM25 model.
3. "COMPARISON_REPORT" text file has the detailed comparison between the two models and their results for all 9 given queries.
4. "IMPLEMENTATION_REPORT" text file has the detailed description of the implementation of the BM25 model.