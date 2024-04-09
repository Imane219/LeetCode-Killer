# Tricks

## Bit Operation

### XOR `^`

`1 xor 1 = 0`; `0 xor 0 = 0`; `1 xor 0 = 1`; `0 xor 1 = 1`.

`a xor a = 0`; `a xor 0 = a`.

> [136. Single Number](https://leetcode.com/problems/single-number/)

Xor all the nums, the duplicate ones can be removed.

```python
return reduce(lambda x,y: x^y, nums)
```



## Array to linked list

> [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

We can use the num as index to search for the next num. Once meet the duplicants, it will point back to form a circle. Use **Floyd's Cycle-Finding algorithm** to find the entrance of the circle.