#导入configparser
from configparser import ConfigParser


class ReadCfg():
    def __init__(self):
        #实例化configparser
        self.cp = ConfigParser()
        #获取文件绝对路径
        self.cp.read("D:\software\pycharmTest\\test1\com\opms\config\config")

    #获取host
    def getHost(self):
        host = self.cp.get("IP","host")
        # print(host)
        return host

    # 获取username
    def getUsername(self):
        username = self.cp.get("login", "username")
        # print(username)
        return username

    # 获取password
    def getPassword(self):
        password = self.cp.get("login", "password")
        # print(password)
        return password

if __name__ == '__main__':
    re =ReadCfg()
    re.getHost()
    re.getUsername()
    re.getPassword()