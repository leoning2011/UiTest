

import time
from common.DataParmes import DataCenter
from playwright.sync_api import sync_playwright
from common.PageGlobalDict import  GlobalDict
import pytest


class TelRegister:
    # 引用声明全局变量
    GlobalDict._init()
    # 使用pytest.mark.parametrize引入用户数据

    @pytest.mark.parametrize('userdata',DataCenter().reg_parmes())
    def add_tel_user(self,userdata):
        """参数区  正向流程：添加手机注册用户--------------------------------------------"""

        wait = int(1)
        re_list = []
        print(userdata)
        #json_save_patch =project_dir[0]
        # 报告生成路径,，取值公共变量中的路径
        json_save_patch =GlobalDict.get_value('project_pwd').get('register_token')

        page_main_url = "https://login.test.gotin.top/login/phone/account"
        page_target_url ='https://create.test.gotin.top/guide/organizer/create'
        GlobalDict.set_value('TelRegister_input', userdata)
        """参数区  正向流程：添加手机注册用户--------------------------------------------"""
        with sync_playwright() as p:

            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            # Go to https://login.test.gotin.top/login/phone/account
            page.goto(page_main_url)
            time.sleep(wait)
            #title1 =page.title()
            #print(title1)
            # Click text=没有账号？去注册
            page.locator("text=没有账号？去注册").click()
            page.wait_for_url(page_main_url)

            # Fill input[type="text"] >> nth=1
            page.locator("input[type=\"text\"]").nth(1).fill(userdata[0])
            page.wait_for_timeout(1000)  #毫秒

            # Click button:has-text("继续")
            page.locator("button:has-text(\"继续\")").click()
            page.wait_for_url("https://login.test.gotin.top/register/phone/detail")
            page.wait_for_timeout(1000)  #毫秒
            # Click input[type="text"] >> nth=0
            # page.locator("input[type=\"text\"]").first.click()
            page.query_selector('//*[@id="app"]/div[2]/div/div/div/div[3]/form/div[1]/div[2]/div/div/div/div/input').click()
            page.query_selector('//*[@id="app"]/div[2]/div/div/div/div[3]/form/div[1]/div[2]/div/div/div/div/input').fill(userdata[1])
            # page.locator("input[type=\"text\"]").first.fill('han')
            page.wait_for_timeout(1000)  #毫秒
            page.locator("input[type=\"text\"]").first.click()
            page.locator("input[type=\"text\"]").first.fill(userdata[2])
            page.wait_for_timeout(1000)  #毫秒
            # Click text=请输入验证码 发送验证码 >> input[type="text"]
            page.locator("text=请输入验证码 发送验证码 >> input[type=\"text\"]").click()
            page.wait_for_timeout(1000)  #毫秒
            # Fill text=请输入验证码 发送验证码 >> input[type="text"]
            page.locator("text=请输入验证码 发送验证码 >> input[type=\"text\"]").fill(userdata[3])
            page.wait_for_timeout(1000)  #毫秒
            # Click input[type="password"]
            page.locator("input[type=\"password\"]").click()
            page.wait_for_timeout(1000)  #毫秒
            # Fill input[type="password"]
            page.locator("input[type=\"password\"]").fill(userdata[4])
            page.wait_for_timeout(1000)  #毫秒
            # Click button:has-text("注册用户")
            page.locator("button:has-text(\"注册用户\")").click()
            page.wait_for_url(page_target_url)
            page.wait_for_timeout(1000)  # 毫秒
            # 进行断言

            assert_url =page.url
            re_list.append(assert_url)
            print(re_list)
            if page_target_url == assert_url :
                print('手机号注册成功')
            else:
                print('手机号注册成功')
            assert page_target_url == page.url
            # 保存状态文件

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

    creat = TelRegister().add_tel_user(DataCenter().reg_parmes())