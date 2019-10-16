#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:15:11 2019

@author: eduardo
"""

import itertools
import nltk
from nltk.tokenize import PunktSentenceTokenizer
from gensim.models.phrases import Phraser, Phrases
#from normalization import stopword_list
from gensim import corpora, models
from nltk.corpus import state_union
import sys

# Get corpus
text = state_union.raw("2005-GWBush.txt")

# Split corpus into sentences
custom_sent_tokenizer = PunktSentenceTokenizer(text)
sentences = custom_sent_tokenizer.tokenize(text)
print len(sentences)
print sentences[0]
print sentences[10]

sentences = [nltk.word_tokenize(sent) for sent in sentences]
print len(sentences)
print sentences[0]
print sentences[10]
              
stopword_list = nltk.corpus.stopwords.words('english')
commmon_terms = stopword_list
#phrases = Phrases(sentences, common_terms=commmon_terms, min_count=1, threshold=1)
phrases = Phrases(sentences, min_count=2)

bigram = Phraser(phrases)

print bigram[sentences[99]]
all_sentences = list(bigram[sentences])

for i,sent in enumerate(all_sentences):
    print i, "===", sent
    
tagged = nltk.pos_tag(all_sentences[99])
print tagged

tagged = nltk.pos_tag(all_sentences[150])
print tagged

################
trigram_phrases = Phrases(bigram[sentences],common_terms=commmon_terms, min_count=2, threshold=2)
trigram = Phraser(trigram_phrases)

all_sentences_trigram = list(trigram[bigram[sentences]])
for i,sent in enumerate(all_sentences_trigram):
    print i, "===", sent
    