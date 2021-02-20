from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import sys

### Initialize objects

tokennizer = RegexpTokenizer(r'\w+')
en_stopwords = set(stopwords.words('english'))
ps = PorterStemmer()


def getCleanReview(review) :
    review = review.lower()
    review = review.replace("<br />br />"," ")
    
    ## Tokenize
    
    tokens = tokennizer.tokenize(review)
    new_tokens = (token for token in tokens if token not in en_stopwords)
    stemmed_tokens = [(ps.stem(token)) for token in new_tokens]
    
    cleaned_review = ' '.join(stemmed_tokens)
    
    return cleaned_review
    



