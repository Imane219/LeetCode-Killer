# Python 语法糖

## 操作/技巧

1. `float("inf")`, `float("-inf")`用来表示正负无穷

2. 整除：

   - 向下取整：`//`, eg: `-11//2 == -6`

   - 向0取整：`int()`, eg: `int(-11/2) == -5`

   - 向上取整：`math.ceil()`, eg: `math.ceil(-11/2)==-5`, `math.ceil(11/2)==6` 

     或者：`math.ceil(x/m) == (x+m-1)//m`

3. $2^k$的快速算法: `1 << k`

4. `for i in range(l,r,stepsize)`, 当跳出循环时，`i=r-1`而不是`r`
   
      `for i in range(r,l,-stepsize)`，反向遍历
   
5. 将字符转化为unicode: `ord('a')`

   将unicode转化为字符: `chr()`

6. **常用函数**：

   - `min(),max()`
   - `random.choice(l)`：从列表l中随机选一个元素
   - `random.randint(l,r)`: 从[l:r+1]中随机选择一个元素

7. **常用初始化**：用`-1`代替最小数；用`None`作为初始状态

8. 函数定义：

   - 函数A种可以定义子函数，如果它们没有从A中传递出去，则只有A可以调用它们。
   - 子函数可以访问外部变量，但不能更改（list等可迭代对象除外）

   - 类内的函数可以定义子函数，子函数无需传递self参数

9. 如果用`nonlocal/global`关键字声明了函数外的变量，则该变量可以在函数内更改。`nonlocal`用于声明函数内的变量（子函数可以修改），`global`用于声明全局变量（不在函数内）

   ```python
   n = 1
   def a():
   	m = 0
   	def b():
   		nonlocal m 
   		global n
   		m += 1
           n += 1
   		return m,n
   ```

10. **序列解包：**

      ```python
      a,b = [1,2] # a=1,b=2
      a,b = b,a   # a=2,b=1; b,a实际上是省略了()的(b,a)
      a,*b,c = [1,2,3,4,5] # a=1,b=[2,3,4],c=5
      ```

11. **平行赋值**：

       ```python
       cur.next, pre, cur = pre, cur, cur.next # 此语句会先计算右边，然后按顺序赋值给左边
       ```

12. **链式赋值：**

       ```python
       a=b=c=0 # a=0,b=a,c=a
       a += 1  # a=1,b=c=0; a+1在内存创建了一个新的常数，a指向它
       
       a=b=c=[1,2]
       a.append(3) # a=b=c=[1,2,3]
       ```

13. `map(fuction,iterable,...)`用可迭代的序列中的每个元素，作为参数传递给function，返回一个迭代器

       ```python
       a=[1,5,3]
       a=list(map(lambda x: -x, a)) # [-1,-5,-3]
       ```

14. `zip(a,b)`可以把两个可迭代对象转化为tuple列表: `[(a[0],b[0]), (a[1],b[1]), ...]`. 如果a,b的长度不同，则返回列表的长度和最短的相同。

       ## 列表/元组

       1. python中的列表是按顺序存储的，但是存储的每个元素是一个指向内容的指针，而内容是离散存储的。

       2. `while`循环更方便控制指针的移动（相较于cpp的for循环对指针的支持）

       3. `[-1]*n`用来快速创建一维数组

          `[[-1]*n for _ in range(m)]`用来快速创建二维数组

          - `[[-1]*n]*m`并不是二维数组，其第一维的每个元素指向同样的一个list。
          - 二维数组被创建后，可以用`dp[0] = [1] * n`初始化第一行，即将dp[0]指向新的一维数组，原来的没有引用会被python回收

       4. 反向遍历：`for i in range(r,l,-1)`

       5. `.sort(cmp=None, key=None, reverse=False)`, list原地操作，O(nlogn)，保持相对位置不变，使用Timesort方式（快排升级版）

          - `key=lambda x: (x[0],-x[1])`，key表示排序依赖的键，x表示待排序序列的元素，`:`后表示输出的内容。即按照元组来排序，先排序x[0]，x[0]无法区分的再逆序排序x[1].

       6. `sorted(iterable,cmp=None,key=None,reverse=False)`，返回一个新的list，并且可以用于所有可迭代对象，包括dict的view: dic.items()

       7. `enumerate(list)` can be used to get both the index and the value.

          ```python
          dic = {val:i for i,val in enumerate(list)}
          ```

       8. 在遍历列表元素的时候，不要试图修改列表长度/没遍历到的元素; 在原地操作的时候，不要用enumerate访问，只用下标即可。

       9. **切片操作**：左闭右开

          - 切片操作是一种浅拷贝，通常会创建一个新的list，存放指向切片元素的指针。但当往切片中赋值的时候（此时切片还不是新列表），原来的列表会改变。

            ```python
            a = [1,2,3,4,5] 
            b = a[1:3]      # [2,3]
            # 列表b上的操作不会改变a
            b[0] = 9        # [9,3], a=[1,2,3,4,5]
            # 原切片上的操作会改变a
            a[1:3] = [9]    # a=[1,9,4,5]
            ```

          - python不支持多维列表跨维度检索

            ```python
            a = [[1,2],[3,4]]
            a[:,0]   # python不支持, 只有numpy和torch支持
            [row[0] for row in a] # python用这种写法
            ```

       10. 判断是否是空列表：

           ```python
           if a == []
           if not a
           if len(a) == 0
           ```

       11. 对于循环列表，对index取模（`%`）即可

       12. **拷贝：**当列表可变且需要在其他地方被用到时，记得拷贝

            ```python
           a = [[1,2],[1],[2]]
           b = a.copy()
           c = copy.deepcopy(a)
           a[0].append(3) # b: [[1,2,3],[1],[2]]; c: [[1,2],[1],[2]]
            ```
           
       13. `tuple(iterable)`函数可以将可迭代对象变成元组：`tuple({a:x,b:y})=(a,b)`, `tuple([a,b,c])=(a,b,c)`，变为元组后可以直接比较。

       ## 字符串

       1. **join函数**用法：

          - `"".join(s.split())`可以去除s中的所有空格

          - `''.join(deque([1,2]))`是合法的，deque也可以用join

          - `''.join(st) or '0'`如果st为空，则or前面的表达式为[]，返回'0'。

            - `[]`等空的容器类型在**布尔上下文**中视为False，但其类型和布尔值False不等。

              ```python
              if not []: 
               	print("Yes")   # 输出yes
              print([]==False) # 输出False
              ```

       ## 字典

       1. `collections.defaultdict(int)`, 当key并不在字典中的时候，会自动向字典中插入`{key: defaultvalue}`. 

          - int：插入0

          - list：插入[]

          - 自定义函数：

            ```python
            def default0():
              return 0
            dic = collections.defaultdict(default0)
            ```

       2. 字段可以用来打表，避免了`if ... else...`判断条件。例如：`BRACKETS={'(':')','{':'}','[':']'}`。规范编码：可以用全大写字母来记录打的表。

       3. 字典的值可以是函数

          ```python
          operators = {'+':add, '-':sub, '*':mul, '/':lambda x,y : int(x/y)}
          res = operators['+'](1,2) # res=3
          ```

       4. 字典转化为列表：

          - `list(dic) == list(dic.keys())`
          - `list(dic.items()) == [(key,value) for key,value in dic.items()]`

       ## 对象

       1. 可以给类别定义一个`__lt__`方法让对象可比

          ```python
          class Node:
            def __init__(self, val):
              self.val = val
            def __lt__(self, other):
              return self.val < other.val
          ```

          或者可以在类别外面定义`__lt__`方法

          ```python
          class Node:
            def __init__(self, val):
              self.val = val
          Node.__lt__ = lambda a,b: a.val < b.val
          ```

          