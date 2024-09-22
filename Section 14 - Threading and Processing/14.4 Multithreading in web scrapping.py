'''
Real - World Example : Multithreading for I/O bound tasks
scenario : Web scrapping

Web scrapping often involves making numerous network requests to fetch web pages. these tasks are I/O bound because they spend a lot of time waiting for responses from servers.

Multithreading can significantly improve the perforamance by allowing multiple web pages to be fetched concurrently



https://python.langchain.com/v0.2/docs/introduction/
https://python.langchain.com/v0.2/docs/concepts/
https://python.langchain.com/v0.2/docs/tutorials/
'''
import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://python.langchain.com/v0.2/docs/introduction/',  'https://python.langchain.com/v0.2/docs/concepts/',
    'https://python.langchain.com/v0.2/docs/tutorials/' ]


def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched : {len(soup.text)} character from {url}')

threads = []

for url in urls:
    thread = threading.Thread(target = fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('All webpages extracted')

'''
Concurrency:

By using threading, the script can fetch multiple URLs simultaneously, making it more efficient than fetching them one at a time. This is especially useful when dealing with multiple pages, as it can significantly reduce the total time taken to collect data.


'''