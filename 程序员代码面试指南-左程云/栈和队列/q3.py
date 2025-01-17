"""
问题描述：一个栈依次压入1、2、3、4、5，那么从栈顶到栈底分别为5、4、3、2、1。将这个栈
转置后，从栈顶到栈底为1、2、3、4、5，也就是实现栈中元素的逆序，要求：
只能用递归函数来实现和初始栈，不能使用其他数据结构，
思路：首先使用一个递归函数获取到栈底元素，再构造另外一个递归函数来进行reverse操作
"""

class ReverseStackTools:
    # 类方法可直接通过类调用
    @classmethod
    def getStackLast(cls, stack):
        result = stack.pop()
        if len(stack) == 0:
            return result
        else:
            last = cls.getStackLast(stack)
            stack.append(result)
            return last

    @classmethod
    def reverse(cls, stack):
        if len(stack) == 0:
            return
        else:
            last = cls.getStackLast(stack)
            cls.reverse(stack)
            stack.append(last)

if __name__ == '__main__':
    my_stack = [1, 2, 3]
    ReverseStackTools.reverse(my_stack)
    print(my_stack)