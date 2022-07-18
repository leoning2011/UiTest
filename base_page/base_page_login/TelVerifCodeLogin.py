

from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
import time
from data_factory.DataParmes import DataCenter
from data_factory.ApiToken import ApiToken
import pytest
import os
import json


class TelVerifCodeLogin:

    # 此处构造测试用例所需的数据，
    #data = ['13853867111','leo','wang','12580','123qwe!@#']
    #data =DataCenter().reg_parmes()
    #print(data)
    #print(type(data))
    # 使用pytest.mark.parametrize引入用户数据

    #@pytest.mark.parametrize('userdata',DataCenter().reg_parmes())
    def tel_verif_code_login(self):
        """  正向流程：验证码登录   """

        re_verif_code = []

        page_main_url = "https://login.test.gotin.top/login/phone/account"
        page_target_url = 'https://create.test.gotin.top/eventlists'
        """  正向流程：验证码登录    """
        with sync_playwright() as p:

            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            # Go to https://login.test.gotin.top/login/phone/account
            page.goto(page_main_url)

            # Click input[type="text"] >> nth=1
            page.locator("input[type=\"text\"]").nth(1).click()

            # Fill input[type="text"] >> nth=1
            page.locator("input[type=\"text\"]").nth(1).fill("18884737126")

            # Click button:has-text("继续")
            page.locator("button:has-text(\"继续\")").click()
            page.wait_for_url("https://login.test.gotin.top/login/phone/detail")

            # Click text=验证码 发送验证码 >> input[type="text"]
            page.locator("text=验证码 发送验证码 >> input[type=\"text\"]").click()

            # Fill text=验证码 发送验证码 >> input[type="text"]
            page.locator("text=验证码 发送验证码 >> input[type=\"text\"]").fill("12580")

            # Click text=+86 188-8473-7126 验证码 发送验证码 密码登录 登录 >> button
            page.locator("text=+86 188-8473-7126 验证码 发送验证码 密码登录 登录 >> button").click()
            page.wait_for_url("https://create.test.gotin.top/eventlists")













            # 进行断言

            assert_url = page.url
            re_verif_code.append(assert_url)
            print(re_verif_code)
            if page_target_url == assert_url:
                print('验证码登录成功')
            else:
                print('验证码登录失败')
            assert page_target_url == page.url
            # 保存状态文件
            os1 = os.path.dirname(os.path.realpath(__file__))
            print(os1)

            context.storage_state(path='tel_verif_code_login.json')

            # 获取当前页面元素，# 获取页面全文
            # html_page_value = page.content()
            page_main_title = page.inner_text(
                "xpath=/html/body/div[1]/section/aside/div/div[3]/ul/li[2]/div/div")
            re_verif_code.append(page_main_title)
            print(page_main_title)
            # print(html_page_value)
            # storage = context.storage_state()
            # os.environ["STORAGE"] = json.dumps(storage)

            context.close()
            browser.close()
            return re_verif_code



if __name__ == '__main__':

    creat = TelVerifCodeLogin().tel_verif_code_login()