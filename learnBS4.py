from bs4 import BeautifulSoup
import urllib.request

req=urllib.request.urlopen('https://kraftly.com/page/krafts-of-india')
xml=BeautifulSoup(req,'xml')

#print (xml.prettify())

for item in xml.findAll('link'):
    print(item)
    #print(item.get('href'))
    url='http:'+item.get('href')
    print(url)
    '''
    news=urllib.request.urlopen(url).read()
    print(news)
    print(20*"#")
    '''  
    
