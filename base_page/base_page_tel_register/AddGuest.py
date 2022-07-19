
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
import time
import pytest
from data_factory.DataParmes import DataCenter
from data_factory.PageGlobalDict import GlobalDict

class AddGuest:
    # 引用声明全局变量
    GlobalDict._init()
    @pytest.mark.parametrize('userdata', DataCenter().guest_info())
    def add_guest(self,guestinfo):
        """  添加一个嘉宾 """
        re_add_guest = []
        print(guestinfo)


        # 报告生成路径,，取值公共变量中的路径
        json_save_patch = GlobalDict.get_value('project_pwd').get('register_token')
        """  添加一个嘉宾   """

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(storage_state=json_save_patch)
            page = context.new_page()

            '''特殊处理:在主办方信息处，输入新的网址，未能正常实现跳转'''
            # Go to https://create.test.gotin.top/guide/event/guest
            page.goto("https://create.test.gotin.top/guide/event/guest")
            time.sleep(1)
            # Click button:has-text("下一步")
            page.locator("button:has-text(\"下一步\")").click()
            # Click button:has-text("创建一场活动")

            #嘉宾姓名
            page.click('xpath = /html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[2]/div/div[1]/div/div/input')
            page.fill(
                'xpath = /html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[2]/div/div[1]/div/div/input',guestinfo[0])

            #嘉宾头衔
            page.click('xpath =/html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[3]/div/div/div/div/input')
            page.fill(
                'xpath = /html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[3]/div/div/div/div/input',guestinfo[1])

            #公司或组织
            page.click('xpath =/html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[4]/div/div/div/div/input')
            page.fill(
                'xpath = /html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[4]/div/div/div/div/input',guestinfo[2])


            #手机号
            page.click('xpath =/html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[6]/div[2]/div[2]/div/div[2]/input')
            page.fill(
                'xpath = /html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[6]/div[2]/div[2]/div/div[2]/input',guestinfo[3])


            # Click button:has-text("下一步")
            page.locator("button:has-text(\"下一步\")").click()
            page.wait_for_url("https://create.test.gotin.top/guide/event/session")

            url2 = 'https://create.test.gotin.top/guide/event/session'

            assert_url = page.url
            re_add_guest.append(assert_url)
            print(re_add_guest)
            if url2 == assert_url:
                print('嘉宾信息填写成功')
            else:
                print('嘉宾信息填写失败')
            assert url2 == page.url
            # 保存状态文件
            context.storage_state(path=json_save_patch)

            # 获取当前页面元素，# 获取页面全文
            #html_page_value = page.content()
            page_main_title =page.inner_text("xpath=/html/body/div[1]/section/section/main/div/div/div[1]/div/div[2]")
            re_add_guest.append(page_main_title)
            print(page_main_title)
            context.close()
            browser.close()

            return re_add_guest


if __name__ == '__main__':
    add_sponsor =AddGuest().add_guest(DataCenter().guest_info())