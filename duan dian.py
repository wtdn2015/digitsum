#测试调试、断点

def aa():
    print("run in aa() start!")
    print("step1")
    a=3
    b=a*3
    c=b*5
    print("step2")
    print("run in aa() end!!!")

if __name__=="__main__":
    print("main:step1")
    aa()
    print("main:step2")
    print("main:end!!!!")