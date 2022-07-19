
import os

class UiProjectDri:
    @staticmethod
    def re_project_dir():
        #新建一个字典
        re_dir_dict ={}
        #获取当前系统的分隔符
        re_sep = os.path.sep
        #project_patch ="C:\\Users\\admin\\PycharmProjects\\UiTest\\data_store\\logintoken"
        path_root = os.path.realpath(__file__)
        json_path  =path_root.split('\\',5)

        re_main_dir = json_path[0] + re_sep + json_path[1] + re_sep  +json_path[2] + re_sep +json_path[3] + re_sep + json_path[4]
        print(re_main_dir)
        #获取ui自动化所处的路径
        #ui_project_patch = os.path.split(path_root)
        #re_main_dir =ui_project_patch[0]
        #print(ui_project_patch[0])
        #print(re_main_dir)

        #重新组装新的存储路径-json文件，保存浏览器当前状态
        storage_state_json_path =re_main_dir + re_sep + 'data_store' + re_sep +'storage_state_json' + re_sep + 'url_token.json'

        #将数据写入数组
        re_dir_dict['register_token'] =storage_state_json_path

        #重新组装新的存储路径-json文件，保存浏览器当前状态
        storage_state_email_path =re_main_dir + re_sep + 'data_store' + re_sep +'logintoken' + re_sep + 'token.json'

        #将数据写入数组
        re_dir_dict['login_token'] =storage_state_email_path

        # 重新组装新的存储路径-json文件，浏览器当前状态
        report_path = re_main_dir + re_sep + 'report'

        re_dir_dict['report_path'] =report_path
        print(re_dir_dict)

        return re_dir_dict

if __name__ == '__main__':
    ss =UiProjectDri().re_project_dir()