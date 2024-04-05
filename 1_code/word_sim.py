# -*- coding: UTF-8 -*-
'''
Test the embeddings on word similarity task
Select 240.txt 297.txt 
'''
import numpy as np
import pdb
import sys,getopt
from gensim.models import Word2Vec
from scipy.stats import spearmanr
from sklearn.metrics.pairwise import cosine_similarity
import csv

def build_dictionary(word_list):
    dictionary = dict()
    cnt = 0
    for w in word_list:
        dictionary[w] = cnt
        cnt += 1
    return dictionary

def read_wordpair(sim_file):
    f1 = open(sim_file, 'r')
    pairs = []
    for line in f1:
        pair = line.split()
        pair[2] = float(pair[2])
        pairs.append(pair)
    f1.close()
    return pairs

def read_word2vec_model(model_file):
    model = Word2Vec.load(model_file)
    word_size = len(model.wv)
    embed_dim = model.vector_size
    dict_word = {word: i for i, word in enumerate(model.wv.index_to_key)}
    embeddings = model.wv.vectors
    return word_size, embed_dim, dict_word, embeddings

if __name__ == '__main__':
    years = range(1979, 2024)
    fname1 = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/0_data/evaluation/297.txt'
    results = []

    for year in years:
        vec_file = f'/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/models/pd_{year}.model'
        pairs = read_wordpair(fname1)
        word_size, embed_dim, dict_word, embeddings = read_word2vec_model(vec_file)
        human_sim = []
        vec_sim = []
        cnt = 0
        total = len(pairs)

        for pair in pairs:
            w1 = pair[0]
            w2 = pair[1]
            if w1 in dict_word and w2 in dict_word:
                cnt += 1
                id1 = dict_word[w1]
                id2 = dict_word[w2]
                vec1 = embeddings[id1].reshape(1, -1)
                vec2 = embeddings[id2].reshape(1, -1)
                vsim = cosine_similarity(vec1, vec2)[0][0]
                human_sim.append(pair[2])
                vec_sim.append(vsim)

        score, p_value = spearmanr(human_sim, vec_sim)
        result = [year, cnt, score, p_value]
        results.append(result)
        print(f'Results of year {year} added.')

    # Save results to CSV file
    csv_file = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/3_output/evaluation_sim_297.csv'
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Year', 'cnt_set240', 'Spearman Correlation', 'p-value'])
        writer.writerows(results)

    print(f"Results saved to {csv_file} successfully.")