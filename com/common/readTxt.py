import os
from configparser import ConfigParser

txt_path=os.path.realpath(__file__)
file_path=os.path.dirname(os.path.dirname(txt_path))
file=os.path.join(file_path,"conf","config.txt")
print(file)

# 读取tt文件内容
with open(file,"r",encoding="utf-8") as f:
    txt=f.read()
    print(txt)

#覆盖写文件
with open(file,"w",encoding="utf-8") as f:
    txt=f.write("钱钱钱钱钱钱钱钱钱钱钱钱钱钱钱钱钱钱钱")
    print(txt)

#追加写文件
with open(file,"a",encoding="utf-8") as f:
    txt=f.write("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
    print(txt)