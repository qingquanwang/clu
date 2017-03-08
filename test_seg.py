#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import json

from nltk.tokenize.stanford_segmenter import StanfordSegmenter

def main():
    model_dir = "/home/qingquan/nltk_data/tokenizers/stanford-segmenter-2016-10-31"

    segmenter = StanfordSegmenter(
        path_to_jar = model_dir + "/" + "stanford-segmenter-3.7.0.jar",
        path_to_slf4j = model_dir + "/" + "stanford-segmenter-3.7.0.jar",
        path_to_sihan_corpora_dict = model_dir + "/" + "data",
        path_to_model = model_dir + "/" + "data/pku.gz",
        path_to_dict = model_dir + "/" + "data/dict-chris6.ser.gz")

    #for line in sys.stdin.readlines():
    #    sentence = line.decode("utf-8").strip()
    #    print segmenter.segment(sentence)
    #sentence = u'苹果黑斑病的防治方法'
    #print segmenter.segment(sentence)
    print segmenter.segment_file('./symptom_text').encode('utf-8')
if __name__ == '__main__':
    main()
