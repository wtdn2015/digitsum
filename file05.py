#测试traceback模块的使用

import  traceback

#将异常信息打印到指定文件中
try:
    print("step1")
    num=1/0
except:
    traceback.print_exc()
    with open("D:\python file store\报错日志.txt","a") as f:
        traceback.print_exc(file=f)

