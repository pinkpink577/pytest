try:
    fh = open("testfile","www")
    fh.write("这是一个测试文件，用于测试异常！")
except Exception:
    print("错误！没有找到该文件或输入错误")
else:
    print("输入成功！")
    fh.close
# 就是现在