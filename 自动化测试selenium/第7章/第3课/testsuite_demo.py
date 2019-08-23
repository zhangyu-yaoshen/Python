# -*- coding: UTF-8 -*-
import unittest

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
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


