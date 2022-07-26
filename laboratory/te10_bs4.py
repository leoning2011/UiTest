
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
import time
from common.DataParmes import DataCenter
import pytest
import os
import json
import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        # Go to https://login.test.gotin.top/login/phone/account
        page.goto(url)

        #r = requests.get(url)
        r = page.request.get(url)
        demo = r.text()
        soup = BeautifulSoup(demo, "lxml")
        print(soup.prettify())


if __name__ == '__main__':
    url = "https://create.test.gotin.top/myevent/overview"
    go_url =getHTMLText(url)
