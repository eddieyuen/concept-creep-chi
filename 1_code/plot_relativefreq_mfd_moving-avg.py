import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/tmp/relativefreq_mfd.csv')

# Extract the data for the five moral foundations
foundations = ['Harm', 'Fairness', 'Ingroup', 'Authority', 'Purity']
data = df[foundations]

# Calculate the moving average with window size = 5
moving_avg_data = data.rolling(window=5, min_periods=1, center=True).mean()

# Plotting the data
plt.figure(figsize=(10, 8))

# Define a list of colors to use for the line plots
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

for i, foundation in enumerate(foundations):
    plt.plot(df['Year'], data[foundation],  alpha=0.6, linewidth=0.6, linestyle='dashed', color=colors[i])  # Plotting the moving average lines 
    plt.plot(df['Year'], moving_avg_data[foundation], label=foundation, linewidth=2.4, color=colors[i])  # Plotting the original lines

plt.xlabel('Year')
plt.ylabel('Relative Frequency')
plt.ylim(bottom=0, top=100)
plt.title('Cultural Salience of Moral Foundations over Time (Moving Average Window = 5)')
plt.legend()

# Save the plot
plt.savefig('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/3_output/relativefreq/cultural-salience_mfd_moving-avg.png', dpi=300)

print('Plot saved')