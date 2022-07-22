import time
from common.DataParmes import DataCenter
from playwright.sync_api import sync_playwright
from common.PageGlobalDict import  GlobalDict
import pytest
import os

class GreateEventReleaseSignUp:

    # 此处构造测试用例所需的数据，
    # 引用声明全局变量
    GlobalDict._init()
    #@pytest.mark.parametrize('userdata',DataCenter().reg_parmes())
    def create_event_release_sign_up(self):
        """参数区  活动报名--------------------------------------------------------------"""

        wait = float(3000)
        create_event_sign_up_list = []
        #print(userdata)

        # 报告生成路径,，取值公共变量中的路径
        json_path =GlobalDict.get_value('project_pwd').get('login_token')

        page_main_url = "https://create.test.gotin.top/myevent/overview"
        page_target_url ='https://nkmkczw.test.gotin.top/newview/home'

        """参数区  活动报名--------------------------------------------------------------"""

        with sync_playwright() as p:

                browser = p.chromium.launch(headless=False)
                context = browser.new_context(storage_state=json_path)
                page = context.new_page()
                # Go to https://login.test.gotin.top/login/phone/account
                page.goto(page_main_url)
                page.wait_for_timeout(wait)
                #title1 =page.title()
                #print(title1)

                page.goto(page_main_url)

                '''---------------------------------------分割线-------------------------------------------'''
                # Go to https://create.test.gotin.top/myevent/overview
                page.goto("https://create.test.gotin.top/myevent/overview")
                # Click text=预览及发布预览您的活动&发布您的活动进入活动 >> button
                with page.expect_popup() as popup_info:
                    page.locator("text=预览及发布预览您的活动&发布您的活动进入活动 >> button").click()
                page1 = popup_info.value
                page1.wait_for_timeout(wait)


                visible = page1.is_visible("text=加入活动")
                print(visible)
                if visible == True:
                    # Click text=中文English进入活动我的活动联系人个人信息语言中文English创建中心退出 >> #head
                    page1.locator("text=加入活动").first.click()

                    page1.wait_for_timeout(wait)
                    page_release_status1 = page1.inner_html("text=报名")
                    create_event_sign_up_list.append(page_release_status1)



                elif  page1.is_visible("text=报名") == True:
                        page1.wait_for_timeout(wait)
                        page1.locator("button:has-text(\"报名\")").click()
                        page_release_status2 = page1.inner_html("text=进入活动")
                        create_event_sign_up_list.append(page_release_status2)
                        '''---------------------------------------分割线-------------------------------------------'''
                        # 进行断言

                        assert_url = page1.url
                        create_event_sign_up_list.append(assert_url)
                        print(create_event_sign_up_list)
                        if   create_event_sign_up_list[0] =='报名' and create_event_sign_up_list[1] =='进入活动':
                            print('报名成功')
                        else:
                            print('报名失败')

                        assert create_event_sign_up_list[0] == '报名'
                        assert create_event_sign_up_list[1] == '进入活动'


                        # 保存状态文件

                        context.storage_state(path=json_path)

                        print(create_event_sign_up_list)
                        context.close()
                        browser.close()
                        return create_event_sign_up_list
                else:
                    page_release_status2 = page1.inner_html("text=进入活动")
                    create_event_sign_up_list.append(page_release_status2)
                    '''---------------------------------------分割线-------------------------------------------'''
                    # 进行断言

                    assert_url = page1.url
                    create_event_sign_up_list.append(assert_url)
                    print(create_event_sign_up_list)
                    if  create_event_sign_up_list[1] == '进入活动':
                        print('报名成功')
                    else:
                        print('报名失败')

                    assert create_event_sign_up_list[1] == '进入活动'

                    # 保存状态文件

                    context.storage_state(path=json_path)

                    print(create_event_sign_up_list)
                    context.close()
                    browser.close()
                    return create_event_sign_up_list








if __name__ == '__main__':
    creat = GreateEventReleaseSignUp().create_event_release_sign_up()