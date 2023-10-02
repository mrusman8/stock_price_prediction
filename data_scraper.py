from datetime import datetime
import requests
from bs4 import BeautifulSoup


class DataScraping():
    def __init__(self):
        self.values = None


    def scrap(self, x):
        try:
            # Send an HTTP GET request to the URL
            response = requests.get(x)
            self.values = []
            # Get the current date for the file name
            current_date = datetime.now().strftime("%d-%m-%Y")
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                table = soup.find(class_="stats stats--noborder")
                self.close = soup.find(class_="numRange")["data-current"]

                for i in table.find_all(class_="stats_value"):
                    self.values.append(float(i.get_text().replace(',', '')))  # Remove commas and convert to float
                self.values.append(self.close)
            else:
                print('Scraping not allowed')
        except Exception as e:
            print(f"An error occurred: {str(e)}")


