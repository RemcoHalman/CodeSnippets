import os
import sys
import time

import pdfkit
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def wuxia(site):
    title = driver.find_element_by_xpath(
        '//*[@id="content-container"]/div[4]/div/div[3]/div[1]/div[1]/div[3]/h4'
    ).get_attribute("innerHTML")
    titleHTML = driver.find_element_by_xpath(
        '//*[@id="content-container"]/div[4]/div/div[3]/div[1]/div[1]/div[3]/h4'
    ).get_attribute("outerHTML")
    content = driver.find_element_by_xpath(
        '//*[@id="content-container"]/div[4]/div/div[3]/div[1]/div[3]'
    ).get_attribute("innerHTML")

    with open(f"{title}.html", "w") as chapter_file:
        chapter_file.writelines(titleHTML)
        chapter_file.writelines(content)
        chapter_file.close()  # to change file access modes
    # print("====== Title ======")
    # print(title)
    # print(content)


if __name__ == "__main__":
    site = input("Novel(url first chapter): ")
    # Path can be set to chromedriver in sites folder
    driver = webdriver.Chrome("/Users/Remco/Sites/chromedriver")
    driver.get(site)
    wuxia(site)
    driver.quit()
