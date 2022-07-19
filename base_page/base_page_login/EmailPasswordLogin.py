

from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
import time
from data_factory.PageGlobalDict import GlobalDict
from data_factory.DataParmes import DataCenter
from data_factory.ApiToken import ApiToken
import pytest
import os
import json


class EmailPasswordLogin:
    GlobalDict._init()
    # 此处构造测试用例所需的数据，
    #data = ['13853867111','leo','wang','12580','123qwe!@#']
    #data =DataCenter().reg_parmes()
    #print(data)
    #print(type(data))
    # 使用pytest.mark.parametrize引入用户数据

    #@pytest.mark.parametrize('userdata',DataCenter().reg_parmes())
    def email_password_login(self):
        """  正向流程：邮箱 密码登录   """



        json_path =GlobalDict.get_value('project_pwd').get('login_token')

        re_emali_code = []

        page_main_url = "https://login.test.gotin.top/login/phone/account"
        page_target_url = 'https://create.test.gotin.top/eventlists'
        """  正向流程：邮箱密码登录    """
        with sync_playwright() as p:

            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            # Go to https://login.test.gotin.top/login/phone/account
            page.goto(page_main_url)

            page.locator("text=邮箱").click()

            page.locator("input[type=\"text\"]").click()
            # Fill input[type="text"]
            page.locator("input[type=\"text\"]").fill("mimeng4a@163.com")
            # Click button:has-text("继续")
            page.locator("button:has-text(\"继续\")").click()
            page.wait_for_url("https://login.test.gotin.top/login/email/detail")
            # Fill input[type="password"]
            page.locator("input[type=\"password\"]").fill("123qwe!@#")
            # Click button:has-text("登录")
            page.locator("button:has-text(\"登录\")").click()

            page_main_title = page.inner_html("text=登录成功")
            time.sleep(3)
            page.wait_for_url(page_target_url)


            # 进行断言

            assert_url = page.url
            re_emali_code.append(assert_url)
            print(re_emali_code)
            if page_target_url == assert_url:
                print('邮箱登录成功')
            else:
                print('邮箱登录失败')
            assert page_target_url == page.url
            # 保存状态文件


            context.storage_state(path=json_path)

            # 获取当前页面元素，# 获取页面全文
            # html_page_value = page.content()
            p#age_main_title = page.inner_text("xpath=/html/body/div[1]/section/aside/div/div[3]/ul/li[2]/div/div")
            re_emali_code.append(page_main_title)
            print(page_main_title)
            # print(html_page_value)
            # storage = context.storage_state()
            # os.environ["STORAGE"] = json.dumps(storage)

            context.close()
            browser.close()
            return re_emali_code



if __name__ == '__main__':

    creat = EmailPasswordLogin().email_password_login()