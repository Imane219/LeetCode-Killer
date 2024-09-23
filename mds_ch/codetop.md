# Codetop

> [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)

滑窗+哈希表

> [206. 反转链表](https://leetcode.cn/problems/reverse-linked-list/)

pre=None,cur=head 逐个反转

注意并行赋值的时候cur.next要先于cur赋值，不然cur就被改变了`cur.next, pre, cur = pre, cur, cur.next`

> [92. 反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/)

创建dummyhead，记录反转部分前一结点before和后一节点after。从left+1开始反转，到cur=right+1结束，`before.next.next=after，before=pre`。

> [146. LRU 缓存](https://leetcode.cn/problems/lru-cache/)

双向链表+字典存储key和Node

> [215. 数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/)

快速选择算法，在快排中每次仅排序第k大的元素可能在的一边

仅需要改变：

1. 开头递归边界return nums[l]为所求 
2. 最后判断k>(n-i)表示在左边，否则右边
3. 函数内部返回值不为空，为left或者right部分的返回值

> [25. K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/)

编写函数实现组内反转，输入head和k，输出head，tail和next

> [15. 三数之和](https://leetcode.cn/problems/3sum/)

排序+双指针+剪枝

> [1. 两数之和](https://leetcode.cn/problems/two-sum/)

边遍历边用哈希表记录num:i，如果当前遍历的complement在之前记录过，则找到

> [53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/)

贪心，记录累和小于0则重置

> [912. 排序数组](https://leetcode.cn/problems/sort-an-array/)

**快排：**

1. random.randint(l,r)随机选index 
2. while i<=j -> i==j的情况也需要和pivot比较
3. while nums[j] > pivot: j-=1 -> 等于的时候双边指针停下交换，不要越过
4. if i>j: break -> 双边指针可能相遇后反向，此时退出不要交换了
5. 交换后双边指针各前进一步
6. 递归是[l:i-1]是一边，[i:r]是一边

> [21. 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/)

创建一个dummy head，用一个pre指向它，p、q分别指向两条链表

> [5. 最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/)

从中心点往外延申判断回文串，中心点可能是i,i或者i,i+1

> [33. 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/)

每次二分一定会有一半有序，根据nums[mid]>=nums[l]判断是否左半有序（因为数值互不相同）。如果target在有序这边继续搜索，如果不在则去划分另一边。左半是[l:mid+1]，右半是[mid+1:r+1]。

target判断是否在有序这边时，需要和两端比对判断值是否在中间。

> [102. 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/)

每次进入while，计算len(queue)作为一层的node数量。

> [200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/)

1. 把遍历过的岛屿改成2，避免创建哈希表
2. 每个dfs只能找到一个岛屿，需要对遍历矩阵中每个元素

> [121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)

用一个min记录遍历到的最小价格，若当前price小于min则更新min，大于min则更新和min的差值ans

> [142. 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/)

快慢指针，首先两者指向head，进入while True循环

判断`if not f or not f.next: return None`；否则指针前进直到相遇

相遇后快指针指向头，两者速度一致直到相遇

> [20. 有效的括号](https://leetcode.cn/problems/valid-parentheses/)

栈加哈希表，key为左括号，value为右括号

和全是小括号不同，只要栈顶不匹配整个不匹配

> [88. 合并两个有序数组](https://leetcode.cn/problems/merge-sorted-array/)

双指针反序填充

> [236. 二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)

**先序搜索**，dfs函数表示返回的LCA。当遇到p/q，则此时根要么为它，要么在它上面，因此直接返回它。没有遇到则递归左右子树，若左右子树都不返回空（左右各有一p/q），则LCA为自己，返回自己；若存在一边为空，则另一边的返回节点就是p/q中高的节点，即LCA。

> [46. 全排列](https://leetcode.cn/problems/permutations/)

回溯+hash记录已遍历的num

> [103. 二叉树的锯齿形层序遍历](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/)

隔层反转列表 或者 用双端队列存结果

> [54. 螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/)

用top,bottom,left,right代表四个边界，`while left<=right and top<=bottom`。

先无脑遍历最上和最右的一条边，接着判断`left<=right and top<=bottom`，再遍历下和左。最后更新四个边界。

> [23. 合并 K 个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/)

用大小为k的最小堆来做,$O(nklogk)$. 这样利用了链表升序的性质，只需要排序k个链表之间的大小关系。

> [300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)

$O(n^2)$ -> 二维dp

$O(nlogn)$ -> 桶排序

用一个st维持升序子序列，每遇到新的num，将其插入对应位置。最后st中不一定是所求的升序子序列，但其长度即所求。可以用bisect_left(st,num)来找插入位置，如果插入位置为n则st.append(num). 

注意单调栈是错误的，因为pop的过程中可能丢失了前面的较长子序列。

> [415. 字符串相加](https://leetcode.cn/problems/add-strings/)

从后往前加，记录进位carry。遍历两个字符串时，以长的为准，如果短的到头了则设置它的加数为0. 注意遍历完成后需判断carry。

> [143. 重排链表](https://leetcode.cn/problems/reorder-list/)

1.找链表中间节点 2.后半段反转链表 3.合并两个链表

> [42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/)

双指针：从头尾往中间遍历，每次遍历计算当前l或者r能够接的雨水。

记录lmax和rmax，表示遍历过程中遇到的最大柱子高度，如果lmax<rmax，则计算l的蓄水`lmax-height[l]`(右边一定能蓄)；反之计算r的`rmax-height[r]`。

> [11. 盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/)

双指针：从头尾往中间遍历，每次遍历更新l,r包含的容器最大雨水量。由于雨水量由短板决定，因此每次移动l,r中较短的才有可能总容积最大。如果移动长的，由于宽度收缩了，高度被短板限制了只可能更小，那么不会有更大的容积。

> [56. 合并区间](https://leetcode.cn/problems/merge-intervals/)

排序左端点 + 合并区间。注意遍历完成后还有最后一个区间没有加入ans。

> [124. 二叉树中的最大路径和](https://leetcode.cn/problems/binary-tree-maximum-path-sum/)

树形dp，遍历每个节点时，考虑包含其在内的最大路径`node.val+max(left_ret,0)+max(right_ret,0)`；但返回给父节点时，只能包含一条路径`return node.val+max(left,right,0)`.

正如最大数组和是`max(dp)`，树形dp也要在每次遍历node的时候更新最大ans。

> [19. 删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)

删除节点，有可能删到头节点，因此创建dummy head。

f先走N步。

> [72. 编辑距离](https://leetcode.cn/problems/edit-distance/)

二维dp。

1. i,j范围是`[0,m][0,n]`,空串也算一个。
2. 更新dp从`dp[1][1]`开始，0的值由初始化给出。
3. 考虑滚动数组优化，需要用pre记录`[i-1][j-1]`的值，且每次更新一行需要更新dp[0]。
4. x==y则无需额外编辑为最小

> [1143. 最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/)

1. x==y, `dp[i-1][j-1]+1`; else, `max(dp[i-1][j],dp[i][j-1])`

> [94. 二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/)

**递归：**每次dfs创建一个ans数组，extend左右，append当前值，最后返回

**迭代：**用栈。一开始栈空，node指向root。只要node存在就入栈并走左子树；否则pop一个记录val，node指向右子树。

node即遍历的指针，根据node的指引入栈，不要自己入栈右子树。

> [82. 删除排序链表中的重复元素 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/)

dummy head+逐个删除，不要先确定范围再删除，这样代码比较复杂。

只需一个指针p，其下一个节点代表可能要删除的节点，判断下一个和下下个值是否相等，相等则进行同值节点逐个删除；否则继续遍历。

> [199. 二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view/)

**DFS：**根右左遍历，每次遇到的第一个节点放入ans。记录层高，如果ans的长度大于等于层高，即当前层已经放入节点了，则不放入ans，继续遍历。

**层序：**层序遍历，每次取一层的最后一个node放入ans

> [232. 用栈实现队列](https://leetcode.cn/problems/implement-queue-using-stacks/)

两个栈，一个入一个出。当需要访问队列顶端的时候，把入栈中的元素转移到出栈中，返回出栈的顶端元素。

> [148. 排序链表](https://leetcode.cn/problems/sort-list/)

1. 归并排序，先递归**划分成两段链表**，对每段排序，最后两个有序链表排序。
2. 递归边界为单个节点或者None。
3. 快慢指针找到链表中点，将`s.next=None`。注意初始化`f=f.next`。
4. 对两段链表分别递归，返回l和r代表排好序后的两个头节点。
5. 合并两个有序链表，返回合并后的头节点。

> [69. x 的平方根 ](https://leetcode.cn/problems/sqrtx/)

二分法查找1-x//2

> [718. 最长重复子数组](https://leetcode.cn/problems/maximum-length-of-repeated-subarray/)

**dp,O(mn)**：用LIS的模板，如果x!=y则`dp[i][j]=0`;如果相等则长度+1

**滑窗,O((m+n)*min(m,n))**：最长重复即可以尝试滑动数组，让重复的部分对齐。对于两个数组AB，用A的尾巴对齐B的头，A向右滑动，直到A的头对齐B的尾。每次滑动，都查看重复的数组中，最长对齐长度(不一定是从头开始的)。

定义一个cal_len(pa,pb)函数计算每次滑动的最长数组。