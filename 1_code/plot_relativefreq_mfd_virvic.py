import pandas as pd
import matplotlib.pyplot as plt

data_virvic = pd.read_csv('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/tmp/relativefreq_mfd_virvic.csv')
data_combined = pd.read_csv('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/tmp/relativefreq_mfd.csv')

foundations = ['Harm', 'Fairness', 'Ingroup', 'Authority', 'Purity']
colors = ['red', 'blue', 'green', 'orange', 'purple']

for foundation, color in zip(foundations, colors):
    virtue_column = f'{foundation}Virtue'
    vice_column = f'{foundation}Vice'
    plt.plot(data_combined['Year'], data_combined[foundation], color=color, linestyle='solid', linewidth=2, label=foundation)
    plt.plot(data_virvic['Year'], data_virvic[virtue_column], color=color, linestyle='dotted', linewidth=0.8, alpha=0.7, label=f'{foundation} Virtue')
    plt.plot(data_virvic['Year'], data_virvic[vice_column], color=color, linestyle='dashed', linewidth=0.8, alpha=0.7, label=f'{foundation} Vice')
    
    plt.xlabel('Year')
    plt.ylabel('Relative Frequency')
    plt.title(f'Cultural Salience of the {foundation} Foundation')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'/Users/kawaiyuen/nlpworkshop/concept-creep-chi/3_output/relativefreq/relativefreq_mf_{foundation.lower()}_virvic.png')
    plt.close()