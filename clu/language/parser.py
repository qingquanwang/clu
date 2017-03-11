#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import utilities

DIC_EXT = u'.txt'


def init_dic(path):
    dic = {}
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
                                utilities.ll(u'发现重复的字典项: {}'.format(line))
                                dic[line].append(dic_type)
                        else:
                            dic[line] = [dic_type]
    return dic


def parse_sentencen(args):
    utilities.is_debug = True
    dic = init_dic(args[0])
    utilities.ll(dic)
