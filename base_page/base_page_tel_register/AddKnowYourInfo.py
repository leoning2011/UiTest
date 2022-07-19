
from playwright.sync_api import sync_playwright
import time
import pytest
from data_factory.PageGlobalDict import GlobalDict
from data_factory.ProjectDir import UiProjectDri

class KnowYourInfo:
    # 引用声明全局变量
    GlobalDict._init()
    #@pytest.mark.parametrize('userdata', DataCenter().sponsor_info())
    def add_your_info(self):
        """  正向流程：让我们了解您 """
        re_know_info = []
        # 报告生成路径,，取值公共变量中的路径
        json_save_patch = GlobalDict.get_value('project_pwd').get('register_token')
        """  正向流程：让我们了解您   """

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(storage_state=json_save_patch)
            page = context.new_page()

            '''特殊处理:在主办方信息处，输入新的网址，未能正常实现跳转'''
            # Go to https://create.test.gotin.top/guide/organizer/survey
            page.goto("https://create.test.gotin.top/guide/organizer/survey")
            # Click button:has-text("下一步")
            page.locator("button:has-text(\"下一步\")").click()
            page.click(
                'xpath=/html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[1]/div/div/div/div/div/input')

            # Click li:has-text("大学或教育机构")
            page.locator("li:has-text(\"大学或教育机构\")").click()

            # Click input[type="text"] >> nth=1
            page.locator("input[type=\"text\"]").nth(1).click()

            # Click li:has-text("大会")
            page.locator("li:has-text(\"大会\")").click()

            # Click li:has-text("论坛")
            page.locator("li:has-text(\"论坛\")").click()

            # Click li:has-text("社区组织见面会")
            page.locator("li:has-text(\"社区组织见面会\")").click()

            # Click li:has-text("展销博览会")
            page.locator("li:has-text(\"展销博览会\")").click()

            # Click li:has-text("社交活动或混合活动")
            page.locator("li:has-text(\"社交活动或混合活动\")").click()

            # Click li:has-text("研讨会、课程或培训")
            page.locator("li:has-text(\"研讨会、课程或培训\")").click()

            # Click text=让我们了解您
            page.locator("text=让我们了解您").click()

            # Click div:has-text("以下哪个描述最贴合您的主办方？您计划举办哪种类型的活动？大会论坛社区组织见面会展销博览会社交活动或混合活动研讨会、课程或培训您举办活动的频率是？上一步下一步") >> nth=3
            page.locator(
                "div:has-text(\"以下哪个描述最贴合您的主办方？您计划举办哪种类型的活动？大会论坛社区组织见面会展销博览会社交活动或混合活动研讨会、课程或培训您举办活动的频率是？上一步下一步\")").nth(
                3).click()

            # Click text=每年举办几次
            page.locator("text=每年举办几次").click()

            # Click button:has-text("下一步")
            page.locator("button:has-text(\"下一步\")").click()
            page.wait_for_url("https://create.test.gotin.top/eventlists")
            assert_url1 = page.url
            re_know_info.append(assert_url1)

            # Click button:has-text("创建一场活动")
            page.locator("button:has-text(\"创建一场活动\")").click()
            page.wait_for_url("https://create.test.gotin.top/guide/event/baseinfo")

            # Click button:has-text("下一步")
            page.locator("button:has-text(\"下一步\")").click()
            page.wait_for_url("https://create.test.gotin.top/guide/event/guest")

            url2 = 'https://create.test.gotin.top/guide/event/guest'

            assert_url2 = page.url
            re_know_info.append(assert_url2)
            print(re_know_info)
            if url2 == assert_url2 and assert_url1 == assert_url1 :
                print('主办方信息填写成功')
            else:
                print('主办方信息填写失败')
            assert url2 == page.url
            # 保存状态文件
            context.storage_state(path=json_save_patch)


            # 获取当前页面元素，# 获取页面全文
            #html_page_value = page.content()
            page_main_title =page.inner_text("xpath=/html/body/div[1]/section/section/main/div/div/div[1]/div/div[2]")
            re_know_info.append(page_main_title)
            print(page_main_title)

            context.close()
            browser.close()

            return re_know_info


if __name__ == '__main__':
    add_sponsor =KnowYourInfo().add_your_info()