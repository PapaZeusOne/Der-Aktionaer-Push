#!/usr/bin/env python
# coding: utf-8

# In[26]:


import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://www.deraktionaer.de/'


# In[27]:


def get_article_information(url,
                            tag_parent, tag_child,
                            class_link):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    article = soup.findAll(tag_parent, {'class': class_link})[0:1]
    for annoucement in article:
        description = annoucement.find(tag_child)
        return description.text

def get_article_href(url,
                     tag_parent, tag_child,
                     class_link):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    article = soup.findAll(tag_parent, {'class': class_link})[0:3]
    for reference in article:
        href = reference.find(tag_child).attrs['href']
        return url + href


# In[28]:


description = get_article_information(url,
                        'div',
                        'h2',
                        'article-list-text-container pure-u-1-1 pure-u-sm-16-24 pure-u-md-1-1 pure-u-lg-12-24')
print(description)

timestamp = get_article_information(url,
                        'div',
                        'small',
                        'article-list-text-container pure-u-1-1 pure-u-sm-16-24 pure-u-md-1-1 pure-u-lg-12-24')

print(timestamp)

reference = get_article_href(url,
                        'div',
                        'a',
                        'article-list-image-container pure-u-1-1 pure-u-sm-8-24 pure-u-md-1-1 pure-u-lg-12-24')

print(reference)


# In[29]:


pip freeze > requirements.txt


# In[ ]:




