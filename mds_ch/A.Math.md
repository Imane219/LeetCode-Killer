# 数学

可以用数学方法解决的问题/数学相关的问题

## 问题

> [343. Integer Break](https://leetcode.com/problems/integer-break/)

For the integer that has the maximum product, it should be broken down to multiple 3 and the remaining.

- integer 2: 1x1=1, smaller that itself.
- integer 3: 1x2=2, smaller that itself.
- integer 4: 2x2=4, equal to itself.
- integer 5: 2x3=6, bigger.
- integer 6: 3x3=9 > 2x2x2=8, three 2 can convert to two 3.
- integer 7: 3x2x2=12.
- ...

So, break the integer down into $3*n$ and the remaining. If the remaining == 1, make it to $3*(n-1)+2*2$.



### 1. 求根号n，m精度

**解法1：牛顿迭代法**

牛顿迭代法可以用来近似$f(x)=0$的根，具体做法：

1. 随机选一个$x_0$来近似，计算$f(x)$在$x_0$处的切线：$y=f(x_0)+f'(x_0)(x-x_0)$
2. 计算该切线与横轴交点坐标：$x_1=x_0-\frac{f(x_0)}{f'(x_0)}$，$x_1$即为根的一次近似
3. 用$x_1$替代$x_0$循环下去

那么对于根号n，其$f(x)=x^2-n, f'(x)=2x$

求根号n，精度m的代码

```python
def func(n,m):
    x = n/2
    e = m+1
    while e > m:
        x = x-(x**2-n)/2x
        e = x*x-n # 牛顿法会逐步逼近根，但不会超过，因为精度差会逐渐减小
    return x
```

### 2. rand(5)实现rand(7)

首先`用rand(5)实现rand(25)`：如果仅仅是rand(5)*5，只能以1/5的概率输出5,10,15,20,25. 并不能以1/25的概率输出[1,25].

进行加法运算：`y=5*(x-1)+x`, 此时y的输出则符合rand(25).

那么对生成的y%7+1就能以1/7的概率输出[1,7]，`当y>21的时候，重新采样计算y即可`。

```python
def func():
    x = inf
    while x > 21:
        y = 5*(random.randint(1,5)-1)+random.randint(1,5)
        x = y
    return x%7+1
```

