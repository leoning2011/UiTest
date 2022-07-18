

from DataParmes import DataCenter
import pytest
import requests
import json
from data_factory.ApiToken import  ApiToken
from bs4 import BeautifulSoup

import warnings


class APiPageSoup:
    #@pytest.mark.parametrize('userdata', ApiToken().user_info_verification_code())
    #token =ApiToken().api_token(DataCenter().user_info_verification_code())
    def page_api_token(self,token):
        '''--------------------------忽略警告--------------------------'''
        warnings.filterwarnings('ignore')
        '''--------------------------忽略警告--------------------------'''

        '''--------------------------参数区域--------------------------'''


        url = 'https://create.test.gotin.top/eventlists'
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
        ss =APiPageSoup().page_api_token()



