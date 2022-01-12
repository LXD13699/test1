from com.opms.api.project import searchProject
import allure

'''
执行测试用例用allure生成报告，优化allure
'''


@allure.feature("opms项目：项目查询管理界面")
def testSearchPro(logins):
    s=logins
    print(s)
    res=searchProject.SearchProject(s).searchProject()
    assert "挂起" in res