#自定义异常类的使用

class AgeError(Exception):

    def __init__(self,errorinfo):
        self.errorinfo=errorinfo

    def __str__(self):
        return str(self.errorinfo)+"岁是错误的年龄，应该在1-150岁之间!"

##############测试代码###############

if __name__=="__main__":
    a=int(input("请输入你的年龄:"))
    if a<1 or a>150:
        raise  AgeError(a)
    else:
        print("正常的年龄:",a)