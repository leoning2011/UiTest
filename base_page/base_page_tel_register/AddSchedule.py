
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
import time
import pytest
from data_factory.DataParmes import DataCenter
from data_factory.ProjectDir import UiProjectDri


class AddSchedule:
    @pytest.mark.parametrize('userdata', DataCenter().schedule_info())
    def add_schedule(self,schedule_info):
        """  增加一个日程 """
        re_add_schedule = []
        wait =1
        print(schedule_info)
        #浏览器状态存储路径
        project_dir=UiProjectDri.re_project_dir()
        json_save_patch =project_dir[0]
        """  增加一个日程   """

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(storage_state=json_save_patch)
            page = context.new_page()

            '''特殊处理:在主办方信息处，输入新的网址，未能正常实现跳转'''
            # Go to https://create.test.gotin.top/guide/event/session
            page.goto("https://create.test.gotin.top/guide/event/session")

            # Click button:has-text("下一步")
            page.locator("button:has-text(\"下一步\")").click()
            page.locator("button:has-text(\"下一步\")").click()
            page.wait_for_url("https://create.test.gotin.top/guide/event/session")
            time.sleep(wait)
            # Click [placeholder="请选择"]
            page.click("[placeholder=\"请选择\"]")
            #page.locator("[placeholder=\"请选择\"]").click()

            # Click li:has-text("论坛")
            page.locator("li:has-text(\"论坛\")").click()

            # 选中主持人
            page.click('xpath=/html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[2]/div[2]/div/div/div/div/input')
            page.click("xpath=/html/body/div[3]/div[2]/div/div/div[1]/ul/li[1]")


            # 场次标题
            page.click('xpath=/html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[3]/div/div[1]/div/div/input')
            page.fill('xpath=/html/body/div[1]/section/section/main/div/div/div[2]/form/div[1]/div/div[3]/div/div[1]/div/div/input',schedule_info[0])


            # Click button:has-text("下一步")
            page.locator("button:has-text(\"下一步\")").click()
            page.wait_for_url("https://create.test.gotin.top/guide/event/ticket")



            url2 = 'https://create.test.gotin.top/guide/event/ticket'

            assert_url = page.url
            re_add_schedule.append(assert_url)
            print(re_add_schedule)
            if url2 == assert_url:
                print('日程信息填写成功')
            else:
                print('日程信息填写失败')
            assert url2 == page.url
            # 保存状态文件
            context.storage_state(path=json_save_patch)
            # 获取当前页面元素，# 获取页面全文
            #html_page_value = page.content()
            page_main_title =page.inner_text("xpath=/html/body/div[1]/section/section/main/div/div/div[1]/div/div[2]")
            re_add_schedule.append(page_main_title)
            print(page_main_title)


            context.close()
            browser.close()

            return re_add_schedule


if __name__ == '__main__':
    add_schedule =AddSchedule().add_schedule(DataCenter().schedule_info())