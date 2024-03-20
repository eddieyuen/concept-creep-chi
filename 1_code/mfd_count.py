import json
import csv

with open('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/0_data/wordlist/mfd_virvic.json') as f:
    mfd = json.load(f)

# Count the number of items for each key
counts = {}
for key in mfd:
    counts[key] = len(mfd[key])

# Output the counts in a CSV file
output_file = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/mfd_count.csv'
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Key', 'Count'])
    for key, count in counts.items():
        writer.writerow([key, count])

print(f"Counts have been written to {output_file}")