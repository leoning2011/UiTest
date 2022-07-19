import pytest
#pytest.main(['-v',  '-s', '--html=./report/huice.html'])
#pytest.main (['./base_page_tel_register/EmailRegister.py' ,'-m',  '-s', '--html=./report/huice.html'])  # 运行模块中的指定用例

#pytest.main(['-m', 'v2', '-s', '--alluredir=./report/allure-json'])
#pytest.main(['./'])
#执行特定文件
#pytest.main(['-v', '-s','./base_page_tel_register/EmailRegister.py',"--html=./report/report.html"])


pytest.main(['-v', '-s',"--html=./report/report.html"])


