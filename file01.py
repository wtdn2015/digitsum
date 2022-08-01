#try...一个except结构

try:
    print("step1")
    a=3/2
    print("step2")
except BaseException as e:
    print(e)
    print(type(e))
    print("step3")

print("end!!!")