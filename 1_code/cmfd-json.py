import csv
import json

csv_file = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/frequency_cmfd_filtered&rmdup.csv'
json_file = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/0_data/wordlist/cmfd_final.json'

foundations = ['care', 'fair', 'loya', 'auth', 'sanc', 'general']
wordlist = {foundation: [] for foundation in foundations}

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        foundation = row['foundation']
        token = row['chinese']
        if foundation in foundations:
            wordlist[foundation].append(token)

with open(json_file, 'w') as file:
    json.dump(wordlist, file, ensure_ascii=False)

for foundation, items in wordlist.items():
    print(f"Number of items in {foundation}: {len(items)}")