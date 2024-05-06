import pandas as pd
import matplotlib.pyplot as plt
import json

# Read the semantic breadth data from the CSV file
data = pd.read_csv('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/tmp/semantic_breadth_mean_window-size-5.csv')

# Read the concept translations from the dictionary
with open('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/0_data/wordlist/concepts.json') as f:
    concept_translations = json.load(f)

# Extract the year and semantic breadth columns
years = data['Year']

# Define the target concepts
target_concepts = ['偏见', '欺凌', '精神病', '创伤', '分裂', '阴谋', '主权', '恐怖主义']

# Reverse the key-value pairs in the concept_translations dictionary
english_translations = {value[0]: key for key, value in concept_translations.items()}

# Set up the figure and axes for the original plot
plt.rcParams['font.family'] = ['Heiti TC']
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_ylim(1.0, 1.8)

# Define a list of colors to use for the line plots
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

# Iterate over each target concept and create line plots for the original plot
for i, concept in enumerate(target_concepts):
    # Get the English translation for the current concept
    english_translation = english_translations.get(concept, concept)

    # Get the color for the current concept
    color = colors[i]

    # Plot semantic breadth values for the concept
    semantic_breadth = data[concept + '_Semantic_Breadth']
    ax.plot(years, semantic_breadth, label=f'{english_translation.capitalize()} ({concept})', color=color)

ax.set_xlabel('Year')
ax.set_ylabel('Semantic Breadth')
ax.set_ylim(1.0, 1.8)
ax.set_title('Semantic Breadth for Target Concepts')
ax.legend()

# Save the original plot
output_dir = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/3_output/semantic_breadth_window-size-5'
plt.savefig(f'{output_dir}/allconcepts.png', dpi=300)

# Create a new figure and axes for the moving average plot
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_ylim(1.0, 1.8)

# Iterate over each target concept and create line plots for the moving average plot
for i, concept in enumerate(target_concepts):
    # Get the English translation for the current concept
    english_translation = english_translations.get(concept, concept)

    # Get the color for the current concept
    color = colors[i]

    # Plot semantic breadth values for the concept
    semantic_breadth = data[concept + '_Semantic_Breadth']
    ax.plot(years, semantic_breadth, alpha=0.7, linestyle='dashed',linewidth=0.6, color=color)

    # Calculate and plot moving average with window=5
    moving_average = semantic_breadth.rolling(window=5, min_periods=1).mean()
    ax.plot(years, moving_average, label=f'{english_translation.capitalize()} ({concept})', linewidth=2, color=color)

ax.set_xlabel('Year')
ax.set_ylabel('Semantic Breadth')
ax.set_title('Semantic Breadth for Target Concepts (Moving Average Window=5)')
ax.legend()

# Save the moving average plot
plt.savefig(f'{output_dir}/allconcepts_moving-avg.png', dpi=300)

print('Plots saved')