from com.opms.api.login import login
import pytest

#单个变量参数化
@pytest.mark.parametrize("username",("libai","","dawdawd"))
def testLogin1(username):
    res = login.LoginPro().login(username)
    print(res)

#单个变量参数化
@pytest.mark.parametrize("password",("opms123456","","dawdawd"))
def testLogin2(password):
    res = login.LoginPro().login(password=password)
    print(res)

#多个变量参数化:组合交叉
@pytest.mark.parametrize("username",("libai","","dawdawd"))
@pytest.mark.parametrize("password",("opms123456","","dawdawd"))
def testLogin3(username,password):
    res = login.LoginPro().login(username,password)

    print(res)

#对入参，出参进行参数化
@pytest.mark.parametrize("username,password,code",
                         [("libai","opms123456",1),
                          ("libai","2423",0)
                         ])
def testLogin4(username,password,code):
    res = login.LoginPro().login(username,password)
    print(res)

