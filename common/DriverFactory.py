from selenium import webdriver
from config.Config import Config
from playwright.sync_api import sync_playwright


class Driver:

    @classmethod
    def get_driver(cls):
        config = Config()
        timeout = config.waitTime
        browerType = config.browserType.strip().lower()

        with sync_playwright() as p:
                if browerType == 'chromium':
                    # 本地chrome浏览器
                    chrome_options = p.chromium.launch(headless=False)
                    context = chrome_options.new_context()
                    page = context.new_page()
                    page.wait_for_timeout(int(timeout))
                elif browerType =='chromium':
                    # chrome headless模式
                    chrome_options = webdriver.ChromeOptions()
                    chrome_options.add_argument("--headless")
                    chrome_options.add_argument("--window-size=1920x1080")
                    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
                    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
                    chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片，提升运行速度


                elif browerType == Driver.Firefox:
                    # 本地firefox浏览器
                    driver = webdriver.Firefox()
                    driver.maximize_window()
                    driver.implicitly_wait(timeout)

                elif browerType == Driver.FirefoxHeadless:
                    # firefox headless模式
                    firefox_options = webdriver.FirefoxOptions()
                    firefox_options.headless = True
                    driver = webdriver.Firefox(firefox_options=firefox_options)

                elif browerType == Driver.Grid:
                    # 通过远程节点运行
                    chrome_capabilities = {
                        "browserName": "chrome",
                        "version": "",
                        "platform": "ANY",
                        "javascriptEnabled": True,
                        # "marionette": True,
                    }

                    driver = webdriver.Remote(config.hubIP, desired_capabilities=chrome_capabilities)

                    driver.set_window_size(1920, 1080)

                else:
                    raise NameError("driver驱动类型定义错误！")
                return driver

    Firefox = 'firefox'
    Chrome = 'chrome'
    IE = 'ie'
    Grid = 'grid'
    FirefoxHeadless = 'firefox-headless'
    ChromeHeadless = 'chrome-headless'