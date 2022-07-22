

from base_page.base_page_creat_event.GreateEvent import GreateEvent
from base_page.base_page_creat_event.GreateEventAddGuest import GreateEventAddGuest
from base_page.base_page_creat_event.GreateEventAddAgenda import GreateEventAddAgenda
from base_page.base_page_creat_event.GreateEventAddTicket import GreateEventAddTicket
from base_page.base_page_creat_event.GreateEventRelease import GreateEventRelease
from base_page.base_page_creat_event.GreateEventReleaseSignUp import GreateEventReleaseSignUp
from base_page.base_page_creat_event.GreateEventInNewWorld import GreateEventInNewWorld
from common.PageGlobalDict import GlobalDict
import pytest

class TestUnifiedCreateEventAssert:

    # 引用声明全局变量
    GlobalDict._init()

    #@pytest.fixture(scope='class')
    def test_assert_create_event(self):

        reg_create_event =GreateEvent().create_event()
        print('--第1步--------------------------------创建大会--------------------------')
        print(reg_create_event)

        #common_dict = GlobalDict.get_value('ResetPassword')
        #print(common_dict)
        assert reg_create_event[0] == '创建成功'
        assert reg_create_event[1] == 'https://create.test.gotin.top/myevent/overview'


    def test_assert_create_event_add_guest(self):

        reg_add_guest =GreateEventAddGuest().create_event_add_guest()
        print('--第2步----------------创建大会------------添加嘉宾------------------------')
        print(reg_add_guest)

        #common_dict = GlobalDict.get_value('ResetPassword')
        #print(common_dict)
        assert reg_add_guest[0] == '添加成功'
        assert reg_add_guest[1] == 'https://create.test.gotin.top/myevent/guest-list'


    def test_assert_create_event_add_agenda(self):

        reg_add_agenda =GreateEventAddAgenda().create_event_add_agenda()
        print('--第3步----------------创建大会------------添加日程------------------------')
        print(reg_add_agenda)

        #common_dict = GlobalDict.get_value('ResetPassword')
        #print(common_dict)
        assert reg_add_agenda[0] == '创建成功'
        assert reg_add_agenda[1] == 'https://create.test.gotin.top/myevent/agenda'

    def test_assert_create_event_add_ticket(self):
        reg_add_ticket = GreateEventAddTicket().create_event_add_ticket()
        print('--第4步----------------创建大会------------添加票务------------------------')
        print(reg_add_ticket)

        # common_dict = GlobalDict.get_value('ResetPassword')
        # print(common_dict)
        assert reg_add_ticket[0] == '添加成功'
        assert reg_add_ticket[1] == 'https://create.test.gotin.top/myevent/overview'

    def test_assert_create_event_release(self):
        reg_event_release = GreateEventRelease().create_event_release()
        print('--第5步----------------创建大会------------预览及发布------------------------')
        print(reg_event_release)

        # common_dict = GlobalDict.get_value('ResetPassword')
        # print(common_dict)
        assert reg_event_release[0] == '发布成功'
        assert reg_event_release[1] == '已发布'
        assert reg_event_release[2] == 'https://create.test.gotin.top/myevent/overview'

    def test_assert_create_event_release_singup(self):
        reg_event_release_singup = GreateEventReleaseSignUp().create_event_release_sign_up()
        print('--第6步----------------创建大会------------报名------------------------')
        print(reg_event_release_singup)

        # common_dict = GlobalDict.get_value('ResetPassword')
        # print(common_dict)
        assert reg_event_release_singup[0] == '报名'
        assert reg_event_release_singup[1] == '进入活动'



    def test_assert_create_event_release_in_new_world(self):
        reg_event_release_in_new_world = GreateEventInNewWorld().create_event_in_new_world()
        print('--第7步----------------创建大会-----报名成功后进入活动并离开--------------')
        print(reg_event_release_in_new_world)

        # common_dict = GlobalDict.get_value('ResetPassword')
        # print(common_dict)
        assert reg_event_release_in_new_world[0] == '分享'


if __name__ == '__main__':
    #ss =TestUnifiedLoginAssert().test_assert_verif_code_login()
    pytest.main(['-v', '-s', 'test_assert_create_event.py', "--html=./report/report.html"])



