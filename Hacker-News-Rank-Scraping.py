#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pprint


# In[2]:


def main():
    num_pages = int(input('Choose the number of pages you want to crawl: '))
    for i in range(1,num_pages+1):
        res = requests.get(f'https://news.ycombinator.com/news?p={i}')
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.storylink')
        subtext = soup.select('.subtext')
        pprint.pprint((create_custom_hn(links, subtext)))

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'],reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().strip(' points'))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

main()


# In[ ]:




