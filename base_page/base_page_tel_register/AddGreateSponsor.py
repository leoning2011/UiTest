
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
import time
import pytest
from data_factory.DataParmes import DataCenter
from data_factory.PageGlobalDict import GlobalDict

class GreateSponsor:
    # 引用声明全局变量
    GlobalDict._init()


    @pytest.mark.parametrize('userdata', DataCenter().sponsor_info())
    def add_sponsor(self,sponsor_info):
        """  正向流程：首先，您需要创建一个主办方 """
        #wait = int(1)
        re_add_sponsor = []
        print(sponsor_info)


        # 报告生成路径,，取值公共变量中的路径
        json_save_patch = GlobalDict.get_value('project_pwd').get('register_token')
        """  正向流程：首先，您需要创建一个主办方   """

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(storage_state=json_save_patch)
            page = context.new_page()

            # Go to https://create.test.gotin.top/guide/organizer/create
            page.goto("https://create.test.gotin.top/guide/organizer/create")

            # Fill 填写主办方名称
            # /html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[1]/div/div[1]/div/div/input
            page.click(
                'xpath=/html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[1]/div/div[1]/div/div/input')
            page.fill(
                'xpath=/html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[1]/div/div[1]/div/div/input',
                sponsor_info[0])


            #主办方邮箱

            page.click(
                'xpath=/html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[2]/div/div[1]/div/div/input')
            page.fill(
                'xpath=/html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[2]/div/div[1]/div/div/input',
                sponsor_info[1])

            # Click textarea 填写关于
            page.locator("textarea").click()
            page.locator("textarea").fill(sponsor_info[2])

            # Click button:has-text("下一步")
            page.locator("button:has-text(\"下一步\")").click()
            page.wait_for_url("https://create.test.gotin.top/guide/organizer/survey")
            url2 = 'https://create.test.gotin.top/guide/organizer/survey'

            assert_url = page.url
            re_add_sponsor.append(assert_url)
            print(re_add_sponsor)
            if url2 == assert_url:
                print('主办方信息填写成功')
            else:
                print('主办方信息填写失败')
            assert url2 == page.url

            # 获取当前页面元素，# 获取页面全文
            #html_page_value = page.content()
            page_main_title =page.inner_text("xpath=/html/body/div[1]/section/section/main/div/div/div[1]/div/div[2]")
            re_add_sponsor.append(page_main_title)
            print(page_main_title)
            # 保存状态文件
            context.storage_state(path=json_save_patch)
            context.close()
            browser.close()

            return re_add_sponsor



if __name__ == '__main__':
    add_sponsor =GreateSponsor().add_sponsor(DataCenter().sponsor_info())