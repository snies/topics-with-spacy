import textacy
import textacy.vsm
import textacy.tm

class TopicModeler:
    def __init__(self, spacy_language: str, data: []):
        self.n_topics=10

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
        self.model=None
        self.doc_topic_matrix=None

    def getTopics(self, n_topics: int=10, n_words: int=10):
        self.n_topics=n_topics
        self.model = textacy.tm.TopicModel("nmf", n_topics=n_topics)
        self.model.fit(self.doc_term_matrix)
        self.doc_topic_matrix = self.model.transform(self.doc_term_matrix)

        result = []
        for topic_idx, top_terms in self.model.top_topic_terms(self.vectorizer.id_to_term, top_n=n_words):
            result.append({'topic_idx': topic_idx, 'top_terms': top_terms})
        return result

    def printInfos(self):
        print('======================================')
        print('=== model ===')
        print(self.model)
        print('=== doc_topic_matrix statistics ===')
        print(self.doc_topic_matrix.shape)
        print(self.doc_topic_matrix)
        print('====== topics by index ============')
        for topic_idx, top_terms in self.model.top_topic_terms(self.vectorizer.id_to_term, topics=range(self.n_topics)):
            print("topic", topic_idx, ":", "   ".join(top_terms))
        print('====== top texts per topic ============')
        for topic_idx, top_docs in self.model.top_topic_docs(self.doc_topic_matrix, topics=range(self.n_topics), top_n=5):
            print('----------')
            print(topic_idx)
            for j in top_docs:
                print(self.corpus[j][:20])
        print('====== most likely topics per text ============')
        for doc_idx, topics in self.model.top_doc_topics(self.doc_topic_matrix, docs=range(30), top_n=3):
            print(self.corpus[doc_idx][:20], ":", topics)
        #p = self.model.termite_plot(self.doc_term_matrix, self.vectorizer.id_to_term, topics=-1,  n_terms=25, sort_terms_by="seriation")
        #p.show()
