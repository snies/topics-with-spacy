import pandas, textacy
from topics import TopicModeler

# prepare data set from csv
print('reading data file')
df = pandas.read_csv('Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products.csv')
reviews = df[['reviews.id','reviews.rating','reviews.text','reviews.title']]

texts = []
for i,row in reviews.iterrows():
    rating = int(row['reviews.rating'])
    # define which rating you want to include "< 6" includes all 
    if rating < 6:
        texts.append(row['reviews.text']) 


# model topics
print('initalizing topic modeler - this might take a while')
tm = TopicModeler("en_core_web_sm", data=texts)

print('extracting topics')
topics = tm.getTopics(n_topics=10, n_words=10)

for topic in topics:
    print(topic)
