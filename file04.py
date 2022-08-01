#try...except...finally结构

try:
    f = open(r"D:\python file store\a.txt", "r",encoding="utf-8")     #在读取a.txt文件时，需指定encoding，否则会因编码方式不同无法进行解码从而发生异常
    content = f.readlines()
    print(content)
except BaseException as e:
    print("文件未找到!")
    print(e)
finally:
    f.close()
    print("释放资源!")

print("程序执行结束!")