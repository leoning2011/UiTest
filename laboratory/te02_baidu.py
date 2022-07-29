import time
from pykeyboard import *
from pymouse import *
from common.DataParmes import DataCenter
from playwright.sync_api import sync_playwright
from common.PageGlobalDict import  GlobalDict
import pytest
import os

class GreateEvent:

    # 此处构造测试用例所需的数据，
    # 引用声明全局变量
    GlobalDict._init()
    #@pytest.mark.parametrize('userdata',DataCenter().reg_parmes())
    def baidu(self):
        """参数区  进入活动界面并离开--------------------------------------------------------------"""

        wait = int(1)
        create_event_sign_up_list = []
        #print(userdata)

        # 报告生成路径,，取值公共变量中的路径
        json_path =GlobalDict.get_value('project_pwd').get('login_token')

        page_main_url = "https://baidu.com"


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
                print('1111')
                m =PyMouse()
                k =PyKeyboard()
                m.click(415,230)
                k.tab_key
                time.sleep(1)
                print('22222')


if __name__ == '__main__':
    creat = GreateEvent().baidu()