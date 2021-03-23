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

make the new folder topics-with-spacy into a python venv
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

This assumes you have a file `german_review_data.json' structured like this:  
```shell
[ 
    {"id": "123", "type": "foo", "attributes": {"date": "2020-12-05T05:40:12Z", "review": "Ein langer Review auf deutsch.", "userName": "User123", "rating": 4}},
    {"id": ...}
    ...    
]
```