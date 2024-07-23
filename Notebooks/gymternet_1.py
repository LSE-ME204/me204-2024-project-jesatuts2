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
    

get_url_and_wait_for_elements_to_load(url, 'div.rt-table > div.rt-tbody')
response = Selector(text=driver.page_source)

print(response)

# ******************************************************************************************************************************
# 2 Pluck out all the Team Names & Divisions from the table that appears (the big main table that the whole page seems to be about) {'name': 'Auburn', 'division': 1}
team_names = []
team_divisions = []
team_links = []
team_ids = []
css_selector = 'div.rt-table > div.rt-tbody'
table = response.css(css_selector)
rows = table.css('.rt-tr-group')

def get_team_info(year, url):  
    #first_one = rows[1].css('div a::text')
    for row in rows:
        a_selector = row.css('a').get()
        link_slug = row.css('a::attr(href)').get()
        link = 'https://roadtonationals.com' + link_slug
        team_name = row.css('a::text').get()
        division = row.css('div > div:nth-child(8)::text').get()
        team_id = link_slug.split('/')[-1]
    
        #print(a_selector)
        #print(a_text)
        #print(a_href)
        # Only add division 1 teams who are not already in the list
        if team_name in team_names:  
            continue # Do nothing
        elif str(division) != '1': 
            continue
        else:
            team_ids.append(team_id)
            team_names.append(team_name)
            team_links.append(link)
            team_divisions.append(division)

    return team_ids, team_names, team_divisions, team_links #I'm not sure about this return statement

# ******************************************************************************************************************************
# 3 Paginate through the 'years' drop down menu and select the next year in the list and call step 2 again
def paginate_through_teams_over_the_years(years, url):
    for year in years:
        # Load the team pages and scrape the information
        new_team_url = url + 'final/' + str(year)
        print(new_team_url)

        get_url_and_wait_for_elements_to_load(new_team_url, css_selector)
        response = Selector(text=driver.page_source)
        get_team_info(year, new_team_url)

paginate_through_teams_over_the_years(years, url)
teams_df = pd.DataFrame({'team_id': team_ids, 'team_name': team_names, 'division': team_divisions, 'link': team_links})
print(teams_df)

# ******************************************************************************************************************************
# 4 Go to each of the team's links and scrape the meet information

team_link = team_links[1]
meet_dates = []
meet_links = []
meet_ids = []
meet_seasons = []


def get_meet_info(url):
    css_selector = 'div.rt-tbody'
    get_url_and_wait_for_elements_to_load(url, css_selector)
    response = Selector(text=driver.page_source)  
    
    table = response.css(css_selector)
    rows = table.css('div.rt-tbody > div.rt-tr-group')
    
    for row in rows:
        team_id = url.split('/')[-1] # To match to the team_id column in the teams table as a foreign key
        link_slug = row.css('a::attr(href)').get()
        link = 'https://roadtonationals.com' + link_slug
        meet_id = link_slug.split('/')[-1] # To act as the primary key for the meets table
        meet_date = table.css('div > div > div:nth-child(2)::text').get() #TODO: Convert to datetime
        season = meet_date.split('-')[-1]
    
        if meet_id in meet_ids:  
            continue
        else:
            meet_ids.append(meet_id)
            meet_dates.append(meet_date)
            meet_seasons.append(season)
            meet_links.append(link)
    print(meet_links)
    return meet_ids, meet_dates, meet_seasons, meet_links #I'm not sure about this return statement

print(team_link)
# get_url_and_wait_for_elements_to_load(team_link, css_selector)
get_meet_info(team_link)

# ******************************************************************************************************************************
# 5 Paginate through every year on a team's page and pick up the meet data
def paginate_through_years_to_get_meet_data(years, url):
    for year in years:

        # Load the team pages and scrape the information
        split_url = url.split('/') # Splitting the url by the '/' character
        split_url[-2] = str(year) # Changing the year in the url to the current year
        new_url = '/'.join(split_url) # Joining the url back together
        print(new_url)

        get_meet_info(new_url)

#         get_url_and_wait_for_elements_to_load(new_url, css_selector)
#         response = Selector(text=driver.page_source)
#         get_meet_info(year, new_url)

# ******************************************************************************************************************************
# 6 Paginate through every year for every team and pick up the meet data
def paginate_through_teams_to_get_meet_data(years, team_links):
    for link in team_links:
        paginate_through_years_to_get_meet_data(years, link)

#         get_url_and_wait_for_elements_to_load(new_url, css_selector)
#         response = Selector(text=driver.page_source)
#         get_meet_info(year, new_url)


paginate_through_teams_to_get_meet_data(years, team_links)
meets_df = pd.DataFrame({'meet_id': meet_ids, 'meet_date': meet_dates, 'season': meet_seasons, 'link': meet_links})
print(meets_df)

