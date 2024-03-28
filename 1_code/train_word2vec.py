import pickle
from gensim.models import Word2Vec

model_folder_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/models'
cleanedtext_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/cleanedtext'

def train_word2vec(year):
    cleaned_data_path = cleanedtext_path + '/cleaned_' + str(year) + '.pkl'
    model_path = model_folder_path + '/pd_' + str(year) + '.model'

    with open(cleaned_data_path, 'rb') as f:
        tokenized_data = pickle.load(f)

    model = Word2Vec(tokenized_data, vector_size=300, sg=1, min_count=2)
    model.save(model_path)

    print(f'Successfully trained Word2Vec model for the year {year}!')

for year in range(1979, 2024):
    train_word2vec(year)