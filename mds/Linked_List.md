# Linked_List

Linked List is a data structure that O(1) when insert O(n) when search.

There's no index only to search in sequence.

## Detect a cycle

**Floyd's Cycle-Finding algorithm/Hare-Tortoise algorithm/Fast and slow pointer**

> [142. Linked List Cycle 2](https://leetcode.com/problems/linked-list-cycle-ii/description/)

The algorithm works by two pointers, a slow and a fast one. The fast one moves twice as fast as the slow one. 

- If there's a cycle in the linked list, the two pointers will meet inside the cycle. When they meet:
  - define `f` as the distance of the fast pointer has moved, and `s` as that of the slow one.
  - define `a` as the distance before the cycle starts, and `b` as the total distance of the cycle.
  - Therefore, `f=2s` and `f=s+nb`, `n`(int) represents the number of extra rounds fast pointer moved. So `s=nb`, which means the slow pointer exactly moved `n` rounds (`n=a+kb`, k is not int) when they meet. When the slow pointer continue moving `a` distance, it will get to the start of the cycle.
  - So we move the fast pointer to the head after they first met. Then they move the same speed and will secondly meet at the start of the cycle after `a` distance.
- If there's no cycle, the fast pointer will reach the end of the linked list.

