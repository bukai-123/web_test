# class people:
#     def __init__(self,name,age,sex,ktc,zwjs):#__init__是一个初始化函数，这个函数传入的参数写在self后面。
#         self.name = name#把输入的参数name传给对象本身self。
#         self.age = age
#         self.ktc = ktc
#         self.zwjs = zwjs
#         # print(name)
#         # print(age)
#         # print(sex)
#     def koutouchan(self, string): #法一：类内部可以加其他函数，但这些函数的参数前面都要加上self
#         print(string)
#     def ziwojieshao(self):#法二：不给这个函数输入参数，直接使用
#         print(self.zwjs)
#
# caiji=people('caixukun',
#            25,
#            1,
#            "你干嘛哎哟",
#            "练习时长两年半") #初始化函数用于给定义为该类(people)的对象输入属性，并执行其自身内部的操作，（如上三个print）
# zhuangrirong=people('zhaungrirong',
#            21,
#            2,
#            "你好",
#            "荣哥")
#
# caiji.koutouchan('唱跳rap篮球')#iam是用people这个类定义出来的一个变量，可以直接在变量后面加个.然后使用这个变量所属的类(people)内的其他函数(koutouchan)
# caiji.ziwojieshao()#刚才定义的ziwojieshao函数并没有传入参数所以这里也不需要传参进来
# zhuangrirong.ziwojieshao()#同理
#
# print(caiji.name)#因为name是初始化函数__init__内的参数，不是类内的其他函数(如koutouchan)，所以不能直接这么输出，需要__init__内加上self.name = name

#
# class animal:
#     def __init__(self,name):#当父类animal的初始化函数__init__中有传入参数(如name)，
#         self.name = name
#     def sound(self):
#         pass
# class dog(animal):
#     def __init__(self):
#         super().__init__("旺财")##当父类animal的初始化函数__init__中有传入参数(如name)时，子类可以用super().__init__("")来继承父类的参数属性
#     def sound(self):
#         print("汪汪汪")
#
# def makesound(animal):#传进来的是一个大类，可以是一个父类也可以是一个子类，而且这个函数不分辨传进来的是什么动物，猫还是狗
#     animal.sound()#
# class cat(animal):
#     def __init__(self):
#         super().__init__("艾露猫")##当父类animal的初始化函数__init__中有传入参数(如name)时，子类可以用super().__init__("")来继承父类的参数属性
#     def sound(self):
#         print("喵喵喵")#子类cat和子类dog内都有这个名称的函数sound
#
# dog1=dog()#用dog类定义实例化dog1这一对象。
# cat1=cat()
# makesound(dog1)#将子类dog实例化的dog1传入，则调用的是子类dog中的sound
# makesound(cat1)#将子类cat实例化的cat1传入，则调用的是子类cat中的sound
#
# print(dog1.name)

class animal:
    burudongwu = True#这里是类的属性
    def __init__(self,name):
        self.__name = name#__name：说明拒绝继承，后面的子类无法继承这一属性
        print(self.__name,id(self.__name))#id表示获得地址
    def __eat(self):#__eat说明拒绝继承，后面的子类无法继承这一函数
        print('eating...')
    def sound(self):
        pass
a1=animal("旺财")
print(id(a1.burudongwu))#a1这一用animal类实例化的对象也具有类的属性animal