from com.common import readCfg
from com.opms.api.login import login

host=readCfg.ReadCfg().getHost()
username=readCfg.ReadCfg().getUsername()
password=readCfg.ReadCfg().getPassword()

class SearchProject():
    def __init__(self,s):
        self.s=s
        self.host=host

    def searchProject(self):
        rul=self.host+"/project/manage"
        res=self.s.get(rul)
        # print(res.text)

        return res.text



if __name__ == '__main__':
    s=login.LoginPro().logins()
    search=SearchProject(s)
    search.searchProject()

