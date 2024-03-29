import pandas as pd
import pickle

# Load the CSV file
cmfd_data = pd.read_csv('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/0_data/wordlist/cmfd.csv')

# Load the pickle file
with open('/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/cleanedtext/cleaned_1979.pkl', 'rb') as file:
    cleaned_tokens = pickle.load(file)

# Function to count frequency
def count_frequency(tokens, target):
    count = 0
    for sentence in tokens:
        for token in sentence:
            if token == target:
                count += 1
    return count

# Add frequency column to cmfd_data
cmfd_data['frequency'] = cmfd_data['chinese'].apply(lambda x: count_frequency(cleaned_tokens, x))

# Save the updated data to a new CSV file
cmfd_data.to_csv('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/frequency_cmfd.csv', index=False)