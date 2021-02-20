from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import sys

### Initialize objects

tokennizer = RegexpTokenizer(r'\w+')
en_stopwords = set(stopwords.words('english'))
ps = PorterStemmer()


def getStemmedReview(review) :
    review = review.lower()
    review = review.replace("<br />br />"," ")
    
    ## Tokenize
    
    tokens = tokennizer.tokenize(review)
    new_tokens = (token for token in tokens if token not in en_stopwords)
    stemmed_tokens = [(ps.stem(token)) for token in new_tokens]
    
    cleaned_review = ' '.join(stemmed_tokens)
    
    return cleaned_review
    
def getStemmedDoc(inputFile,outputFile):

    out = open(outputFile,'w',encoding="utf8")
    
    with open(inputFile,encoding="utf8") as f:
        reviews = f.readlines()
        
    for review in reviews :
        cleaned_review = getStemmedReview(review)
        print((cleaned_review),file=out)

	
    
## Read command line arguments

inputFile = sys.argv[1]
outputFile = sys.argv[2]

getStemmedDoc(inputFile,outputFile)



## run this code on command prompt and give input and output file name