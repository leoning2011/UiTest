import time
from data_factory.DataParmes import DataCenter
from playwright.sync_api import sync_playwright
from data_factory.PageGlobalDict import  GlobalDict
import pytest
import os

class GreateEventAddAgenda:

    # 此处构造测试用例所需的数据，
    # 引用声明全局变量
    GlobalDict._init()
    #@pytest.mark.parametrize('userdata',DataCenter().reg_parmes())
    def create_event_add_agenda(self):
        """参数区  重置密码--------------------------------------------------------------"""

        wait = int(1)
        create_event_add_guest_list = []
        #print(userdata)

        # 报告生成路径,，取值公共变量中的路径
        json_path =GlobalDict.get_value('project_pwd').get('login_token')

        page_main_url = "https://create.test.gotin.top/myevent/overview"
        page_target_url ='https://create.test.gotin.top/myevent/agenda'

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
                page.wait_for_url("https://create.test.gotin.top/myevent/agenda")
                # Click button:has-text("添加日程")
                page.locator("button:has-text(\"添加日程\")").click()
                page.wait_for_url("https://create.test.gotin.top/myevent/agenda-create")
                # Click [placeholder="请选择"]
                page.locator("[placeholder=\"请选择\"]").click()
                # Click li:has-text("论坛")
                page.locator("li:has-text(\"论坛\")").click()

                # 中文场次标题
                page.fill('xpath=/html/body/div[1]/section/section/main/div[3]/div/form/div[3]/div[1]/div/div/div/input','11111111111')

                # 英文场次标题
                page.fill('xpath=/html/body/div[1]/section/section/main/div[3]/div/form/div[3]/div[2]/div/div[1]/div/input','222222222222')

                # 中文场次简介
                page.locator("text=中文0/5000 >> textarea").fill("3333333333")

                # 英文场次简介
                page.locator("text=英文0/5000 >> textarea").fill("444444444444444444")
                # Click text=+ 添加嘉宾
                page.locator("text=+ 添加嘉宾").click()
                # Click text=嘉宾+ 添加嘉宾 >> [placeholder="请选择"]
                page.locator("text=嘉宾+ 添加嘉宾 >> [placeholder=\"请选择\"]").click()
                # 选择嘉宾
                page.click('xpath=/html/body/div[2]/div[9]/div/div/div[1]/ul/li[1]')
                # 选择主持人
                page.click('xpath=/html/body/div[1]/section/section/main/div[3]/div/form/div[11]/div/div/div/div/div/div/input')
                page.click('xpath=/html/body/div[2]/div[8]/div/div/div[1]/ul/li[2]')
                # 选择场次标签
                page.locator("[placeholder=\"主标签\"]").click()
                # Click text=IT互联网创业科技金融游戏教育电商文娱营销设计地产医疗服务业区块链
                page.locator("text=IT互联网创业科技金融游戏教育电商文娱营销设计地产医疗服务业区块链").click()
                # Click button:has-text("保存")
                page.locator("button:has-text(\"保存\")").click()
                page.wait_for_url("https://create.test.gotin.top/myevent/agenda")
                # Click text=创建成功
                page.locator("text=创建成功").click()
                page_release_status = page.inner_html("text=创建成功")
                create_event_add_guest_list.append(page_release_status)



                '''---------------------------------------分割线-------------------------------------------'''

                # 进行断言

                assert_url = page.url
                create_event_add_guest_list.append(assert_url)
                print(create_event_add_guest_list)
                if page_target_url == assert_url and page_release_status =='创建成功':
                    print('创建成功')
                else:
                    print('创建失败')
                assert page_release_status == '创建成功'
                assert page_target_url == page.url

                # 保存状态文件

                context.storage_state(path=json_path)

                print(create_event_add_guest_list)
                context.close()
                browser.close()
                return create_event_add_guest_list

if __name__ == '__main__':
    creat = GreateEventAddAgenda().create_event_add_agenda()