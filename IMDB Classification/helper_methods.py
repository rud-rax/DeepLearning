import re
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def get_word_count(text) :
    return len(text.split())

def data_preprocessing(text) :

    text = text.lower()
    text = re.sub('<br />' , "" , text)
    text = re.sub(r"http\S+www\S+https\S+" , "", text , flags= re.MULTILINE)
    text = re.sub(r"\@w+|\#", "" , text)
    text = re.sub(r"[^\w\s]" , "" , text)
    text_tokens = word_tokenize(text)
    filtered_text = [w for w in text_tokens if not w in stop_words]

    return " ".join(filtered_text)

stemmer= PorterStemmer()
def stemming(data) :
    text = [stemmer.stem(word) for word in data]

if __name__ == "__main__" :

    # Test data_preprocessing
    print(data_preprocessing("A wonderful little production. <br /><br />The"))