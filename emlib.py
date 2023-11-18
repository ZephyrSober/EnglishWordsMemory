import ssl
import urllib
import urllib.request
def gethtml(url):
    headers={
        "Host": "www.dancihu.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.dancihu.com/zaojuen/",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"}
    #e.g. url = "https://www.dancihu.com/zaojuen/6/access.htm"
    ctx = ssl._create_unverified_context()
    req = urllib.request.Request(url = url,headers=headers)
    
    return urllib.request.urlopen(req,context=ctx).read()
if __name__=='__main__':
    word = input("input:")
    print(gethtml(word))
