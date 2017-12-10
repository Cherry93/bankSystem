#用户类
class User(object):
    def __init__(self,name,IDNumber,phone,card):
        self.name = name    #用户名字
        self.IDNumber = IDNumber    #用户的身份证号
        self.phone = phone  #用户手机号
        self.card = card