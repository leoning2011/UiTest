




import time
from data_factory.DataParmes import DataCenter
from playwright.sync_api import sync_playwright
from data_factory.PageGlobalDict import  GlobalDict
import pytest
import os

class ResetPassword:

    # 此处构造测试用例所需的数据，
    #data = ['13853867111','leo','wang','12580','123qwe!@#']
    #data =DataCenter().reg_parmes()
    #print(data)
    #print(type(data))
    # 使用pytest.mark.parametrize引入用户数据

    #@pytest.mark.parametrize('userdata',DataCenter().reg_parmes())
    def reset_password(self):
        """参数区  重置密码--------------------------------------------------------------"""

        wait = int(1)
        reset_password_list = []
        #print(userdata)

        #引用声明全局变量
        GlobalDict._init()
        # 报告生成路径,，取值公共变量中的路径
        json_path =GlobalDict.get_value('project_pwd').get('login_token')


        page_main_url = "https://create.test.gotin.top/eventlists"
        page_target_url ='https://personal.test.gotin.top/personal/reset-password'

        """参数区  重置密码--------------------------------------------------------------"""
        with sync_playwright() as p:

            browser = p.chromium.launch(headless=False)
            context = browser.new_context(storage_state=json_path)
            page = context.new_page()
            # Go to https://login.test.gotin.top/login/phone/account
            page.goto(page_main_url)
            time.sleep(wait)
            #title1 =page.title()
            #print(title1)

            page.wait_for_url(page_main_url)

            '''---------------------------------------分割线-------------------------------------------'''
            # Click header img
            page.locator("header img").click()
            # Click text=个人信息
            with page.expect_popup() as popup_info:
                page.locator("text=个人信息").click()
            page1 = popup_info.value
            page1.wait_for_url("https://personal.test.gotin.top/personal/overview?aim=event&lang=cn")
            # Click button:has-text("设置")
            page1.locator("button:has-text(\"设置\")").click()

            page1.wait_for_url("https://personal.test.gotin.top/personal/reset-password")
            # 输入当前密码

            page1.click('xpath=/html/body/div[1]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/input')
            # Fill #el-id-5990-4
            page1.fill('xpath=/html/body/div[1]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/input','123qwe!@#')
            # 点击输入新密码
            page1.locator("text=设置新密码密码至少为8位字符，并同时包含字母和数字 >> input[type=\"password\"]").click()
            # 输入新密码
            page1.locator("text=设置新密码密码至少为8位字符，并同时包含字母和数字 >> input[type=\"password\"]").fill("ccb123qwe!@#")

            #
            page1.click('xpath=/html/body/div[1]/div/div/div/div[2]/div[2]/div/form/div[3]/div/div/div/input')
            # Fill #el-id-5990-6
            page1.fill('xpath=/html/body/div[1]/div/div/div/div[2]/div[2]/div/form/div[3]/div/div/div/input',"ccb123qwe!@#")

            # Press Enter
            page1.locator("button:has-text(\"保存\")").click()


            page1.wait_for_url(page_target_url)

            '''---------------------------------------分割线-------------------------------------------'''
            # 进行断言

            assert_url =page1.url
            reset_password_list.append(assert_url)
            print(reset_password_list)
            if page_target_url == assert_url :
                print('密码重置成功')
            else:
                print('密码重置失败')
            assert page_target_url == assert_url
            # 保存状态文件

            context.storage_state(path=json_path)

            # 获取当前页面元素，# 获取页面全文
            #html_page_value = page.content()
            page1.locator("text=密码重置成功").click()
            page_main_title =page1.inner_html("text=密码重置成功")
            reset_password_list.append(page_main_title)
            print(page_main_title)
            #print(html_page_value)
            #storage = context.storage_state()
            #os.environ["STORAGE"] = json.dumps(storage)

            context.close()
            browser.close()
            GlobalDict.set_value('ResetPassword',reset_password_list)
            return reset_password_list




if __name__ == '__main__':

    creat = ResetPassword().reset_password()