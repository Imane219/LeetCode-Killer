# Math

Record problems that can be solved mathematically.

## Problems

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



## 求根号n，m精度