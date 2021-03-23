import textacy
import textacy.vsm
import textacy.tm

class TopicModeler:
    def __init__(self, spacy_language: str, data: []):

        self.corpus = textacy.Corpus(
                textacy.load_spacy_lang(spacy_language, 
                disable=("parser", "tagger")), data=data
            )
        self.vectorizer = textacy.vsm.Vectorizer(
                tf_type="linear", apply_idf=True, idf_type="smooth", norm="l2",
                min_df=2, max_df=0.95
            )
        self.doc_term_matrix = self.vectorizer.fit_transform(
                (doc._.to_terms_list(ngrams=1, entities=True, as_strings=True)
                for doc in self.corpus)
            )

    def getTopics(self, n_topics: int=10, n_words: int=10):
        model = textacy.tm.TopicModel("nmf", n_topics=n_topics)
        model.fit(self.doc_term_matrix)
        doc_topic_matrix = model.transform(self.doc_term_matrix)

        result = []
        for topic_idx, top_terms in model.top_topic_terms(self.vectorizer.id_to_term, top_n=n_words):
            result.append({'topic_idx': topic_idx, 'top_terms': top_terms})
        return result
