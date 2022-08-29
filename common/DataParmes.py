from common.FakerData import DeptData
import datetime


class DataCenter:
    @staticmethod
    def reg_parmes():
        """
        手机号注册信息 5个信息，第6个为email
        返回6个入参：
        :return:
        """
        # 声明空列表
        data_value = []
        # 获取中国大陆的手机号
        tel = DeptData.get_phone_num()
        data_value.append(tel)
        # 获取中国的名字
        las_name = DeptData.person_las_name()
        data_value.append(las_name)
        # 获取中国的姓氏
        fir_name = DeptData.person_fir_name()
        data_value.append(fir_name)
        # 万能验证码
        every_code = DeptData.every_code()
        data_value.append(every_code)

        #统一的密码
        every_password = DeptData.every_password()
        data_value.append(every_password)
        # 获取主办方邮箱
        sponsor_info_email = DeptData.sponorEmail()
        data_value.append(sponsor_info_email)

        #print(data_value)
        return data_value

    @staticmethod
    def sponsor_info():
        """
        手机号注册信息
        返回3个入参：
        :return:
        """
        # 声明空列表
        sponsor_info = []
        # 获取主办方信息
        sponsor_info_name = DeptData.sponsorName()
        sponsor_info.append(sponsor_info_name)
        # 获取主办方邮箱
        sponsor_info_email = DeptData.sponorEmail()
        sponsor_info.append(sponsor_info_email)
        # 获取一段文字（读不懂是正常的，没那么智能）
        sponsor_info_text = DeptData.sponorText()
        sponsor_info.append(sponsor_info_text)

        #print(data_value)
        return sponsor_info


    @staticmethod
    def guest_info():
        """
        手机号注册信息
        返回4个入参：
        :return:
        """
        # 声明空列表
        guest_info = []
        # 获取主办方信息
        # 获取中国的名字
        las_name = DeptData.person_las_name()
        fir_name = DeptData.person_fir_name()
        china_name = las_name +  fir_name
        guest_info.append(china_name)
        # title
        guest_info_bus_name = DeptData.title_job()
        guest_info.append(guest_info_bus_name)

        # 单位名称
        guest_info_bus_name = DeptData.sponsorName()
        guest_info.append(guest_info_bus_name)

        # 手机号
        guest_info_tel = DeptData.get_phone_num()
        guest_info.append(guest_info_tel)

        #print(data_value)
        return guest_info


    @staticmethod
    def schedule_info():
        """
        获取主办方信息
        返回1个入参：
        :return:
        """
        # 声明空列表
        schedule_info = []
        # 获取主办方信息
        # 获取中国的名字
        las_name = DeptData.title_sentence()
        schedule_info.append(las_name)

        #print(data_value)
        return schedule_info


    @staticmethod
    def ticket_info():
        """
        票据注册信息
        返回1个入参：
        :return:
        """
        # 声明空列表
        ticket_info = []
        # 获取主办方信息
        # 获取中国的名字
        las_name = DeptData.ticket_info()
        ticket_info.append(las_name)

        #print(data_value)
        return ticket_info

    @staticmethod
    def user_info_verification_code():
        """验证码，{用户名&万能验证码}
        :return:
        """
        # 声明空列表
        user_info = {"user_name": "17114261964","verification_code": "1258"}
        #print(data_value)
        print(user_info.get('user_name'))
        return user_info

    @staticmethod
    def user_email_info():
        """验证码，{用户名&万能验证码}
        :return:
        """
        # 声明空列表
        user_email_info = {"user_name": "xiangjian_yd@163.com","password": "yd222222"}
        #print(data_value)
        print(user_email_info.get('user_name'))
        return user_email_info


    @staticmethod
    def local_time():
        """验证码，{用户名&万能验证码}
        :return:
        """
        # 声明空列表
        now_time = datetime.datetime.now().strftime('%Y-%m-%d')
        time_list =now_time.split('-')
        print(time_list)

        return now_time

if __name__ == '__main__':
    data =DataCenter.local_time()