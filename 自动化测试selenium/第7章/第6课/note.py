# -*- coding: UTF-8 -*-
import unittest
import HTMLTestRunner
import time

class XdclassTestCase(unittest.TestCase):
    def setUp(self):
        self.age = 32
        self.name = "小D课堂"
        print(" setUp method=======")


    def tearDown(self):
        print(" tearDown method=======")
        #断言是否相同
        self.assertEqual('foo'.upper(), 'FOO')


    def test_one(self):
        u"test_one方法"
        print(" test_one 二当家小D 来了")
        #断言是否相同
        self.assertEqual(self.name, "小D课堂",msg="名字不对")


    def test_two(self):
        u"test_TWO方法说明"
        print(" test_two 前端 来了")
        #断言是否为 true, msg是断言错误的提示信息
        self.assertTrue('XD'.isupper(), msg="不是大写")
        


    def test_three(self):
        u"这是首页登录测试用例"
        print(" test_three 后端 来了")
        self.assertEqual(self.age,32)



    def test_four(self):
        print(" test_four 小D课堂官网上线啦 https://www.xdclass.net")
        self.assertEqual(self.age,32)




if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(XdclassTestCase("test_two"))
    suite.addTest(XdclassTestCase("test_one"))
    
    suite.addTest(XdclassTestCase("test_three"))
    suite.addTest(XdclassTestCase("test_four"))

    #verbosity参数可以控制执行结果的输出，0 是简单报告、1 是一般报告（默认）、2 是详细报告
    #runner = unittest.TextTestRunner(verbosity=2)
    #runner.run(suite)
    #文件名中加了当前时间，为了每次生成不同的测试报告
    file_prefix = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    print(file_prefix)
    #创建测试报告，此时这个文件还是空文件
    # wb 以二进制格式打开一个文件，只用于写入，如果文件存在则覆盖，不存在则创建
    fp = open("./"+file_prefix+"_result.html","wb")
    # stream定义一个测试报告写入的文件，title就是标题，description就是描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"小D课堂 测试报告",description=u"测试用例执行情况")
    
    runner.run(suite)
    fp.close()

   
