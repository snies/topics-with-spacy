import pandas
from topics import TopicModeler

# prepare data set from csv
print('reading data file')
df = pandas.read_csv('BBC-News-Train.csv')

texts = []
for i,row in df.iterrows():
    texts.append(row['Text']) 


# model topics
print('initalizing topic modeler - this might take a while')
tm = TopicModeler("en_core_web_sm", data=texts)

print('extracting topics')
topics = tm.getTopics(n_topics=5, n_words=10)

for topic in topics:
    print(topic)
