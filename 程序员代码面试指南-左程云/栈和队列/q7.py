"""
问题描述：有一个整型数组arr和一个大小为w的窗口从数组的最左边滑到最右边，窗口每次向
右边滑一个位置。例如，数组为[4,3,5,4,3,3,6,7]，窗口大小为3时：
[4 3 5] 4 3 3 6 7      窗口中最大值为5
4 [3 5 4] 3 3 6 7      窗口中最大值为5
4 3 [5 4 3] 3 6 7      窗口中最大值为5
4 3 5 [4 3 3] 6 7      窗口中最大值为4
4 3 5 4 [3 3 6] 7      窗口中最大值为6
4 3 5 4 3 [3 6 7]      窗口中最大值为7

如果数组长度为n，窗口大小为w，则一共产生 n-w+1 个窗口的最大值。

请实现一个函数，要求：
1）输入整型数组arr，窗口大小为w
2）输出一个长度为 n-w+1 的数组res，res[i]表示每一种窗口状态下的最大值。以本题为例，
结果应该返回[5, 5, 5, 4, 6, 7]

思路：借助双端队列来保存上一个滑动窗口的值状态
"""

class MaxValueOFWindow:
    @classmethod
    def get_max_values(cls, arr, window):
        if len(arr) == 0 or window < 1 or len(arr) < window:
            return None

        index = 0
        deque = list()
        max_values = list()

        while index < len(arr):
            # 加入双端队列的规则：保证队列中队头存放的是最大的
            while len(deque) > 0 and arr[deque[-1]] <= arr[index]:
                deque.pop()
            deque.append(index)
            # 队头的下标过期了 即 不在大小为k的窗口内
            if deque[-1] - deque[0] >= window:
                deque.pop(0)
            # 遍历到大小为k的窗口时
            if index >= window - 1:
                max_values.append(arr[deque[0]])
            # 一步一步后移
            index += 1

        return max_values

if __name__ == '__main__':
    res = MaxValueOFWindow.get_max_values([4, 3, 5, 4, 3, 3, 6, 7], 3)
    print(res)
