
from data_factory.ProjectDir import UiProjectDri

class GlobalDict:
    '''
    def page_global_dict(self) -> object:
        global MY_GLOBAL_DICT
        MY_GLOBAL_DICT = {}
        report_dir_path =UiProjectDri.re_project_dir()
        new_dir_path =report_dir_path[1]
        print(new_dir_path)
        MY_GLOBAL_DICT['report_path'] =new_dir_path
        print(MY_GLOBAL_DICT)
        return MY_GLOBAL_DICT
    '''


    # -*- coding: utf-8 -*-

    @staticmethod
    def _init():  # 初始化
        global _global_dict
        _global_dict = {}
        project_pwd =UiProjectDri().re_project_dir()
        _global_dict.setdefault('project_pwd',project_pwd)


    def set_value(key, value):
        # 定义一个全局变量
        _global_dict[key] = value


    def get_value(key):
        # 获得一个全局变量，不存在则提示读取对应变量失败
        try:
            return _global_dict[key]
        except:
            print('读取' + key + '失败\r\n')


if __name__ == '__main__':
    print('1')


