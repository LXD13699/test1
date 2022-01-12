from com.common import connectMysql
sql = "select username from pms_users"
res_sql=connectMysql.ConnectSql().selectSqls(sql,10)
key_dic = res_sql[0]
key = list(key_dic.keys())[0]
data_list=[]
for i in range(0,10):
    pdi=res_sql[i][key]
    data_list.append(pdi)
print(data_list)







#     def getValue(self):
#         key = self.getKey()
#         for i in range (self.num):
#             pid = self.sql_res[i][key]
#             self.list_data.append(pid)
#             # print(f"第{i}次添加,list_data的值为:{list_data}")
#         # print(list_data)
#         print(self.list_data)
#         return self.list_data
# print(key)