#循环输入数字，如果不是数字则处理异常，直到输入88，循环结束

while True:
    try:
        x =int(input("请输入一个数字:") )       #若输入字母则发生异常
        if x==88:
            print("输入88，循环结束")
            break
    except ValueError as e:
        print("x不是数字，请重新输入!")
