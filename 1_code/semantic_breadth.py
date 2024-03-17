import random
import numpy as np
import pandas as pd
from gensim.models import Word2Vec
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import json
import time

# Initialize an empty list to store the results
results = []

# Initialize an empty dictionary to store the concept usages
concept_usages_dict = {}

# Read the concepts from the JSON file
with open('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/0_data/wordlist/concepts.json', 'r') as f:
    concepts = json.load(f)

# Prompt the user for input regarding the naming of the output files
file_number = input("Enter the filenumber (1, 2, 3, 4, etc.): ")

# Loop through the years from 1979 to 2021
for year in range(1979, 2022):

    # Load the pretrained Word2Vec model and cleaned data for the year
    model_path = f'/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/models/pd_{year}.model'
    try:
        model = Word2Vec.load(model_path)
    except FileNotFoundError:
        print(f"Model not found for {year}. Skipping...")
        continue

    cleaned_data_path = f'/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/cleanedtext/cleaned_{year}.pkl'
    with open(cleaned_data_path, 'rb') as f:
        cleaned_data = pickle.load(f)

    # Loop through the concepts and their first items in the list
    for key, value in concepts.items():
        concept = value[0]  # Get the first item in the list

        # Step 1: Randomly sample specific usages of a concept from the corpus
        token_occurrence = [token for sentence in cleaned_data for token in sentence if token == concept]
        token_frequency = len(token_occurrence)
        print(f'Frequency for {concept} in {year}: {token_frequency}')

        # Check the population size and adjust the sampling accordingly
        if token_frequency < 20:
            print(f"The frequency for '{concept}' in {year} is smaller than 20. Skipping the year.")
            # Append 'NA' values to the results list for this year and concept
            results.append({'Year': year, 'Concept': concept, 'Mean Cosine Similarity': 'NA', 'Semantic Breadth': 'NA'})
            continue
        elif 20 <= token_frequency <= 50:
            concept_usages = [sentence for sentence in cleaned_data if concept in sentence]
        else:
            concept_usages = [sentence for sentence in cleaned_data if concept in sentence]
            if len(concept_usages) > 50: 
                random.seed(int(time.time()))
                random_concept_usages = random.sample(concept_usages, k=50)
                concept_usages = random_concept_usages

        # Store the concept usages in the dictionary
        key = (year, concept)
        concept_usages_dict[str(key)] = concept_usages
            
        # Step 2: Compute the context vectors for each specific usage of the concept
        if 'concept_usages' in locals():
            context_vectors = []
            window_size = 9
            context_window_lists = []  # To store the words within the context window for each specific usage

            for sentence in concept_usages:
                context_words = []  # To store the words within the context window

                # Find the position of the target concept within the sentence
                concept_position = [i for i, token in enumerate(sentence) if token == concept]

                # For each instance of the target concept, extract the words within the context window
                for position in concept_position:
                    start_index = max(0, position - window_size)
                    end_index = min(len(sentence), position + window_size + 1)
                    context_words.extend(sentence[start_index:position] + sentence[position + 1:end_index])

                # Get the word vectors for the context words (if available in the Word2Vec model)
                context_vectors.extend([model.wv[word] for word in context_words if word in model.wv])

                # Store the context words in a list for printing
                context_window_lists.append(context_words)

            # Normalize the context vectors
            context_vectors = np.array(context_vectors)
            normalized_context_vectors = context_vectors / np.linalg.norm(context_vectors, axis=1, keepdims=True)

            # Step 3: Calculate pairwise cosine similarities among the sampled specific usages
            pairwise_similarities = cosine_similarity(normalized_context_vectors)

            # Step 4: Calculate semantic breadth index as the inverse of the mean cosine similarity
            mean_cosine_similarity = np.mean(pairwise_similarities)
            semantic_breadth = 1 / mean_cosine_similarity

            # Append the results to the list
            results.append({'Year': year, 'Concept': concept, 'Mean Cosine Similarity': mean_cosine_similarity, 'Semantic Breadth':semantic_breadth})

# Convert the results list to a DataFrame
results_df = pd.DataFrame(results)

# Define the path to the output CSV file
output_path = f'/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/semantic_breadth/semantic_breadth_{file_number}.csv'

# Save the DataFrame as a CSV file
results_df.to_csv(output_path, index=False)

print("Semantic breadth output saved to: ", output_path)

# Transposing the CSV file output
# Read the original CSV file
df = pd.read_csv(output_path)

# Transpose the DataFrame to have concepts as columns and years as rows
transposed_df = df.pivot(index='Year', columns='Concept', values=['Mean Cosine Similarity', 'Semantic Breadth'])

# Flatten the column labels
transposed_df.columns = [f"{col[1]}_{col[0].replace(' ', '_')}" for col in transposed_df.columns]

# Save the transposed DataFrame to a new CSV file
transposed_df.to_csv(f'/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/semantic_breadth/semantic_breadth_{file_number}_transposed.csv', index_label='Year')

print("CSV file with the desired structure has been created.")

# Save the concept usages dictionary as a JSON file
concept_usages_output_path = f'/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/semantic_breadth/concept_usages_{file_number}.json'
with open(concept_usages_output_path, 'w') as f:
    json.dump(concept_usages_dict, f, indent=4)
print('Concept usages JSON file saved.')
