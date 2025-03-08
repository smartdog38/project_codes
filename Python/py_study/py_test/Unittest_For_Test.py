#################################################################################################
#################################################################################################
"""

单元测试（unittest）
Python 标准库中的一个单元测试框架，用于编写和运行测试用例

"""
#################################################################################################
"""

基本概念

"""
#################################################################################################

# 测试用例（TestCase）：一个测试用例是一个独立的测试单元，通常对应一个类，继承自 unittest.TestCase
# 测试方法（Test Method）：测试用例中的每个以 test_ 开头的方法都是一个测试方法
# 测试套件（Test Suite）：一组测试用例或测试方法的集合
# 测试运行器（Test Runner）：用于执行测试用例并输出结果的工具

#################################################################################################
"""

测试用例

"""
#################################################################################################

# 测试用例类需要继承 unittest.TestCase，并且测试方法以 test_ 开头
import unittest


class TestMathOperations(unittest.TestCase):
    def test_add(self):
        # assertEqual 是断言方法，用于验证结果是否符合预期
        self.assertEqual(1 + 1, 2)

    def test_subtract(self):
        self.assertEqual(3 - 1, 2)

    def test_multiply(self):
        self.assertEqual(2 * 3, 6)

    def test_divide(self):
        self.assertEqual(6 / 2, 3)


if __name__ == "__main__":
    # 在终端里输入 python D:\code\Python\py_study\py_test\Unittest_For_Test.py
    # 会运行每个 test_ 开头的函数
    unittest.main()

# ....
# ----------------------------------------------------------------------
# Ran 4 tests in 0.001s
#
# OK

# . 表示一个测试通过

#################################################################################################
"""

断言方法
unittest 提供了多种断言方法，用于验证测试结果

"""
#################################################################################################

# assertEqual(a, b)	验证 a == b
# assertNotEqual(a, b)	验证 a != b
# assertTrue(x)	验证 x 为 True
# assertFalse(x)	验证 x 为 False
# assertIs(a, b)	验证 a is b
# assertIsNot(a, b)	验证 a is not b
# assertIsNone(x)	验证 x is None
# assertIsNotNone(x)	验证 x is not None
# assertIn(a, b)	验证 a in b
# assertNotIn(a, b)	验证 a not in b
# assertRaises(exception, callable, *args, **kwargs)	验证 callable 抛出指定异常

#################################################################################################
"""

测试套件
测试套件用于组织多个测试用例或测试方法

"""
#################################################################################################

import unittest


class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_subtract(self):
        self.assertEqual(3 - 1, 2)


class TestStringOperations(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("hello".upper(), "HELLO")


# 创建测试套件
suite = unittest.TestSuite()
# 添加测试用例，以 TestClsdd('test_method') 来添加
suite.addTest(TestMathOperations('test_add'))
suite.addTest(TestStringOperations('test_upper'))

# 运行测试套件
# 添加执行器
runner = unittest.TextTestRunner()
# 执行套件
runner.run(suite)

#################################################################################################
"""

setUp 和 tearDown
setUp：在每个测试方法运行之前执行，用于初始化测试环境
tearDown：在每个测试方法运行之后执行，用于清理测试环境

"""
#################################################################################################

# import unittest
#
# class TestDatabase(unittest.TestCase):
#     def setUp(self):
#         # 初始化数据库连接
#         self.db = Database()
#         self.db.connect()
#
#     def tearDown(self):
#         # 关闭数据库连接
#         self.db.disconnect()
#
#     def test_query(self):
#         result = self.db.query("SELECT * FROM users")
#         self.assertIsNotNone(result)
#
#
# if __name__ == "__main__":
#     unittest.main()

#################################################################################################
"""

跳过测试
可以使用 @unittest.skip 装饰器跳过某些测试

"""
#################################################################################################

import unittest


class TestSkip(unittest.TestCase):
    # @unittest.skip("message")
    @unittest.skip("暂时跳过")
    def test_skip(self):
        self.fail("This test should be skipped")
    # 可以带上条件，带条件时为 @unittest.skipIf(condition ,"message")
    # 就像 if condition 就测试
    @unittest.skipIf(1 > 0, "条件为真时跳过")
    def test_skip_if(self):
        self.fail("This test should be skipped if condition is true")


if __name__ == "__main__":
    unittest.main()

#################################################################################################
#################################################################################################