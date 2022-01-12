import requests


from com.opms.config import readCfg

host=readCfg.ReadCfg().getHost()
username=readCfg.ReadCfg().getUsername()
password=readCfg.ReadCfg().getPassword()
class LoginPro():
    def __init__(self,s=requests.session()):
        self.s = s
        self.host=host
        self.username=username
        self.password=password
        self.url=self.host+"/login"

    def login(self,username=username,password=password):
        data={"username":username,"password":password}
        res = self.s.post(self.url,data)
        print(res.text)
        return res.json()

    def logins(self,username=username,password=password):
        data = {"username": username, "password": password}
        self.s.post(self.url, data)

        return self.s

if __name__ == '__main__':
    logins=LoginPro()
    # logins.login()
    logins.logins()