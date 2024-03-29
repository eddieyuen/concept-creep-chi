import pickle
import json
import csv

# Path to the cleaned text pickle files
cleanedtext_folder = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/cleanedtext/'

# Path to the MFD
mfd_file = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/0_data/wordlist/mfd_short.json'

# Path to the output CSV file
output_csv = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/frequency_mfd_items.csv'

def extract_token_frequency(token, year):
    # Load the cleaned tokens from the pickle file
    cleanedtext_path = cleanedtext_folder + f'cleaned_{year}.pkl'
    with open(cleanedtext_path, 'rb') as f:
        cleaned_tokens = pickle.load(f)

    # Count the frequency of the token
    token_frequency = sum(token == t for sentence in cleaned_tokens for t in sentence)

    return token_frequency

# Load the items from the MFD
with open(mfd_file, 'r') as f:
    mfd_data = json.load(f)

# Prepare the header and data for the CSV file
header = ['Year'] + [token for token_set in mfd_data.values() for token in token_set]
data = []
print('Header set-up successfully.')

# Extract the frequencies for each token and year
for year in range(1979, 2024):
    row = [year]
    for token_set in mfd_data.values():
        for token in token_set:
            frequency = extract_token_frequency(token, year)
            row.append(frequency)
            print(f'Frequency for {token} in {year} computed.')
    data.append(row)
    print(f'Frequency data ready for year {year}')

# Write the data to the output CSV file
with open(output_csv, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print("Frequency data has been successfully stored in the CSV file.")