

from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
from data_factory.PageGlobalDict import GlobalDict
import time
from data_factory.DataParmes import DataCenter
from data_factory.ApiToken import ApiToken
import pytest
import os
import json


class TelPasswordLogin:

    # 此处构造测试用例所需的数据，
    #data = ['13853867111','leo','wang','12580','123qwe!@#']
    #data =DataCenter().reg_parmes()
    #print(data)
    #print(type(data))
    # 使用pytest.mark.parametrize引入用户数据

    #@pytest.mark.parametrize('userdata',DataCenter().reg_parmes())
    def tel_password_login(self):
        """  正向流程：密码登录   """

        GlobalDict._init()

        json_path =GlobalDict.get_value('project_pwd').get('login_token')
        re_verif_code = []

        page_main_url = "https://login.test.gotin.top/login/phone/account"
        page_target_url = 'https://create.test.gotin.top/eventlists'
        """  正向流程：密码登录    """
        with sync_playwright() as p:

            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            # Go to https://login.test.gotin.top/login/phone/account
            page.goto(page_main_url)


            # Fill input[type="text"] >> nth=1
            page.locator("input[type=\"text\"]").nth(1).fill("18884737126")

            # Click button:has-text("继续")
            page.locator("button:has-text(\"继续\")").click()
            page.wait_for_url("https://login.test.gotin.top/login/phone/detail")

            # Click text=密码登录
            page.locator("text=密码登录").click()

            # Click input[type="password"]
            page.locator("input[type=\"password\"]").click()

            # Fill input[type="password"]
            page.locator("input[type=\"password\"]").fill("123qwe!@#")

            # Click text=+86 188-8473-7126 密码密码验证码登录 忘记密码 登录 >> button
            page.locator("text=+86 188-8473-7126 密码密码验证码登录 忘记密码 登录 >> button").click()

            # 获取当前页面元素，# 获取页面全文
            # html_page_value = page.content()
            page_main_title = page.inner_html("text=登录成功")
            time.sleep(3)
            page.wait_for_url("https://create.test.gotin.top/eventlists")



            # 进行断言

            assert_url = page.url
            re_verif_code.append(assert_url)
            print(re_verif_code)
            if page_target_url == assert_url:
                print('密码登录成功')
            else:
                print('密码登录失败')
            assert page_target_url == page.url
            # 保存状态文件


            context.storage_state(path=json_path)

            # 获取当前页面元素，# 获取页面全文
            # html_page_value = page.content()
            #page_main_title = page.inner_text(
                #"xpath=/html/body/div[1]/section/aside/div/div[3]/ul/li[2]/div/div")
            re_verif_code.append(page_main_title)
            print(page_main_title)


            context.close()
            browser.close()
            return re_verif_code



if __name__ == '__main__':

    creat = TelPasswordLogin().tel_password_login()