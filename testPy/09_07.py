__metaclass__ = type
#-*- coding: UTF-8 -*- 
class MyClass:
    val1 = 'Value 1'
    def __init__(self):
        self.val2 = 'Value 2'
    @staticmethod
    def staticmd():
		print 'static method'
    @classmethod
    def classmd(cls):
        print 'class method, class:' + str(cls) + ',val1:' + cls.val1 + ', cannot access val2', cls.val2