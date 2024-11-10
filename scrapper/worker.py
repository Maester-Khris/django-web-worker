import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://devicon.dev/"



def launch_scrapper():
    # page = requests.get(URL)
    # soup = BeautifulSoup(page.content, "html.parser")
    # iconlist = soup.find("ul", class_="cbp-ig-grid")
    # #print(iconlist)
    # titles = iconlist.find_all("h3", class_="cbp-ig-title")
    # for index, title in enumerate(titles):
    #     print(title.text)

    # Set up the headless browser
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    # Load the page
    driver.get(URL)

    # Wait for the content to load (you may need to adjust this)
    driver.implicitly_wait(10)

    # Scrape the rendered content
    iconlist = driver.find_elements(By.CLASS_NAME, 'cbp-ig-title')
    iconsdict = {"name": "","icon": ""}
    jsonicons = []
    for index, title in enumerate(iconlist):
        iconsdict = {"name": "","icon": ""}
        iconsdict["name"] = title.text
        iconsdict["icon"] = f"devicon-{title.text}-original"
        jsonicons.append(iconsdict)
        
        #json_icon_object = json.dumps(iconsdict, indent=4)
        #print(title.text)

    with open("allicons.json", "w") as outfile:
        json.dump(jsonicons, outfile)
    print("hello les nazes")