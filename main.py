from ast import While
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import datetime
import tkinter as tk
from tkinter import FIRST, messagebox



class WebScraper:
    def __init__(self):
        # Initialize the webdriver
        self.firefox_options = Options()
        self.firefox_options.headless = True
        self.driver = webdriver.Firefox(options=self.firefox_options)
        self.actions = ActionChains(self.driver)
        self.data_export = []

    def close_browser(self):
        self.driver.quit()

    def navigate_to_url(self, url):
        self.driver.get(url)
        sleep(15)  # Adjust sleep as needed

    def Start(self,Item_max):

        try:
            self.actions.send_keys(Keys.TAB * 37)
            self.actions.perform()

            Stop_number = Item_max
            count_enter = 0
            while count_enter <= Stop_number:
                self.actions.send_keys(Keys.ENTER).perform()
                print('enter')

                # Wait for a specific element to be present
                wait = WebDriverWait(self.driver, 20)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.xyamay9.x1pi30zi.x18d9i69.x1swvt13')))
                
                # Now that the content is loaded, get the HTML
                print('Render the dynamic content to static HTML')
                html = self.driver.page_source       
                print(' Parse the static HTML')
                soup = BeautifulSoup(html, "html.parser")
                
                #Quick demo for some info:
                FIRST_DIV = soup.find("div", {"class": "xyamay9 x1pi30zi x18d9i69 x1swvt13"})


                # Get the text of Title:
                Title = FIRST_DIV.select_one('div.xyamay9.x1pi30zi.x18d9i69.x1swvt13 h1 span').get_text(strip=True)
                print('Title: ', Title)

                # Get the text of Price:
                price_text = FIRST_DIV.select_one('div.xyamay9.x1pi30zi.x18d9i69.x1swvt13 div.x1xmf6yo span').get_text(strip=True)
                print("Price:", price_text)

                # Get the text of location:
                location_text = FIRST_DIV.select_one('div.xyamay9.x1pi30zi.x18d9i69.x1swvt13 div.x1xmf6yo a span').get_text(strip=True)
                print("Location:", location_text)


                # Append the data to the list
                self.data_export.append({'Title': Title, 'Price': price_text, 'Location': location_text})

                # Back to list:
                self.driver.back()
                print('Navigated back')

                #Tab new:
                self.actions.send_keys(Keys.TAB).perform()
          
                sleep(10)
                count_enter +=1
            
        except Exception as e:
            print(f"Error accepting cookies: {e}")

    def export_to_excel(self, file_name='output.xlsx'):
        # Create a DataFrame from the list of dictionaries
        df = pd.DataFrame(self.data_export)

        # Export DataFrame to Excel
        df.to_excel(file_name, index=False)
        print(f'Data exported to {file_name}')

# Example usage:
if __name__ == "__main__":
    ##Filter the option in Marketplace and copy the url
    url = "https://www.facebook.com/marketplace/denver/search/?query=Antiques%20%26%20Collectibles"
    scraper = WebScraper()

    try:
        scraper.navigate_to_url(url)

        Item_max = 5 ###The max items that you want to scrape
        scraper.Start(Item_max)

        # Export the data to Excel after the loop
        scraper.export_to_excel()

    finally:
        scraper.close_browser()
