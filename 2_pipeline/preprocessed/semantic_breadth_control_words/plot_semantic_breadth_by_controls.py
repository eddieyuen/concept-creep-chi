import pandas as pd
import matplotlib.pyplot as plt
import json

# Read the mean semantic breadth file
mean_data = pd.read_csv('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/semantic_breadth_control_words/controls_semantic_breadth_mean.csv', index_col='Year')

# Read the concept translations from the dictionary
with open('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/0_data/wordlist/control_words.json') as f:
    concept_translations = json.load(f)

# Define the target concepts
target_concepts = ['衣服', '米饭', '图书馆', '运输']
# Reverse the key-value pairs in the concept_translations dictionary
english_translations = {value[0]: key for key, value in concept_translations.items()}

# Specify the output directory
output_directory = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/semantic_breadth_control_words/'

# Iterate over each target concept and create line plots
for concept in target_concepts:
    # Get the English translation for the current concept
    english_translation = english_translations.get(concept, concept)

    # Set up the figure and axes
    plt.rcParams['font.family'] = ['Heiti TC']
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Read the individual files for the current concept
    individual_files = [f'/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/semantic_breadth_control_words/controls_sb_{i}_transposed.csv' for i in range(1, 11)]
    
    # Iterate over each individual file and plot as dashed lines
    for file in individual_files:
        df = pd.read_csv(file, index_col='Year')
        semantic_breadth_values = df[concept + '_Semantic_Breadth']
        ax.plot(semantic_breadth_values, linestyle='dashed', alpha=0.5)
    
    # Plot the mean semantic breadth as a thicker line with data points
    mean_semantic_breadth = mean_data[concept + '_Semantic_Breadth']
    ax.plot(mean_semantic_breadth, linewidth=2, color='black', label='Mean', marker='o', markersize=5)
    mean_semantic_breadth.interpolate().plot(linewidth=2, color='black', linestyle='dashed', alpha=0.5, label='')
    
    # Set the x-axis range from 1979 to 2023
    ax.set_xlim(1979, 2024)
    
    # Set the x-axis and y-axis labels
    ax.set_xlabel('Year')
    ax.set_ylabel('Semantic Breadth')
    
    # Set the title of the plot
    ax.set_title(f'Semantic Breadth of Concept: {english_translation.capitalize()} ({concept})')
    
    # Show the legend
    ax.legend()
    
    # Save the plot to the output directory
    output_file = output_directory + f'semantic-breadth_{english_translation}.png'
    plt.savefig(output_file)

    # Close the plot
    plt.close()

print("Plots saved successfully.")