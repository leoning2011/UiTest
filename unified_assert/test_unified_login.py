

from base_page.base_page_login.TelPasswordLogin import TelPasswordLogin
from base_page.base_page_login import TelVerifCodeLogin
from data_factory.PageGlobalDict import GlobalDict
import pytest

class TestUnifiedLoginAssert:
    #登录流程
    def test_assert_password_login(self):
        reg_password_login =TelPasswordLogin().tel_password_login()
        print('--第1步----------------手机号、密码登录流程进行中----------登录中------------')
        print(reg_password_login)
        assert reg_password_login[0] == 'https://create.test.gotin.top/eventlists'
        assert reg_password_login[1] == '添加主办方'

    def test_assert_verif_code_login(self):
        reg_verif_code_login =TelVerifCodeLogin().tel_verif_code_login()
        print('--第2步----------------手机号、验证码登录流程进行中----------登录中------------')
        print(reg_verif_code_login)
        assert reg_verif_code_login[0] == 'https://create.test.gotin.top/eventlists'
        assert reg_verif_code_login[1] == '添加主办方'


if __name__ == '__main__':
    #ss =TestUnifiedLoginAssert().test_assert_verif_code_login()
    path =GlobalDict().page_global_dict()
    new_report =path['report_path']

    pytest.main(['-v', '-s', 'test_unified_login.py', "--html=./report/report.html"])



