# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import re
import shutil
#coding:utf-8

#按照文件类型放入到不同的文件夹下
def mkTypeDir(fileName):
    os.chdir(fileName)
    for each in os.listdir(os.path.curdir):
        os.chdir(each)

        for each_f in os.listdir(os.path.curdir):
            #print each_f
            txtFile = os.mkdir(os.path.curdir+os.sep+'words')
            pngFile = os.mkdir(os.path.curdir+os.sep+'pictures')
            
            (name,extend) = os.path.splitext(each_f)
            if extend == '.txt':
                
                shutil.copy(each_f,os.path.curdir+os.sep+'words')
                
            if extend == '.png':
                
                shutil.copy(each_f,os.path.curdir+os.sep+'pictures')
                
        os.chdir(os.pardir)
            
            
        
    
def isFileName(fileName):
    s = ['/','\\',':','*','<','>','|','\n','&']
    flag = True
    for bf in s:
        if bf in fileName:
            flag = False
    
    return flag

     
def save_Img(img_Name,url):
    
    
    req = requests.get(url)
    img = req.content
    with open('%s.png'%img_Name,'wb')as f:
        f.write(img)
                             
def get_INFO(filepath):
    os.chdir(filepath)
    listFile = os.listdir(os.path.curdir)

    for i in range(len(listFile)):
        fileName = listFile[i]
        os.chdir(fileName)
        listCrop = os.listdir(os.path.curdir)

        for j in range(1):
            html = open(listCrop[j]).read()
            soup = BeautifulSoup(html,'html.parser')
            
            imgTag = soup.find_all('div',class_='row images-collection')
            for img in imgTag:
                
                aTag = img.find_all('a')
                for hr in aTag:
                    ref = hr.get('href')
                    title = hr.get('title')
                    with open('hrefs.txt','a+')as f:
                        f.write(ref)
                    if isFileName(title):
                        save_Img(title,ref)      
            descTag = soup.select('.info-description')
            description = descTag[0].text
            with open('description.txt','wb')as f:
                f.write(description.encode('utf-8'))
            uses = descTag[1].text
            with open('uses.txt','wb')as f:
                f.write(uses.encode('utf-8'))
            pragation = descTag[2].text
            with open('pragation.txt','wb')as f:
                f.write(pragation.encode('utf-8'))
            reference = descTag[3].text
            with open('reference.txt','wb')as f:
                f.write(reference.encode('utf-8'))
            diseaseTitle = soup.select('.disease-title')
            
            for tag in diseaseTitle:
                disease = tag.stripped_strings
                sibling = tag.next_sibling
                siblings = sibling.next_siblings
                for dise in disease:
                    #print dise
                    fileName = "%s.txt"%(dise)
                    s = ['/','\\',':','*','<','>','|']
                    flag = True
                    for bf in s:
                        #print bf
                        if bf in fileName:
                            flag = False
                            
                    if flag:
                        for sibl in siblings:
                            tx = sibl.string
                            if tx!=None:
                                with open(fileName,'a+')as f:
                                    f.write(tx.encode('utf-8'))
                                    f.close()



        os.chdir(os.pardir)
                
         
                

 
           
 

                    
                


            
        


            

                      
                     

        

    

    
    
    
    
    