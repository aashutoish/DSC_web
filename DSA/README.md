# DSA Lab Programs (Python)

This folder contains Data Structures and Algorithms lab programs, organized topic-wise.

## Folder Structure

- 01_Stacks_and_Queues
  - Stack (from scratch, using list)
  - Bracket matching
  - Infix to postfix
  - Postfix evaluation
  - Queue using array
  - Priority queue

- 02_Linked_List
  - Basic linked list
  - Singly linked list
  - Doubly linked list
  - Circular linked list
  - Stack and queue using linked list

- 03_Trees
  - Tree insert and retrieve
  - BFS traversal
  - DFS traversal
  - Binary search tree
  - AVL tree
  - Heap
  - Priority queue using heap

- 04_Searching
  - Sequential search
  - Binary search
  - Basic hashing
  - Probing and double hashing
  - Separate chaining

- 05_Sorting
  - Bubble, insertion, selection, merge, quick, and heap sort

- 06_Graphs
  - Graph BFS and DFS
  - Kruskal MST
  - Prim MST

- 07_Algorithm_Design
  - Fibonacci (recursive, memoized, tabulation, optimized)

## Combined Notebook

- DSA_Final_All_Code.ipynb
  - Single notebook containing all programs from all folders

## Run Any Program

From the DSA folder:

```bash
python3 03_Trees/06_heap.py
```

## Run All Programs

```bash
passed=0; failed=0;
for file in 01_Stacks_and_Queues/*.py 02_Linked_List/*.py 03_Trees/*.py 04_Searching/*.py 05_Sorting/*.py 06_Graphs/*.py 07_Algorithm_Design/*.py; do
  python3 "$file" > /dev/null 2>&1 && ((passed++)) || ((failed++))
done

echo "PASSED:$passed"
echo "FAILED:$failed"
```
