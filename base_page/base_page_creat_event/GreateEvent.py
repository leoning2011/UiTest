

import time
from data_factory.DataParmes import DataCenter
from playwright.sync_api import sync_playwright
from data_factory.PageGlobalDict import  GlobalDict
import pytest
import os

class GreateEvent:

    # 此处构造测试用例所需的数据，
    # 引用声明全局变量
    GlobalDict._init()
    #@pytest.mark.parametrize('userdata',DataCenter().reg_parmes())
    def create_event(self):
        """参数区  重置密码--------------------------------------------------------------"""

        wait = int(1)
        create_event_list = []
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
                # 中文标题
                page.fill('xpath=/html/body/div[1]/section/section/main/div[2]/div/form/div[2]/div[1]/div/div[1]/div/input','123')
                #英文标题
                page.fill('xpath=/html/body/div[1]/section/section/main/div[2]/div/form/div[2]/div[2]/div/div[1]/div/input','1231')
                # 中文详情
                page.locator("text=中文0/1500 >> textarea").click()
                # Fill text=中文0/1500 >> textarea
                page.locator("text=中文0/1500 >> textarea").fill("12121")
                # # 英文详情
                page.locator("text=英文0/1500 >> textarea").click()
                # Fill text=英文0/1500 >> textarea
                page.locator("text=英文0/1500 >> textarea").fill("1212")
                # Click div:nth-child(11) > .el-form-item__content > div > .select-trigger > .el-input > .el-input__wrapper > .el-input__suffix > .el-input__suffix-inner > .el-icon > svg >> nth=0
                page.locator(
                    "div:nth-child(11) > .el-form-item__content > div > .select-trigger > .el-input > .el-input__wrapper > .el-input__suffix > .el-input__suffix-inner > .el-icon > svg").first.click()
                # Click li:has-text("创业")
                page.locator("li:has-text(\"创业\")").click()


                # Click button:has-text("创建活动")
                page.locator("button:has-text(\"创建活动\")").click()
                page.wait_for_url("https://create.test.gotin.top/myevent/overview")

                page_release_status = page.inner_html("text=创建成功")
                create_event_list.append(page_release_status)

                '''---------------------------------------分割线-------------------------------------------'''

                # 进行断言

                assert_url = page.url
                create_event_list.append(assert_url)

                if page_target_url == assert_url and page_release_status =='创建成功':
                    print('大会创建成功')
                else:
                    print('大会创建失败')
                assert page_target_url == page.url
                assert page_release_status =='创建成功'
                # 保存状态文件

                context.storage_state(path=json_path)

                print(create_event_list)
                context.close()
                browser.close()
                return create_event_list

if __name__ == '__main__':

    creat = GreateEvent().create_event()