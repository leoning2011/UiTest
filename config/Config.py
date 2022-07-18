import configparser
import threading
class Config:
    # __new__ 用于创建实例，而__init__用于初始化实例
    __configfile = r'D:\workspace\2021\webflash20\venv\api\config\config.ini'
    __flag = False
    __instance_lock = threading.Lock() # 定义一把锁

    def __init__(self):
        # 如果配置初始化已经完成，直接返回
        if Config.__flag:
            return

        config = configparser.ConfigParser()
        config.read(Config.__configfile, encoding='UTF-8')
        self.__testcasefile = config.get('TestCaseFile', 'file')
        self.__testcasejsonfile = config.get('TestCaseFile', 'jsonfile')
        self.__logpath = config.get('LogPath', 'path')
        Config.__flag = True

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls.__instance_lock.acquire()
            if not hasattr(cls, '_instance'):
                cls._instance = super().__new__(cls)
            cls.__instance_lock.release()

        return cls._instance

    @property
    def testCaseJsonFile(self):
        return self.__testcasejsonfile

    @property
    def testCaseFile(self):
        return self.__testcasefile

    @property
    def logPath(self):
        return self.__logpath
