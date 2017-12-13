'''
使用pickle进行二进制IO（读写任意类型的Python数据，而不限于字符或字节）
'''
import pickle
from tkinter import filedialog

class Person:
    def __init__(self,name,age,hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies

    def __str__(self):
        return str({"name":self.name,"age":self.age,"hobbies":self.hobbies})

def pickleDumpOutput():
    global file
    savePath = filedialog.asksaveasfilename()
    file = open(savePath, mode="ab")
    data = [1, 2, 3]
    data = True
    data = Person("张三丰",100,["太极","八卦","喝茶"])
    pickle.dump(data, file)
    file.close()


def pickleLoadInput():
    global file
    with open(filedialog.askopenfilename(), mode="rb") as file:
        data = pickle.load(file)
        print(data,type(data))

        data = pickle.load(file)
        print(data,type(data))

        data = pickle.load(file)
        print(data,type(data))

        data = pickle.load(file)
        print(data,type(data))


pickleDumpOutput()
#pickleLoadInput()

