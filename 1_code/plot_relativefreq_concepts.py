import pandas as pd
import matplotlib.pyplot as plt
import json

# Load the concepts from the concepts.json file
concepts_file = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/0_data/wordlist/concepts.json'
with open(concepts_file, 'r') as f:
    concepts_data = json.load(f)
    # Reverse the key-value pairs for English translations
    concept_translations = {value[0]: key for key, value in concepts_data.items()}

# Define the corresponding column names of the target concepts
concepts_columns = [concept[0] + '_freq' for concept in concepts_data.values()]

# Specify file path
relativefreq_concepts_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/tmp/relativefreq_concepts.csv'
# Read relative frequency data
data = pd.read_csv(relativefreq_concepts_path)
years = data['Year']

# Set up the figure and axes for the normal plot
plt.rcParams['font.family'] = ['Heiti TC']
fig, ax = plt.subplots(figsize=(10, 8))
# Define a list of colors to use for the line plots
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

# Iterate over each target concept and create line plots
for i, concepts_column in enumerate(concepts_columns):
    # Get the English translation for the current concept
    english_translation = concept_translations.get(concepts_column.split('_')[0])
    # Get the color for the current concept
    color = colors[i]
    # Plot relative frequency values for each concept with a unique color
    relativefreq = data[concepts_column]
    ax.plot(years, relativefreq, label=f'{english_translation} ({concepts_column.split("_")[0]})', color=color)

ax.set_ylim(bottom=0)
ax.set_xlabel('Year')
ax.set_ylabel('Relative Frequency')
ax.set_title('Relative Frequency of Target Concepts')
ax.legend()

# Save the normal plot
output_dir = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/3_output/relativefreq'
plt.savefig(f'{output_dir}/relativefreq_concepts.png', dpi=300)

print('Plot saved successfully!')