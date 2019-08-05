import pandas as pd
import re
import nltk

#reading the dataset
dataset = pd.read_csv('amazon_cells_labelled.txt', delimiter = '\t', header=None)

#downloading the new stopwords in case of updation
nltk.download('stopwords')
#importing the stopwords
from nltk.corpus import stopwords
#importing stemmer
from nltk.stem.porter import PorterStemmer
#creating an empty list to store the filtered data
corpus = []
#object for stemmer
ps = PorterStemmer()
#running the loop for every review 
for i in range(0,len(dataset)):
    #replacing anything other than text with space
    review = re.sub('[^a-zA-Z]',' ',dataset[0][1])
    #converting every text to lower
    review = review.lower()
    review = review.split()
    #checking if the word is in stopwords or not
    review = [word for word in review 
          if not word 
          in set(stopwords.words('english'))]
    #stemming the review 
    review = [ps.stem(word) for word in review]
    #making it a list again
    review = ' '.join(review)
    #appending it to a new list
    corpus.append(review)

#initializing Vectorizer
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
#creating features with converting text data to numeric
features = cv.fit_transform(corpus).toarray()
labels = dataset.iloc[:, 1].values

#creating data for training and testing
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

#training the data through MultinomialNB 
from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_nb = confusion_matrix(labels_test, labels_pred)