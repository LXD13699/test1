from com.common import readIni
from com.opms.api.login import login

host=readIni.ReadIni().getvalues("IP","host")
class AddProManager():
    def __init__(self,s):
        self.s=s
        self.host=host

    def addManager(self,name="20220112项目",aliasname="0122项目",started="2022-01-12",ended="2022-01-12",desc="20220112"):
        url=self.host+"/project/add"
        data={"name":name,"aliasname":aliasname,"started":started,"ended":ended,"desc":desc}
        res=self.s.post(url,data)
        # print(res.json())

        return res.json()

    def addManager2(self, name="20220112项目", aliasname="0122项目", started="2022-01-12", ended="2022-01-12",
                   desc="20220112"):
        url = self.host + "/project/add"
        data = {"name": name, "aliasname": aliasname, "started": started, "ended": ended, "desc": desc}
        res = self.s.post(url, data)
        # print(res.json())

        return res


if __name__ == '__main__':
    s=login.LoginPro().logins()
    addpro=AddProManager(s)
    addpro.addManager()