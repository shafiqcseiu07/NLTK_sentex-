import string
from itertools import chain

from nltk.corpus import movie_reviews as mr
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.classify import NaiveBayesClassifier as nbc
import nltk

stop = stopwords.words('english')
documents = [([w for w in mr.words(i) if w.lower() not in stop and w.lower() not in string.punctuation], i.split('/')[0]) for i in mr.fileids()]

word_features = FreqDist(chain(*[i for i,j in documents]))
#word_features = word_features.keys()[:100]
word_features = word_features.keys()

numtrain = int(len(documents) * 90 / 100)
train_set = [({i:(i in tokens) for i in word_features}, tag) for tokens,tag in documents[:numtrain]]
test_set = [({i:(i in tokens) for i in word_features}, tag) for tokens,tag in documents[numtrain:]]

classifier = nbc.train(train_set)
print (nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(5)


#Output:
#Most Informative Features
 #            astounding = True              pos : neg    =     14.6 : 1.0
 #                avoids = True              pos : neg    =     14.6 : 1.0
   #         fascination = True              pos : neg    =     13.7 : 1.0
    #          ludicrous = True              neg : pos    =     12.3 : 1.0