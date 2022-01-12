import  os
from configparser import ConfigParser

class ReadCfg():
    def __init__(self):
        #获取cfg文件绝对路径
        desc_path=os.path.realpath(__file__)
        #获取cfg文件的上两级目录
        file_path=os.path.dirname(os.path.abspath(os.path.dirname(desc_path)))
        #拼接找到cfg文件
        file = os.path.join(file_path,"conf","config.cfg")
        #实例化configparser
        self.con = ConfigParser()
        self.con.read(file)

    #获取cfg文件中的host
    def getHost(self):
        host = self.con.get("IP", "host")
        # print(host)
        return host
    # 获取cfg文件中的username
    def getUsername(self):
        username =self.con.get("login","username")
        # print(username)
        return username

    # 获取cfg文件中的username
    def getPassword(self):
        password = self.con.get("login", "password")
        # print(password)
        return password



if __name__ == '__main__':
    readcfg = ReadCfg()
    readcfg.getHost()
    readcfg.getUsername()
    readcfg.getPassword()