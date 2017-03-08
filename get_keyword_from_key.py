#!/usr/bin/python
import os, sys
from nltk.tokenize.stanford_segmenter import StanfordSegmenter
import pprint

model_dir = './dependency/stanford-segmenter-2016-10-31'

pp = pprint.PrettyPrinter(indent=2)

segmenter = StanfordSegmenter(
    path_to_jar = model_dir + "/" + "stanford-segmenter-3.7.0.jar",
    path_to_slf4j = model_dir + "/" + "stanford-segmenter-3.7.0.jar",
    path_to_sihan_corpora_dict = model_dir + "/" + "data",
    path_to_model = model_dir + "/" + "data/pku.gz",
    path_to_dict = model_dir + "/" + "data/dict-chris6.ser.gz")

if __name__ == '__main__':
    sents = []
    freqs = []
    for line in sys.stdin.readlines():
        fs = line.strip().split(' ')
        freq = int(fs[0])
        key = fs[1].decode('utf-8')
        sents.append(key)
        freqs.append(freq)
    #print '\n'.join(sents)
    res = segmenter.segment('\n'.join(sents)).split('\n')
    #pp.pprint(res)
    tok_freq = {}
    for i in range(len(freqs)):
        toks = res[i].split(' ')
        for t in toks:
            if t in tok_freq:
                tok_freq[t] = tok_freq[t] + freqs[i]
            else:
                tok_freq[t] = freqs[i]
    for t in tok_freq:
        print t.encode('utf-8') + '\t' + str(tok_freq[t])
