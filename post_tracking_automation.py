#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')
get_ipython().system('pip install webdriver_manager')
get_ipython().system('pip install pandas')
get_ipython().system('pip install openpyxl')


# In[1]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


# In[2]:


data = pd.read_excel('barcode.xlsx')
data


# In[3]:


#%%timeit
result_list = []

driver = webdriver.Chrome()

driver.get("https://tracking.post.ir/")
for code in data.barcode :
    input_field = driver.find_element(By.ID, 'txtbSearch')
    input_field.clear()
    input_field.send_keys(code)
    input_button = driver.find_element(By.ID, 'btnSearch')
    input_button.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)
    try:
        alert_div = driver.find_element(By.CSS_SELECTOR, 'div.alert.alert-danger')
        result_list.append(alert_div.text)
    except:
        result_div = driver.find_element(By.CSS_SELECTOR, 'div.newtddata.col-lg-5.col-md-5.col-xs-12.col-sm-5')
        result_list.append(result_div.text)

driver.quit()

data['result'] = result_list


# In[4]:


data


# In[5]:


data.to_excel('output.xlsx')


# In[6]:


result_list = []

# Setup Chrome options for better performance (e.g., headless mode)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open the target webpage
driver.get("https://tracking.post.ir/")

# Loop through each barcode
for code in data.barcode:
    input_field = driver.find_element(By.ID, 'txtbSearch')
    input_field.clear()
    input_field.send_keys(code)

    input_button = driver.find_element(By.ID, 'btnSearch')
    input_button.send_keys(Keys.RETURN)

    # Wait until the alert or result div is found
    driver.implicitly_wait(5)
    
    try:
        # If there's an alert, append its text to the result list
        alert_div = driver.find_element(By.CSS_SELECTOR, 'div.alert.alert-danger')
        result_list.append(alert_div.text)
    except:
        # Otherwise, append the result text
        result_div = driver.find_element(By.CSS_SELECTOR, 'div.newtddata.col-lg-5.col-md-5.col-xs-12.col-sm-5')
        result_list.append(result_div.text)

# Close the browser
driver.quit()

# Add the results to the DataFrame
data['result'] = result_list


# In[7]:


data


# In[ ]:




