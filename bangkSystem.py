'''

类：
类名：程序界面类
属性：
方法：显示欢迎页面，显示登陆页面登陆，显示主程序界面

类名：user
属性：名字，身份证号，手机号
方法：


类名：卡card
属性：卡号，密码，金额
方法：


类名：bankFunc
属性：
方法:开户。查询，存款。取款，转账，改密，锁定，解锁，补卡，注销，退出

类名：
属性：
方法


'''

#mian 函数
import adminView
from bankFunc import BankFunc
import time
import pickle
import os
def main():
    adminView.welcomView()
    if adminView.loginView() == -1: #表示登录失败
#    作业：重新登录，一般出错三次，程序直接退出
       pass
#    登录成功，则跳到主页面
#   显示主功能页面
    path = os.path.join(os.getcwd(), "alluser.txt")
    #判断该文件是否存在
    if not os.path.exists(path):
        #不存在用户信息时，传入一个空的字典
        bank = BankFunc({})
    else:#存在
        rf = open(path,"rb")
        #读取alluser
        alluser = pickle.load(rf)
    #从文件中获取所有用户有信息
    #pickle.load()



    #创建银行对象
        bank = BankFunc(alluser)
    while True:
        adminView.funcView()
        #bank = BankFunc()
        funNumber= input("请输入您要选择的功能：")
        if funNumber == "1": #开户
            bank.createUser()
        elif funNumber =="2": #查询
            bank.queryMoney()
        elif funNumber =="3": #存款
            bank.saveMoney()
        elif funNumber =="4": #取款
            bank.getMoney()
        elif funNumber =="5": #转账
            bank.translateMoney()
        elif funNumber =="6": #改密
            bank.ditPasswd()
        elif funNumber =="7": #锁定
            bank.lockCard()
        elif funNumber =="8": #解锁
            bank.unlockCard()
        elif funNumber =="9": #补卡
            bank.fillCard()
        elif funNumber =="0": #注销
            bank.killCard()
        elif funNumber =="q": #退出
         #   验证
         #将所有的用户信息存储到文件中去

            #打开一个文件
            #获取路径

         wf = open(path,"wb")
         pickle.dump(bank.allUser,wf)


         print("您正在退出系统......")



         time.sleep(1.5)
         print("退出成功")
         break
        else:
            print("您输入的不正确：")

def test():
    bank = BankFunc()
    print(bank.createCardNumber())
if __name__ == '__main__':
    main()
    #test()