# *******************************************************************************************************************************
# Importing the necessary programs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy import Selector
from pprint import pprint as print
import pandas as pd

# *******************************************************************************************************************************
# Setting program-level variables
driver = webdriver.Chrome()
url = "https://roadtonationals.com/results/standings/"
years = [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015] # These are the years that we are interested in evaluating

print('honk')

# ******************************************************************************************************************************
# PART 1: Go to the url, wait until everything on the page loads

def get_url_and_wait_for_elements_to_load(url):
    try:
        driver.get(url)
        print("*****************************")
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.rt-table > div.rt-tbody')) # (Source: https://selenium-python.readthedocs.io/waits.html )
        )
        print(element)
    except:
        print("oh no it didn't work")
        exit()

get_url_and_wait_for_elements_to_load(url)
response = Selector(text=driver.page_source)

print(response)

# ******************************************************************************************************************************
# 2 Pluck out all the Team Names & Divisions from the table that appears (the big main table that the whole page seems to be about) {'name': 'Auburn', 'division': 1}
team_names = []
team_divisions = []
team_links = []
table = response.css('div.rt-table > div.rt-tbody')
rows = table.css('.rt-tr-group')

def get_team_info(year, url):  

    #first_one = rows[1].css('div a::text')
    for row in rows:
        a_selector = row.css('a').get()
        link = row.css('a::attr(href)').get()
        team_name = row.css('a::text').get()
        division = row.css('div > div:nth-child(8)::text').get()
    
        #print(a_selector)
        #print(a_text)
        #print(a_href)
        # Only add division 1 teams who are not already in the list
        if team_name in team_names:  
            continue # Do nothing
        elif str(division) != '1': 
            continue
        else:
            team_names.append(team_name)
            team_links.append(link)
            team_divisions.append(division)

    print(team_divisions)
    return team_names, team_divisions, team_links #I'm not sure about this return statement

# 3 Click on the 'years' drop down menu and select the next year in the list (but we have determined we don't have to do this, but this is how I would instruct a person, not a machine)
def paginate_through_years(years, url):
    for year in years:
        new_url = url + 'final/' + str(year)
        print(new_url)
        get_url_and_wait_for_elements_to_load(new_url)
        get_team_info(year, new_url)

paginate_through_years(years, url)
teams_df = pd.DataFrame({'team_name': team_names, 'division': team_divisions, 'link': team_links})

# 4 Do step 2 again
# 5 Do step 3 again (etc until end of the years list)