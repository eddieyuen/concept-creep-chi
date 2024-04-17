import glob
from gensim.models import Word2Vec
from utils import smart_procrustes_align_gensim, intersection_align_gensim

# --- List all raw models and order them by name
allmodels = sorted(glob.glob('/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/models/pd_*.model'))

# --- Load last model (fixed time slice)
model1 = Word2Vec.load(allmodels[-1])

# --- Just get the model name and make a copy in the aligned folder
model1_name = allmodels[-1].split('/')[-1]
model1.save('/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/models_aligned/{}'.format(model1_name))

# --- Align each of the models to the model for the last time slice
for model in allmodels[:-1]:
    model2_name = model.split('/')[-1]
    print('Now aligning {} to {}...'.format(model1_name, model2_name))
    
    # -- Load model
    model2 = Word2Vec.load(model)

    # -- Temporarily create a third model and save it in the aligned folder
    model3 = smart_procrustes_align_gensim(model1, model2)

    model3.save('/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/models_aligned/{}'.format(model2_name))

print('Alignment complete!')
