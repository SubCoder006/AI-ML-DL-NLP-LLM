
import threading
import requests
from bs4 import BeautifulSoup as Bs

urls=['https://www.coursera.org/articles/what-is-machine-learning-engineer',
'https://www.cloudflare.com/learning/ai/what-is-large-language-model/',
'https://en.wikipedia.org/wiki/Mummy',
'https://chatgpt.com/c/6a0f2f95-ea70-8323-86d2-d540f5e76574']

def fetch_cnt(url):
    response = requests.get(url)
    soup = Bs(response.content,'html.parser')
    print(f'fetched {len(soup.text)} characters from {url}')

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_cnt,args=(url,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    
print("All web pages fetched.")

