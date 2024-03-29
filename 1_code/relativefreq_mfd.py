import pandas as pd

# Specify the file path
relativefreq_mfd_items_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/relativefreq_mfd_items.csv'
# Read the CSV file
data = pd.read_csv(relativefreq_mfd_items_path)
# Extract the relevant column sets
harm_columns = data.iloc[:, 1:9]
fairness_columns = data.iloc[:, 9:17]
ingroup_columns = data.iloc[:, 17:25]
authority_columns = data.iloc[:, 25:33]
purity_columns = data.iloc[:, 33:41]

# Calculate the mean values for each set of columns
harm_mean = harm_columns.mean(axis=1)
fairness_mean = fairness_columns.mean(axis=1)
ingroup_mean = ingroup_columns.mean(axis=1)
authority_mean = authority_columns.mean(axis=1)
purity_mean = purity_columns.mean(axis=1)

# Assign labels to the calculated mean values
harm_mean.name = 'Harm'
fairness_mean.name = 'Fairness'
ingroup_mean.name = 'Ingroup'
authority_mean.name = 'Authority'
purity_mean.name = 'Purity'

# Combine the mean values into a new DataFrame
mean_values = pd.concat([data['Year'], harm_mean, fairness_mean, ingroup_mean, authority_mean, purity_mean], axis=1)

# Save the mean values as a CSV file
output_dir = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/tmp'
output_path = f'{output_dir}/relativefreq_mfd.csv'
mean_values.to_csv(output_path, index=False)

print('Mean values saved successfully as a CSV file!')