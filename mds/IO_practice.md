# IO practice

In some situation, we need to process the input by ourselves (ACM mode). So we record the tips here.

[A good website to practice IO](https://ac.nowcoder.com/acm/contest/5657#question)





## 1. Finite and fixed inputs

- `input()` to read in strings

- `strip()` to remove the \t \n ' '
- `split()` to separate the substrings -> returns [substring1, substring2]
- `map(int, iterable)` to change each substring to int -> returns a iterator
- `a, b = map(xxx)` can get the elements in the iterator.

```python
# 4 3 2
line = input()
a, b, c = map(int,line.strip().split())
```

## 2. Non-fixed inputs

- Use for loop to get the total elements.

```python
# 1 2 3
line = input()
num_list = [int(num) for num in line.strip().split()]
```

## 3. Infinite groups of numbers

- Use `try ... except` to get the input until meet `EOFError`.

```python
# 1 2
# 3 4
# ...
while True:
    try:
        a, b = map(int, input().strip().split())
        # process a, b
    except EOFError:
        break
```

## 4. Get the first number of each row

- Use `list` to change the map generator.

```python
While True:
	try:
        data = list(map(int, input().strip().split()))
        n, array = data[0], data[1:]
    except EOFError:
        break
```

## Format output

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

