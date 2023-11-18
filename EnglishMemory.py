from emlib import gethtml
from emlib2 import search
from bs4 import BeautifulSoup
import numpy

lenth=50#lenth of the word list   !!!!!!!!no change

def get(word):
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
    
    ###day1###
    with open('day1.txt','w',encoding='utf-8') as f:
        for i in range(lenth):
            f.write(word[i]+' ')
        f.write('\n')
        for j in range(lenth):
            f.write(sentence[j][0]+'\n')
    ###day2###
    with open('day2.txt','w',encoding='utf-8') as f:
        for i in range(lenth):
            f.write(word[i]+' ')
        f.write('\n')
        for j in range(lenth):
            f.write(sentence[lenth-j-1][1]+'\n')
    ###day3###
    with open('day3.txt','w',encoding='utf-8') as f:
        for i in range(lenth):
            f.write(word[i]+' ')
        f.write('\n')
        for j in range(int(lenth/2)):
            f.write(sentence[j*2][2]+'\n')
        for j in range(int(lenth/2)):
            f.write(sentence[j*2+1][2]+'\n')
    ###day4###
    with open('day4.txt','w',encoding='utf-8') as f:
        for i in range(lenth):
            f.write(word[i]+' ')
        f.write('\n')
        for i in range(5):
            for j in range(4,50,5):
                f.write(sentence[lenth+3-j-i][3]+'\n')
    ###day5###
    with open('day5.txt','w',encoding='utf-8') as f:
        for i in range(lenth):
            f.write(word[i]+' ')
        f.write('\n')
        for i in range(10):
            for j in range(0,41,10):
                f.write(sentence[j+i][4]+'\n')
