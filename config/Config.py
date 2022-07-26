import configparser
import threading
import os

class Config:
    # __new__ 用于创建实例，而__init__用于初始化实例
    # 获取当前系统的分隔符
    path_sep = os.path.sep
    #获取当前配置文件的路径
    pwd =os.getcwd()
    __filepath = pwd + path_sep + 'config.ini'

    __configfile = __filepath
    __flag = False
    __instance_lock = threading.Lock() # 定义一把锁

    def __init__(self):
        # 如果配置初始化已经完成，直接返回
        if Config.__flag:
            return

        config = configparser.ConfigParser()
        config.read(Config.__configfile, encoding='UTF-8')
        self.__browserType = config.get('BrowserType', 'type')
        self.__waitTime = config.get('WaitTime','waitTime')
        Config.__flag = True

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls.__instance_lock.acquire()
            if not hasattr(cls, '_instance'):
                cls._instance = super().__new__(cls)
            cls.__instance_lock.release()

        return cls._instance

    @property
    def browserType(self):
        return self.__browserType

    @property
    def waitTime(self):
        print(self.__waitTime)
        return self.__waitTime


if __name__ == '__main__':
    Config().waitTime