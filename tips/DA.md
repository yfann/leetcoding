
# Dynamic Programming

## Steps to solve a DP

1. Identify if it is a DP problem
    - min,max,count problems
    - overlapping subproblems
    - optimal substructure

2. Decide a state expression with least parameters
    - state:uniquely identify a subproblem

3. *Formulate state relationship    
    - 找到当前state和之前state的联系
    - 写出递归

4. Do tabulation (or add memoization)
    - 优化递归
        + Memoization
        + Tabulation

## Overlapping Subproblems

+ store value
   - Memoization (Top Down) 
        + 缓存递归的中间值
   - Tabulation (Bottom Up)
        + 从底层开始循环

## Optimal Substructure 

+ the Shortest Path problem 
    + A到B的最短路径上有x
        + short(A,B)=short(A,X)+short(X,B)

## ref
+ [Overlapping Subproblems Property in Dynamic Programming | DP-1](https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/)
+ [Optimal Substructure Property in Dynamic Programming | DP-2](https://www.geeksforgeeks.org/optimal-substructure-property-in-dynamic-programming-dp-2/)
+ [How to solve a Dynamic Programming Problem ?](https://www.geeksforgeeks.org/solve-dynamic-programming-problem/)