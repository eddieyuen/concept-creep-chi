# -*- coding: UTF-8 -*-
'''
Test the embeddings on word analogy task
Dataset: 
'''
from gensim.models import Word2Vec
import numpy as np
import csv

def read_word_analogy(ana_file):
        f1 = open(ana_file, 'r')
        capital = []
        state = []
        family = []
        cnt = 0
        for line in f1:
                pair = line.split()
                if pair[0] == ':':
                        cnt = cnt + 1
                        continue
                if cnt == 1:
                        capital.append(pair)
                elif cnt == 2:
                        state.append(pair)
                else:
                        family.append(pair)
        f1.close()
        return capital,state,family

def predict_word(w1, w2, w3, w4, embeddings, dict_word):
        #return the index of predicted word
        id1 = dict_word[w1]
        id2 = dict_word[w2]
        id3 = dict_word[w3]
        reverse_dict = dict(zip(dict_word.values(), dict_word.keys()))
        pattern = embeddings[id2] - embeddings[id1] + embeddings[id3]
        pattern = pattern / np.linalg.norm(pattern)
        sim = embeddings.dot(pattern.T)
        sim[id1] = sim[id2] = sim[id3] = -1   #remove the input words
        predict_index = np.argmax(sim)
        id4 = dict_word[w4]
        if predict_index == id4:
                return 1
        else:
                return 0
        
def analogy(pairs, embeddings,dict_word):
        total = len(pairs)
        reverse_dict = dict(zip(dict_word.values(), dict_word.keys()))
        in_dict_cnt = 0
        predict_cnt = 0
        #print('dictionary_length ', len(dict_word))
        for pair in pairs:
                in_dict = True
                for i in range(len(pair)):
                        #pair[i] = pair[i].decode('utf-8')
                        in_dict = in_dict and (pair[i] in dict_word)
                if(in_dict):
                        in_dict_cnt = in_dict_cnt + 1
                        predict_cnt = predict_cnt + predict_word(pair[0], pair[1], pair[2],pair[3], embeddings, dict_word)
        return total,in_dict_cnt,predict_cnt

if  __name__ == '__main__':
        years = range(1979, 2024)
        results = []

        for year in years:
            ana_file = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/0_data/evaluation/analogy.txt'
            embed_file = f'/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/models_aligned/pd_{year}.model'

            capital,state,family = read_word_analogy(ana_file)
            #print(len(capital), len(state), len(family))

            model = Word2Vec.load(embed_file)
            embeddings = model.wv.vectors
            dict_word = {word: index for index, word in enumerate(model.wv.index_to_key)}

            capital_total, capital_dict, capital_correct = analogy(capital, embeddings, dict_word)
            state_total, state_dict, state_correct = analogy(state, embeddings, dict_word)
            family_total, family_dict, family_correct = analogy(family, embeddings, dict_word)
            total = capital_total + state_total + family_total
            indict = capital_dict + state_dict + family_dict
            correct = capital_correct + state_correct + family_correct
            result = [year, capital_total, capital_dict, capital_correct/capital_dict, 
                      state_total, state_dict, state_correct/state_dict,
                      family_total, family_dict, family_correct/family_dict, 
                      total, indict, correct/indict]
            results.append(result)
            print(f'Results of year {year} appended.')

        # Save results to CSV file
        csv_file = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/3_output/evaluation/aligned_analogy.csv'
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Year', 'Capital_total', 'Capital_in dict', 'Capital_correct',
                             'State_total', 'State_indict', 'State_correct',
                             'Family_total', 'Family_indict', 'Family_correct',
                             'Total', 'Indict', 'Correct'])
            writer.writerows(results)

        print(f"Results saved to {csv_file} successfully.")
        