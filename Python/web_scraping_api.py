#About the project:
#It uses parse hub to get data from covid-19 website.
#The structure of the data you can get from "Data class"
#get_total_data --> to get all the data of cases, reovered and deaths from all countries.
#get_country_data --> to get data of cases, reovered and deaths from singel country.
#get_list_of_countries --> to get the list of countries we have scraped and all my calculations are based on.



import requests
import json

import time
import threading


#Needed for api connection
api_key = "tTFUuPu8c8T6"
Projet_token = "tcHTyB6TMZAm"
run_token = "tjQAJAoQuTYX"


class Data:
	def __init__(self, api_key, project_token):
		self.api_key = api_key
		self.project_token = project_token
		self.params = {
		"api_key": self.api_key
		}
		self.data = self.get_data()

	def get_data(self):
		
		# response = requests.post(f"https://parsehub.com/api/v2/projects/{self.project_token}/run", params = {"api_key": api_key})
		response = requests.get(f"https://parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data", params = {"api_key": api_key})
		data_json = json.loads(response.text) #It will print all the scraped data in json format
		
		return data_json


	def get_total_data(self, state): #[state can be [Coronavirus Cases - recovered - deaths]]
		data = self.data['Total']
		for content in data:
			if content['name'][:-1].lower() == state:
				return content['value']


	def get_country_data(self, country):
		data = self.data["country"]
		for content in data:
			if content['name'].lower() == country.lower():
				return content

		return "0"

	def get_list_of_countries(self):
		countries = []
		for country in self.data['country']:
			countries.append(country['name'].lower())

		return countries

	def update_data(self):
		response = requests.post(f"https://parsehub.com/api/v2/projects/{self.project_token}/run", params = {"api_key": api_key})

		def poll():
			time.sleep(0.1)
			old_data = self.data
			while True:
				new_data = self.get_data()
				if new_data != old_data:
					self.data = new_data
					print("Updated")
					break
				time.sleep(5)
		t = threading.Thread(target=poll)
		t.start()

bes = Data(api_key, Projet_token)
bes.update_data()
print(bes.get_data()['Total'])




