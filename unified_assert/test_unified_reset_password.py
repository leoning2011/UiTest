

from base_page.base_page_reset_password.ResetPassword import ResetPassword
from base_page.base_page_login.TelVerifCodeLogin import TelVerifCodeLogin
import pytest

class TestUnifiedResetPasswordAssert:
    #登录流程

    #@pytest.fixture(scope='class')
    def test_assert_verif_code_login(self):
        reg_verif_code_login =TelVerifCodeLogin().tel_verif_code_login()
        print('--第1步----------------手机号、验证码登录流程进行中----------登录中------------')
        print(reg_verif_code_login)
        assert reg_verif_code_login[0] == 'https://create.test.gotin.top/eventlists'
        assert reg_verif_code_login[1] == '登录成功'

    #@pytest.fixture(scope='class')
    def test_assert_reset_password(self):
        reg_reset_password =ResetPassword().reset_password()
        print('--第2步--------------------------------重置密码--------------------------')
        print(reg_reset_password)
        assert reg_reset_password[0] == 'https://personal.test.gotin.top/personal/reset-password'
        assert reg_reset_password[1] == '密码重置成功'


if __name__ == '__main__':
    #ss =TestUnifiedLoginAssert().test_assert_verif_code_login()
    pytest.main(['-v', '-s', 'test_unified_reset_password.py', "--html=./report/report.html"])



