'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

listpol = []
listsub =[]
# Continue your program below! 

for tweet in tweetData:
    #print("tweet test: " + tweet["text"])
    
    tweety=TextBlob(tweet["text"])
    
    #print(tweety.polarity)
    
    listpol.append(tweety.polarity)
    listsub.append(tweety.subjectivity)
print(listpol)
print(listsub)
                
# Textblob sample:
tb = TextBlob("I love potato.")
print(tb.polarity)

averagepol = sum(listpol)/len(listpol)
averagesub = sum(listsub)/len(listsub)

print("-------------------------------------")
print(averagepol)
print("-------------------------------------")
print(averagesub)


plt.hist(listpol)
plt.xlabel('Polarities')
plt.ylabel('Number of Tweets')
plt.title('Histogram of Tweet Polarity')
plt.axis([-1.1, 1.1, 0, 100])
plt.grid(True)
plt.show()

plt.hist(listsub)
plt.xlabel('Polarities')
plt.ylabel('Number of Tweets')
plt.title('Histogram of Tweet Polarity')
plt.axis([-1.1, 1.1, 0, 100])
plt.grid(True)
plt.show()


