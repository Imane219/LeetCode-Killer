# 笔试

## 一、输入输出

某些情况下需要自己处理输入(ACM模式)，在此记录一些I/O tips.

[练习IO的网址](https://ac.nowcoder.com/acm/contest/5657#question)



### 1. 有限行且固定的输入

- `input()`读取字符串

- `strip()`移除前后的`\t,\n,' '`
- `split()`分割字符串为字符串列表，默认分隔符为' ' -> 返回[substring1, substring2]
- `map(int, iterable)`把每个子串转化成int -> 返回迭代器
- `a, b = map(xxx)`从迭代器中获取元素

```python
# 4 3 2
line = input()
a, b, c = map(int,line.strip().split())
```

### 2. 有限行不固定的输入

- 用循环从字符串列表中转换格式

```python
# 1 2 3 ...
line = input()
num_list = [int(num) for num in line.strip().split()]
```

### 3. 无限行的输入

- 用`try ... except`去获取输入`EOFError`.

```python
# 1 2
# 3 4
# ...
while True:
    try:
        a, b = map(int, input().strip().split())
        # 处理a, b
    except EOFError:
        break
```

### 4. 获取每一行的第一个元素

- 用`list()`函数将迭代器转化成list

```python
While True:
	try:
        data = list(map(int, input().strip().split()))
        n, array = data[0], data[1:]
    except EOFError:
        break
```

### 技巧

#### 格式化输出

- str.format()

```python
"{} and {}".format("a", "b")     # a and b
"{1} and {0}".format("a", "b")   # b and a
"name: {name}, number: {num}".format(name='ab', num=1)
"name: {0[0]}, number: {0[1]}".format(['ab',1])
"{:.2f}".format(3.14159)         # 3.14
"{:+.2f}".format(3.14159)        # +3.14
"{:.0f}".format(3.14159)         # 3.
```

#### eval函数的使用



#### 快读快写

- python3超时可以试试pypy



## 二、笔试题





```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class MHA(nn.Module):
    def __init__(self, dim, num_heads, qkv_bias=False):
        self.num_heads = num_heads
        head_dim = dim // num_heads
        self.scale = head_dim ** -0.5
        
        assert (head_dim * num_heads == dim)
        
        self.qkv = nn.Linear(dim,dim*3,bias=qkv_bias)
        self.proj = nn.Linear(dim, dim)
        
    def forward(self,x):
        B,N,C = x.shape
        # (3,B,num_heads,N,head_dim)
        qkv = self.qkv(x).reshape(B,N,3,self.num_heads,C//self.num_heads)
        qkv = qkv.permute(2,0,3,1,4)
        q,k,v = qkv[0], qkv[1], qkv[2]
        # (B,num_heads,N,N)
        attn = q @ k.transpose(-2,-1)
        attn *= self.scale
        attn = F.softmax(attn, dim=-1)
        
        x = attn @ v
        x = x.transpose(1,2)
        x = x.reshape(B,N,C)
        x = self.proj(x)
        return x
```

