
import gensim
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
# need to install nltk corpus first!
# nltk.download()


def score(text, label, model):
    score_list = []
    for word in text:
        try:
            score_list.append(model.similarity(word, label))
        except KeyError as e:
            continue
    return score_list


def remove_stop_words(text):
    text = [w for w in text if w not in stopwords.words('english')]
    return text


def tokenize_remove_punctuation(txt_str):
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(txt_str)
    return text


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
    
    txt_string = 'Count me among the embittered, my frustration growing with each passing year as another ' \
                 'European sports wagon or hot hatch fails to make it to this side of the Atlantic.'
    words = tokenize_remove_punctuation(txt_string)
    words = remove_stop_words(words)
    scores = score(words, keywords[0], model)
    print scores
    print max(scores)