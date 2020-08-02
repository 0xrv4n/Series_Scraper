import requests
from bs4 import BeautifulSoup
import json

def get_series_and_links():
	url = 'http://todaytvseries1.com/tv-series/428-13-reasons-why-netflix-tv3'
	response = requests.get(url)
	if response.status_code == 200:
		soup = BeautifulSoup(response.text, 'html.parser')
		
		# parse document soup
		episodes_mash = soup.find_all(class_= 'uk-accordion-content')
		season_break = {}
		for season_number, season_data in enumerate(episodes_mash[::-1], start=1):
			season_break['S' + str(season_number)] = season_data
		season_break['total_season'] = len(episodes_mash)

		# dump season content
		# with open('data_dummy.json', 'w') as outfile:
		# 	json.dump(season_data, outfile)
		# 	outfile.close()

		return season_break['S1']
	else:
		return 'Invalid response from host'

def get_all_episodes_and_links(ep):
	for episodes in ep:
		ep_elements = [episodes.find('div', class_='cell2').text],{ 
		'size': episodes.find('div', class_='cell3').text, 
		'link': episodes.find('div', class_='cell4').find('a', class_='hvr-icon-sink-away').get('href')
		}

		return ep_elements

epsd_list = get_series_and_links()
epsd_check = get_all_episodes_and_links(epsd_list)

