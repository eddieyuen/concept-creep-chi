import pandas as pd
import matplotlib.pyplot as plt
import json

# Define the target concepts and their corresponding column names
target_concepts = ['偏见', '欺凌', '精神病', '创伤', '分裂', '阴谋', '主权', '恐怖主义']

# Read the concept translations from the dictionary
with open('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/0_data/wordlist/concepts.json') as f:
    concept_translations = json.load(f)
# Reverse the key-value pairs in the concept_translations dictionary
english_translations = {value[0]: key for key, value in concept_translations.items()}

# Specify file path
relative_frequency_file_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/tmp/relativefreq_concepts.csv'

# Read relative frequency data
data = pd.read_csv(relative_frequency_file_path)
years = data['Year']

# Set up the figure and axes for the normal plot
plt.rcParams['font.family'] = ['Heiti TC']
fig, ax = plt.subplots(figsize=(10, 8))

# Define a list of colors to use for the line plots
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

# Iterate over each target concept and create line plots
for i, concept in enumerate(target_concepts):
    # Get the English translation for the current concept
    english_translation = english_translations.get(concept, concept)
    # Find the column name that matches the target concept
    matched_column = data.columns[data.columns.str.contains(concept)]
    # Get the color for the current concept
    color = colors[i]
    # Plot relative frequency values for each concept with a unique color
    relativefreq = data[matched_column]
    ax.plot(years, relativefreq, label=f'{english_translation} ({concept})', color=color)

ax.set_ylim(bottom=0)
ax.set_xlabel('Year')
ax.set_ylabel('Relative Frequency')
ax.set_title('Relative Frequency of Target Concepts')
ax.legend()

# Save the normal plot
output_dir = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/3_output/relativefreq'
plt.savefig(f'{output_dir}/relativefreq_concepts.png', dpi=300)

print('Plot saved successfully!')