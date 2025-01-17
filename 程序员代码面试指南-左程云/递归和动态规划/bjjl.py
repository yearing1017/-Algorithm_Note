'''
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
    插入一个字符
    删除一个字符
    替换一个字符
例如：
    输入：word1 = "horse", word2 = "ros"
    输出：3
    解释：
    horse -> rorse (将 'h' 替换为 'r')
    rorse -> rose (删除 'r')
    rose -> ros (删除 'e')
'''
'''
https://leetcode-cn.com/problems/edit-distance/solution/bian-ji-ju-chi-by-leetcode-solution/
https://leetcode-cn.com/problems/edit-distance/solution/zi-di-xiang-shang-he-zi-ding-xiang-xia-by-powcai-3/
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        row = len(word1)
        col = len(word2)

        # dp[i][j] 表示word1[1...i]变为word2[1...j]的编辑距离
        dp = [[0 for _ in range(col+1)]for _ in range(row+1)]

        # 第一行：word1由空字符串变为word2的步数  每次都新增一个字符
        for j in range(1, col+1):
            dp[0][j] = dp[0][j-1] + 1
        
        # 第一列：word1由原字符串变为word2空字符串的步数 每次都删除一个字符  
        for i in range(1, row+1):
            dp[i][0] = dp[i-1][0] + 1

        for i in range(1, row+1):
            for j in range(1, col+1):
                # 当尾部字符相等时 等价于去看前面的字符转换所需步数
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 三种情况取最小 + 1
                    # 情况1：word1:xxxxE word2:xxxxF 替换尾部字符 说明等于前面字符的转换次数 + word1的1次替换次数
                    # 情况2：word1:xxx  word2:xxxD   word1尾部添加字符   说明等于前面字符的转换次数 + word1的1次添加次数
                    # 情况3：word1:xxxD  word2:xxx   删除word1的尾部字符  说明等于前面字符的转换次数 + word1的1次删除次数
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]


