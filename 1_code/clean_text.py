import pickle
import re
import jieba

rawtext_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/renmin_raw_data'
cleanedtext_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/cleanedtext'

def split_into_sentences(text):
    # Regular expression for Chinese sentence splitting
    sentence_endings = re.compile(r'[\u3002\uff1f\uff01]+')
    list_of_sentences = []
    passages_split_by_line = text.split('\n')
    for passage in passages_split_by_line:
        sentences = sentence_endings.split(passage)
        list_of_sentences.extend(sentences)
    # Filter out empty sentences and strip whitespace
    cleaned_sentences = [sentence.strip() for sentence in list_of_sentences if sentence.strip()]
    return cleaned_sentences

def tokenCleaner(token):
    '''Clear token, return empty str "" if the token is bad for Chinese text.'''
    # # Keep only Chinese characters
    new_token = re.sub(r'[^\u4e00-\u9fff]+', '', token)

    # Keep only Chinese characters, English letters and numbers
    # new_token = re.sub(r'[^\u4e00-\u9fff0-9a-zA-Z]+', '', token)
    if new_token:
        return new_token
    else:
        return ""

def sen2token(sentence):
    '''Segment and clean Chinese sentence, return a list of tokens.'''
    clear_tokens = []
    word_punct_token = jieba.cut(sentence)
    for token in word_punct_token:
        token = tokenCleaner(token)
        if token:
            clear_tokens.append(token)
    return clear_tokens

def list_sen2token(text, year):
    sentences = split_into_sentences(text)
    alltokens = [sen2token(sentence) for sentence in sentences]
    # save cleaned sentences to pickle file
    with open(cleanedtext_path+'/cleaned_'+year+'.pkl', 'wb') as f:
        pickle.dump(alltokens, f)
    return alltokens

try:
    year = str(int(input("Please enter the year for which you want to preprocess the data: ")))
    # Load txt data
    with open(rawtext_path+'/renmin'+year+'.txt', 'r', encoding='utf-8', errors='replace') as f:
        data = f.readlines()
    # Join the data into a single string
    text = ''.join(data)    
    # Process the text
    list_sen2token(text, year)

except ValueError:
    print("Invalid input. Please enter a valid year.")
