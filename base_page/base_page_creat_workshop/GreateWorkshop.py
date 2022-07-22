

import time
from common.DataParmes import DataCenter
from playwright.sync_api import sync_playwright
from common.PageGlobalDict import  GlobalDict
import pytest
import os

class GreateWorkshop:

    # 此处构造测试用例所需的数据，
    # 引用声明全局变量
    GlobalDict._init()
    #@pytest.mark.parametrize('userdata',DataCenter().reg_parmes())
    def create_workshop(self):
        """参数区  重置密码--------------------------------------------------------------"""

        wait = int(1)
        create_workshop_list = []
        #print(userdata)

        # 报告生成路径,，取值公共变量中的路径
        json_path =GlobalDict.get_value('project_pwd').get('login_token')

        page_main_url = "https://create.test.gotin.top/eventlists"
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

                page.wait_for_url(page_main_url)

                '''---------------------------------------分割线-------------------------------------------'''

                # Click div:has-text("大会彩虹传媒有限公司的活动7月19日 0:00 至 7月21日 0:00已发布复制链接管理进入活动") >> nth=2
                page.locator("div:has-text(\"大会彩虹传媒有限公司的活动7月19日 0:00 至 7月21日 0:00已发布复制链接管理进入活动\")").nth(2).click()
                # Click button:has-text("创建活动")
                page.locator("button:has-text(\"创建活动\")").click()
                # Click text=组织一场研讨会
                page.locator("text=组织一场研讨会").click()
                page.wait_for_url("https://create.test.gotin.top/create/workshop")

                # 选择语种
                page.locator("label:nth-child(3) > .el-radio__input > .el-radio__inner").click()
                time.sleep(2)
                # 填写中文标题
                page.click('xpath=/html/body/div[1]/section/section/main/div[2]/div/form/div[2]/div[1]/div/div[1]/div/input')
                page.fill('xpath=/html/body/div[1]/section/section/main/div[2]/div/form/div[2]/div[1]/div/div[1]/div/input','战斗天使')
                # 填写英文标题
                page.click('xpath=/html/body/div[1]/section/section/main/div[2]/div/form/div[2]/div[2]/div/div[1]/div/input')
                page.fill('xpath=/html/body/div[1]/section/section/main/div[2]/div/form/div[2]/div[2]/div/div[1]/div/input','Battle Angel Alitalia')

                # 从英文标题切换到中文详情

                page.locator('xpath=/html/body/div[1]/section/section/main/div[2]/div/form/div[2]/div[2]/div/div[1]/div/input').press("Tab")
                # 模拟键盘输入
                page.keyboard.press('1')
                # 中文详情切换到英文详情
                page.locator('xpath=/html/body/div[1]/section/section/main/div[2]/div/form/div[4]/div[1]/div[1]').press("Tab")
                # 模拟键盘输入
                page.keyboard.press('1')
                # 英文详情切换到时区
                page.locator('xpath=/html/body/div[1]/section/section/main/div[2]/div/form/div[4]/div[2]/div[1]').press("Tab")
                # 选择时区
                page.click("xpath=/html/body/div[1]/section/section/main/div[2]/div/form/div[9]/div/div/div/div/div/input")
                #page.locator("li:has-text(\"北京，新加坡，香港 (+08:00)\")").click()
                page.locator("text=叶卡捷琳堡，伊斯兰堡 (+05:00)").click()
                # 添加主持人
                page.click('xpath=/html/body/div[1]/section/section/main/div[2]/div/form/div[10]/div/div/div/div/div/div/input')
                page.click('xpath=/html/body/div[3]/div[6]/div/div/div[1]/ul/li/div')
                # Click [placeholder="请输入价格，0为免费票"]
                page.locator("[placeholder=\"请输入价格，0为免费票\"]").click()
                # Fill [placeholder="请输入价格，0为免费票"]
                page.locator("[placeholder=\"请输入价格，0为免费票\"]").fill("10")
                # Click button:has-text("创建工作坊")
                page.locator("button:has-text(\"创建工作坊\")").click()
                page.wait_for_url("https://create.test.gotin.top/myevent/overview")
                # Click div[role="alert"]:has-text("创建成功")
                page.locator("div[role=\"alert\"]:has-text(\"创建成功\")").click()
                page_suc_title = page.inner_html("text=创建成功")
                create_workshop_list.append(page_suc_title)
                # Click button:has-text("发布")
                page.locator("button:has-text(\"发布\")").click()
                # Click div[role="alert"]:has-text("发布成功")
                page.locator("div[role=\"alert\"]:has-text(\"发布成功\")").click()
                page_release_title = page.inner_html("text=发布成功")
                create_workshop_list.append(page_release_title)

                '''---------------------------------------分割线-------------------------------------------'''

                # 进行断言

                assert_url = page.url
                create_workshop_list.append(assert_url)
                print(create_workshop_list)
                if page_target_url == assert_url:
                    print('工作坊创建成功')
                else:
                    print('工作坊创建失败')
                assert page_target_url == page.url
                # 保存状态文件

                context.storage_state(path=json_path)

                #print(create_workshop_list)
                context.close()
                browser.close()
                return create_workshop_list

if __name__ == '__main__':

    creat = GreateWorkshop().create_workshop()