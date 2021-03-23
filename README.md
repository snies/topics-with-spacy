# topics-with-spacy

Some examples on how to extract topics from a collection of texts using spacy and textacy.

## Uses spaCy and Textacy 
https://spacy.io/

https://github.com/chartbeat-labs/textacy

https://textacy.readthedocs.io/en/stable/

## Installation

clone from github:
```shell
git clone git@github.com:snies/topics-with-spacy.git
```

make the new folder `topics-with-spacy` into a python venv
```shell
python3 -m venv topics-with-spacy/
```

go into the new folder and activate the venv
```shell
cd topics-with-spacy/
source bin/activate
```
More info: https://docs.python.org/3/tutorial/venv.html


user pip to install all the dependencies 
```shell
pip3 install -r requirements.txt
```

Download default trained pipeline packages for English (12MB) and/or German (570MB)
```shell
python -m spacy download en_core_web_sm
python -m spacy download de_core_news_lg
```
More info: https://spacy.io/usage/models

## Run the examples

### english news from kaggle (BBC)

this assumes you have a file called `BBC-News-Train.csv` from this kaggle dataset: 

https://www.kaggle.com/c/learn-ai-bbc


run the english news example 
```shell
python topics_from_english_news.py

```

expected result:

```shell
{'topic_idx': 0, 'top_terms': ('game', 's', 'win', 'play', 'england', '6', 'player', 'say', 't', 'match')}
{'topic_idx': 1, 'top_terms': ('mr', 'labour', 'election', 'blair', 'party', 'brown', 'say', 'minister', 'government', 'howard')}
{'topic_idx': 2, 'top_terms': ('$', 's', 'say', 'growth', 'be', 'year', 'us', 'sale', 'economy', 'rise')}
{'topic_idx': 3, 'top_terms': ('film', 'award', 'well', 'star', 'actor', 's', 'actress', 'win', 'director', 'oscar')}
{'topic_idx': 4, 'top_terms': ('mobile', 'phone', 'people', 'technology', 'music', 'service', 'say', 'user', 'digital', 'gadget')
```

### english reviews from kaggle (amazon dataset)

this assumes you have a file called `Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products.csv` from this kaggle dataset: 

https://www.kaggle.com/datafiniti/consumer-reviews-of-amazon-products

run the english reviews example 
```shell
python topics_from_english_reviews.py

```


expected result:
```shell
reading data file
initalizing topic modeler - this might take a while
extracting topics
{'topic_idx': 0, 'top_terms': ('Alexa', 'Echo', 'music', 'echo', 'device', 'Love', 'like', 'light', 'Amazon', 'home')}
{'topic_idx': 1, 'top_terms': ('love', 'buy', 'gift', 'daughter', 'Christmas', 'absolutely', 'Bought', 'son', 'grandson', 'wife')}
{'topic_idx': 2, 'top_terms': ('tablet', 'app', 'price', 'need', 'child', 'game', 'little', 'perfect', 'Great', 'Amazon')}
{'topic_idx': 3, 'top_terms': ('use', 'easy', 'Easy', 'set', 'setup', 'fun', 'son', 'light', 'navigate', 'convenient')}
{'topic_idx': 4, 'top_terms': ('read', 'book', 'Kindle', 'kindle', 'game', 'size', 'like', 'light', 'Fire', 'well')}
{'topic_idx': 5, 'top_terms': ('product', 'Great', 'recommend', 'price', 'friend', 'highly', 'buy', 'family', 'service', 'Best')}
{'topic_idx': 6, 'top_terms': ('great', 'work', 'Works', 'price', 'sound', 'little', 'battery', 'life', 'need', 'gift')}
{'topic_idx': 7, 'top_terms': ('kid', 'app', 'game', 'lot', 'play', 'amazon', 'friendly', 'learn', 'free', 'entertain')}
{'topic_idx': 8, 'top_terms': ('old', 'year', '2', '3', '4', 'Bought', '2 year old', 'son', '8', 'grandson')}
{'topic_idx': 9, 'top_terms': ('good', 'price', 'quality', 'sound', 'pretty', 'picture', 'work', 'nice', 'Good', 'look')}
```


### german reviews from an app store
This assumes you have a file `german_review_data.json` structured like this:  
```shell
[ 
    {"id": "123", "type": "foo", "attributes": {"date": "2020-12-05T05:40:12Z", "review": "Ein langer Review auf deutsch.", "userName": "User123", "rating": 4}},
    {"id": ...}
    ...    
]
```

run the german reviews example:
```shell
python topics_from_german_reviews.py
```

expected result:
```shell
reading data file
initalizing topic modeler - this might take a while
extracting topics
{'topic_idx': 0, 'top_terms': ('App', 'Auto', 'Brand', 'neu', 'laufen', 'Problem', 'Datum', 'nutzen', 'einfach', 'Woche')}
{'topic_idx': 1, 'top_terms': ('Update', 'stürzen', 'iOS', '13', 'App', 'letzt', 'iOS 13', 'iPhone', 'Version', 'starten')}
{'topic_idx': 2, 'top_terms': ('Fahrzeug', 'Verbindung', 'Datum', 'Meldung', 'anzeigen', 'obwohl', 'falsch', 'Kommunikation', 'senden', 'aufbauen')}
{'topic_idx': 3, 'top_terms': ('Funktion', 'nützliche', 'nutzen', 'frei', 'spannen', 'instabil', 'Passat', 'tollen', 'Ziel', 'senden')}
{'topic_idx': 4, 'top_terms': ('funktionieren', 'zuverlässig', 'App', 'Woche', 'Stern', 'perfekt', 'Monat', 'bekommen', 'Connect', 'rein')}
{'topic_idx': 5, 'top_terms': ('Funktioniert', 'Verbindung', 'irgendwie', 'wunderbar', 'Versuch', 'komplizieren', 'Passat', 'zuverlässig', 'GTE', 'WLAN')}
{'topic_idx': 6, 'top_terms': ('Login', 'stürzen', 'nutzbar', 'scheitern', 'Woche', 'unbrauchbar', 'Sitzung', 'Fehler', 'Update', 'ablaufen')}
{'topic_idx': 7, 'top_terms': ('Standheizung', 'starten', 'lässt', 'Versuch', 'ausreifen', 'aktivieren', '2.', 'einschalten', '10', 'dauern')}
{'topic_idx': 8, 'top_terms': ('Stürzt', 'Start', 'sofort', 'letzt', 'iPhone', 'genau', 'benutzen', 'Katastrophe', 'starten', 'einloggen')}
{'topic_idx': 9, 'top_terms': ('mal', 'Mal', 'Verbindungsprobleme', 'Schaut', 's', 'laufen', 'tun', 'jed', 'Auto', 'Tesla')}
```
