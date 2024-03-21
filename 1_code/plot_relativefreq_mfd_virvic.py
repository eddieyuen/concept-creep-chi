import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/tmp/relativefreq_mfd_virvic.csv')

foundations = ['Harm', 'Fairness', 'Ingroup', 'Authority', 'Purity']
colors = ['red', 'blue', 'green', 'orange', 'purple']

for foundation, color in zip(foundations, colors):
    virtue_column = f'{foundation}_virtue'
    vice_column = f'{foundation}_vice'
    plt.plot(data['Year'], data[virtue_column], color=color, label=f'{foundation} Virtue')
    plt.plot(data['Year'], data[vice_column], color=color, linestyle='dashed', label=f'{foundation} Vice')
    
    plt.xlabel('Year')
    plt.ylabel('Relative Frequency')
    plt.title(f'Cultural Salience of the {foundation} Foundation')
    plt.legend()
    plt.savefig(f'/Users/kawaiyuen/nlpworkshop/concept-creep-chi/3_output/relativefreq/relativefreq_{foundation.lower()}_virvic.png')
    plt.close()