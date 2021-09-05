'''模块化'''
import os
#for push

#从文件载入词法信息
def readFile():
    return open('MyFinanceController.java', 'r',encoding='utf-8')

def closeFile(f):
    f.close();
#字符文件接口，持续输入
#trust

#return
#单字句柄

if __name__ == '__main__' :
    f=readFile()
    print(f.read())
    closeFile(f)



