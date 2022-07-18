

import time
from data_factory.DataParmes import DataCenter
from playwright.sync_api import sync_playwright
from data_factory.PageGlobalDict import  GlobalDict
import pytest
import os

class EmailRegister:

    # 此处构造测试用例所需的数据，
    #data = ['13853867111','leo','wang','12580','123qwe!@#']
    #data =DataCenter().reg_parmes()
    #print(data)
    #print(type(data))
    # 使用pytest.mark.parametrize引入用户数据

    @pytest.mark.parametrize('userdata',DataCenter().reg_parmes())
    def add_email_user(self,userdata):
        """参数区  正向流程：添加邮箱注册用户--------------------------------------------"""

        wait = int(1)
        re_list = []
        print(userdata)

        #引用声明全局变量
        GlobalDict._init()
        GlobalDict.set_value('TelRegister_input', userdata)
        GlobalDict.get_value('project_pwd')
        #json_save_patch =project_dir[0]
        # 报告生成路径,，取值公共变量中的路径
        json_save_patch =GlobalDict.get_value('project_pwd')[0]

        page_main_url = "https://login.test.gotin.top/login/phone/account"
        page_target_url ='https://create.test.gotin.top/guide/organizer/create'

        """参数区  正向流程：添加邮箱注册用户--------------------------------------------"""
        with sync_playwright() as p:

            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            # Go to https://login.test.gotin.top/login/phone/account
            page.goto(page_main_url)
            time.sleep(wait)
            page.locator("input[type=\"text\"]").fill(userdata[5])
            # Click button:has-text("继续")
            page.locator("button:has-text(\"继续\")").click()

            # Click text=没有账号？去注册
            page.locator("text=没有账号？去注册").click()
            page.wait_for_url("https://login.test.gotin.top/register/email/account")
            # Click button:has-text("继续")
            page.locator("button:has-text(\"继续\")").click()
            page.wait_for_url("https://login.test.gotin.top/register/email/detail")
            # Fill input[type="text"] >> nth=1
            page.locator("input[type=\"text\"]").nth(1).fill(userdata[1])
            # Press Tab
            page.locator("input[type=\"text\"]").nth(1).press("Tab")
            # Fill input[type="text"] >> nth=0
            page.locator("input[type=\"text\"]").first.fill(userdata[2])
            # Click input[type="password"]
            page.locator("input[type=\"password\"]").click()
            # Fill input[type="password"]
            page.locator("input[type=\"password\"]").fill(userdata[3])
            # Click button:has-text("注册用户")
            page.locator("button:has-text(\"注册用户\")").click()
            # 进行断言
            page.wait_for_url("https://create.test.gotin.top/guide/organizer/create")

            assert_url =page.url
            re_list.append(assert_url)
            print(re_list)
            if page_target_url == assert_url :
                print('手机号注册成功')
            else:
                print('手机号注册成功')
            assert page_target_url == page.url
            # 保存状态文件
            os1 =os.path.dirname(os.path.realpath(__file__))
            print(os1)

            context.storage_state(path=json_save_patch)

            # 获取当前页面元素，# 获取页面全文
            #html_page_value = page.content()
            page_main_title =page.inner_text("xpath=/ html / body / div[1] / section / section / main / div / div / div[1] / div / div[2]")
            re_list.append(page_main_title)
            print(page_main_title)
            #print(html_page_value)
            #storage = context.storage_state()
            #os.environ["STORAGE"] = json.dumps(storage)

            context.close()
            browser.close()
            GlobalDict.set_value('TelRegister_relist',re_list)
            return re_list




if __name__ == '__main__':

    creat = EmailRegister().add_email_user()