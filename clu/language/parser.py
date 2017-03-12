#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import utilities

DIC_EXT = u'.txt'


def init_dic(path):
    dic = {}
    duplicated = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(DIC_EXT):
                file_path = os.path.join(root, name)
                dic_type = file_path.replace(path, '', 1)
                dic_type = dic_type.replace(DIC_EXT, '')
                dic_type = dic_type.replace('/', '_')
                with open(file_path, 'r') as file:
                    for line in file:
                        line = line.decode('utf-8').strip()
                        if not line:
                            continue
                        if line in dic:
                            if dic_type not in dic[line]:
                                duplicated.append(line)
                                dic[line].append(dic_type)
                        else:
                            dic[line] = [dic_type]
    for key in duplicated:
        # utilities.ll(u'发现重复的字典项: {}'.format(key))
        # utilities.ll(dic[key])
        pass
    return dic


def get_list(keyword_list):
    # utilities.ll(keyword_list)
    temp = u''
    for keyword in keyword_list:
        temp += keyword
    return temp


def find_longest_keyword(text, keywords, result, dic):
    if not text:
        return result
    utilities.ll(text)
    for i in range(len(text)):
        candidate = text[:(-1) * i]
        if len(text) == 1:
            candidate = text[0]
        if candidate in keywords:
            # print(candidate)
            result += u'[' + candidate + u':' + get_list(dic[candidate]) + u']'
            # utilities.ll(result)
            if i < len(text) and i != 0:
                return find_longest_keyword(text[(-1) * i:], keywords, result, dic)
            else:
                return result
    result += text[0]
    # utilities.ll(result)
    return find_longest_keyword(text[1:], keywords, result, dic)


def parse_sentencen(args):
    utilities.is_debug = True
    dic = init_dic(args[0])
    # utilities.ll(dic)
    text = args[1]
    # ngram查找所有匹配的关键词
    keywords = []
    for i in range(1, 5):
        keywords.extend(getNgramsKeyord(text, i, dic))
    utilities.ll(keywords)
    # 用长度优先原则找到关键词组合
    result = u''
    result = find_longest_keyword(text, keywords, result, dic)
    utilities.ll(result)


def getNgramsKeyord(input, n, dic):
    output = []
    for i in range(len(input) - n + 1):
        ngramTemp = input[i:i + n]
        # utilities.ll(ngramTemp)
        if ngramTemp in dic and ngramTemp not in output:
            output.append(ngramTemp)
    # utilities.ll(output)
    return output
