# -*- coding: utf-8 -*-
#!/usr/bin/python
import os, sys
import json
import argparse
from clu.dataset import BaiduBaikePlant

FLAGS = None
sys.path.append('./clu')
def main():
    # 1. baidu/baike/plants data cleanup & normalization
    rootDir = os.path.join(FLAGS.data_dir, 'json/baidu/baike-diseases')
    if os.path.exists(rootDir):
        norm = BaiduBaikePlant(rootDir, 'models/nltk_data')
        norm.cleanup()
        norm.normalize()
        norm.save(FLAGS.output_dir)
    else:
        raise IOError(rootDir + " not existed!")
    # 2. baidu/baike/diseases data cleanup & normalization
    # 3. baidu/zhidao/diseases data cleanup & normalization

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--data_dir',
        type=str,
        default='./data',
        help='Path to the root folder of all data'
    )
    parser.add_argument(
        '--output_dir',
        type=str,
        default='./content_norm',
        help='output root dir of content normalization'
    )
    FLAGS, unparsed = parser.parse_known_args()
    main()
