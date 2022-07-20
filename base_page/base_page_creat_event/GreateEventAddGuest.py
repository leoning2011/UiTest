import time
from data_factory.DataParmes import DataCenter
from playwright.sync_api import sync_playwright
from data_factory.PageGlobalDict import  GlobalDict
import pytest
import os

class GreateEventAddGuest:

    # 此处构造测试用例所需的数据，
    # 引用声明全局变量
    GlobalDict._init()
    #@pytest.mark.parametrize('userdata',DataCenter().reg_parmes())
    def create_event_add_guest(self):
        """参数区  重置密码--------------------------------------------------------------"""

        wait = int(1)
        create_event_add_guest_list = []
        #print(userdata)

        # 报告生成路径,，取值公共变量中的路径
        json_path =GlobalDict.get_value('project_pwd').get('login_token')

        page_main_url = "https://create.test.gotin.top/myevent/overview"
        page_target_url ='https://create.test.gotin.top/myevent/guest-list'

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

                # Click button:has-text("添加")
                page.locator("button:has-text(\"添加\")").click()
                page.wait_for_url("https://create.test.gotin.top/myevent/guest-list")
                # Click button:has-text("添加嘉宾")
                page.locator("button:has-text(\"添加嘉宾\")").click()
                time.sleep(1)
                # 中文姓名
                page.fill('xpath=/html/body/div[1]/section/section/main/div[3]/div/form/div[2]/div[1]/div[1]/div/div/div[1]/div/input','111111')
                # 英文姓名
                page.fill('xpath=/html/body/div[1]/section/section/main/div[3]/div/form/div[2]/div[1]/div[2]/div/div/div[1]/div/input','222222')
                # 中文头衔
                page.fill('xpath=/html/body/div[1]/section/section/main/div[3]/div/form/div[2]/div[2]/div[1]/div/div/div/div/input','333333333')
                # 英文头衔
                page.fill('xpath=/html/body/div[1]/section/section/main/div[3]/div/form/div[2]/div[2]/div[2]/div/div/div/div/input','444444444444')
                # 中文-公司名称
                page.fill('xpath=/html/body/div[1]/section/section/main/div[3]/div/form/div[3]/div[1]/div/div/div/input','555555555')
                # 英文-公司名称
                page.fill('xpath=/html/body/div[1]/section/section/main/div[3]/div/form/div[3]/div[2]/div/div/div/input','66666666666666')
                # 中文简介
                page.locator("text=中文0/500 >> textarea").fill("7777777777777")

                #英文简介
                page.locator("text=英文0/500 >> textarea").fill("8888888888888")
                #手机号
                page.fill('xpath=/html/body/div[1]/section/section/main/div[3]/div/form/div[6]/div[2]/div/div[2]/input','12310241015')
                # Click button:has-text("保存")
                page.locator("button:has-text(\"保存\")").click()
                page.wait_for_url("https://create.test.gotin.top/myevent/guest-list")

                # 获取添加状态

                page_release_status = page.inner_html("text=添加成功")
                create_event_add_guest_list.append(page_release_status)
                print(create_event_add_guest_list)

                '''---------------------------------------分割线-------------------------------------------'''

                # 进行断言

                assert_url = page.url
                create_event_add_guest_list.append(assert_url)
                print(create_event_add_guest_list)
                if page_target_url == assert_url and page_release_status =='添加成功':
                    print('添加成功')
                else:
                    print('添加失败')
                assert page_release_status == '添加成功'
                assert page_target_url == page.url
                # 保存状态文件

                context.storage_state(path=json_path)

                print(create_event_add_guest_list)
                context.close()
                browser.close()
                return create_event_add_guest_list

if __name__ == '__main__':
    creat = GreateEventAddGuest().create_event_add_guest()