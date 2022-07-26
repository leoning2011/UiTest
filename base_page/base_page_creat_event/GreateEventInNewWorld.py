import time
from common.DataParmes import DataCenter
from playwright.sync_api import sync_playwright
from common.PageGlobalDict import  GlobalDict
import pytest
import os

class GreateEventInNewWorld:

    # 此处构造测试用例所需的数据，
    # 引用声明全局变量
    GlobalDict._init()
    #@pytest.mark.parametrize('userdata',DataCenter().reg_parmes())
    def create_event_in_new_world(self):
        """参数区  进入活动界面并离开--------------------------------------------------------------"""

        wait = int(1)
        create_event_sign_up_list = []
        #print(userdata)

        # 报告生成路径,，取值公共变量中的路径
        json_path =GlobalDict.get_value('project_pwd').get('login_token')

        page_main_url = "https://create.test.gotin.top/myevent/overview"


        """参数区  进入活动界面并离开--------------------------------------------------------------"""

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
                # Click text=预览及发布预览您的活动&发布您的活动进入活动 >> button
                with page.expect_popup() as popup_info:
                    page.locator("text=预览及发布预览您的活动&发布您的活动进入活动 >> button").click()

                time.sleep(wait)

                page1 = popup_info.value
                page1.click('xpath=/html/body/div/div/div[1]/div/div/div[1]/div[1]/div/div/button')
                #page2 = popup_info.value
                page_release_status = page1.inner_html("text=分享")
                create_event_sign_up_list.append(page_release_status)



                '''---------------------------------------分割线-------------------------------------------'''


                # 进行断言

                assert_url = page.url
                create_event_sign_up_list.append(assert_url)
                print(create_event_sign_up_list)
                if  page_release_status =='分享' :
                    print('进入活动成功')
                else:
                    print('进入活动失败')
                assert page_release_status == '分享'


                # 保存状态文件

                context.storage_state(path=json_path)

                print(create_event_sign_up_list)
                context.close()
                browser.close()
                return create_event_sign_up_list

if __name__ == '__main__':
    creat = GreateEventInNewWorld().create_event_in_new_world()