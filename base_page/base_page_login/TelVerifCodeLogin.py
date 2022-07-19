

from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
import time
from data_factory.PageGlobalDict import GlobalDict
from data_factory.ApiToken import ApiToken
import pytest
import os
import json


class TelVerifCodeLogin:
    GlobalDict._init()

    # 使用pytest.mark.parametrize引入用户数据

    #@pytest.mark.parametrize('userdata',DataCenter().reg_parmes())
    def tel_verif_code_login(self):
        """  正向流程：验证码登录   """



        json_path =GlobalDict.get_value('project_pwd').get('login_token')

        print(json_path)
        re_verif_code = []

        #print(token_dir)
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
            page.locator("input[type=\"text\"]").nth(1).fill("17114261964")

            # Click button:has-text("继续")
            page.locator("button:has-text(\"继续\")").click()
            page.wait_for_url("https://login.test.gotin.top/login/phone/detail")

            # Click text=验证码 发送验证码 >> input[type="text"]
            page.locator("text=验证码 发送验证码 >> input[type=\"text\"]").click()

            # Fill text=验证码 发送验证码 >> input[type="text"]
            page.locator("text=验证码 发送验证码 >> input[type=\"text\"]").fill("12580")

            # Click text=+86 188-8473-7126 验证码 发送验证码 密码登录 登录 >> button

            page.click('xpath =/html/body/div/div[2]/div/div/div/div[3]/div[2]/button')
            # 获取当前页面元素，# 获取页面全文
            # html_page_value = page.content()
            page_main_title = page.inner_html("text=登录成功")
            time.sleep(3)
            #page.locator("text=+86 171-1426-1964 验证码 发送验证码 密码登录 登录 >> button").click()
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

            context.storage_state(path=json_path)


            re_verif_code.append(page_main_title)
            print(page_main_title)
            # print(html_page_value)
            #context.storage_state(path=token_dir)
            # os.environ["STORAGE"] = json.dumps(storage)

            #context.close()
            #browser.close()
            return re_verif_code



if __name__ == '__main__':

    creat = TelVerifCodeLogin().tel_verif_code_login()