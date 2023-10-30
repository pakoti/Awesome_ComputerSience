
# Fibonacci sequence 
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers. The sequence starts with 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on. There are two popular approaches to solve the Fibonacci sequence problem: divide and conquer and dynamic programming.

Divide and Conquer Approach:
The divide and conquer approach recursively divides the problem into smaller subproblems and solves them independently. The solution is then combined to get the final solution. In the case of the Fibonacci sequence, we can use the divide and conquer approach to break the problem into two subproblems, i.e., finding the nth and (n-1)th Fibonacci numbers. We can then combine these two numbers to get the nth Fibonacci number. The time complexity of this approach is O(2^n).

Dynamic Programming Approach:
The dynamic programming approach solves the problem by breaking it down into smaller subproblems and storing the solutions to these subproblems in an array or table. We can then use these solutions to solve the larger problem. In the case of the Fibonacci sequence, we can use dynamic programming to store the solutions to the subproblems in an array and then use these solutions to calculate the nth Fibonacci number. The time complexity of this approach is O(n).

To summarize, the divide and conquer approach has exponential time complexity, while the dynamic programming approach has linear time complexity. Therefore, the dynamic programming approach is more efficient for solving the Fibonacci sequence problem.



# devide and conquer
```python
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    # Example usage
    print(fibonacci(6)) # Output: 8
```

# dynamic programming 
```python
    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]

    # Example usage
    print(fibonacci(6)) # Output: 8
```
# Merge Sort Algorithm without using memory
Mergesort is an inherently memory-intensive algorithm because it relies on creating new arrays to hold sublists during the merging process. It's not practical to implement a true "in-place" mergesort algorithm in Python that doesn't use any extra memory for sublists.

However, if your goal is to reduce memory usage, you can modify the standard mergesort algorithm to minimize additional memory allocations by using slicing. Here's a modified version of mergesort that avoids creating new arrays for sublists but still uses some additional memory for slicing:

```python
def merge_sort(arr):
    if len(arr) <= 1:
         return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage
my_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = merge_sort(my_list)
print(sorted_list)
```

In this modified version, we avoid creating new arrays for sublists by using slicing (`left = arr[:mid]` and `right = arr[mid:]`). However, keep in mind that slicing still consumes some memory, and this approach is not a true "in-place" algorithm. If you need an algorithm that doesn't use any additional memory, you would need to consider other sorting algorithms like Heapsort or in-place variations of Quicksort.



# Resource

Thanks to chatgpt!