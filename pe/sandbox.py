
import gensim
import numpy as np
from nltk.corpus import stopwords


def score(text, label, model):
    score = []
    text = text.split(' ')
    for word in text:
        try:
            score.append(model.similarity(word, label))
        except KeyError as e:
            continue
    return score

def remove_stop_words(text, model):
    return ' '.join([word for word in text.split() if word in model.vocab])    

keywords = ['Fun', 
            'Cheap Interior', 
            'Mustang', 
            'Performant', 
            'Expensive', 
            'WRX STI', 
            'Fast', 
            'Bad MPG', 
            'Golf R', 
            'Parctical', 
            'Uncomfortable', 
            'Special',
            ]

if __name__ == "__main__":
    
    print("Importing model...")
    
    # Load Google's pre-trained Word2Vec model.
    model = gensim.models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)  
    
    txt = 'Count me among the embittered, my frustration growing with each passing year as another European sports wagon or hot hatch fails to make it to this side of the Atlantic.'
    txt = remove_stop_words(txt, model)
    scores = score(txt, keywords[0], model) 
    print scores
    print max(scores)