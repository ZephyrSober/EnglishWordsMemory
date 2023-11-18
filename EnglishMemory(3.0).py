# The core code was rewriten by Hu Jinghao. July 2, 2023.

from bs4 import BeautifulSoup
import urllib.request
import sys, os


def get(_word_: str):
    soup = BeautifulSoup(urllib.request.urlopen("http://dict.cn/search?q={}".format(_word_)).read(), features="html.parser")
    part: bs4.element.Tag
    for part in soup.find_all('div'):
        if part.get('class') == ['layout', 'sort']:
            part = part.find_next('ol')
            break
    return part.find_all('li')


def out(_word_: str):

    parts: List[str] = []
    txt = get(_word_)

    for child in txt:
        parts.append(str(child).replace('<li>', '').replace('<br/>', '\n').replace('</li>', ''))
        # Processing string.
    return parts


if __name__ == '__main__':
    # Changed by Hu Jinghao on July 2, 2023.
    WordList = []
    sep = [' ', '\n']
    InputFile = open('in.txt', 'r', encoding='utf-8')
    string = ''

    for char in InputFile.read():
        if char in sep:
            WordList.append(string)
            string = ''    
        else:
            string += char
            
    InputFile.close()

    WordList = list(set(WordList)) # Deduplicate 去重
    length = len(WordList) + 1  # Index begins from 0.
    # This code makes it possible for flexible input file. You can put as many words as you like.

    # Changed by Hu Jinghao on July 2, 2023.
    print('Finding example sentences online...')
    SentenceGroup: str
    process = 1
    OutFile = open('Words.txt', 'w', encoding='utf-8')
    
    for word in WordList:
        
        SentenceGroup = out(word)
        if SentenceGroup == []:
            process += 1
            continue
        
        OutFile.write(word + '\n')
        for sentence in SentenceGroup:
            OutFile.write(sentence + '\n')
        OutFile.write('\n')
        
        process += 1
        sys.stdout.write("{:.2%} | ".format(process/length) + '█' * round(process / length * 100) +  '\r')
        sys.stdout.flush()
        
    OutFile.close()
    print()

    print("Done!")
    os.system("pause")
