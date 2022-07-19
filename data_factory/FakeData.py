

import mimesis
import random
from faker import Faker
from faker import Factory # 引入工厂类


class DeptData:

    @staticmethod
    def person_fir_name():
        """
        返回中文名称
        :return:
        """
        fir_name = mimesis.Person('zh')
        re_fir_name = fir_name.first_name()
        #print(re_fir_name)
        return re_fir_name

    @staticmethod
    def person_las_name():
        """
        返回中文姓氏
        :return:
        """
        las_name = mimesis.Person('zh')
        re_las_name  = las_name.last_name()
        return re_las_name

    @staticmethod
    def person_tel_num():
        """
        返回境外电话号码
        :return:
        """
        re_tel_num = mimesis.Person()
        #print(re_tel_num.telephone())
        return re_tel_num.telephone()

    @staticmethod
    def get_phone_num():
        """
        返回中国电话号码
        :return:
        """
        second_spot = random.choice([3, 4, 5, 7, 8])
        third_spot = {3: random.randint(0, 9),
                      4: random.choice([5, 7, 9]),
                      5: random.choice([i for i in range(10) if i != 4]),
                      7: random.choice([i for i in range(10) if i not in [4, 9]]),
                      8: random.randint(0, 9), }[second_spot]
        remain_spot = random.randint(9999999, 100000000)
        phone_num = "1{}{}{}".format(second_spot, third_spot, remain_spot)

        #print(phone_num)
        return phone_num


    @staticmethod
    def every_code():
        """
        返回万能验证码
        :return:
        """
        number = '12580'
        return number

    @staticmethod
    def every_password():
        """
        返回万能验证码
        :return:
        """
        password = '123qwe!@#'
        return password

    @staticmethod
    def sponsorName():
        """
        返回商业名称
        :return:
        """
        fake = Faker("zh_CN")
        sponsorName = fake.company() # 生成名称
        #print(sponsorName)
        return sponsorName

    @staticmethod
    def sponorEmail():
        """
        返回email
        :return:
        """
        fake = Faker()
        sponorEmail = fake.company_email() # 生成名称
        #print(sponorEmail)
        return sponorEmail

    @staticmethod
    def sponorText():
        """
        返回简单文档信息
        :return:
        """
        fake = Faker("zh_CN")
        sponorText = fake.text() # 生成一段话
        #print(sponorText)
        return sponorText

    @staticmethod
    def title_job():
        """
        返回职位title
        :return:
        """
        fake = Faker("zh_CN")
        title_job = fake.job() # 职位title
        #print(sponorText)
        return title_job


    @staticmethod
    def title_sentence():
        """
        返回职位title
        :return:
        """
        fake = Faker("zh_CN")
        title_sentence = fake.sentence() # 一句话主题
        #print(sponorText)
        return title_sentence

    @staticmethod
    def ticket_info():
        """
        返回职位title
        :return:
        """
        fake = Faker("zh_CN")
        ticket_info = fake.random_int(1,100)
        #print(sponorText)
        return ticket_info


if __name__ == '__main__':
    #p1 =DeptData().person_tel_num()
    p2 =DeptData().sponorText()