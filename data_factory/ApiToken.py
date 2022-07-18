

from data_factory.DataParmes import  DataCenter
import pytest
import requests
import json

from bs4 import BeautifulSoup

import warnings


class ApiToken:
    @pytest.mark.parametrize('userdata', DataCenter().user_info_verification_code())

    def api_token(self,user_info):
        '''--------------------------忽略警告--------------------------'''
        warnings.filterwarnings('ignore')
        '''--------------------------忽略警告--------------------------'''

        '''--------------------------参数区域--------------------------'''


        url = 'https://api-gateway.test.gotin.top/web/user/login/by_verification_code'
        headers = {'Content-Type': 'application/json'}

        userdata = {'user_name': user_info.get('user_name'), 'verification_code': user_info.get('verification_code')}
        '''--------------------------参数区域--------------------------'''
        with requests.post(url=url,
                           headers=headers,
                           data=json.dumps(userdata),verify=False) as response:
            verify_response = json.loads(response.text)
            #print(verify_response)
            verify_token =verify_response.get('data').get('token')
            print(verify_token)
            return verify_token


if __name__ == '__main__':
        ss =ApiToken().api_token(DataCenter().user_info_verification_code())



