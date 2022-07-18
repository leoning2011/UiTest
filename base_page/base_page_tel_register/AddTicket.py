
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
from data_factory.ProjectDir import UiProjectDri
import time
import pytest
from data_factory.DataParmes import DataCenter
from bs4 import BeautifulSoup
import requests

class AddTicket:
    @pytest.mark.parametrize('userdata', DataCenter().ticket_info())
    def add_ticket(self,ticket_info):
        """  增加门票 """
        re_add_ticket= []
        wait =2
        #浏览器状态存储路径
        project_dir=UiProjectDri.re_project_dir()
        json_save_patch =project_dir[0]
        page_main_url = "https://create.test.gotin.top/guide/event/ticket"
        page_target_url ='https://create.test.gotin.top/myevent/overview'
        print(ticket_info)
        """  增加门票   """

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(storage_state=json_save_patch)
            page = context.new_page()

            '''特殊处理:在主办方信息处，输入新的网址，未能正常实现跳转'''
            # Go to https://create.test.gotin.top/guide/event/session
            page.goto(page_main_url)

            # Click button:has-text("下一步")
            page.locator("button:has-text(\"下一步\")").click()
            page.locator("button:has-text(\"下一步\")").click()
            page.locator("button:has-text(\"下一步\")").click()
            page.wait_for_url(page_main_url)
            time.sleep(wait)

            # Click text=数量/10 >> input[type="text"]
            page.click('xpath=/html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[3]/div/div/div/div/input')
            #page.click('xpath=/html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[3]/div/div/div/div/input')
            time.sleep(2)
            #模拟键盘
            page.type('xpath=/html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[3]/div/div/div/div/input','10', delay=100)
            #page.keyboard('11')
            #page.press('#el-id-9180-65','11')
           #page.press("xpath=/html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[3]/div/div/div/div/input", 'Enter')
            # Click button:has-text("完成")
            page.locator("button:has-text(\"完成\")").click()
            page.wait_for_url(page_target_url)
            time.sleep(wait)

            # Click button:has-text("关闭")
            page.locator("button:has-text(\"关闭\")").click()

            # Click main button:has-text("发布")
            page.locator("main button:has-text(\"发布\")").click()

            html_title =page.inner_html("xpath=/html/body/div[1]/section/section/header/div/div[2]/div[1]/button[2]/span")
            print(html_title)
            assert_url = page.url

            #re_add_ticket.append(assert_url)
            #print(re_add_ticket)
            if page_target_url == assert_url:
                print('门票信息填写完成并发布成功')
            else:
                print('门票信息填写失败')
            assert page_target_url == page.url
            # 保存状态文件
            context.storage_state(path=json_save_patch)


            # 获取当前页面元素，# 获取页面全文
            #html_page_value = page.content()
            page_main_title =page.inner_text("xpath=/html/body/div[1]/section/section/header/div/div[2]/div[1]/button[2]/span")


            re_add_ticket.append(page_main_title)
            print(page_main_title)
            context.close()
            browser.close()

            return re_add_ticket


if __name__ == '__main__':
    add_schedule =AddTicket().add_ticket(DataCenter().ticket_info())
