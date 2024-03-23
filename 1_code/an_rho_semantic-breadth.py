import pandas as pd
from scipy.stats import spearmanr

data = pd.read_csv('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/tmp/semantic_breadth_mean.csv')
years = data["Year"]
semantic_breadth = data.iloc[:, 9:17]  

# Perform complete case analysis by excluding missing values
complete_cases = semantic_breadth.dropna()
complete_case_counts = []

# Compute the Spearman correlation and p-values for complete cases
correlations = []
p_values = []

for i in range(complete_cases.shape[1]):
    concept = complete_cases.columns[i]
    complete_case_count = complete_cases.iloc[:, i].count()
    complete_case_counts.append(complete_case_count)
    correlation, p_value = spearmanr(years.loc[complete_cases.index], complete_cases.iloc[:, i])
    correlations.append(correlation)
    p_values.append(p_value)

# Save the output to the specified directory
output_dir = "/Users/kawaiyuen/nlpworkshop/concept-creep-chi/3_output/semantic_breadth/"
output_file = output_dir + "spearman-rho_output.txt"
with open(output_file, "w") as file:
    for i in range(len(correlations)):
        concept = semantic_breadth.columns[i]
        file.write(f"Target Concept: {concept}\n")
        file.write(f"Number of Complete Cases: {complete_case_counts[i]}\n")
        file.write(f"Spearman Correlation: {correlations[i]}\n")
        file.write(f"P-value: {p_values[i]}\n\n")