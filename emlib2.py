from selenium import webdriver
from bs4 import BeautifulSoup
from emlib import gethtml

#word = input ('请输入搜索内容：')
#driver=webdriver.Edge("D:\edgedriver_win64\msedgedriver.exe")
#driver.get('https://www.dancihu.com/zaojuen/6/access.htm')
#driver.find_element('id','q').send_keys('access')
#driver.find_element('id','q').submit()
#with open ( word+'.html' ,'w', encoding ='utf-8') as f : f . write (driver.page_source)
def search(word):
    #word=input("input")
    url = "https://www.dancihu.com/search/?q={}&m=24"
    url=url.format(word)
    #print(gethtml(url))
    soup=BeautifulSoup(gethtml(url))
    temp=0
    for link in soup.find_all('a'):
        temp=temp+1
        if temp==3:
            return link.get('href')

if __name__=="__main__":
    word=input("input")
    print(search(word))
