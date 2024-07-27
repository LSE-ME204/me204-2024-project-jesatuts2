from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy import Selector
import os
import json
import requests

import pandas as pd
import numpy as np

from tqdm.notebook import tqdm
from pprint import pprint as print

# *******************************************************************************************************************************
# Setting program-level variables
driver = webdriver.Chrome()
teams_url_slug = "https://www.roadtonationals.com/api/women/finalresults/"
years = [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015] # These are the years that we are interested in evaluating

print('honk')

# *******************************************************************************************************************************

team_urls = []
for year in years:
    year_url = teams_url_slug + str(year)

    payload = {}
    headers = {
        'Cookie': 'PHPSESSID=c48eb24102c0c45390a5d64809741f95'
    }

    response = requests.request("GET", year_url, headers=headers, data=payload)

    print(response.text)

    with open(f'../Data/Raw/teams/{year}_teams.json', 'w') as f:
        # pure text
        f.write(response.text)

team_data = {}
for filename in os.listdir('../Data/Raw/teams'):
    with open(f'../Data/Raw/teams/{filename}', 'r') as f:
        json_data = json.load(f)
    
    season = filename.split('_')[0]
    team_data = json_data['data']
    
    print(team_data)
        

# ******************************************************************************************************************************

meet_url = "https://www.roadtonationals.com/api/women/meetresults/17947"
meet_id = meet_url.split('/')[-1]

payload = {}
headers = {
  'Cookie': 'PHPSESSID=c48eb24102c0c45390a5d64809741f95'
}

response = requests.request("GET", meet_url, headers=headers, data=payload)

print(response.text)

with open('../Data/Raw/meet_scores/meets.json', 'w') as f:
    # pure text
    f.write(response.text)

# meet_data = {}
# for filename in os.listdir('../Data/Raw/meet_scores'):
#     with open(f'data/{filename}', 'r') as f:
#         json_data = json.load(f)


        