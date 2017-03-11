import json
import urllib2
from bs4 import BeautifulSoup

def getQuestions(url):
    req = urllib2.urlopen(url)
    html = req.read()
    #print "html",html
    questionsList = []
    soup = BeautifulSoup(html,'html.parser')
    questionTags = soup.find_all('div',class_='question row')
   # print questionTags
    for queTag in questionTags:
        
        question ={}
        ImgTag = queTag.find('div',class_='question-image image-square lazy-loaded')
        #print ImgTag
        if ImgTag!=None:
            ImgUrl = ImgTag.get('style')
            question['url']=ImgUrl
        QTags = queTag.find('h2',class_='question-title')
        Txt = queTag.find('p')
        
        if QTags!=None:
            title = QTags.string
            question[title]=Txt.string
            questionsList.append(question)
            
            
    for dictQ in questionsList:
        json.dump(dictQ,open('E:/Test/DataMining/grape.txt','a+'))
        #print l
 
        
    
 

            
            

                
              
        