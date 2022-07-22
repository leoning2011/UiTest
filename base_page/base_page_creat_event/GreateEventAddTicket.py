import time
from common.DataParmes import DataCenter
from playwright.sync_api import sync_playwright
from common.PageGlobalDict import  GlobalDict
import pytest
import os

class GreateEventAddTicket:

    # 此处构造测试用例所需的数据，
    # 引用声明全局变量
    GlobalDict._init()
    #@pytest.mark.parametrize('userdata',DataCenter().reg_parmes())
    def create_event_add_ticket(self):
        """参数区  新增票务--------------------------------------------------------------"""

        wait = int(1)
        create_event_add_ticket_list = []
        #print(userdata)

        # 报告生成路径,，取值公共变量中的路径
        json_path =GlobalDict.get_value('project_pwd').get('login_token')

        page_main_url = "https://create.test.gotin.top/myevent/overview"
        page_target_url ='https://create.test.gotin.top/myevent/overview'

        """参数区  新增票务--------------------------------------------------------------"""

        with sync_playwright() as p:

                browser = p.chromium.launch(headless=False)
                context = browser.new_context(storage_state=json_path)
                page = context.new_page()
                # Go to https://login.test.gotin.top/login/phone/account
                page.goto(page_main_url)
                time.sleep(wait)
                #title1 =page.title()
                #print(title1)

                page.goto(page_main_url)

                '''---------------------------------------分割线-------------------------------------------'''
                # Click button:has-text("添加")
                page.locator("button:has-text(\"添加\")").click()
                time.sleep(1)
                #page.wait_for_url("https://create.test.gotin.top/myevent/ticketform?type=create")

                #page.locator("#el-id-804-30").fill("普通票1")

                #page.locator("#el-id-804-31").fill("Regular2")

                # 请输入价格
                page.locator("[placeholder=\"请输入价格，0为免费票\"]").fill("1")

                #开始日期
                page.fill(
                    'xpath=/html/body/div[1]/section/section/main/div[2]/div[2]/div/form/div[4]/div/div/div/input',
                    '')
                page.fill('xpath=/html/body/div[1]/section/section/main/div[2]/div[2]/div/form/div[4]/div/div/div/input','00:00')
                page.click("text=中文0/500 >> textarea")
                time.sleep(wait)

                # 中文描述
                page.locator("text=中文0/500 >> textarea").click()
                page.locator("text=中文0/500 >> textarea").fill("121311")
                # 英文描述
                page.locator("text=英文0/500 >> textarea").fill("1231321")

                # 保存按钮
                page.locator("button:has-text(\"保存\")").click()
                page.wait_for_url("https://create.test.gotin.top/myevent/overview")

                # Click text=创建成功
                page.locator("text=添加成功").click()
                page_release_status = page.inner_html("text=添加成功")
                create_event_add_ticket_list.append(page_release_status)



                '''---------------------------------------分割线-------------------------------------------'''

                # 进行断言

                assert_url = page.url
                create_event_add_ticket_list.append(assert_url)
                print(create_event_add_ticket_list)
                if page_target_url == assert_url and page_release_status =='添加成功':
                    print('添加成功')
                else:
                    print('添加失败')
                assert page_release_status == '添加成功'
                assert page_target_url == page.url

                # 保存状态文件

                context.storage_state(path=json_path)

                print(create_event_add_ticket_list)
                context.close()
                browser.close()
                return create_event_add_ticket_list

if __name__ == '__main__':
    creat = GreateEventAddTicket().create_event_add_ticket()








