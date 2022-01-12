import requests

from com.common import connectMysql
from com.opms.config import readCfg

host=readCfg.ReadCfg().getHost()
# username=readCfg.ReadCfg().getUsername()
password=readCfg.ReadCfg().getPassword()


class LoginPro():
    def __init__(self,s=requests.session()):
        self.s = s
        self.host=host
        self.username=self.getuname()
        self.password=password
        self.url=self.host+"/login"

    def getuname(self):
        sql = "select username from pms_users"
        username = connectMysql.ConnectSql().selectSqls(sql, 1)
        uname = username[0]["username"]
        return uname
    def login(self,username="libai",password="opms123456"):
        data={"username":self.username,"password":password}
        res = self.s.post(self.url,data)
        print(res.text)
        return res.json()


if __name__ == '__main__':
    logins=LoginPro()
    logins.login()