'''模块化'''
import os
import json
#for push

#从文件载入词法信息
def readFile():
    return open('MyFinanceController.java', 'r',encoding='utf-8')

def closeFile(f):
    f.close()

#import lex
def importLex(file,language):
    f=json.load(file)
    lan=f[language]
    return lan
#字符文件接口，持续输入
#trust

#return
#单字句柄

if __name__ == '__main__' :
    f=open(r"resource\lex.json",encoding="utf-8")
    fdj=importLex(f,"java")
    #lexInfo=fdj.dumps()
    print(fdj)



