## Graph

> [2477. Minimum oil consumption](https://leetcode.cn/problems/minimum-fuel-cost-to-report-to-the-capital/description/?envType=daily-question&envId=2023-12-05)

> [332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/description/)

Euler Path



## Shortest path

### Dijkstra

```python
import heapq
 
def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    
    # use heap to sort the minimum path to start node.
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        (distance, current_node) = heapq.heappop(heap)
        
        # a longer path
        if distance > dist[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            dist_neighbor = dist[current_node] + weight
            
            if dist_neighbor < dist[neighbor]:
                dist[neighbor] = dist_neighbor
                heapq.heappush(heap, (dist_neighbor, neighbor))
    
    return dist
 
graph = {'A': {'B': 5, 'C': 1},
         'B': {'A': 5, 'C': 2, 'D': 1},
         'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
         'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
         'E': {'C': 8, 'D': 3},
         'F': {'D': 6}}
print(dijkstra(graph, 'A'))
```

