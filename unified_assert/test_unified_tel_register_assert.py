from base_page.base_page_tel_register.TelRegister import TelRegister
from base_page.base_page_tel_register.AddGreateSponsor import  GreateSponsor
from base_page.base_page_tel_register.AddKnowYourInfo import KnowYourInfo
from base_page.base_page_tel_register.AddGuest import AddGuest
from base_page.base_page_tel_register.AddSchedule import AddSchedule
from base_page.base_page_tel_register.AddTicket import AddTicket
from common.DataParmes import DataCenter
import pytest

class TestUnifiedTelRegisterAssert:

    def test_assert_tel_user(self):
        reg_tel_user =TelRegister().add_tel_user(DataCenter.reg_parmes())
        print('--第1步----------------手机号注册流程进行中----------填写个人信息中------------')
        print(reg_tel_user)
        assert reg_tel_user[0] == 'https://create.test.gotin.top/guide/organizer/create'

    def test_assert_sponsor_info(self):
        greateSponsor_info =GreateSponsor().add_sponsor(DataCenter.sponsor_info())
        print('--第2步-----------------手机号注册流程进行中----------填写主办方信息------------')
        print(greateSponsor_info)
        assert greateSponsor_info[0] == 'https://create.test.gotin.top/guide/organizer/survey'

    def test_assert_knowInfo(self):
        know_your_info =KnowYourInfo().add_your_info()
        print('--第3步-----------------手机号注册流程进行中----------正向流程：让我们了解您------')
        print(know_your_info)
        assert know_your_info[0] == 'https://create.test.gotin.top/eventlists'
        assert know_your_info[1] == 'https://create.test.gotin.top/guide/event/guest'

    def test_assert_add_guest(self):
        guest_info =AddGuest().add_guest(DataCenter().guest_info())
        print('--第4步-----------------手机号注册流程进行中----------填写嘉宾信息---------------')
        print(guest_info)
        assert guest_info[0] == 'https://create.test.gotin.top/guide/event/session'


    def test_assert_add_schedule(self):
        schedule_info =AddSchedule().add_schedule(DataCenter().schedule_info())
        print('--第5步-----------------手机号注册流程进行中----------填写日程信息---------------')
        print(schedule_info)
        assert schedule_info[0] == 'https://create.test.gotin.top/guide/event/ticket'

    def test_assert_add_ticket(self):
        ticket_info =AddTicket().add_ticket(DataCenter().ticket_info())
        print('--第6步-----------------手机号注册流程进行中----------填写票务信息并发布-----------')
        print(ticket_info)
        assert ticket_info[0] == '发布' or ticket_info[0] == '已发布'


if __name__ == '__main__':
    #ss =TestUnifiedTelRegisterAssert().test_assert_tel_user()
    pytest.main(['-v', '-s', 'test_unified_tel_register_assert.py', "--html=./report/report.html"])



