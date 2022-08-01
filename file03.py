#try...多个except结构

while True:
    try:
        a = input("请输入一个被除数:")
        b = input("请输入一个除数:")
        c = float(a) / float(b)
        print(c)
    except ZeroDivisionError:
        print("异常，除数不能为零!程序结束!")
        break
    except ValueError:
        print("异常，不能将字符串转化为数字!程序结束!")
        break
    except NameError:
        print("异常，变量不存在!程序结束!")
        break
    except BaseException as e:
        print("发生异常!程序结束!")
        break