from com.common import connectMysql

sql="select username from pms_users"
user= connectMysql.ConnectSql().selectSqls(sql, 10)
print(list(user[0]))



# @pytest.mark.parametrize("username",username)
# def testLogins(username):
#     a=logins.LoginPro().login(username)
#     print(a)
