

import requests
from com.common import readCfg
import pytest
'''
conftest文件主要做前置作用，例如把登录当作其他case调用的前置条件
用pytest.fixture作为前置，便于其他case调用

'''


@pytest.fixture(scope="session")
def logins():
    ri = readCfg.ReadCfg()
    s=requests.session()
    username = ri.getUsername()
    password = ri.getPassword()
    host = ri.getHost()
    url = host +"/login"

    data = {"username": username, "password": password}
    a=s.post(url, data)
    return s


@pytest.fixture(scope="session")
def getData(request):
    name=request.param["name"]
    aliasname=request.param["aliasname"]
    started=request.param["started"]
    ended=request.param["ended"]
    desc=request.param["desc"]

    return name,aliasname,started,ended,desc