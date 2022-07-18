
from data_factory.PageGlobalDict import  GlobalDict

import os

GlobalDict._init()

GlobalDict.set_value('name', '帅哥')


'''
s1 =os.getcwd()
s2 =os.path.split(s1)

#print(s1)
#print(s2,type(s2),s2[0])
s3 =GlobalDict().page_global_dict()
s3['22'] = 11
print(s3,type(s3))
s3['33'] = 11
'''
name = GlobalDict.get_value('name')

name2 = GlobalDict.get_value('project_pwd')[0]
print(name2)