

from common.DataParmes import  DataCenter
import pytest
import requests
import json
import warnings


class ApiResponse:
    @pytest.mark.parametrize('userdata', DataCenter().user_info_verification_code())
    def api_token(self,user_name):
        '''--------------------------忽略警告--------------------------'''
        warnings.filterwarnings('ignore')
        '''--------------------------忽略警告--------------------------'''

        '''--------------------------参数区域--------------------------'''


        url = 'https://api-gateway.test.gotin.top/web/user/login/by_verification_code'
        headers = {'Content-Type': 'application/json'}

        userdata = {'user_name': user_name.get('user_name'), 'verification_code': user_name.get('verification_code')}
        '''--------------------------参数区域--------------------------'''
        with requests.post(url=url,
                           headers=headers,
                           data=json.dumps(userdata),verify=False) as response:
            verify_response = json.loads(response.text)
            #print(verify_response)
            verify_token =verify_response.get('data').get('token')
            print(verify_token)
            return verify_token



    def api_user_info_hash(self,api_token):
        '''--------------------------忽略警告--------------------------'''
        warnings.filterwarnings('ignore')
        '''--------------------------忽略警告--------------------------'''

        '''--------------------------参数区域--------------------------'''


        url = 'https://api-gateway.test.gotin.top/web/user/info'
        headers = {'Content-Type': 'application/json','Authorization': api_token}

        '''--------------------------参数区域--------------------------'''
        with requests.get(url=url,
                           headers=headers,
                           verify=False) as response:
            properties_response = json.loads(response.text)
            print(properties_response)
            user_hash =properties_response.get('data').get('properties').get('hash')
            print(hash)
            return user_hash


    def api_organization_info_hash(self,api_token):
        '''--------------------------忽略警告--------------------------'''
        warnings.filterwarnings('ignore')
        '''--------------------------忽略警告--------------------------'''

        '''--------------------------参数区域--------------------------'''


        url = 'https://creation.test.gotin.top/organization/list'
        headers = {'Content-Type': 'application/json','Authorization': api_token}

        '''--------------------------参数区域--------------------------'''
        with requests.get(url=url,
                           headers=headers,
                           verify=False) as response:
            organization_response = json.loads(response.text)
            print(organization_response)
            organization_hash =organization_response.get('data')[0].get('hash')
            print(organization_hash)
            return organization_hash

if __name__ == '__main__':
    s1=ApiResponse().api_token(DataCenter().user_info_verification_code())
    s2 =ApiResponse().api_user_info_hash(s1)
    ss =ApiResponse().api_organization_info_hash(s1)



