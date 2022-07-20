

import time
from data_factory.DataParmes import DataCenter
from playwright.sync_api import sync_playwright
from data_factory.PageGlobalDict import  GlobalDict
import pytest
import os

class GreateWorkshop:

    # 此处构造测试用例所需的数据，
    # 引用声明全局变量
    GlobalDict._init()
    #@pytest.mark.parametrize('userdata',DataCenter().reg_parmes())
    def create_workshop(self):
        """参数区  重置密码--------------------------------------------------------------"""

        wait = int(1)
        create_workshop_list = []
        #print(userdata)

        # 报告生成路径,，取值公共变量中的路径
        json_path =GlobalDict.get_value('project_pwd').get('login_token')

        page_main_url = "https://create.test.gotin.top/eventlists"
        page_target_url ='https://create.test.gotin.top/myevent/overview'

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

                # Click button:has-text("创建活动")
                page.locator("button:has-text(\"创建活动\")").click()
                # Click text=举办一场大会
                page.locator("text=举办一场大会").click()
                page.wait_for_url("https://create.test.gotin.top/create/event")
                # 选择中英双语
                page.locator("label:nth-child(3) > .el-radio__input > .el-radio__inner").click()
                time.sleep(1)
                # Click #el-id-8853-261
                page.locator("#el-id-8853-261").click()
                # Click #el-id-8853-261
                page.locator("#el-id-8853-261").click()
                # Fill #el-id-8853-261
                page.locator("#el-id-8853-261").fill("1212")
                # Click #el-id-8853-262
                page.locator("#el-id-8853-262").click()
                # Fill #el-id-8853-262
                page.locator("#el-id-8853-262").fill("1212")
                # Click text=中文0/1500 >> textarea
                page.locator("text=中文0/1500 >> textarea").click()
                # Click text=中文0/1500 >> textarea
                page.locator("text=中文0/1500 >> textarea").click()
                # Fill text=中文0/1500 >> textarea
                page.locator("text=中文0/1500 >> textarea").fill("12121")
                # Click text=英文0/1500 >> textarea
                page.locator("text=英文0/1500 >> textarea").click()
                # Fill text=英文0/1500 >> textarea
                page.locator("text=英文0/1500 >> textarea").fill("1212")
                # Click div:nth-child(11) > .el-form-item__content > div > .select-trigger > .el-input > .el-input__wrapper > .el-input__suffix > .el-input__suffix-inner > .el-icon > svg >> nth=0
                page.locator(
                    "div:nth-child(11) > .el-form-item__content > div > .select-trigger > .el-input > .el-input__wrapper > .el-input__suffix > .el-input__suffix-inner > .el-icon > svg").first.click()
                # Click li:has-text("创业")
                page.locator("li:has-text(\"创业\")").click()
                # Click div:nth-child(2) > .el-input__wrapper > .el-input__suffix > .el-input__suffix-inner > .el-icon > svg
                page.locator(
                    "div:nth-child(2) > .el-input__wrapper > .el-input__suffix > .el-input__suffix-inner > .el-icon > svg").click()
                # Click [placeholder="主标签"]
                page.locator("[placeholder=\"主标签\"]").click()
                # Click li:has-text("IT互联网")
                page.locator("li:has-text(\"IT互联网\")").click()
                # Click .el-select__input
                page.locator(".el-select__input").click()
                # Click .el-select__input
                page.locator(".el-select__input").click()
                # Click button:has-text("创建活动")
                page.locator("button:has-text(\"创建活动\")").click()
                page.wait_for_url("https://create.test.gotin.top/myevent/overview")

                '''---------------------------------------分割线-------------------------------------------'''

                # 进行断言

                assert_url = page.url
                create_workshop_list.append(assert_url)
                print(create_workshop_list)
                if page_target_url == assert_url:
                    print('工作坊创建成功')
                else:
                    print('工作坊创建失败')
                assert page_target_url == page.url
                # 保存状态文件

                context.storage_state(path=json_path)

                #print(create_workshop_list)
                context.close()
                browser.close()
                return create_workshop_list

if __name__ == '__main__':

    creat = GreateWorkshop().create_workshop()