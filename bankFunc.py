import random
from card import Card
from user import User
import pickle


class BankFunc(object):
    #  方法:开户。查询，存款。取款，转账，改密，锁定，解锁，补卡，注销，退出
    #   开户

    #   需要一个字典存储该银行系统的账户信息，卡号作为key,---user作为value
    def __init__(self, alluser):
        self.allUser = alluser
        # self.allUser ={}

    def createUser(self):
        # 输入名字
        name = input("请输入您的名字：")
        # 输入身份证号
        idNumber = input("请输入您的身份证号：")
        # 输入用户手机号
        phone = input("请输入您的手机号：")
        # 验证，数据格式的合法性，数据是否正确（身份证号是否合法，手机号是否是个人的等）

        # 系统随机生产一个卡号（唯一的，不能与系统中其他卡号重复）
        cardNumber = self.createCardNumber()

        # 设置密码（新密码需要输入两次（不一样需要重新设置））
        resPasswd = self.setPasswd()
        if resPasswd == -1:  # 如果设置密码时返回的是 -1 ，表示是个恶意的行为，则终止开户
            return -1

        # 设置余额
        money = input("请输入您的金额：")
        # 判断money需要大于零
        # 创建一个card对象


        card = Card(cardNumber, resPasswd, money)
        # 创建一个user对象
        user = User(name, idNumber, phone, card)

        # 把用户存到allUser中，卡号作为key,user作为value
        self.allUser[cardNumber] = user
        #   测试
        print(self.allUser)

    # 设置密码
    def setPasswd(self):
        for i in range(3):
            passwd1 = input("请输入您的新密码：")
            passwd2 = input("请确认您的密码：")
            if passwd1 == passwd2:  # 设置密码成功
                return passwd1
                #   此时三次设置都失败
        return -1

    # 生产一个随机卡号
    def createCardNumber(self):
        #       666 666  0-9

        while True:
            cardNumber = ""
            for i in range(0, 6):
                cardNumber += str(random.randrange(0, 10))
                # ··     检查该卡号已经存在
            if not cardNumber in self.allUser:  # 卡号是否不存在
                return cardNumber
                # print()

            #   查询

    def queryMoney(self):

        # 查询余额
        # 请输入您的卡号
        cardNumber = input("请输入您要查询的卡号:")
        # 在alluser中查到对应的卡
        user = self.allUser.get(cardNumber)
        if user == None:
            #
            # 作业：可以输入三次卡号，超过三次，推出
            print("您输入的卡号不存在")
            return -1

        # 判断该卡是否已锁定
        if user.card.lock == True:
            print("此卡已经被锁定，无法查询")

            return -1

        # 输入密码（输入错误，则可以重新输入三次，就锁定）
        passwd = input("请输入您的密码")
        res = self.checkPasswd(passwd, user)
        if res == -1:  # 多次输入的密码多次错误，锁定该卡，并退出该功能
            # 锁起来
            user.card.lock = True

            return -1

            # 查询数据
        print("cardNumber:%s,money:%s" % (cardNumber, int(user.card.money)+int(user.card.money1)-int(user.card.money2)))

        # 找到user
        # 找到卡
        # pass

    # 用来检查密码是否正确
    def checkPasswd(self, passwd, user):
        for i in range(3):
            if passwd == user.card.passwd:  # 表示密码匹配成功
                return 1
            # 表示最后一次没有匹配成功
            if i == 2:
                return -1
            # 匹配失败
            passwd = input("您的密码错误，请重新输入：")





        #   存款


    def saveMoney(self):



    #   请输入您要存入的卡号
        cardNumber = input("请输入您要存入的卡号:")

        user = self.allUser.get(cardNumber)
        if user == None:
        #
        # 作业：可以输入三次卡号，超过三次，推出
            print("您输入的卡号不存在")
            return -1

    # 判断该卡是否已锁定
        if user.card.lock == True:
            print("此卡已经被锁定，无法查询")

            return -1
            # 输入密码（输入错误，则可以重新输入三次，就锁定）
        passwd = input("请输入您的密码")
        res = self.checkPasswd(passwd, user)
        if res == -1:  # 多次输入的密码多次错误，锁定该卡，并退出该功能
                # 锁起来
            user.card.lock = True

            return -1
    #   请输入您要存入的金额
        user.card.money1 = input("请输入您要存入的金额:")
        print("您账户余额为:%s"%(int(user.card.money1)+int(user.card.money)))
    #    需要把存的金额返到总金额里面

    #   取款
    def getMoney(self):
        cardNumber = input("请输入您要存入的卡号:")

        user = self.allUser.get(cardNumber)
        if user == None:
            #
            # 作业：可以输入三次卡号，超过三次，推出
            print("您输入的卡号不存在")
            return -1

            # 判断该卡是否已锁定
        if user.card.lock == True:
            print("此卡已经被锁定，无法取款")

            return -1
            # 输入密码（输入错误，则可以重新输入三次，就锁定）
        passwd = input("请输入您的密码")
        res = self.checkPasswd(passwd, user)
        if res == -1:  # 多次输入的密码多次错误，锁定该卡，并退出该功能
            # 锁起来
            user.card.lock = True

            return -1
        user.card.money2 = input("请输入您要取出的金额:")
        print("您账户余额为:%s" % (int(user.card.money1) + int(user.card.money)-int(user.card.money2)))


    #   转账
    def translateMoney(self):
        cardNumber = input("请输入您要存入的卡号:")

        user = self.allUser.get(cardNumber)
        if user == None:
            #
            # 作业：可以输入三次卡号，超过三次，推出
            print("您输入的卡号不存在")
            return -1

            # 判断该卡是否已锁定
        if user.card.lock == True:
            print("此卡已经被锁定，无法取款")

            return -1
            # 输入密码（输入错误，则可以重新输入三次，就锁定）
        passwd = input("请输入您的密码")
        res = self.checkPasswd(passwd, user)
        if res == -1:  # 多次输入的密码多次错误，锁定该卡，并退出该功能
            # 锁起来
            user.card.lock = True

            return -1
        cardNumber2 = input("请输入您要转账的卡号:")
        if cardNumber2 == None:
            #作业,可以输入三次卡号,超过三次,退出
            return -1

    #   改密
    def editPasswd(self):
        pass

    #   锁卡
    def lockCard(self):
        pass

    #   解锁
    def unlockCard(self):
        pass

    #   补卡
    def fillCard(self):
        pass

    #   注销
    def killCard(self):
        pass
