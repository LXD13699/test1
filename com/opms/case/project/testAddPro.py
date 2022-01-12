import random
from urllib import request

import requests

from com.opms.api.project import addProjectManager
import allure
import pytest
import time



''''
pytest 测试类格式：类名以Test开头，且不能有__init__
'''
class TestAdd():
    #使用time时间函数，拿取当前时间作为入参参数化
    nowTime=time.strftime("%Y-%m-%d")
    #使用random随机函数
    rand=random.randint(1,100)

    test_data=[{"name":f"{nowTime}--{rand}项目",
                "aliasname":f"{nowTime}--{rand}项目",
                "started":f"{nowTime}",
                "ended":f"{nowTime}",
                "desc":f'{nowTime}'}
               ]
    @allure.feature("功能点：opms添加项目")
    @allure.step("测试步骤：必填项不为空且填写正确，点击添加")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("getData",test_data,indirect=True)
    def testAddProject(self,logins,getData):
        s=logins
        res=addProjectManager.AddProManager(s).addManager(name=getData[0],aliasname=getData[1],started=getData[2],ended=getData[3],desc=getData[4])
        print(res)

    @allure.feature("功能点：opms添加项目")
    @allure.step("测试步骤：name为空，点击添加")
    @allure.severity(allure.severity_level.NORMAL)
    def testAddProject2(self, logins):
        s = logins
        res = addProjectManager.AddProManager(s).addManager(name="")
        assert res["code"] ==0

    @allure.feature("功能点：opms添加项目")
    @allure.step("测试步骤：aliasname为空，点击添加")
    @allure.severity(allure.severity_level.NORMAL)
    def testAddProject3(self, logins):
        s = logins
        res = addProjectManager.AddProManager(s).addManager(aliasname="")
        assert res["code"] == 0

    @allure.feature("功能点：opms添加项目")
    @allure.step("测试步骤：started为空，点击添加")
    @allure.severity(allure.severity_level.NORMAL)
    def testAddProject4(self, logins):
        s = logins
        res = addProjectManager.AddProManager(s).addManager(started="")
        assert res["code"] == 0

    @allure.feature("功能点：opms添加项目")
    @allure.step("测试步骤：ended为空，点击添加")
    @allure.severity(allure.severity_level.NORMAL)
    def testAddProject5(self, logins):
        s = logins
        res = addProjectManager.AddProManager(s).addManager(ended="")
        assert res["code"] == 0

    @allure.feature("功能点：opms添加项目")
    @allure.step("测试步骤：desc为空，点击添加")
    @allure.severity(allure.severity_level.NORMAL)
    def testAddProject6(self, logins):
        s = logins
        res = addProjectManager.AddProManager(s).addManager(desc="")
        assert res["code"] == 1
