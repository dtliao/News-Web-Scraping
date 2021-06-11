#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time


# In[2]:


chrome_browser = webdriver.Chrome('./chromedriver')


# In[3]:


chrome_browser.maximize_window()


# In[4]:


chrome_browser.get(f'https://www.reuters.com/search')
user_message = chrome_browser.find_element_by_id('newsSearchField')
keyword = input('Type in the keywords you want to search: ')

user_message.send_keys(f'{keyword}')
user_button = chrome_browser.find_element_by_css_selector('.search-button')
user_button.click()


# In[5]:


num_pages = int(input('Choose the number of pages you want to crawl: '))
print('------------------------------------------------------------------------------------') 

page = chrome_browser.find_element_by_class_name('search-result-more-txt')
count = 1

while count <= num_pages:
    contents = chrome_browser.find_elements_by_class_name('search-result-indiv')
    for content in contents:
        title = content.find_element_by_class_name('search-result-title')
        title = title.find_element_by_tag_name('a')
        print(title.text)

        texts = content.find_element_by_class_name('search-result-excerpt')
        print(texts.text)

        date = content.find_element_by_class_name('search-result-timestamp')
        print(date.get_attribute('innerHTML'))
        print()
        
    print('------------------------------------------------------------------------------------') 
    page.click()
    time.sleep(1)
    count += 1


# In[6]:


chrome_browser.quit()

