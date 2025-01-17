# 统计一个数字在升序数组中出现的次数
# 例如 [1,2,3,3,3,3,4,5],3  返回4
def GetNumberOfK(data, k):
    low = getlow(data,k)
    print(low)
    high = gethigh(data,k)
    print(high)
    return high - low + 1

# 获取到 target第一次出现的下标 若数字大于最大的 则返回len(nums)
def getlow(data, k):
    l = 0
    r = len(data) - 1
    while l <= r:
        mid = (l+r) // 2
        if data[mid] < k:
            l = mid + 1
        else:
            r = mid - 1
    return l

# 获取到 target最后一次出现的下标 若数字小于最小的 则返回-1
def gethigh(data, k):
    l = 0
    r = len(data) - 1
    while l <= r:
        mid = (l+r)//2
        if data[mid] <= k:
            l = mid + 1
        else:
            r = mid - 1
    return r

nums = [1,2,3,3,3,3,3,3]
k = 3
print(GetNumberOfK(nums, k))