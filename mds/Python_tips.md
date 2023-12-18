# Python tips

## Operations

1. `float("inf")`, `float("-inf")` are exactly the meaning in math.

2. - round down to int: `//`,`-11 // 2 == -6`
   - truncates down to 0: `int()`, `int(-11/2) == -5`

   - round up to int: `math.ceil()` , `math.ceil(-11/2)==-5`, `math.ceil(11/2)==6`

     or `math.ceil(x/m)==(x+m-1)//m`

3. $2^k$ can be counted with `1 << k`

4. `ord('a')` turns a char into its unicode(int)；`chr()` does the reverse.

5. `min(), max()` to replace if condition.

6. the function in class can define a inner function, where the self param is not needed.

7. `-1` can represent minus nums.

8. **Sequence unpacking**:

   ```python
   a, b = [1,2]   # a = 1, b = 2
   a, b = b, a    # a = 2, b = 1; b,a is tuple (b,a) actually, () can be omitted
   a, *b, c = [1,2,3,4,5]   # a = 1, b = [2,3,4], c = 5
   ```

9. **Chained assignment:**

   ```python
   a = b = c = 0   # a=0,b=a,c=a
   a += 1          # a=1,b=c=0 ; because a = a+1 creates a new int variable a+1
   
   a = b = c = [1,2]
   a.append(3)    # a=b=c=[1,2,3]
   ```

10. `map(function, iterable, ...)`, use every element in the iterable sequence as parameter to call the function. Returning an iterator.

    ```python
    a = [1,5,3]
    a = list(map(lambda x: -x, a)) # [-1,-5,-3]
    ```

11. In python, local functions can be defined inside a function A. Only A can call these functions if they are not returned in A. They can visit the variables outside, but can not edit them(except for sequences like list).

12. If use **nonlocal/global** announcing variables that are outside local funtions, then they can be modified in the local funtions.

    ```python
    n = 1
    def a():
    	m = 0
    	def b():
    		nonlocal m # for variables that are inside outer function
    		global n   # for variables in the global scope
    		m += 1
            n += 1
    		return m,n
    ```

13. `zip(a,b)` can pack two iterable objects into tuples: `[(a[0],b[0]),(a[1],b[1]),...]`. If the length of a,b are different, the returned list has the same length with the short one.

## List

1. In python, `while loop` is better to control the pointers' move. 

2. `[-1]*len(nums)` can be used to malloc an array, no need to use `append()` or `insert()`.

4. iterate inversely: `for i in range(r,l,-1)`, l can be -1.

   iterate with step size: `for i in range(r,l,step_size)`
   
4. `append()`: a=[1,2].append([1]) -> a[1,2,[1]]

   `extend()`: a=[1,2].extend([1]) -> a[1,2,1]

5. `.sort(cmp=None, key=None, reverse=False)`, inplace operation, O(nlogn), keep the relative position unchanged. Uses Timsort method.

6. `enumerate(list)` can be used to get both the index and the value.

   ```python
   dic = {val:i for i,val in enumerate(list)}
   ```

7. Do not modify the list while traverse it.

8. slice operation is also left close and right open.

9. Judge whether a is an empty list:

   ```python
   if a == []
   if not a  # yeah, this works
   if len(a) == 0
   ```

10. for circular list, just use the `%` to circulate the index.

## String

1. `"".join(s.split())` can strip all the whitespaces in s.
2. `''.join(deque([1,2]))` is also legal.
3. `''.join(st) or '0'` will return '0' if st is empty. `or` will return the second operand is st is False/0/''/[]/...

## Dict

1. `collections.defaultdict(int)`，when key is not in the dict, insert `{key: defaultvalue}` into dict. int -> 0, list -> []. the 'int' can be replaced with a self-defined function as below.

   ```python
   def default0():
   	return 0
   dic = collections.defaultdict(default0)
   ```

2. Dict can be used to match the elements so you don't need to use the if...else. eg, `brackets = {'(':')','{':'}','[':']'}`

3. The value of a dict can be function

   ```python
   operators = {'+':add,'-':sub,'*':mul,'/':lambda x,y : int(x/y)}
   res = operators['+'](1,2) # 3
   ```

4. `list(dic)` == list(dic.keys()); `list(dic.items())` == [(key,value) for key,value in dic.items()]
