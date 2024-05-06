import pandas as pd
import json
from gensim.models import Word2Vec

folderpath = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/quali_cos-sim-time-series'
# Load the JSON data into a dictionary
json_file = f'{folderpath}/all-n.json'
with open(json_file, 'r', encoding='utf-8') as file:
    word_neighbors_dict = json.load(file)

# Load the concept mappings from English to Chinese
concepts_file = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/0_data/wordlist/concepts.json'
with open(concepts_file, 'r', encoding='utf-8') as file:
    concept_mappings = json.load(file)

# Iterate over the target concepts
for concept, word_neighbors in word_neighbors_dict.items():
    # Get the Chinese concept name from the mappings
    chinese_concept = concept_mappings[concept][0]

    # Create a new CSV file for the target concept
    csv_file = f'{folderpath}/{concept}_cos-sim.csv'

    # Load the yearly Word2Vec models
    word2vec_models = {}  # Dictionary to store the models
    print(f'{concept}: Loading Word2Vec models')
    for year in range(1979, 2024):
        model_file = f'/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/models/pd_{year}.model'
        model = Word2Vec.load(model_file)
        word2vec_models[year] = model

    # Create the DataFrame with 'Year' as the first column
    df = pd.DataFrame({'Year': range(1979, 2024)})

    # Iterate over the word neighbors and calculate cosine similarity
    for neighbor in word_neighbors:
        similarity_scores = []
        for year in range(1979, 2024):
            model = word2vec_models[year]
            try:
                similarity = model.wv.similarity(chinese_concept, neighbor)
            except KeyError:
                similarity = None
            similarity_scores.append(similarity)
        df[neighbor] = similarity_scores

    # Save the DataFrame to the CSV file
    df.to_csv(csv_file, index=False)
    print(f'Processing for {chinese_concept} done!!')