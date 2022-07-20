

from base_page.base_page_reset_password.ResetPassword import ResetPassword
from base_page.base_page_login.TelVerifCodeLogin import TelVerifCodeLogin
from data_factory.PageGlobalDict import GlobalDict
import pytest

class TestUnifiedResetPasswordAssert:
    #登录流程
    # 引用声明全局变量
    GlobalDict._init()

    #@pytest.fixture(scope='class')
    def test_assert_reset_password(self):

        reg_reset_password =ResetPassword().reset_password()
        print('--第1步--------------------------------重置密码--------------------------')
        print(reg_reset_password)

        common_dict = GlobalDict.get_value('ResetPassword')
        print(common_dict)
        assert common_dict[0] == '密码重置成功'


if __name__ == '__main__':
    #ss =TestUnifiedLoginAssert().test_assert_verif_code_login()
    pytest.main(['-v', '-s', 'test_unified_reset_password.py', "--html=./report/report.html"])



