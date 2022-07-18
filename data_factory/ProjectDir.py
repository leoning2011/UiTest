
import os

class UiProjectDri:
    @staticmethod
    def re_project_dir():
        #新建一个字典
        re_dir_list =[]
        #获取当前系统的分隔符
        re_sep = os.path.sep

        #获取ui自动化所处的路径
        ui_project_patch = os.path.split(os.getcwd())
        re_main_dir =ui_project_patch[0]
        #print(ui_project_patch[0])

        #重新组装新的存储路径-json文件，保存浏览器当前状态
        storage_state_json_path =re_main_dir + re_sep + 'data_store' + re_sep +'storage_state_json' + re_sep + 'url_token.json'

        #将数据写入数组
        re_dir_list.append(storage_state_json_path)

        # 重新组装新的存储路径-json文件，浏览器当前状态
        report_path = re_main_dir + re_sep + 'report'

        re_dir_list.append(report_path)

        re_dir_list.append(re_main_dir)
        #print(re_dir_list)

        return re_dir_list

if __name__ == '__main__':
    ss =UiProjectDri().re_project_dir()