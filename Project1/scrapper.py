######################################################################
#
# scrapper.py
# This file contains the selenium scraper webdriver and scraping loop
# Arnoldas Cvirka 2022-08-30
#
######################################################################


# import libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

loop = True

brand = []
model = []
price = []

while loop is True:
    # webdriver config
    try:
        page
    except NameError:
        page = 1

    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    ...

    # disable image and javascript loading
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        "prefs",
        {"profile.managed_default_content_settings.images": 2},
    )
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument("headless")

    ...

    # get page and options for the driver
    driver = webdriver.Chrome(
        options=options,
        chrome_options=chrome_options,
        executable_path="D:\PProjects\Project1\WebDriver\chromedriver.exe",
    )
    driver.get(
        f"https://autogidas.lt/skelbimai/automobiliai/?f_50=kaina_asc&page={page}"
    )
    all_titles = driver.find_elements(By.CLASS_NAME, "item-title")
    prices = driver.find_elements(By.CLASS_NAME, "item-price")

    ...

    # convert web elements to text strings and apppend them to given lists
    for title in all_titles:
        t = title.text.split()[0]
        tt = title.text.split(maxsplit=1)[1]
        brand.append(t)
        model.append(tt)

    for pr in prices:
        p = pr.text
        pf = filter(str.isdigit, p)
        ns = "".join(pf)
        price.append(ns)

    # switch to new page
    page += 1

    # close previous page
    driver.quit()

    # prints
    print(f"I scraped {page} out of 200 pages!")

    # quit loop after 200 pages
    if page == 200:
        loop = False

# create csv with said data
columns = {"Brand": brand, "Model": model, "Price": price}
df = pd.DataFrame(columns)
print(df)
df.to_csv("car_info.csv", index=False)

...
