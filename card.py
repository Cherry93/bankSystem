#   银行卡的类
class Card(object):
    def __init__(self,cardNumbe,passwd,money=0,money1=0,money2=0):
        self.cardNumber = cardNumbe #银行卡卡号
        self.passwd = passwd    #银行卡密码
        self.money = money  #银行余额
        self.money1 = money1 #存入的钱
        self.money2 = money2#取出的钱
        self.lock = False   #此属性表示该卡是否锁定，默认是不锁定状态