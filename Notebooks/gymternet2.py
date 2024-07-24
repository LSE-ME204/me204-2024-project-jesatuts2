# *******************************************************************************************************************************
# Importing the necessary programs
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
url = "https://roadtonationals.com/results/standings/"
years = [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015] # These are the years that we are interested in evaluating

print('honk')

# ******************************************************************************************************************************
# PART 1: Go to the url, wait until everything on the page loads


def get_url_and_wait_for_elements_to_load(url, css_selector):
    try:
        driver.get(url)
        print("*****************************")
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)) # (Source: https://selenium-python.readthedocs.io/waits.html )
        )
        print(element)
    except:
        print("oh no it didn't work")
        pass # ?? Trying to make it so that the program doesn't crash if the element isn't found
    
css_selector = 'div.rt-table > div.rt-tbody'
get_url_and_wait_for_elements_to_load(url, 'div.rt-table > div.rt-tbody')
response = Selector(text=driver.page_source)

print(response)

# ******************************************************************************************************************************
# PART 2: Set up the dataframes we exported in the last session as variables

teams_df = pd.read_csv('../Data/Raw/teams.csv')
meets_df = pd.read_csv('../Data/Raw/meets.csv')

print(teams_df)
print(meets_df)

# ******************************************************************************************************************************
# 5 Go to each of the meet's links and scrape the score information

# dfs we are adding to: meets_df, team_scores_df (meet_id, team_id), gymnast_scores_df (team_id, meet_id)

meet_link = meets_df['link'][1]
meet_ids = []
team_ids = []
team_meet_ids = []
team_vt_scores = []
team_ub_scores = []
team_bb_scores = []
team_fx_scores = []
team_meet_scores = []
gymnast_ids = []
gymnast_names = []
gymnast_team_ids = []
gymnast_meet_ids = []
gymnast_vt_scores = []
gymnast_ub_scores = []
gymnast_bb_scores = []
gymnast_fx_scores = []
gymnast_aa_scores = []
meet_hosts = []

def get_team_score_info(url):

    #Load the page and set the selectors
    get_url_and_wait_for_elements_to_load(url, css_selector)
    response = Selector(text=driver.page_source)  
    meet_results_table_rows = response.css('div.rt-tr-group')

    # Determind the meet id
    meet_id = url.split('/')[-1]
    meet_ids.append(meet_id)
    
    # Find out if there is a host for the meet, and if so add to the meet_hosts list
    meet_host = ''
    
    if response.css('p:nth-child(4)').get():
        meet_host = response.css('p:nth-child(4)::text').get()
    else:
        meet_host = 'NaN'

    meet_hosts.append(meet_host)
    
    # Find out how many teams are competing in the meet
    team_count = len(meet_results_table_rows)

    # Add the meet id to the list of team_meet_ids list for each team
    for team_meet_id in range(0, team_count):
        team_meet_id = meet_id
        team_meet_ids.append(team_meet_id)
    
    # Get the hrefs for each team
    team_hrefs = meet_results_table_rows.css('div > div > a::attr(href)').getall()
    # Splitting out the team_id and adding them to the team_ids list
    for team_href in team_hrefs:
        team_id = team_href.split('/')[-1]
        team_ids.append(team_id)

    # Get the scores for each event and the total meet score (this generates a list of lists)
    current_meet_team_vt_scores = meet_results_table_rows.css('div:nth-child(4)::text').getall()
    current_meet_team_ub_scores = meet_results_table_rows.css('div:nth-child(5)::text').getall()
    current_meet_team_bb_scores = meet_results_table_rows.css('div:nth-child(6)::text').getall()
    current_meet_team_fx_scores = meet_results_table_rows.css('div:nth-child(7)::text').getall()
    current_meet_team_meet_scores = meet_results_table_rows.css('div:nth-child(8) > strong::text').getall()

    # Iterating over the lists generated above and adding them to the appropriate (variable) list
    for score in current_meet_team_vt_scores:
        team_vt_scores.append(score)
    
    for score in current_meet_team_ub_scores:
        team_ub_scores.append(score)
    
    for score in current_meet_team_bb_scores:
        team_bb_scores.append(score)
    
    for score in current_meet_team_fx_scores:
        team_fx_scores.append(score)
    
    for score in current_meet_team_meet_scores:
        team_meet_scores.append(score)
    
    
    return team_ids, team_meet_ids, team_vt_scores, team_ub_scores, team_bb_scores, team_fx_scores, team_meet_scores, meet_hosts
    


# def get_gymnast_score_info(url):
#     teams_button_clicker.click()
#     response = Selector(text=driver.page_source)
#     number_of_teams = row_count
#     team_results_table = response.css('div.rt-tbody')
#     results_table_rows = team_results_table.css('div.rt-tr-group')
    

#     for team in range(0, number_of_teams):
#         # Click on the team name
#         selector = '#team' + str(team)
#         driver.find_element(By.CSS_SELECTOR, selector).click()
#         response = Selector(text=driver.page_source)
#         # Iterate over the rows and scrape the gymnast data and scores
#         # Add the data to the lists
#         for row in results_table_rows:
#             gymnast_meet_id = url.split('/')[-1] # To match to the meet_id column in the meets table as a foreign key
#             gymnast_name = results_table_rows.css('a::text').get()
#             gymnast_href = results_table_rows.css('a::attr(href)').get()
#             gymnast_id = gymnast_href.split('/')[-1]
#             gymnast_team = gymnast_href.split('/')[-2]

#             if results_table_rows.css('div:nth-child(3)::text').get():
#                 gymnast_vt_score = (results_table_rows.css('div:nth-child(3)::text').get())
#             else:
#                 gymnast_vt_score = 'NaN'

#             if results_table_rows.css('div:nth-child(4)::text').get():
#                 gymnast_ub_score = (results_table_rows.css('div:nth-child(4)::text').get())
#             else:
#                 gymnast_ub_score = 'NaN'

#             if results_table_rows.css('div:nth-child(5)::text').get():
#                 gymnast_bb_score = (results_table_rows.css('div:nth-child(5)::text').get())
#             else:
#                 gymnast_bb_score = 'NaN'

#             if results_table_rows.css('div:nth-child(6)::text').get():
#                 gymnast_fx_score = (results_table_rows.css('div:nth-child(6)::text').get())
#             else:
#                 gymnast_fx_score = 'NaN'

#             if results_table_rows.css('div:nth-child(7)::text').get():
#                 gymnast_aa_score = (results_table_rows.css('div:nth-child(7)::text').get())
#             else:
#                 gymnast_aa_score = 'NaN'
        
#             gymnast_ids.append(gymnast_id)
#             gymnast_names.append(gymnast_name)
#             gymnast_team_ids.append(gymnast_team)
#             gymnast_meet_ids.append(gymnast_meet_id)
#             gymnast_vt_scores.append(gymnast_vt_score)
#             gymnast_ub_scores.append(gymnast_ub_score)
#             gymnast_bb_scores.append(gymnast_bb_score)
#             gymnast_fx_scores.append(gymnast_fx_score)
#             gymnast_aa_scores.append(gymnast_aa_score)

#         print(gymnast_ids)
#         print(gymnast_names)
#         print(gymnast_team_ids)
#         print(gymnast_meet_ids)
#         print(gymnast_vt_scores)
#         print(gymnast_ub_scores)
#         print(gymnast_bb_scores)
#         print(gymnast_fx_scores)
#         print(gymnast_aa_scores)
#         print(len(gymnast_ids))
#         print(len(gymnast_names))
#         print(len(gymnast_team_ids))
#         print(len(gymnast_meet_ids))
#         print(len(gymnast_vt_scores))
#         print(len(gymnast_ub_scores))
#         print(len(gymnast_bb_scores))
#         print(len(gymnast_fx_scores))
#         print(len(gymnast_aa_scores))


#     return 'honk' #I'm not sure about this return statement

print(meet_link)
# get_url_and_wait_for_elements_to_load(team_link, css_selector)
meet_links = meets_df['link']

def get_all_meet_score_info(url):
    for meet_link in meet_links:
        get_team_score_info(meet_link)
    
    return team_ids, team_meet_ids, team_vt_scores, team_ub_scores, team_bb_scores, team_fx_scores, team_meet_scores, meet_hosts

get_all_meet_score_info(url)
# meets_df['host'] = meet_hosts
# print(meets_df)
# team_scores_df = pd.DataFrame({'team_id': team_ids, 'meet_id': meet_ids, 'vt_score': team_vt_scores, 'ub_score': team_ub_scores, 'bb_score': team_bb_scores, 'fx_score': team_fx_scores, 'meet_score': team_meet_scores})
# team_scores_df.to_csv('../Data/Raw/team_scores.csv', index=False)

# gymnast_scores_df = pd.DataFrame({'gymnast_id': gymnast_ids, 'gymnast_firstname': gymnast_firstnames, 'gymnast_lastname': gymnast_lastnames, 'team_id': team_ids, 'meet_id': meet_ids, 'vt_score': gymnast_vt_scores, 'ub_score': gymnast_ub_scores, 'bb_score': gymnast_bb_scores, 'fx_score': gymnast_fx_scores, 'aa_score': gymnast_aa_scores})
# gymnast_scores_df.to_csv('../Data/Raw/gymnast_scores.csv', index=False)