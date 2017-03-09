# -*- coding: utf-8 -*-
import numpy as np

import json
from pandas import Series,DataFrame
import nltk
from nltk.corpus import stopwords

def split_Word(text):
    
    #disease_List = re.split(r'\W+',text)
    disease_List = nltk.word_tokenize(text)
    #去除停用词
    filtered = [w for w in disease_List if(w not in stopwords.words('english')and w not in [',',';',')','('])]
    #进行词性分析，去掉动词、助词等
    Rfiltered =nltk.pos_tag(filtered)
    removed = ['PRB','VBP',',','.','RB','VBZ','CC','RB','IN','MD']
    for w in Rfiltered:
        if w[1] in removed:
            print 'w[1]',w[1]
            if Rfiltered.index(w)<len(filtered):
                print 'test'
                del filtered[Rfiltered.index(w)]
            #del(filtered[Rfiltered.index(w)])
    return filtered
def split_Sentence(text):
    
    list_ret = list()
    if isinstance(text,(str,unicode)):
        for s_str in text.split(';'):
            if '?' in s_str:
                list_ret.extend(s_str.split('?'))
            elif '!' in s_str:
                list_ret.extend(s_str.split('!'))
            else:
                list_ret.append(s_str)
    return list_ret
    

def sumBigram(filePath):
    main_Text = read_Data_S(filePath)
    #print type(main_Text)
    bigramDict={}
    for line in main_Text:
        #print type(line)
        #print line
        list_ret = split_Sentence(line)
        print list_ret
        for sent in list_ret:
            #print sent
            filtered = split_Word(sent)
            for i in range(len(filtered)):
                if i <= len(filtered)-2:
                    for j in range(i+1,i+2,1):
                        key = '%s,%s'%(filtered[i],filtered[j])
                        print key
                        bigramDict[key]=bigramDict.get(key,0)+1
                        
    for key,value in bigramDict.items():
        with open('E:/Test/plant-json/json/plantvillage/dict_bigrams.txt','a+')as f:
            
            f.write(key.encode('utf-8'))
            f.write('\t')
            f.write(str(value))
            f.write('\n')
                
    return bigramDict
            
        
        
    
def read_Data_S(filePath):
    main_Text = []
    with open(filePath,'r')as f:
        data = json.load(f)
    for (key,values) in data.items():
        diseases = data[key]['diseases']
        for dise in diseases:
            text = dise.get('symptoms',0)
            main_Text.append(text)
            
    return main_Text
        
def create_Vocab(dise_Word_List):
    vocabSet = set([])
    for doc in dise_Word_List:
        vocabSet = vocabSet|set(doc)
    #这里又重新装载为了list形式
    return list(vocabSet)
    
#将文本处理成向量的形式
def bagOfWords2VecMN(vocabList, diseaseS):
    returnVec = [0]*len(vocabList)
    for word in diseaseS:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec
    
    
    
def read_Data_Topic(filePath):
    
    with open(filePath,'r')as f:
        data = json.load(f)
        
   #将去除了停用词的所有词都放入到dise_Word_List中
    dise_Word_List = []
    for (key,values) in data.items():
        diseaseName = key
        #print diseaseName
        diseases = data[key]['diseases']
        
        for dise in diseases:
            #print type(dise)
            text = dise.get('symptoms',0)
            #print text
            if text!=0:
                dise_Word = split_Word(text)
                dise_Word_List.append(dise_Word)
            
            
            
    return data,dise_Word_List
    
def read_Data_Quest(filePath):
    with open(filePath,'r')as f:
        data = json.load(f)
        
   #将去除了停用词的所有词都放入到dise_Word_List中
    quest_Word_List = []
    for (key,values) in data.items():
        diseaseName = key
        #print diseaseName
        for quest in data[key]:
            question = quest['text']
            quest_Word = split_Word(question)
            quest_Word_List.append(quest_Word)
            
            
            
    return data,quest_Word_List
    
def read_Data_Title(filePath):
    with open(filePath,'r')as f:
        data = json.load(f)
        
   #将去除了停用词的所有词都放入到dise_Word_List中
    quest_Word_List = []
    for (key,values) in data.items():
        diseaseName = key
        #print diseaseName
        for quest in data[key]:
            question = quest['title']
            quest_Word = split_Word(question)
            quest_Word_List.append(quest_Word)
            
            
            
    return data,quest_Word_List
    
def creat_Vect_Title(filePath):
    
    data,title_Word_List = read_Data_Title(filePath)
    vocablist = create_Vocab(title_Word_List)
    symptomSerList = []
    for symptom in title_Word_List:
        
        symptom_Vect = bagOfWords2VecMN(vocablist,symptom)
        symptomSer = Series(symptom_Vect,index=vocablist)
        #设置对应的Frame结构
        symptomSerList.append(symptomSer)
        
    frame = DataFrame(symptomSerList,index=range(len(title_Word_List)))
    return frame    
def creat_Vect_Quest(filePath):
    
    data,quest_Word_List = read_Data_Quest(filePath)
    vocablist = create_Vocab(quest_Word_List)
    symptomSerList = []
    for symptom in quest_Word_List:
        
        symptom_Vect = bagOfWords2VecMN(vocablist,symptom)
        symptomSer = Series(symptom_Vect,index=vocablist)
        #设置对应的Frame结构
        symptomSerList.append(symptomSer)
        
    frame = DataFrame(symptomSerList,index=range(len(quest_Word_List)))
    return frame    
def creat_Vect_Topic(filePath):
    
    data,dise_Word_List = read_Data_Topic(filePath)
    vocablist = create_Vocab(dise_Word_List)
    symptomSerList = []
    for symptom in dise_Word_List:
        
        symptom_Vect = bagOfWords2VecMN(vocablist,symptom)
        symptomSer = Series(symptom_Vect,index=vocablist)
        #设置对应的Frame结构
        symptomSerList.append(symptomSer)
        
    frame = DataFrame(symptomSerList,index=range(len(dise_Word_List)))
    return frame
def getMainTitle(filePath,k):
    RFrame = DataFrame()
    frame = creat_Vect_Title(filePath)
    sum_Columns = frame.sum(axis=0)
    seriSorted = sum_Columns.sort_values(ascending=False)
    mainWords = []
    for j in range(k):
        print 'word:%s,num:%d'%(seriSorted.index[j],seriSorted[j])
        mainWords.append(seriSorted.index[j])
        
    return mainWords
def getMainQuest(filePath,k):
    RFrame = DataFrame()
    frame = creat_Vect_Quest(filePath)
    sum_Columns = frame.sum(axis=0)
    seriSorted = sum_Columns.sort_values(ascending=False)
    mainWords = []
    for j in range(k):
        #print 'word:%s,num:%d'%(seriSorted.index[j],seriSorted[j])
        mainWords.append(seriSorted.index[j])
        
    return mainWords
    
     
def getTopic(filePath,k):
    import sys    
    reload(sys)    
    sys.setdefaultencoding('utf8')
    RFrame = DataFrame()
    frame = creat_Vect_Topic(filePath)
    #sum_Rows = frame.sum(axis=1)
    sum_Columns = frame.sum(axis=0)
    
    print sum_Columns
    #sum_All = sum_Rows.sum()
    #for i in frame.index:
        
        #for j in frame.columns:
            
            #tfNum = frame.loc[i,j]
            #tfNum = sum_Columns(j)
            #tfValue = tfNum/sum_All
            #tfValue = tfNum/float(sum_Rows[i])
            #idfValue = tfNum/float(sum_Columns[j])
            #RFrame.loc[i,j]=float(tfValue*idfValue)
    
    #我们得到了最终盛放tf-idf的文档，然后应该是按照axis=1进行排序
    #DataFrame结构应该是不能整体进行排序
    
    #统计词频
    #for j in frame.columns:
        #tfNum = sum_Columns(j)
    seriSorted = sum_Columns.sort_values(ascending=False)
    #seriSorted = np.argsort(-sum_Columns)
    #print 'seriSorted',seriSorted
    #print 'sortedColumns',
    mainWords = []
    dictWords={}
    for j in range(k):
        dictWords[seriSorted.index[j]]=seriSorted[j]
        with open('E:/Test/plant-json/json/plantvillage/dict_words.txt','a+')as f:
            f.write((seriSorted.index[j]).encode('utf-8'))
            f.write('\t')
            f.write(str(seriSorted[j]))
            f.write('\n')    
        mainWords.append(seriSorted.index[j])
        
    #jsFile = json.dumps(dictWords)             
    
    return mainWords
        
def coverageWords(filePath1,filePath2,k1,k2,k3):
    mainWords1 = getTopic(filePath1,k1)
    mainWords2 = getMainQuest(filePath2,k2)
    mainWords3 = getMainTitle(filePath2,k3)
    #求这三个列表的交集、并集，差集
    set1 = set(mainWords1)
    set2 = set(mainWords2)
    set3 = set(mainWords3)
    unionSets = set1|set2|set3
    intersectionSets = set1&set2&set3
    differenceSets1 = set1-set2
    differenceSets2 = set1-set3
    differenceSets3 = set2-set3
    return unionSets,intersectionSets,differenceSets1,differenceSets2,differenceSets3
            
    
                
                
            
        
            
    
    
    

    
    
        
        
    
            
        
        
    
    
    
    
    