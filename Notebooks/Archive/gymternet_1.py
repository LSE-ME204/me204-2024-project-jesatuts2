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
teams_df.to_csv('../Data/Raw/teams.csv', index=False)

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
meets_df.to_csv('../Data/Raw/meets.csv', index=False)

# ******************************************************************************************************************************
# 5 Go to each of the meet's links and scrape the score information

meet_link = meet_links[1]
meet_ids = []
team_ids = []
team_vt_scores = []
team_ub_scores = []
team_bb_scores = []
team_fx_scores = []
team_meet_scores = []
gymnast_ids = []
gymnast_names = []
gymnast_vt_scores = []
gymnast_ub_scores = []
gymnast_bb_scores = []
gymnast_fx_scores = []
gymnast_aa_scores = []
meet_hosts = []

def get_score_info(url):
    css_selector = 'div.rt-tbody'
    get_url_and_wait_for_elements_to_load(url, css_selector)
    response = Selector(text=driver.page_source)  
    
    meet_table = response.css(css_selector)
    meet_table_rows = response.css('div.rt-tbody > div.rt-tr-group')
    team_button_clicker = driver.find_element(By.CSS_SELECTOR, '#teambtn')
    row_count = 0

    if response.css('p:nth-child(4)').get():
        meet_host = response.css('p:nth-child(4)::text').get()
    else:
        meet_host = 'NaN'
    
    meet_hosts.append(meet_host)

    for row in meet_table_rows:
        row_count = row_count + 1
        meet_id = url.split('/')[-1] # To match to the meet_id column in the meets table as a foreign key
        team_href = meet_table_rows.css('div > div > a::attr(href)').get()
        team_id = team_href.split('/')[-1]
        
        team_vt_score = (meet_table_rows.css('div:nth-child(4)::text').get())
        team_ub_score = (meet_table_rows.css('div:nth-child(5)::text').get())
        team_bb_score = (meet_table_rows.css('div:nth-child(6)::text').get())
        team_fx_score = (meet_table_rows.css('div:nth-child(7)::text').get())
        team_meet_score = (meet_table_rows.css('div:nth-child(8) > strong::text').get())

        team_ids.append(team_id)
        team_vt_scores.append(team_vt_score)
        team_ub_scores.append(team_ub_score)
        team_bb_scores.append(team_bb_score)
        team_fx_scores.append(team_fx_score)
        team_meet_scores.append(team_meet_score)

    team_button_clicker.click()
    response = Selector(text=driver.page_source)

    number_of_teams = row_count
    team_results_table = response.css('div.rt-tbody')
    results_table_rows = team_results_table.css('div.rt-tr-group')

    for team in range(0, number_of_teams):
        # Click on the team name
        selector = '#team' + str(team)
        driver.find_element(By.CSS_SELECTOR, selector).click()
        # Iterate over the rows and scrape the gymnast data and scores
        # Add the data to the lists
        for row in results_table_rows:
            meet_id = url.split('/')[-1] # To match to the meet_id column in the meets table as a foreign key

            gymnast_name = results_table_rows.css('a::text').get()
            gymnast_href = results_table_rows.css('a::attr(href)').get()
            gymnast_id = gymnast_href.split('/')[-1]
            gymnast_team = gymnast_href.split('/')[-2]
            gymnast_meet_id = meet_id

            if results_table_rows.css('div:nth-child(3)::text').get():
                gymnast_vt_score = float(results_table_rows.css('div:nth-child(3)::text').get())
            else:
                gymnast_vt_score = 'NaN'

            if results_table_rows.css('div:nth-child(4)::text').get():
                gymnast_ub_score = float(results_table_rows.css('div:nth-child(4)::text').get())
            else:
                gymnast_ub_score = 'NaN'

            if results_table_rows.css('div:nth-child(5)::text').get():
                gymnast_bb_score = float(results_table_rows.css('div:nth-child(5)::text').get())
            else:
                gymnast_bb_score = 'NaN'

            if results_table_rows.css('div:nth-child(6)::text').get():
                gymnast_fx_score = float(results_table_rows.css('div:nth-child(6)::text').get())
            else:
                gymnast_fx_score = 'NaN'

            if results_table_rows.css('div:nth-child(7)::text').get():
                gymnast_aa_score = float(results_table_rows.css('div:nth-child(7)::text').get())
            else:
                gymnast_aa_score = 'NaN'
        
            gymnast_ids.append(gymnast_id)
            gymnast_names.append(gymnast_name)
            gymnast_vt_scores.append(gymnast_vt_score)
            gymnast_ub_scores.append(gymnast_ub_score)
            gymnast_bb_scores.append(gymnast_bb_score)
            gymnast_fx_scores.append(gymnast_fx_score)
            gymnast_aa_scores.append(gymnast_aa_score)

    return 'honk' #I'm not sure about this return statement

print(meet_link)
# get_url_and_wait_for_elements_to_load(team_link, css_selector)
get_score_info(meet_link)
meets_df['host'] = meet_hosts
print(meets_df)
team_scores_df = pd.DataFrame({'team_id': team_ids, 'meet_id': meet_ids, 'vt_score': team_vt_scores, 'ub_score': team_ub_scores, 'bb_score': team_bb_scores, 'fx_score': team_fx_scores, 'meet_score': team_meet_scores})
team_scores_df.to_csv('../Data/Raw/team_scores.csv', index=False)

gymnast_scores_df = pd.DataFrame({'gymnast_id': gymnast_ids, 'gymnast_firstname': gymnast_firstnames, 'gymnast_lastname': gymnast_lastnames, 'team_id': team_ids, 'meet_id': meet_ids, 'vt_score': gymnast_vt_scores, 'ub_score': gymnast_ub_scores, 'bb_score': gymnast_bb_scores, 'fx_score': gymnast_fx_scores, 'aa_score': gymnast_aa_scores})
gymnast_scores_df.to_csv('../Data/Raw/gymnast_scores.csv', index=False)