import time
from data_factory.DataParmes import DataCenter
from playwright.sync_api import sync_playwright
from data_factory.PageGlobalDict import  GlobalDict
import pytest
import os

class GreateEventRelease:

    # 此处构造测试用例所需的数据，
    # 引用声明全局变量
    GlobalDict._init()
    #@pytest.mark.parametrize('userdata',DataCenter().reg_parmes())
    def create_event_release(self):
        """参数区  重置密码--------------------------------------------------------------"""

        wait = int(1)
        create_event_release_list = []
        #print(userdata)

        # 报告生成路径,，取值公共变量中的路径
        json_path =GlobalDict.get_value('project_pwd').get('login_token')

        page_main_url = "https://create.test.gotin.top/myevent/overview"
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

                page.goto(page_main_url)

                '''---------------------------------------分割线-------------------------------------------'''

                # Click main button:has-text("发布")
                page.locator("main button:has-text(\"发布\")").click()
                # Click text=发布成功

                page_release_status = page.inner_html("text=发布成功")
                create_event_release_list.append(page_release_status)
                # Click button:has-text("已发布")
                page.locator("button:has-text(\"已发布\")").click()
                event_status = page.inner_html("text=已发布")
                create_event_release_list.append(event_status)



                '''---------------------------------------分割线-------------------------------------------'''


                # 进行断言

                assert_url = page.url
                create_event_release_list.append(assert_url)
                print(create_event_release_list)
                if page_target_url == assert_url and page_release_status =='发布成功':
                    print('发布成功')
                else:
                    print('发布失败')
                assert page_release_status == '发布成功'
                assert event_status == '已发布'
                assert page_target_url == page.url

                # 保存状态文件

                context.storage_state(path=json_path)

                print(create_event_release_list)
                context.close()
                browser.close()
                return create_event_release_list

if __name__ == '__main__':
    creat = GreateEventRelease().create_event_release()