import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/tmp/relativefreq_mfd.csv')

# Extract the data for the five moral foundations
foundations = ['Harm', 'Fairness', 'Ingroup', 'Authority', 'Purity']
data = df[foundations]

# Plotting the data
plt.figure(figsize=(10, 8))

for foundation in foundations:
    plt.plot(df['Year'], data[foundation], label=foundation)

plt.xlabel('Year')
plt.ylabel('Relative Frequency')
plt.ylim(bottom=0,top=100)
plt.title('Cultural Salience of Moral Foundations over Time')
plt.legend()

# Save the plot
plt.savefig('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/3_output/relativefreq/cultural-salience_mfd.png', dpi=300)

print('Plot saved')