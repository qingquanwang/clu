#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import clu.language.parser


functions = {'simulator': clu.language.parser.parse_sentence,
             'sequences': clu.language.parser.list_sequences,
             }

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='clu: content and language understanding', usage='''
        测试模拟器: python main.py simulator --parameters dict/ '西红柿得灰霉病怎么治'
        列出所有关键词组合: python main.py sequences --parameters dict/ '西红柿得灰霉病怎么治'
        ''', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('type', help='指定指令')
    parser.add_argument('--parameters', help='指定各个参数', nargs='*')
    args = parser.parse_args()
    if args.type not in functions:
        print('请输入有效的关键词类型，参见-h')

    func = functions[args.type]
    parameters = [p.decode('utf-8') for p in args.parameters]
    func(parameters)
