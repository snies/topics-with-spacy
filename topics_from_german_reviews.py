import json
from topics import TopicModeler

# prepare data as list of texts
print('reading data file')
texts = []
f = open('german_review_data.json','r')
json_data = json.load(f)
f.close()
for jobject in json_data:
    texts.append(jobject['attributes']['review'])

# model topics
print('initalizing topic modeler - this might take a while')
tm = TopicModeler("de_core_news_lg", data=texts)
print('extracting topics')
topics = tm.getTopics(n_topics=10, n_words=10)

for topic in topics:
    print(topic)
