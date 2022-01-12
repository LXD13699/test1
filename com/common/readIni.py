import os
from configparser import ConfigParser

#读取ini配置文件
class ReadIni():
    def __init__(self):
        #获取绝对路径
        desc_path=os.path.realpath(__file__)
        #获取ini文件上级目录
        file_path = os.path.dirname(os.path.dirname(desc_path))
        #拼接文件
        file = os.path.join(file_path,"conf","config.ini")
        #实例化
        self.con=ConfigParser()
        self.con.read(file,encoding="utf-8")

    #获取ini文件中的快
    def getSection(self):
        section=self.con.sections()
        print(section)
        return section
    #通过快名称获取值
    def getValue(self):
        value = self.con.items("login")
        #将得到的值通过字典转化
        val=dict(value)
        print(val)
        return val

    def getvalues(self,option,section):
        val = self.con.get(option,section)
        return val
if __name__ == '__main__':
    readini = ReadIni()
    # readini.getSection()
    # readini.getValue()
    readini.getvalues("dbinfo","dbinfo")
