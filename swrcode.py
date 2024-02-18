import nltk
import string
from nltk.corpus import stopwords
cachedStopWords = set(stopwords.words("english"))
cachedStopWords.update('and')
with open('data/jsptf.txt','r') as inFile, open('data/newfile.txt','w') as outFile:
    for line in inFile.readlines():
        print(" ".join([word for word in line.lower().translate(str.maketrans('', '', string.punctuation)).split()
                        if len(word) >=4 and word not in cachedStopWords]), file=outFile)
        
