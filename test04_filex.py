import pytest

from base_page.base_page_login.TelVerifCodeLogin import  TelVerifCodeLogin

@pytest.fixture()
def test_a_channel(TelVerifCodeLogin):


    print('123131321')

if __name__ == '__main__':
    test_a_channel(TelVerifCodeLogin)