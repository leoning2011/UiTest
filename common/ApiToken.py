

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
            #print(properties_response)
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
            #print(organization_response)
            #print(organization_response)
            organization_hash =organization_response.get('data')[0].get('hash')
            #print(organization_hash)
            return organization_hash

    @pytest.mark.parametrize('userdata', DataCenter().user_email_info())
    def get_emailUserToken(self,emailUserInfo):
        '''--------------------------忽略警告--------------------------'''
        warnings.filterwarnings('ignore')
        '''--------------------------忽略警告--------------------------'''

        '''--------------------------参数区域--------------------------'''

        url = 'https://api-gateway.test.gotin.top/web/user/login'
        headers = {'Content-Type': 'application/json'}

        userdata = {'user_name': emailUserInfo.get('user_name'), 'password': emailUserInfo.get('password')}
        '''--------------------------参数区域--------------------------'''
        with requests.post(url=url,
                           headers=headers,
                           data=json.dumps(userdata), verify=False) as response:
            response = json.loads(response.text)
            #print(response)
            email_token = response.get('data').get('token')
            #print(email_token)
            return email_token

    def set_giftOrg(self,email_token,organization_hash,quantity):
        #print(email_token)
        #print(organization_hash)
        #print(quantity)
        '''--------------------------忽略警告--------------------------'''
        warnings.filterwarnings('ignore')
        '''--------------------------忽略警告--------------------------'''

        '''--------------------------参数区域--------------------------'''


        url = 'https://paycenter.test.gotin.top/tools/gift-traffic'
        headers = {'Content-Type': 'application/json','Authorization': email_token}

        userdata = {'organization_hash': organization_hash, 'quantity': quantity}
        '''--------------------------参数区域--------------------------'''
        with requests.post(url=url,
                           headers=headers,
                           data=json.dumps(userdata),verify=False) as response:
            response =json.loads(response.text)

            response_status =response.get('message')
            print(response_status)
            return response_status


    def add_traffic(self):
        '''
        参数为固定参数（如需修改，请在dataParmes中找到对应的值，并且做成配置项
        :return: 返回状态
        '''
        print('第1步，获取被操作账户的token--------------------------------')
        get_user_token = self.api_token(DataCenter().user_info_verification_code())
        print('第2步，获取被操作账户的哈希值--------------------------------')
        get_organization_hash = self.api_organization_info_hash(get_user_token)
        print('第3步，获取具有赋权账户的token（项建账户的权限）--------------------------------')
        get_jurisdiction_account_token = self.get_emailUserToken(DataCenter().user_email_info())
        print('第4步，给被操作用户进行赠送流量包--------------------------------')
        number2 = int(999999)
        add_traffic = self.set_giftOrg(get_jurisdiction_account_token, get_organization_hash, number2)
        assert add_traffic == 'success'
        return  add_traffic

if __name__ == '__main__':
        s1 =ApiResponse().add_traffic()



