import pandas as pd
from scipy.stats import spearmanr

# Read the CSV file
data = pd.read_csv('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/tmp/semantic_breadth_mean.csv')
years = data["Year"]
semantic_breadth = data.iloc[:, 9:17]

# Compute the Spearman correlation and p-values for each target concept
correlations = []
p_values = []
complete_case_counts = []

for i in range(semantic_breadth.shape[1]):
    concept = semantic_breadth.columns[i]
    concept_values = semantic_breadth.iloc[:, i]

    # Perform complete case analysis for the current concept
    complete_cases = concept_values.dropna()
    complete_case_counts.append(complete_cases.shape[0])

    # Compute Spearman correlation and p-value for the complete cases
    correlation, p_value = spearmanr(years.loc[complete_cases.index], complete_cases)
    correlations.append(correlation)
    p_values.append(p_value)

# Save the output to the specified directory
output_dir = "/Users/kawaiyuen/nlpworkshop/concept-creep-chi/3_output/semantic_breadth/"
output_file = output_dir + "spearman-rho_semantic-breadth_concepts.txt"
with open(output_file, "w") as file:
    for i in range(len(correlations)):
        concept = semantic_breadth.columns[i]
        file.write(f"Target Concept: {concept}\n")
        file.write(f"Number of Complete Cases: {complete_case_counts[i]}\n")
        file.write(f"Spearman Correlation: {correlations[i]}\n")
        file.write(f"P-value: {p_values[i]}\n\n")