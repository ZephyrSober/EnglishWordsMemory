from emlib import gethtml
from emlib2 import search
from bs4 import BeautifulSoup
from time import sleep
import numpy

lenth=50#lenth of the word list   !!!!!!!!no change

def get(word):
    sear=search(word)
    if sear=='//www.dancihu.com/':
        print('error:no found word:'+word)
        sleep(1)
        return gethtml(search('no'))
    return gethtml(search(word))

def out(word):
    parts=[''for i in range(5)]
    soup=BeautifulSoup(get(word))
    txt=soup.get_text()
    for i in range(1,6):
        temp=txt.find(str(i))+2
        sen=''
        while(txt[temp]!=str(i+1)):
            sen=sen+txt[temp]
            temp=temp+1
        with open(word+'.txt','a',encoding='utf-8') as f:
            f.write(sen+'\n')
            parts[i-1]=sen
    return parts
            

if __name__=='__main__':
    word=[''for i in range(lenth)]
    with open('in.txt','r',encoding='utf-8') as f:
        temp=0
        for i in f.read():
            if i==' ':
                temp+=1
            else:
                word[temp]+=i
    #print(word)
    #word=input("input the word that you want its sentence")
    #out(word)
    sentence=[[''for i in range(5)]for j in range(lenth)]
    for i in range(lenth):
        sentence[i]=out(word[i])
        print(str(i*2)+"%")
    #print(sentence)
    print("waiting for output")
    
    for t in range(1,6):
        with open('day'+str(t)+'.txt','w',encoding='utf-8') as f:
            for i in range(lenth):
                f.write(word[i]+' ')
            f.write('\n')
            for j in range(lenth):
                f.write(sentence[j][t-1]+'\n')