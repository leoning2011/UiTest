


from playwright.sync_api import sync_playwright



class EmailRegister1:

    # 此处构造测试用例所需的数据，


    def add_email_user1(self):
        """参数区  正向流程：添加邮箱注册用户--------------------------------------------"""
        page_main_url ='https://login.test.gotin.top/login/phone/account'
        wait = float(3000)
        email_re_list = []


        with sync_playwright() as p:

            browser = p.chromium.launch(headless=False)
            context = browser.new_context( proxy={"server": "http://192.168.0.132:8888/", "bypass": " ", "username": "", "password": ""})
            page = context.new_page()
            # Go to https://login.test.gotin.top/login/phone/account
            page.goto(page_main_url)



            page.wait_for_timeout(wait)

            page.locator("text=邮箱").click()
            page.locator("input[type=\"text\"]").fill('123131@13.com')

            # Click button:has-text("继续")
            page.locator("text=没有账号？去注册").click()


            ti = page.title()
            print(ti)
            print(ti)
            page.wait_for_timeout(5000)

            # Click text=没有账号？去注册
            page.locator("text=没有账号？去注册").click()
            page.wait_for_url("https://login.test.gotin.top/register/email/account")
            # Click button:has-text("继续")
            page.locator("button:has-text(\"继续\")").click()
            page.wait_for_url("https://login.test.gotin.top/register/email/detail")
            # Fill input[type="text"] >> nth=1
            page.locator("input[type=\"text\"]").nth(1).fill('11')
            # Press Tab
            page.locator("input[type=\"text\"]").nth(1).press("Tab")
            # Fill input[type="text"] >> nth=0
            page.locator("input[type=\"text\"]").first.fill('122')
            # Click input[type="password"]
            page.locator("input[type=\"password\"]").click()


if __name__ == '__main__':
    EmailRegister1().add_email_user1()