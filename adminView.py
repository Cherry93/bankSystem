
#设计欢迎的界面
import time
def welcomView():
    print("******************************************")
    print("******************************************")
    print("*****                                *****")
    print("*****     欢迎进入系统                *****")
    print("******************************************")
    print("******************************************")
    time.sleep(2)
def loginView():
    #模拟帐号和密码
    amdinUserName = 1
    adminPasswd = 1
    username = eval(input("请输入你的帐号:"))
    passwd = int(input("请输入密码："))
#验证帐号和密码
    if not username == amdinUserName:   #账户不正确
        print("您输入的帐号不存在！")
        loginView()
        return -1   #用-1表示输入的结果不对
    if not  passwd ==adminPasswd:
        print("您输入的密码不存在")
        loginView()
        return -1
    print("恭喜您登录成功！")
    return 1
#显示主功能页面
def funcView():
    print("******************************************")
    print("*****       开户（1）  查询（2）       *****")
    print("*****       存款（3）  取款（4）       *****")
    print("*****       转账（5）  改密（6）       *****")
    print("*****       锁定（7）  解锁（8）       *****")
    print("*****       补卡（9）  注销（0）       *****")
    print("*****             退出（q）           *****")

