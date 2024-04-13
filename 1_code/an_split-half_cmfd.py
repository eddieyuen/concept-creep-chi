import pandas as pd
import random

data = pd.read_csv('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/relativefreq_cmfd_items.csv')

year_column = data['Year']
harm_columns = data.columns[(data.columns.get_loc('同情')):(data.columns.get_loc('摒弃') + 1)].tolist()
fairness_columns = data.columns[(data.columns.get_loc('一纸空文')):(data.columns.get_loc('不当') + 1)].tolist()
ingroup_columns = data.columns[(data.columns.get_loc('万众一心')):(data.columns.get_loc('暴恐') + 1)].tolist()
authority_columns = data.columns[(data.columns.get_loc('一把手')):(data.columns.get_loc('抱怨') + 1)].tolist()
purity_columns = data.columns[(data.columns.get_loc('一尘不染')):(data.columns.get_loc('肮脏') + 1)].tolist()
general_morality_columns = data.columns[(data.columns.get_loc('一往无前')):(data.columns.get_loc('雷打不动') + 1)].tolist()

random.shuffle(harm_columns)
random.shuffle(fairness_columns)
random.shuffle(ingroup_columns)
random.shuffle(authority_columns)
random.shuffle(purity_columns)
random.shuffle(general_morality_columns)

shuffled_columns = ['Year'] + harm_columns + fairness_columns + ingroup_columns + authority_columns + purity_columns + general_morality_columns
shuffled_data = data[shuffled_columns]
shuffled_data.to_csv('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/relativefreq_cmfd_items_shuffled.csv', index=False)