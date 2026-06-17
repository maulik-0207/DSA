# 🚀 DSA Preparation Roadmap

## 📊 Progress Tracker

| Section                     | Topics | Status         |
| --------------------------- | ------ | -------------- |
| 1. Arrays & Strings         | 8      | 🟡 Not Started |
| 2. Linked Lists             | 5      | ⬜ Not Started |
| 3. Stacks                   | 4      | ⬜ Not Started |
| 4. Queues                   | 4      | ⬜ Not Started |
| 5. Recursion                | 3      | ⬜ Not Started |
| 6. Sorting Algorithms       | 7      | ⬜ Not Started |
| 7. Searching Algorithms     | 3      | ⬜ Not Started |
| 8. Hashing                  | 3      | ⬜ Not Started |
| 9. Trees                    | 8      | ⬜ Not Started |
| 10. Heaps & Priority Queues | 4      | ⬜ Not Started |
| 11. Graphs                  | 10     | ⬜ Not Started |
| 12. Backtracking            | 3      | ⬜ Not Started |
| 13. Greedy Algorithms       | 3      | ⬜ Not Started |
| 14. Dynamic Programming     | 6      | ⬜ Not Started |
| 15. Bit Manipulation        | 3      | ⬜ Not Started |
| 16. Math & Number Theory    | 4      | ⬜ Not Started |
| 17. String Algorithms       | 3      | ⬜ Not Started |

> Update the **Status** column as you go: ⬜ Not Started → 🟡 In Progress → ✅ Done

---

## 🏗️ 1. Arrays & Strings

> **Folder:** `01_arrays_and_strings/`

### 📦 Implementation — Build From Scratch

Implement the core data structures and their operations. No tricks, no patterns — just understand how they work internally.

- [ ] **Dynamic Array** — Build a resizable array from scratch
  - Operations: `insert(index, value)`, `append(value)`, `delete(index)`, `get(index)`, `set(index, value)`, `size()`, `reverse()`, `traverse()`
- [ ] **String as Char Array** — Implement basic string operations manually
  - Operations: `reverse()`, `isPalindrome()`, `isAnagram(str1, str2)`, `concatenate()`, `substring(start, end)`
- [ ] **Matrix (2D Array)** — Implement a 2D array with operations
  - Operations: `insert(row, col, value)`, `get(row, col)`, `transpose()`, `rotate90()`, `spiralOrder()`

### 🏋️ LeetCode Practice

| #   | Problem                                        | Difficulty | Technique                 |
| --- | ---------------------------------------------- | ---------- | ------------------------- |
| 1   | Two Sum                                        | Easy       | Hashing / Two Pointers    |
| 121 | Best Time to Buy and Sell Stock                | Easy       | Kadane's / Sliding Window |
| 53  | Maximum Subarray                               | Medium     | Kadane's Algorithm        |
| 3   | Longest Substring Without Repeating Characters | Medium     | Sliding Window            |
| 238 | Product of Array Except Self                   | Medium     | Prefix Product            |
| 49  | Group Anagrams                                 | Medium     | Hashing                   |
| 75  | Sort Colors                                    | Medium     | Dutch National Flag       |
| 11  | Container With Most Water                      | Medium     | Two Pointers              |
| 42  | Trapping Rain Water                            | Hard       | Two Pointers / Stack      |

---

## 🔗 2. Linked Lists

> **Folder:** `02_linked_lists/`

### 📦 Implementation — Build From Scratch

- [ ] **Singly Linked List** — Build the node class and list from scratch
  - Operations: `insertAtHead(value)`, `insertAtTail(value)`, `insertAt(index, value)`, `deleteAtHead()`, `deleteAtTail()`, `deleteAt(index)`, `search(value)`, `reverse()`, `traverse()`, `size()`
- [ ] **Doubly Linked List** — Build with prev + next pointers
  - Operations: Same as above + `traverseBackward()`
- [ ] **Circular Linked List** — Singly & Doubly circular variants
  - Operations: Same as singly/doubly but with circular traversal logic

### 🏋️ LeetCode Practice

| #   | Problem                          | Difficulty | Technique                      |
| --- | -------------------------------- | ---------- | ------------------------------ |
| 206 | Reverse Linked List              | Easy       | Iterative / Recursive reversal |
| 21  | Merge Two Sorted Lists           | Easy       | Two Pointers                   |
| 141 | Linked List Cycle                | Easy       | Fast & Slow Pointers           |
| 19  | Remove Nth Node From End of List | Medium     | Two Pointers                   |
| 143 | Reorder List                     | Medium     | Fast/Slow + Reverse + Merge    |
| 146 | LRU Cache                        | Medium     | DLL + HashMap                  |
| 23  | Merge k Sorted Lists             | Hard       | Divide & Conquer / Heap        |

---

## 🥞 3. Stacks

> **Folder:** `03_stacks/`

### 📦 Implementation — Build From Scratch

- [ ] **Stack (Array-based)** — Build using a simple array/list
  - Operations: `push(value)`, `pop()`, `peek()`, `isEmpty()`, `size()`
- [ ] **Stack (Linked List-based)** — Build using a singly linked list
  - Operations: Same as above
- [ ] **Min Stack** — Stack that also tracks the minimum element in O(1)
  - Operations: `push(value)`, `pop()`, `peek()`, `getMin()`

### 🏋️ LeetCode Practice

| #   | Problem                          | Difficulty | Technique             |
| --- | -------------------------------- | ---------- | --------------------- |
| 20  | Valid Parentheses                | Easy       | Parenthesis matching  |
| 155 | Min Stack                        | Medium     | Auxiliary stack       |
| 150 | Evaluate Reverse Polish Notation | Medium     | Expression evaluation |
| 739 | Daily Temperatures               | Medium     | Monotonic Stack       |
| 496 | Next Greater Element I           | Easy       | Monotonic Stack       |
| 84  | Largest Rectangle in Histogram   | Hard       | Monotonic Stack       |

---

## 📬 4. Queues

> **Folder:** `04_queues/`

### 📦 Implementation — Build From Scratch

- [ ] **Simple Queue (Array-based)** — Build with front/rear pointers
  - Operations: `enqueue(value)`, `dequeue()`, `front()`, `rear()`, `isEmpty()`, `size()`
- [ ] **Simple Queue (Linked List-based)** — Build using linked list nodes
  - Operations: Same as above
- [ ] **Circular Queue** — Fixed-size queue with wraparound
  - Operations: Same as above + handle full/empty conditions
- [ ] **Deque (Double-Ended Queue)** — Build from scratch
  - Operations: `insertFront(value)`, `insertRear(value)`, `deleteFront()`, `deleteRear()`, `getFront()`, `getRear()`

### 🏋️ LeetCode Practice

| #   | Problem                      | Difficulty | Technique       |
| --- | ---------------------------- | ---------- | --------------- |
| 225 | Implement Stack using Queues | Easy       | Design          |
| 232 | Implement Queue using Stacks | Easy       | Design          |
| 622 | Design Circular Queue        | Medium     | Design          |
| 641 | Design Circular Deque        | Medium     | Design          |
| 239 | Sliding Window Maximum       | Hard       | Monotonic Deque |

---

## 🔄 5. Recursion

> **Folder:** `05_recursion/`

### 📦 Implementation — Build From Scratch

Implement these recursive algorithms to understand how recursion works — base case, recursive case, call stack.

- [ ] **Basic Recursion** — Implement from scratch
  - `factorial(n)`, `fibonacci(n)`, `power(base, exp)`, `sumOfDigits(n)`
- [ ] **Recursion on Arrays** — Implement using recursion only (no loops)
  - `sum(arr)`, `reverse(arr)`, `isSorted(arr)`, `findMax(arr)`
- [ ] **Recursion on Strings** — Implement using recursion only
  - `isPalindrome(str)`, `reverseString(str)`, `countOccurrences(str, char)`

### 🏋️ LeetCode Practice

| #   | Problem                | Difficulty | Technique               |
| --- | ---------------------- | ---------- | ----------------------- |
| 509 | Fibonacci Number       | Easy       | Basic recursion         |
| 50  | Pow(x, n)              | Medium     | Divide & Conquer        |
| 78  | Subsets                | Medium     | Subset generation       |
| 779 | K-th Symbol in Grammar | Medium     | Pattern-based recursion |
| 22  | Generate Parentheses   | Medium     | Backtracking recursion  |

---

## 📶 6. Sorting Algorithms

> **Folder:** `06_sorting/`

### 📦 Implementation — Build From Scratch

Implement each sorting algorithm from scratch. Understand the time/space complexity and when to use each.

- [ ] **Bubble Sort** — Implement with optimization (early stop if no swaps)
- [ ] **Selection Sort** — Find min and swap to front
- [ ] **Insertion Sort** — Insert each element into its correct position
- [ ] **Merge Sort** — Divide, sort, merge (recursive)
- [ ] **Quick Sort** — Partition around pivot (recursive)
- [ ] **Counting Sort** — Non-comparison based, integer keys
- [ ] **Radix Sort** — Digit-by-digit using Counting Sort as subroutine

### 🏋️ LeetCode Practice

| #   | Problem                         | Difficulty | Technique                 |
| --- | ------------------------------- | ---------- | ------------------------- |
| 912 | Sort an Array                   | Medium     | Merge/Quick Sort          |
| 75  | Sort Colors                     | Medium     | Dutch National Flag       |
| 148 | Sort List                       | Medium     | Merge Sort on Linked List |
| 56  | Merge Intervals                 | Medium     | Sort + Merge              |
| 179 | Largest Number                  | Medium     | Custom Comparator         |
| 215 | Kth Largest Element in an Array | Medium     | Quick Select              |

---

## 🔍 7. Searching Algorithms

> **Folder:** `07_searching/`

### 📦 Implementation — Build From Scratch

- [ ] **Linear Search** — Implement on arrays and linked lists
  - `search(arr, target)` → returns index or -1
- [ ] **Binary Search** — Implement iterative & recursive versions
  - `binarySearch(arr, target)`, `lowerBound(arr, target)`, `upperBound(arr, target)`

### 🏋️ LeetCode Practice

| #   | Problem                                                 | Difficulty | Technique         |
| --- | ------------------------------------------------------- | ---------- | ----------------- |
| 704 | Binary Search                                           | Easy       | Standard BS       |
| 35  | Search Insert Position                                  | Easy       | Lower Bound       |
| 33  | Search in Rotated Sorted Array                          | Medium     | Modified BS       |
| 34  | Find First and Last Position of Element in Sorted Array | Medium     | Lower/Upper Bound |
| 875 | Koko Eating Bananas                                     | Medium     | BS on Answer      |
| 74  | Search a 2D Matrix                                      | Medium     | BS on 2D          |
| 4   | Median of Two Sorted Arrays                             | Hard       | BS on Answer      |

---

## #️⃣ 8. Hashing

> **Folder:** `08_hashing/`

### 📦 Implementation — Build From Scratch

- [ ] **Hash Map** — Build from scratch with an array of buckets
  - Collision handling: Chaining (linked list) & Open Addressing (linear probing)
  - Operations: `put(key, value)`, `get(key)`, `remove(key)`, `containsKey(key)`, `size()`, `resize()`
- [ ] **Hash Set** — Build from scratch (Hash Map where value is always `true`)
  - Operations: `add(value)`, `remove(value)`, `contains(value)`, `size()`

### 🏋️ LeetCode Practice

| #   | Problem                      | Difficulty | Technique              |
| --- | ---------------------------- | ---------- | ---------------------- |
| 217 | Contains Duplicate           | Easy       | Hash Set               |
| 242 | Valid Anagram                | Easy       | Frequency Count        |
| 1   | Two Sum                      | Easy       | Hash Map Lookup        |
| 49  | Group Anagrams               | Medium     | Hashing + Sorting      |
| 347 | Top K Frequent Elements      | Medium     | Frequency Count + Heap |
| 128 | Longest Consecutive Sequence | Medium     | Hash Set               |
| 560 | Subarray Sum Equals K        | Medium     | Prefix Sum + Hash Map  |

---

## 🌳 9. Trees

> **Folder:** `09_trees/`

### 📦 Implementation — Build From Scratch

- [ ] **Binary Tree** — Build the Node class and tree structure
  - Operations: `insert(value)`, `delete(value)`, `search(value)`, `height()`, `size()`, `countLeaves()`
- [ ] **Tree Traversals** — Implement all four traversals
  - `preOrder()`, `inOrder()`, `postOrder()` — both Recursive & Iterative
  - `levelOrder()` — using a queue (BFS)
- [ ] **Binary Search Tree (BST)** — Build with BST property maintained
  - Operations: `insert(value)`, `delete(value)`, `search(value)`, `findMin()`, `findMax()`, `inOrderSuccessor()`, `isValidBST()`
- [ ] **Trie (Prefix Tree)** — Build the TrieNode class and Trie
  - Operations: `insert(word)`, `search(word)`, `startsWith(prefix)`, `delete(word)`
- [ ] **Segment Tree** — Build for range queries
  - Operations: `build(arr)`, `query(left, right)`, `update(index, value)`

### 🏋️ LeetCode Practice

| #   | Problem                                 | Difficulty | Technique           |
| --- | --------------------------------------- | ---------- | ------------------- |
| 104 | Maximum Depth of Binary Tree            | Easy       | DFS                 |
| 226 | Invert Binary Tree                      | Easy       | DFS / BFS           |
| 100 | Same Tree                               | Easy       | DFS                 |
| 543 | Diameter of Binary Tree                 | Easy       | DFS + height        |
| 102 | Binary Tree Level Order Traversal       | Medium     | BFS                 |
| 98  | Validate Binary Search Tree             | Medium     | Inorder / DFS       |
| 230 | Kth Smallest Element in a BST           | Medium     | Inorder traversal   |
| 208 | Implement Trie (Prefix Tree)            | Medium     | Trie                |
| 236 | Lowest Common Ancestor of a Binary Tree | Medium     | LCA                 |
| 124 | Binary Tree Maximum Path Sum            | Hard       | DFS + Path tracking |

---

## ⛰️ 10. Heaps & Priority Queues

> **Folder:** `10_heaps/`

### 📦 Implementation — Build From Scratch

- [ ] **Min Heap** — Build from scratch using an array
  - Operations: `insert(value)`, `extractMin()`, `peek()`, `heapifyUp()`, `heapifyDown()`, `size()`, `buildHeap(arr)`
- [ ] **Max Heap** — Build from scratch using an array
  - Operations: Same as Min Heap but max-oriented
- [ ] **Heap Sort** — Implement using a Max Heap
  - `heapSort(arr)` — in-place sorting

### 🏋️ LeetCode Practice

| #   | Problem                         | Difficulty | Technique           |
| --- | ------------------------------- | ---------- | ------------------- |
| 703 | Kth Largest Element in a Stream | Easy       | Min Heap of size K  |
| 215 | Kth Largest Element in an Array | Medium     | Quick Select / Heap |
| 347 | Top K Frequent Elements         | Medium     | Heap + Frequency    |
| 373 | Find K Pairs with Smallest Sums | Medium     | Min Heap            |
| 295 | Find Median from Data Stream    | Hard       | Two Heaps           |

---

## 🕸️ 11. Graphs

> **Folder:** `11_graphs/`

### 📦 Implementation — Build From Scratch

- [ ] **Graph Representation** — Build both from scratch
  - Adjacency Matrix: `addEdge(u, v)`, `removeEdge(u, v)`, `hasEdge(u, v)`, `getNeighbors(u)`
  - Adjacency List: Same operations using dictionary/list of lists
- [ ] **BFS (Breadth-First Search)** — Implement on the graph
  - `bfs(startNode)` — using a queue, track visited
- [ ] **DFS (Depth-First Search)** — Implement iterative & recursive
  - `dfs(startNode)` — using a stack / recursion, track visited
- [ ] **Disjoint Set Union (Union-Find)** — Build from scratch
  - Operations: `find(x)`, `union(x, y)`, `isConnected(x, y)` — with rank & path compression

### 🏋️ LeetCode Practice

| #   | Problem                         | Difficulty | Technique                          |
| --- | ------------------------------- | ---------- | ---------------------------------- |
| 200 | Number of Islands               | Medium     | DFS / BFS                          |
| 133 | Clone Graph                     | Medium     | BFS / DFS                          |
| 207 | Course Schedule                 | Medium     | Topological Sort / Cycle Detection |
| 210 | Course Schedule II              | Medium     | Topological Sort                   |
| 994 | Rotting Oranges                 | Medium     | Multi-source BFS                   |
| 743 | Network Delay Time              | Medium     | Dijkstra's                         |
| 323 | Number of Connected Components  | Medium     | Union-Find / DFS                   |
| 127 | Word Ladder                     | Hard       | BFS                                |
| 269 | Alien Dictionary                | Hard       | Topological Sort                   |
| 787 | Cheapest Flights Within K Stops | Medium     | Bellman-Ford / BFS                 |

---

## 🔙 12. Backtracking

> **Folder:** `12_backtracking/`

### 📦 Implementation — Build From Scratch

Implement the backtracking template and these classic algorithms:

- [ ] **Backtracking Template** — Understand the choose → explore → unchoose pattern
  - `generateSubsets(arr)` — all subsets of an array
  - `generatePermutations(arr)` — all permutations of an array
  - `generateCombinations(arr, k)` — all combinations of size k

### 🏋️ LeetCode Practice

| #   | Problem         | Difficulty | Technique               |
| --- | --------------- | ---------- | ----------------------- |
| 78  | Subsets         | Medium     | Subset generation       |
| 46  | Permutations    | Medium     | Permutation generation  |
| 39  | Combination Sum | Medium     | Combination + pruning   |
| 79  | Word Search     | Medium     | Grid backtracking       |
| 51  | N-Queens        | Hard       | Constraint backtracking |
| 37  | Sudoku Solver   | Hard       | Constraint backtracking |

---

## 💰 13. Greedy Algorithms

> **Folder:** `13_greedy/`

### 📦 Implementation — Build From Scratch

Implement these classic greedy algorithms from scratch:

- [ ] **Activity Selection / Interval Scheduling** — Select maximum non-overlapping intervals
- [ ] **Fractional Knapsack** — Greedy by value/weight ratio
- [ ] **Huffman Encoding** — Build a Huffman tree and encode/decode strings

### 🏋️ LeetCode Practice

| #   | Problem                   | Difficulty | Technique             |
| --- | ------------------------- | ---------- | --------------------- |
| 55  | Jump Game                 | Medium     | Greedy forward scan   |
| 45  | Jump Game II              | Medium     | Greedy BFS-like       |
| 435 | Non-overlapping Intervals | Medium     | Interval scheduling   |
| 763 | Partition Labels          | Medium     | Greedy + Two Pointers |
| 134 | Gas Station               | Medium     | Greedy accumulation   |

---

## 🧠 14. Dynamic Programming

> **Folder:** `14_dynamic_programming/`

### 📦 Implementation — Build From Scratch

Implement these classic DP algorithms. For each, write both **top-down (memoization)** and **bottom-up (tabulation)** versions.

- [ ] **Fibonacci** — top-down with memo, bottom-up with table, space-optimized
- [ ] **0/1 Knapsack** — given weights and values, maximize value within capacity
- [ ] **Longest Common Subsequence (LCS)** — 2D DP on two strings
- [ ] **Longest Increasing Subsequence (LIS)** — 1D DP + binary search optimization
- [ ] **Coin Change** — unbounded knapsack variant, minimum coins to make amount
- [ ] **Edit Distance** — 2D DP on two strings, min operations to convert

### 🏋️ LeetCode Practice

| #    | Problem                        | Difficulty | Technique          |
| ---- | ------------------------------ | ---------- | ------------------ |
| 70   | Climbing Stairs                | Easy       | 1D DP              |
| 198  | House Robber                   | Medium     | 1D DP              |
| 322  | Coin Change                    | Medium     | Unbounded Knapsack |
| 300  | Longest Increasing Subsequence | Medium     | LIS                |
| 1143 | Longest Common Subsequence     | Medium     | 2D DP              |
| 62   | Unique Paths                   | Medium     | 2D Grid DP         |
| 72   | Edit Distance                  | Medium     | 2D String DP       |
| 152  | Maximum Product Subarray       | Medium     | Modified Kadane's  |
| 10   | Regular Expression Matching    | Hard       | 2D DP              |
| 312  | Burst Balloons                 | Hard       | Interval DP        |

---

## 🔢 15. Bit Manipulation

> **Folder:** `15_bit_manipulation/`

### 📦 Implementation — Build From Scratch

Implement these bitwise operations and utilities:

- [ ] **Bitwise Operators** — Understand AND, OR, XOR, NOT, Left Shift, Right Shift
- [ ] **Common Bit Tricks** — Implement as utility functions
  - `isEven(n)`, `isPowerOfTwo(n)`, `countSetBits(n)`, `getBit(n, i)`, `setBit(n, i)`, `clearBit(n, i)`, `toggleBit(n, i)`

### 🏋️ LeetCode Practice

| #   | Problem                      | Difficulty | Technique      |
| --- | ---------------------------- | ---------- | -------------- |
| 136 | Single Number                | Easy       | XOR trick      |
| 191 | Number of 1 Bits             | Easy       | Count set bits |
| 338 | Counting Bits                | Easy       | DP + Bit       |
| 268 | Missing Number               | Easy       | XOR / Math     |
| 371 | Sum of Two Integers          | Medium     | Bit addition   |
| 201 | Bitwise AND of Numbers Range | Medium     | Bit shifting   |

---

## ➗ 16. Math & Number Theory

> **Folder:** `16_math/`

### 📦 Implementation — Build From Scratch

- [ ] **Sieve of Eratosthenes** — Generate all primes up to N
  - `sieve(n)` → returns list of primes
- [ ] **GCD / LCM** — Euclidean Algorithm
  - `gcd(a, b)`, `lcm(a, b)`
- [ ] **Modular Exponentiation** — Fast power with modulo
  - `modPow(base, exp, mod)`
- [ ] **Combinatorics** — Compute nCr and nPr
  - `nCr(n, r)`, `nPr(n, r)` — using DP / Pascal's Triangle

### 🏋️ LeetCode Practice

| #   | Problem                   | Difficulty | Technique                |
| --- | ------------------------- | ---------- | ------------------------ |
| 204 | Count Primes              | Medium     | Sieve of Eratosthenes    |
| 50  | Pow(x, n)                 | Medium     | Fast Exponentiation      |
| 7   | Reverse Integer           | Medium     | Math / Overflow handling |
| 9   | Palindrome Number         | Easy       | Math                     |
| 172 | Factorial Trailing Zeroes | Medium     | Math / Prime factors     |

---

## 🔤 17. String Algorithms

> **Folder:** `17_string_algorithms/`

### 📦 Implementation — Build From Scratch

- [ ] **KMP (Knuth-Morris-Pratt)** — Pattern matching algorithm
  - Build the LPS (Longest Prefix Suffix) array, then search
  - `buildLPS(pattern)`, `kmpSearch(text, pattern)`
- [ ] **Rabin-Karp** — Rolling hash-based pattern matching
  - `rabinKarp(text, pattern)` — using polynomial rolling hash
- [ ] **Z-Algorithm** — Z-array based pattern matching
  - `buildZArray(str)`, `zSearch(text, pattern)`

### 🏋️ LeetCode Practice

| #   | Problem                                            | Difficulty | Technique                 |
| --- | -------------------------------------------------- | ---------- | ------------------------- |
| 28  | Find the Index of the First Occurrence in a String | Easy       | KMP / Rabin-Karp          |
| 5   | Longest Palindromic Substring                      | Medium     | Expand around center / DP |
| 647 | Palindromic Substrings                             | Medium     | Expand around center      |
| 76  | Minimum Window Substring                           | Hard       | Sliding Window            |
| 438 | Find All Anagrams in a String                      | Medium     | Sliding Window            |

---

## 📂 Folder Structure

```
DSA/
├── readme.md
├── 01_arrays_and_strings/
│   ├── implementation/
│   │   ├── dynamic_array.py
│   │   ├── string_operations.py
│   │   └── matrix_operations.py
│   └── leetcode/
│       ├── two_sum.py
│       └── ...
├── 02_linked_lists/
│   ├── implementation/
│   │   ├── singly_linked_list.py
│   │   ├── doubly_linked_list.py
│   │   └── circular_linked_list.py
│   └── leetcode/
│       └── ...
├── 03_stacks/
│   ├── implementation/
│   │   ├── stack_array.py
│   │   ├── stack_linkedlist.py
│   │   └── min_stack.py
│   └── leetcode/
│       └── ...
├── 04_queues/
│   ├── implementation/
│   │   ├── queue_array.py
│   │   ├── queue_linkedlist.py
│   │   ├── circular_queue.py
│   │   └── deque.py
│   └── leetcode/
│       └── ...
├── ...
```

> Each folder has an **`implementation/`** subfolder for building data structures from scratch + a **`leetcode/`** subfolder for technique-based problem solving.

---

## 📌 How to Use This Plan

1. **Start with 📦 Implementation** — For each section, FIRST build the data structure / algorithm from scratch. Understand the internals, operations, and time/space complexity.
2. **Then move to 🏋️ LeetCode Practice** — Learn the techniques listed and solve the problems. The techniques are patterns that USE the data structure you just built.
3. **Check off items** as you complete them.
4. **Don't skip implementation** — If you can't build a stack from scratch, you won't truly understand why monotonic stack works. Implementation first, patterns second.
