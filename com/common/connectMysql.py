from com.common import readIni
import pymysql
class ConnectSql():
    def __init__(self,database="aiopms"):
        #拿到配置文件中的值：dbinfo
        dbinfo= readIni.ReadIni().getvalues("dbinfo", "dbinfo")
        #转化成mapping
        db=eval(dbinfo)
        #创建数据库游标cursorclass
        self.con = pymysql.connect(database=database,
                                   cursorclass=pymysql.cursors.DictCursor,
                                   **db)
        #创建游标
        self.curso=self.con.cursor()

    #查询方法
    def selectSql(self,sql):
        self.curso.execute(sql)
        #查询多条：fetchall()，单条fetchone
        selct=self.curso.fetchall()
        return selct

    #根据需求传参
    def selectSqls(self,sql,size=5):
        self.curso.execute(sql)
        select=self.curso.fetchmany(size)
        return select



if __name__ == '__main__':
    con = ConnectSql()
    sql="select username from pms_users"
    con.selectSql(sql)
    con.selectSqls(sql,2)