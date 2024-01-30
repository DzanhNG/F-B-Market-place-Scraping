# F-B-Market-place-Scraping
This project focuses on scraping data from Facebook Marketplace in Denver, CO, and a +75 mile radius, specifically targeting "local pick-up" items. Our goal is to analyze categories such as Antiques, Electronics, Vehicles, etc., extracting key details like item name, listing price, seller rating, and reviews. Optionally, item links may be included. The extracted data will be conveniently exported to a CSV file, providing a concise and structured dataset for quick insights into local market trends and pricing dynamics.


# How to use: Main.py
```python 

if __name__ == "__main__":
    ##Filter the option in Marketplace and copy the url
    url = "https://www.facebook.com/marketplace/denver/search/?query=Antiques%20%26%20Collectibles" 
    scraper = WebScraper()
    try:
        scraper.navigate_to_url(url)
        Item_max = 5  ###The max items that you want to scrape
        scraper.Start(Item_max)
        # Export the data to Excel after the loop
        scraper.export_to_excel()
    finally:
        scraper.close_browser()
```
# Video Demo:


# Export data to excel:
<img src="./Images\output_data.PNG" width="15000" height="500">
