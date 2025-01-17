"""
问题描述:设计一种缓存结构,该结构在构造时确定大小,假设大小为K,并且有两个功能,
1.set(key, value):将记录(key, value)插入该结构
2.get(key):返回key对应的value值.

要求:
1.set和get方法的时间复杂度为O(1)
2.某个key的set或者get操作一旦发生,认为这个key的记录成了最经常使用的.
3.当缓存的大小超过Ｋ时,移除最不经常使用的记录,即set或者get最久的.
"""

# 建立双向链表的结点
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None

# 双向链表
class DoubleNodeList:
    def __init__(self):
        self.tail = None
        self.head = None

    # 将新加入的结点放在尾部 并将其设置为新的尾部
    def add(self, node):
        if not node:
            return
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.pre = self.tail
            self.tail = node

    # 将链表中的任意节点分离出来 放到尾部
    def move_to_tail(self, node):
        if self.tail == node:
            return
        if self.head == node:
            # 先分离
            self.head = node.next
            self.head.pre = None
        else:
            node.pre.next = node.next
            node.next.pre = node.pre
        # 将node放到尾部
        node.pre = self.tail
        node.next = None
        self.tail.next = node
        self.tail = node
    # 移除head并返回  将head设置为下一个
    def remove_head(self):
        if self.head is None:
            return
        res = self.head

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = res.next
            res.next = None
            self.head.pre = None

        return res

class LRUCache:
    def __init__(self, k):
        self.cap = k # 容量
        self.data_container = dict() # key-node
        self.key_container = dict() #node-key
        self.node_list = DoubleNodeList()
    # 一旦set或get 就将key对应的node调整到尾部 表示最常使用
    # 一旦cap满了  就移除当前的头部 头部表示最不常使用
    def set(self, key, value):
        if key in self.data_container:
            node = self.data_container[key]
            node.value = value
            self.node_list.move_to_tail(node)
        else:
            node = Node(value)
            self.data_container[key] = node
            self.key_container[node] = key
            self.node_list.add(node)
            if len(self.data_container) > self.cap:
                res = self.node_list.remove_head()
                key = self.key_container.get(res)
                self.data_container.pop(key)
                self.key_container.pop(res)

    def get(self, key):
        if key not in self.data_container:
            return -1

        node = self.data_container[key]
        self.node_list.move_to_tail(node)

        return node.value

    def get_all(self):
        #return [node.value for node in self.data_container.values()]
        head = self.node_list.head
        while head:
            print(head.value, end='')
            head = head.next

class Solution:
    def __init__(self):
        self.LRUca = None
    def LRU(self , operators , k ):
        # write code here
        self.LRUca = LRUCache(k)
        ret=[]
        SET=1
        GET=2
        for items in operators:
            if items[0]==SET:
                self.LRUca.set(str(items[1]), items[2])
            elif items[0]==GET:
                ret.append(self.LRUca.get(str(items[1])))
        return ret

# 牛客 解法
class Solution:
    dic_lru = {}
    list_lru = []

    def set(self, key, val, k):
        self.dic_lru[key] = val
        # 列表负责记录key的常用(尾部) 不常用情况（头部）
        self.list_lru.append(key)
        # 超出长度时  先排出一个
        if len(self.list_lru) > k:
            del self.dic_lru[self.list_lru[0]]
            del self.list_lru[0]
    
    def get(self, key):
        if key in self.dic_lru:
            # 先把这个key移除
            self.list_lru.remove(key)
            # 再添加到尾部 代表常用
            self.list_lru.append(key)
            return self.dic_lru[key]
        return  -1

    def LRU(self, operators, k):
        res = []
        SET = 1
        GET = 2
        for items in operators:
            if items[0] == SET:
                self.set(str(items[1]), items[2], k)
            elif items[0] == GET:
                res.append(self.get(str(items[1])))
        return res
    

if __name__ == '__main__':
    '''
    cache = LRUCache(3)
    cache.set('A', 1)
    cache.set('B', 2)
    cache.set('C', 3)
    print(cache.get('A'))
    cache.set('D', 4)
    print(cache.get_all())
    '''
    s = Solution()
    res = s.LRU([[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]],3)
    print(res)

