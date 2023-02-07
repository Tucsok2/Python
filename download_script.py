import urllib.request
import sys

def dowmload_function(url):
    try:
        content=urllib.request.urlopen(url)
        page_content=content.read()
        file=open('page_content.txt','wb')
        file.write=(page_content)
        file.close()
        print('Content download successfully')
    except:
        print('Something went wrong')

url=input('please inset the url')
dowmload_function(url)