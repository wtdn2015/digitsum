u1={"name":"张三","pos":1,"hob":"bee"}
u2={"name":"李四","pos":2,"hob":"study"}
u3={"name":"王五","pos":4,"hob":"hulu"}
a=[u1,u2,u3]

#循环打印每个人的数据

for i in range(3):
    print(a[i].get("name"),a[i].get("pos"),a[i].get("hob"))
