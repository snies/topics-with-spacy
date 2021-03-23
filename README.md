# topics-with-spacy

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

Download default trained pipeline packages for English () and/or German (570MB)
```shell
python -m spacy download en_core_web_sm
python -m spacy download de_core_news_lg
```
More info: https://spacy.io/usage/models

## Run the examples



# english reviews from kaggle (amazon dataset)

download the dataset from kaggle 

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
/home/snies/repos/topics-with-spacy/lib/python3.8/site-packages/sklearn/decomposition/_nmf.py:1076: ConvergenceWarning: Maximum number of iterations 200 reached. Increase it to improve convergence.
  warnings.warn("Maximum number of iterations %d reached. Increase it to"
{'topic_idx': 0, 'top_terms': ('the', 'of', 'is', 'and', 'screen', 'The', 'Kindle', 'better', 'one', 'Echo')}
{'topic_idx': 1, 'top_terms': ('loves', 'it', 'for', 'she', 'my', 'old', 'this', 'he', 'and', 'year')}
{'topic_idx': 2, 'top_terms': ('tablet', 'for', 'price', 'kids', 'good', 'games', 'apps', 'perfect', 'this', 'This')}
{'topic_idx': 3, 'top_terms': ('use', 'to', 'easy', 'Easy', 'set', 'up', 'and', 'Very', 'Easy to use', 'read')}
{'topic_idx': 4, 'top_terms': ('I', 'my', 'it', 'this', 'bought', 'would', 'have', 'one', 'that', 'to')}
{'topic_idx': 5, 'top_terms': ('Great', 'product', 'recommend', 'Great product', 'price', 'would', 'family', 'friends', 'gift', 'and')}
{'topic_idx': 6, 'top_terms': ('great', 'is', 'This', 'It', 'works', 'The', 'and', 'Works', 'product', 'it')}
{'topic_idx': 7, 'top_terms': ('to', 'you', 'can', 'it', 'Alexa', 'with', 'on', 'have', 'music', 'that')}
{'topic_idx': 8, 'top_terms': ('love', 'they', 'kids', 'them', 'it', 'They', 'and', 'We', 'My', 'these')}
{'topic_idx': 9, 'top_terms': ('very', 'good', 'happy', 'with', 'is', 'and', 'purchase', 'quality', 'The', 'Very')}
```


# german reviews from an app store
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
python topics_from_english_reviews.py
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
