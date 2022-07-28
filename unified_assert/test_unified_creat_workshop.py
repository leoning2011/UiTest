

from base_page.base_page_creat_workshop import GreateWorkshop
from common.PageGlobalDict import GlobalDict
from common.ApiToken import ApiResponse
import pytest

class TestUnifiedCreateWorkshopAssert:

    # 引用声明全局变量
    GlobalDict._init()

    def test_work_add_traffic(self):
        add_traffic =ApiResponse().add_traffic()
        print('--初始化数据------------------------------给被测方赠送流量包---------------')
        print(add_traffic)
        assert add_traffic == 'success'

    #@pytest.fixture(scope='class')
    def test_assert_create_workshop(self):

        reg_create_workshop =GreateWorkshop().create_workshop()
        print('--第1步--------------------------------创建工作坊--------------------------')
        print(reg_create_workshop)

        #common_dict = GlobalDict.get_value('ResetPassword')
        #print(common_dict)
        assert reg_create_workshop[0] == '创建成功'
        assert reg_create_workshop[1] == '发布成功'
        assert reg_create_workshop[2] == 'https://create.test.gotin.top/myevent/overview'

if __name__ == '__main__':
    #ss =TestUnifiedLoginAssert().test_assert_verif_code_login()
    pytest.main(['-v', '-s', 'test_assert_create_workshop.py', "--html=./report/report.html"])



