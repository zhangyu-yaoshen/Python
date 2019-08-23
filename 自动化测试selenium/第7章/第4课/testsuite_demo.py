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
        print(" test_one 二当家小D 来了")
        #断言是否相同
        self.assertEqual(self.name, "小D课堂",msg="名字不对")


    def test_two(self):
        print(" test_two 前端 来了")
        #断言是否为 true, msg是断言错误的提示信息
        self.assertFalse('XD'.isupper(), msg="不是大写")
        


    def test_three(self):
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

    #文件名中加了当前时间,每次生成不同的测试报告
    file_prefix = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())

    #创测试报告的result.html文件，此时还是个空文件   
    #wb 以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
    fp = open('./'+file_prefix+'_result.html', 'wb')
    #stream 定义报告所写入的文件；title 为报告的标题；description 为报告的说明与描述
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'<小D课堂>test report', description=u'用例执行情况:')

    #运行测试容器中的用例，并将结果写入的报告中
    runner.run(suite)

    #关闭文件流，将HTML内容写进测试报告文件
    fp.close()


