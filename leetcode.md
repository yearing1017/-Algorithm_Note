# LeetCode
- 此文用来记录自己在leetcode上的simple题集解决方案。

## 1. 两数之和

- 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。

- 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

  > 示例:
  >
  > 给定 nums = [2, 7, 11, 15], target = 9
  >
  > 因为 nums[0] + nums[1] = 2 + 7 = 9
  > 所以返回 [0, 1]

- **思路：两个for循环暴力**

```
int* twoSum(int* nums, int numsSize, int target) {
  static int a[2]={0};
  for (int i = 0; i < numsSize - 1; i++)
  {
    for (int j = i+1; j < numsSize; j++)
    {
      if (nums[i] + nums[j] == target)
      {
        a[0] = i;
        a[1] = j;
        return a;
      }
    }
  }
  return 0;
}
```

## 7. 整数反转

- **题目描述**

  - 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

  > 输入: 123
  > 输出: 321
  >
  > 输入: -123
  > 输出: -321
  >
  > 输入: 120
  > 输出: 21

  - 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

- 通过循环将数字x的每一位拆开，在计算新值时每一步都判断是否溢出。

  - 溢出条件有两个，**一个是大于整数最大值MAX_VALUE，另一个是小于整数最小值MIN_VALUE，**设当前计算结果为ans，下一位为pop。

  - **从ans * 10 + pop > MAX_VALUE这个溢出条件来看:**
    当出现 ans > MAX_VALUE / 10 且 还有pop需要添加 时，则一定溢出;
    当出现 ans == MAX_VALUE / 10 且 pop > 7 时，则一定溢出，7是2^31 - 1的个位数;

    **不知道最后一位是7可以这样思考：`pop > Integer.MAX_VALUE%10`**

  - **从ans * 10 + pop < MIN_VALUE这个溢出条件来看:**
    当出现 ans < MIN_VALUE / 10 且 还有pop需要添加 时，则一定溢出
    当出现 ans == MIN_VALUE / 10 且 pop < -8 时，则一定溢出，8是-2^31的个位数

  - **不知道最后一位是-8可以这样思考：`pop < Integer.MIN_VALUE%10`**

```java
class Solution {
    public int reverse(int x) {
         int res = 0;
         while(x!=0){
             int pop = x%10;
             if(res > Integer.MAX_VALUE/10 || (res==Integer.MAX_VALUE/10 && pop > Integer.MAX_VALUE%10))
                 return 0;
             if(res < Integer.MIN_VALUE/10 || (res==Integer.MIN_VALUE/10 && pop < Integer.MIN_VALUE%10))
                 return 0;
             res = res*10 + pop;
             x /=10;
         }
        return res;
    }
}
```

## 9. 回文数

- 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

> 示例 1:
> 输入: 121
> 输出: true
>
> 示例 2:
> 输入: -121
> 输出: false
> 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
>
> 示例 3:
> 输入: 10
> 输出: false
> 解释: 从右向左读, 为 01 。因此它不是一个回文数。

- **进阶:**

  你能不将整数转为字符串来解决这个问题吗？

- 代码如下：

```java
class Solution {
    public boolean isPalindrome(int x) {
        int sum = 0;
        int temp = x;
        if(x<0){
            return false;
        }
        if(x==0){
            return true;
        }
        else{
            while(x!=0){
                int a = x%10;
                sum = sum *10 + a;
                x/=10;
            }
            return sum==temp;
        }
    }
}
```

## 13. 罗马数字转数字

- 罗马数字包含以下七种字符: `I`， `V`， `X`， `L`，`C`，`D` 和 `M`。

> 字符          数值
> I             1
> V             5
> X             10
> L             50
> C             100
> D             500
> M             1000

- 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 

- 通常情况下，罗马数字中小的数字在大的数字的右边。但也
- 存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
  - I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
  - X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
  - C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

- 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

> 示例 1:
>
> 输入: "III"
> 输出: 3
> 示例 2:
>
> 输入: "IV"
> 输出: 4
> 示例 3:
>
> 输入: "IX"
> 输出: 9
> 示例 4:
>
> 输入: "LVIII"
> 输出: 58
> 解释: L = 50, V= 5, III = 3.
> 示例 5:
>
> 输入: "MCMXCIV"
> 输出: 1994
> 解释: M = 1000, CM = 900, XC = 90, IV = 4.

- **思路：**
  - 从一开始判断num（后面的）是否比prenum（前面的）小，如果小，证明要加prenum。
  - 如果大，则要减去prenum，num和prenum移动位置。一直到最后一个数。
  - 最后的prenum肯定要加上。

- 代码：

```java
class Solution {
    public int romanToInt(String s) {
        int sum = 0;
        int prenum = Solution.getValue(s.charAt(0));
        for(int i=1; i<s.length(); i++){
            int num = Solution.getValue(s.charAt(i));
            if(num < prenum || num == prenum){
                sum += prenum;
            }
            else{
                sum -= prenum;
            }
            prenum = num;
        }
        sum = sum + prenum;
        return sum;
    }
    public static int getValue(char a){
        switch(a) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }
}
```

## 14. 最长公共前缀

- 编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 `""`。

> 示例 1:
>
> 输入: ["flower","flow","flight"]
> 输出: "fl"
> 示例 2:
>
> 输入: ["dog","racecar","car"]
> 输出: ""
> 解释: 输入不存在公共前缀。

- **说明:** 所有输入只包含小写字母 `a-z` 。

- **自己的思路，有点麻烦，最终结果是：**

> 执行用时 :1 ms, 在所有 java 提交中击败了93.91%的用户
>
> 内存消耗 :37.8 MB, 在所有 java 提交中击败了71.58%的用户

- **记录一下自己的思路：**
  - 首先排除一些最容易想到的特例：
  - 如果没有字符串，则返回空；
  - 如果只有一个字符串，则返回第一个字符串；
  - 遍历所有的字符串，找出最短的字符串，首先设定strs[0]是最短的，再往下依次取代；
  - 遍历过程中，若发现有一个空串，则返回空；
  - 找到最短字符串之后，将其余的串一个字符一个字符与之比较，找一个最短的长度。
  - 一开始设定min_num很大，如果找不到j来代替这个值，说明字符串都相等。
  - 最后一步就是根据上述两种情况进行截取。
- 代码：

```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
         if(strs.length == 0){
             return "";
         }
         if(strs.length == 1){
             return strs[0];
         }
         int min_length = strs[0].length();
         int flag = 0;//标记最短串的位置
         int min_num = Integer.MAX_VALUE; //记录最短的相同串的长度
         //循环遍历出最短字符串
         for(int i=0; i<strs.length; i++){
             if(strs[i].length()==0){
                 return "";
             }
             if(strs[i].length() < min_length){
                 min_length = strs[i].length();
                 flag = i;
             }
             else{
                 continue;
             }
         }
         //对每个字符串与strs[flag]相比较
         for(int i=0; i<strs.length; i++){
             if(flag==i){
                 continue;
             }
             for(int j=0;j<min_length;j++){
                 if(strs[flag].charAt(j)!=strs[i].charAt(j)){
                     if(j<min_num){
                         min_num = j;
                     }
                 }
             }
         }
         if(min_num != Integer.MAX_VALUE){
             return strs[flag].substring(0,min_num);
         }else{
             return strs[flag];
         }
    }
}
```

- **官方题解：**

```java
public String longestCommonPrefix(String[] strs) {
   if (strs.length == 0) return "";
   String prefix = strs[0];
   for (int i = 1; i < strs.length; i++)
       while (strs[i].indexOf(prefix) != 0) {
           prefix = prefix.substring(0, prefix.length() - 1);
           if (prefix.isEmpty()) return "";
       }        
   return prefix;
}
```

## 20. 有效的括号

- 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
- 有效字符串需满足：
  - 左括号必须用相同类型的右括号闭合。
  - 左括号必须以正确的顺序闭合。
  - 注意空字符串可被认为是有效字符串。

> 示例 1:
>
> 输入: "()"
> 输出: true
> 示例 2:
>
> 输入: "()[]{}"
> 输出: true
> 示例 3:
>
> 输入: "(]"
> 输出: false
> 示例 4:
>
> 输入: "([)]"
> 输出: false
> 示例 5:
>
> 输入: "{[]}"
> 输出: true

- **思路记录：栈的典型应用**
  - 首先要把对应的括号进行匹配，python可用字典，java这里用的是hashmap。
  - 从开始遍历字符串，将字符串转换为字符数组，对每个字符进行判断：
  - 若为左边的起始括号，例如"("、"["、"{"，直接push进栈；
  - 若为右边的结束括号，则要进行判断，若栈为空，则直接返回false，因为栈里面没有与之匹配的元素了
  - 若栈不空，但是取出top元素，不与对应的map中的值对应，则不匹配，返回false；
  - 注意上面一步，已经取出了栈顶元素，匹配则返回true，不匹配则返回false，所以在遍历完：
  - 有两种情况：1.偶数，遍历完且匹配成功，栈空；2.奇数，栈不空，但是有不匹配的；
  - 所以此时返回stack.isEmpty();对应上面的两种情况。
- **代码：**

```java
class Solution {
    public boolean isValid(String s) {
        int len = s.length();
        if(len == 0){
            return true;
        }
        //HashMap 键值对
        HashMap<Character,Character> map = new HashMap();
        map.put(')','(');
        map.put(']','[');
        map.put('}','{');

        Stack<Character> stack = new Stack();

        for(char ch: s.toCharArray()){
            if(ch=='('||ch=='['||ch=='{'){
                stack.push(ch);
            }

            if((ch==')'||ch==']'||ch=='}') &&(stack.isEmpty() || stack.pop()!=map.get(ch))){
                return false;
            }
        }
        return stack.isEmpty();
    }
}
```

## 21. 合并两个有序链表

- 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

> 示例：
>
> 输入：1->2->4, 1->3->4
> 输出：1->1->2->3->4->4

- **思路解析：**
  - 创建了一个新的结点，根据比较两个链表元素的大小进行插入到新的结点之后。
  - 谁小谁就链接到后面，且新建的p结点和l1、l2结点的指针都向后移动。
  - 如果有一条链表到头了，那就将新的p结点指针指向没空的另一条链表剩余元素。
- **代码：**

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null){
            return l2;
        }
        if(l2 == null){
            return l1;
        }
        ListNode p = new ListNode(0);
        ListNode head = p;//存下来p的位置，后面要移动
        while(l1!=null && l2!=null){
            if(l1.val<=l2.val){
                p.next = l1;
                p = p.next;
                l1 = l1.next;
            }else{
                p.next = l2;
                p = p.next;
                l2 = l2.next;
            }
        }
        if(l1==null){
            p.next = l2;
        }else{
            p.next = l1;
        }

        return head.next;
    }
}
```

## 26. 删除排序数组中的重复项

- 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

> 示例 1:
>
> 给定数组 nums = [1,1,2], 
>
> 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
>
> 你不需要考虑数组中超出新长度后面的元素。
> 示例 2:
>
> 给定 nums = [0,0,1,1,1,2,2,3,3,4],
>
> 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
>
> 你不需要考虑数组中超出新长度后面的元素。

- **思路分析：**
  - 两个指针i和j，从头开始遍历，j首先固定不变，i在变化，直到找到不相等的元素；
  - 因为已经是排好序的数组，所以肯定相等的元素都相邻；
  - 找到不相等的元素，使i对应的该元素赋值到之前的相等的某个元素上，那个元素就是相等的第2个。
  - 例如：1，1，2就将2赋给第二个1。1，1，1，2就将2赋给第二个1。
  - 最后j的位置就在不重复的倒数第二个位置，所以返回j+1。
- **代码：**

```python
class Solution {
    public int removeDuplicates(int[] nums) {
        int j=0;
        for(int i=0; i<nums.length; i++){
            if(nums[i] != nums[j]){
                j = j+1;
                nums[j] = nums[i];
            }
        }
        return j+1;
    }
}
```

## 27. 移除元素

- 给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
- 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
- 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

> 示例 1:
>
> 给定 nums = [3,2,2,3], val = 3,
>
> 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
>
> 你不需要考虑数组中超出新长度后面的元素。
> 示例 2:
>
> 给定 nums = [0,1,2,2,3,0,4,2], val = 2,
>
> 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
>
> 注意这五个元素可为任意顺序。
>
> 你不需要考虑数组中超出新长度后面的元素。

- **思路分析**
  - 遍历数组nums，每次取出的数字变量为num，同时设置一个下标ans
  - 在遍历过程中如果出现数字与需要移除的值不相同时，则进行拷贝覆盖nums[ans] = num，ans自增1
  - 如果相同的时候，则跳过该数字不进行拷贝覆盖，最后ans即为新的数组长度
  - 这种思路在移除元素较多时更适合使用，最极端的情况是全部元素都需要移除，遍历一遍结束

- **代码**

```java
class Solution {
    public int removeElement(int[] nums, int val) {
        int loc = 0;
        for(int num: nums){
            if(num!= val){
                nums[loc] = num;
                loc++;
            }
        }
        return loc;
    }
}

```

### 35. 搜索插入位置

- 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
- 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。你可以假设数组中无重复元素。

> 示例 1:
>
> 输入: [1,3,5,6], 5
> 输出: 2
> 示例 2:
>
> 输入: [1,3,5,6], 2
> 输出: 1
> 示例 3:
>
> 输入: [1,3,5,6], 7
> 输出: 4
> 示例 4:
>
> 输入: [1,3,5,6], 0
> 输出: 0

- 思路：
  - 首先排除两个边界，对极限情况进行考虑
  - 其次考虑中间有大于等于，就返回该索引位置
- 代码如下：

```java
class Solution {
    public int searchInsert(int[] nums, int target) {
        int loc = 0;
        if(nums[0]>target){
            return 0;
        }
        if(nums[nums.length-1]<target){
            return nums.length;
        }
        for(int i=0; i< nums.length; i++){
            if(nums[i] >= target){
                loc = i;
                break;
            }
        }
        return loc;
    }
}

```
## 38. 报数

- 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

> 1. 1
>
> 2. 11
>
> 3. 21
>
> 4. 1211
>
> 5. 111221
>
>    
>
>    1 被读作  "one 1"  ("一个一") , 即 11。
>    11 被读作 "two 1s" ("两个一"）, 即 21。
>    21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
>
> 
>
> 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
>
> 注意：整数顺序将表示为一个字符串。
>
>  示例 1:
>
> 输入: 1
> 输出: "1"
>
> 示例 2:
>
> 输入: 4
> 输出: "1211"

- **解题思路**
  - 函数从str='1'开始向后求
  - 使用两个循环，外层循环控制求到第几个数，内存循环求该数
  - 函数中取pre和j两个元素，相当于使用两个指针来判断前面的和后面相邻的是否相等
  - 相等则计数++，计算出有多少该元素，添加count+字符
  - 若不相等，则直接添加1+该字符，并且挪动pre至后方元素，j也随之挪动，count恢复为1
  - 外层每次结束一次循环，求得第n个数
- **代码**

```java
class Solution {
    public String countAndSay(int n) {
        String str = "1";
        for (int i = 2; i <= n; i++) {
            StringBuilder builder = new StringBuilder();
            char pre = str.charAt(0);
            int count = 1;
            for (int j = 1; j < str.length(); j++) {
                char c = str.charAt(j);
                if (c == pre) {
                    count++;
                } else {
                    builder.append(count).append(pre);
                    pre = c;
                    count = 1;
                }
            }
            builder.append(count).append(pre);
            str = builder.toString();
        }
        return str;
    }
}
```

## 53. 最大子序和

- 给定整数数组 `nums` ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

  > 示例:
  >
  > 输入: [-2,1,-3,4,-1,2,1,-5,4],
  > 输出: 6
  > 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

- **解题思路：**
  - 定义一个局部临时sum，初始赋值为0，用来存储当前的局部子序和
  - 定义结果res，初始赋值为nums[0]
  - 因为数组中有正负数，所以要去判断临时sum的大小
  - 若sum>0，说明无论后面的数正负，都要加该数
  - 但是如果当前sum<0，就要舍弃sum，因为会减小后面继续加和。
  - 舍弃sum，就要将当前的sum赋值循环中的num，继续从此数开始加和

- 代码

```java
class Solution {
    public int maxSubArray(int[] nums) {
        int res = nums[0];
        int sum = 0;
        for(int num: nums){
            if(sum>0){
                sum += num;
            }else{
                sum = num;
            }
            res = Math.max(res, sum);
        }
        return res;
    }
}
```

- 更多详细解法：[最大子序和 c++实现四种解法 暴力法、动态规划、贪心法和分治法 图示讲解](https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-cshi-xian-si-chong-jie-fa-bao-li-f/)

## 58. 最后一个单词的长度

- 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
- 如果不存在最后一个单词，请返回 0 。
- 说明：一个单词是指由字母组成，但不包含任何空格的字符串。

> 示例:
>
> 输入: "Hello World"
> 输出: 5

- 解法一思路：
  - 从字符串末尾开始向前遍历，其中主要有两种情况：
  - **第一种情况**，以字符串"Hello World"为例，从后向前遍历直到遍历到头或者遇到空格为止，即为最后一个单词"World"的长度5；
  - **第二种情况**，以字符串"Hello World "为例，需要先将末尾的空格过滤掉，再进行第一种情况的操作，即认为最后一个单词为"World"，长度为5；
  - **所以完整过程为先从后过滤掉空格找到单词尾部，再从尾部向前遍历，找到单词头部，最后两者相减，即为单词的长度**。
  - 时间复杂度：O(n)，n为结尾空格和结尾单词总体长度。

- 代码：

```java
class Solution {
    public int lengthOfLastWord(String s) {
        int end = s.length() - 1;
        while(end >= 0 && s.charAt(end) == ' ') end--;
        if(end < 0) return 0;
        int start = end;
        while(start >= 0 && s.charAt(start) != ' ') start--;
        return end - start;
    }
}
```

- 解法二：
  - 首先使用`strim`函数去除首尾空格
  - 再使用Java的寻找最后一个空格位置函数，末尾-空格位置即单词长度
- 代码：

```java
class Solution {    
    public  int lengthOfLastWord(String s) {
    	//空串
    	s=s.trim();
    	if(s.length()==0){
    		return 0;
    	}
    	int lastEmptyIndex =s.lastIndexOf(" ");
        return s.length()-1-lastEmptyIndex;
    }
}
```
## 66. 加一

- 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
- 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
- 你可以假设除了整数 0 之外，这个整数不会以零开头。

> 示例 1:
>
> 输入: [1,2,3]
> 输出: [1,2,4]
> 解释: 输入数组表示数字 123。
> 示例 2:
>
> 输入: [4,3,2,1]
> 输出: [4,3,2,2]
> 解释: 输入数组表示数字 4321。

- **思路**：
  - 首先要判断末尾是不是9，若为9，则变为0，在此情况后还需考虑后面数字是否为9，以便连续进位。
  - 若不是9，直接将末尾加1，返回该数组。
  - 若产生进位，则要根据是否如99，999该数一样会多一位，返回新的数组，首尾直接置为1，其余为0.
- **代码**：

```java
class Solution {
    public int[] plusOne(int[] digits) {
        
        for(int i=digits.length-1;i>=0;i--){
            if(digits[i]==9){//此位为9，需要进位
                digits[i]=0;
                continue;
            }
            if(digits[i]!=9){
                digits[i]+=1;
                break;
            }
        }

        int[] ans=new int[digits.length+1];# int数组默认为0
        ans[0]=1;
        if(digits[0]==0)return ans;
        else return digits;
    }
}
```

## 67. 二进制求和

- 给定两个二进制字符串，返回他们的和（用二进制表示）。
- 输入为**非空**字符串且只包含数字 `1` 和 `0`。

> 示例 1:
>
> 输入: a = "11", b = "1"
> 输出: "100"
> 示例 2:
>
> 输入: a = "1010", b = "1011"
> 输出: "10101"

- **思路**
  - 利用enumerate枚举方法可以得到索引和数字，算出结果
  - 相加求和
  - 再求出二进制数

- **代码**

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a==b=='0':
            return "0"
        num1 = num2 = 0;
        # enumerate方法返回索引+数字的二元组
        for i,x in enumerate(a):
            num1 += int(x)*(2**(len(a)-i-1))
        for i,x in enumerate(b):
            num2 += int(x)*(2**(len(b)-i-1))
        num = num1 + num2
        res = ''
        while num > 1:
            num_temp = num%2
            res += str(num_temp)
            num = num//2
        res+='1' 
        return res[::-1] # 倒序遍历字符串
```
## 69. x的平方根

- 实现 int sqrt(int x) 函数。
- 计算并返回 x 的平方根，其中 x 是非负整数。
- 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

> 示例 1:
>
> 输入: 4
> 输出: 2
> 示例 2:
>
> 输入: 8
> 输出: 2
> 说明: 8 的平方根是 2.82842..., 
> 由于返回类型是整数，小数部分将被舍去。

- **解题思路：**
  - 采用二分法无限逼近正确值
  - 当max和min差1以上的情况下，m为中值
  - 根据x/m大于m还是小于等于m，来挪动指针max和min
- **代码：**

```java
class Solution {
    public int mySqrt(int x) {
        if(x==0||x==1){
            return x;
        }
        int min = 0;
        int max = x;
        while(max - min >1){
            int m = (min+max)/2;
            if(x/m<m){
                max = m; //x/m比m小，说明除的m大了点，去左半部分逼近m
            }else{
                min = m;//x/m比m大,或者等于m，说明除的m小了点，去右半部分继续逼近m
            }
        }
        return min;
    }
}
```
## 70. 爬楼梯

- 假设你正在爬楼梯。需要 *n* 阶你才能到达楼顶。

- 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

- **注意：**给定 *n* 是一个正整数。

  > 示例 1：
  >
  > 输入： 2
  > 输出： 2
  > 解释： 有两种方法可以爬到楼顶。
  >
  > 1.  1 阶 + 1 阶
  > 2.  2 阶
  >     示例 2：
  >
  > 输入： 3
  > 输出： 3
  > 解释： 有三种方法可以爬到楼顶。
  >
  > 1.  1 阶 + 1 阶 + 1 阶
  > 2.  1 阶 + 2 阶
  > 3.  2 阶 + 1 阶

- **思路：**

  - 此题可以采用**动态规划**的思想，将大问题分为子问题，爬第n阶楼梯的方法数量，等于 2 部分之和：
  - 1. **爬上 n-1阶楼梯的方法数量。因为再爬1阶就能到第n阶**
  - 2. **爬上 n-2 阶楼梯的方法数量，因为再爬2阶就能到第n阶**
  - 所以我们得到公式 $dp[n] = dp[n-1] + dp[n-2]$
  - 同时需要初始化 $dp[1]=1 和 dp[2]=2$
  - 时间复杂度：$O(n)$

- **代码：**

```java
class Solution {
    public int climbStairs(int n) {
        int[] dp = new int[n + 2];
        dp[1] = 1;
        dp[2] = 2;
        for(int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
}
```

- 注：**使用递归，反馈超时**

## 83. 删除排序链表中的重复元素

- 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

  > 示例 1:
  >
  > 输入: 1->1->2
  > 输出: 1->2
  > 示例 2:
  >
  > 输入: 1->1->2->3->3
  > 输出: 1->2->3

- **代码**

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *p = head;
        ListNode *q;
        while(p!=NULL&&p->next!=NULL)
        {
            if(p->val==p->next->val)
            {
                q=p->next;
                p->next =q ->next;
                delete q;
            }
            else
            {
                p = p->next;
            }
        }
        return head;
    }
};
```

## 88. 合并两个有序数组

- 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

- 说明:

  - 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
  - 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

- 示例:

- > 输入:
  > nums1 = [1,2,3,0,0,0], m = 3
  > nums2 = [2,5,6],       n = 3
  >
  > 输出: [1,2,2,3,5,6]

- **思路**
  - **从后向前数组遍历**
  - 因为 nums1 的空间都集中在后面，所以从后向前处理排序的数据会更好，节省空间，一边遍历一边将值填充进去
  - 设置指针 len1 和 len2 分别指向 nums1 和 nums2 的有数字尾部，从尾部值开始比较遍历，同时设置指针 len 指向 nums1 的最末尾，每次遍历比较值大小之后，则进行填充
  - 当 len1<0 时遍历结束，此时 nums2 中海油数据未拷贝完全，将其直接拷贝到 nums1 的前面，最后得到结果数组
  - 时间复杂度：O(m+n)

- **代码**

```python
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int len1 = m - 1;
        int len2 = n - 1;
        int len = m + n - 1;
        while(len1 >= 0 && len2 >= 0) {
            // 注意--符号在后面，表示先进行计算再减1，这种缩写缩短了代码
            nums1[len--] = nums1[len1] > nums2[len2] ? nums1[len1--] : nums2[len2--];
        }
        // 表示将nums2数组从下标0位置开始，拷贝到nums1数组中，从下标0位置开始，长度为len2+1
        System.arraycopy(nums2, 0, nums1, 0, len2 + 1);
    }
}
```

## 100. 相同的树

- 给定两个二叉树，编写一个函数来检验它们是否相同。
- 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

> **示例 1:**
>
> ```
> 输入:       1         1
>           / \       / \
>          2   3     2   3
> 
>         [1,2,3],   [1,2,3]
> 
> 输出: true
> ```
>
> **示例 2:**
>
> ```
> 输入:      1          1
>           /           \
>          2             2
> 
>         [1,2],     [1,null,2]
> 
> 输出: false
> ```
>
> **示例 3:**
>
> ```
> 输入:       1         1
>           / \       / \
>          2   1     1   2
> 
>         [1,2,1],   [1,1,2]
> 
> 输出: false
> ```

- **思路：**
  - 判断根节点的情况
  - 递归
- **代码：**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # p,q 都为none
        if not p and not q:
            return True
        # 一个为none
        if not p or not q:
            return False
        # 都不为none
        if p and q:
            if p.val == q.val:
                # 递归判断子树
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
```

## 101. 对称二叉树

- 给定一个二叉树，检查它是否是镜像对称的。
- 例如，二叉树 `[1,2,2,3,4,4,3]` 是对称的。

> ```
>     1
>    / \
>   2   2
>  / \ / \
> 3  4 4  3
> ```

- 但是下面这个 `[1,2,2,null,3,null,3]` 则不是镜像对称的:

> ```
>     1
>    / \
>   2   2
>    \   \
>    3    3
> ```

- **思路：单独写一个函数去递归，也可在原函数中递归**
- **代码：**

```python
class Solution:
    def dfs(self, left: TreeNode, right: TreeNode):
        if (left == None and right == None):
            return True
        if (left == None or right == None):
            return False
        if left.val!=right.val:
            return False
        return self.dfs(left.left,right.right) and self.dfs(left.right,right.left)
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.dfs(root.left, root.right)
```

## 107. 二叉树的层次遍历 II

- 给定一个二叉树，返回其节点值自底向上的层次遍历。 
- 即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历
- 例如：给定二叉树 `[3,9,20,null,null,15,7]`

> ```
>     3
>    / \
>   9  20
>     /  \
>    15   7
> ```

- 返回其自底向上的层次遍历为：

> ```
> [
>   [15,7],
>   [9,20],
>   [3]
> ]
> ```

- **由于本题的输出格式，使用到了list的append、extend、insert函数**
- 思路：**从顶端遍历，存放结果时每次都insert到最顶端的位置，即index=0**

- 代码

```python
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = []                                         # 结果列表
        cur = [root]                                       # 接下来要循环的当前层节点，存的是节点
        while cur:                                         # 当前层存在结点时
            cur_layer_val = []                             # 初始化当前层结果列表为空，存的是val
            next_layer_node = []                           # 初始化下一层结点列表为空
            for node in cur:                               # 遍历当前层的每一个结点
                if node:                                   # 如果该结点不为空，则进行记录
                    cur_layer_val.append(node.val)         # 将该结点的值加入当前层结果列表的末尾
                    next_layer_node.extend([node.left, node.right]) 
                    # 将该结点的左右孩子结点加入到下一层结点列表
            if cur_layer_val:                              # 只要当前层结果列表不为空
                queue.insert(0, cur_layer_val)             # 则把当前层结果列表插入到队列首端
            cur = next_layer_node                          # 下一层的结点变成当前层，接着循环
        return queue 

```

## 108. 将有序数组转换为二叉搜索树

- 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
- 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
- **思路**
  - 平衡二叉搜索树需要保证俩点：
    - 根节点大于左子树任意节点，小于右子树任意节点
    - 左右子数高度相差不超过 1
  - 由以上性质，一个可行的递归条件可以得出：
    - 每次返回的根节点处于数组中间，以其左右半数组分别递归构造左右子树
    - 那么就意味着左子小于根，右子大于根，且所有节点左右子树节点数相差不超过 1 （由于递归的构树方式相同，所有节点都满足高度平衡）
- **代码**

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums:
            loc = len(nums) // 2  # 返回整数
            root = TreeNode(nums[loc])
            root.left = self.sortedArrayToBST(nums[:loc])
            root.right = self.sortedArrayToBST(nums[loc+1:])
            return root
```

## 110. 平衡二叉树

- 给定一个二叉树，判断它是否是高度平衡的二叉树。
- 本题中，一棵高度平衡二叉树定义为：

> 一个二叉树*每个节点* 的左右两个子树的高度差的绝对值不超过1。

- 构造一个获取当前节点最大深度的方法`depth(root)` ，通过比较此子树的左右子树的最大高度差`abs(depth(root.left) - depth(root.right))`，来判断此子树是否是二叉平衡树。若树的所有子树都平衡时，此树才平衡。

- **代码**

```python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
```
