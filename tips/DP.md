
# Dynamic Programming

## Steps to solve a DP

1. Identify if it is a DP problem
    - min,max,count problems
    - overlapping subproblems
    - optimal substructure

2. Decide a state expression with least parameters
    - state:uniquely identify a subproblem
    - 一组参数，唯一标识子问题

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
        + 部分子问题求解
        + `DP[n] = DP[n - 1] + DP[n - 3] + DP[n-5]` 自顶向下相对容易
        + 递归一致

   - Tabulation (Bottom Up)
        + 从底层开始循环
        + 每个子问题求解
        + DP table保存所有子问题的解
        + 迭代一致

## Optimal Substructure 

+ the Shortest Path problem 
    + A到B的最短路径上有x
        + short(A,B)=short(A,X)+short(X,B)

## tips

+ 不做重复计算
+ 子问题不是孤立的

## ref
+ [动态规划之武林秘籍](https://mp.weixin.qq.com/s?__biz=MzA4NDE4MzY2MA==&mid=2647523785&idx=1&sn=7df30854c688a51b01bd5e369900b4f5&scene=21#wechat_redirect)

+ [帽子](https://toutiao.io/posts/zym4cal/preview)

+ [Overlapping Subproblems Property in Dynamic Programming | DP-1](https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/)
+ [Optimal Substructure Property in Dynamic Programming | DP-2](https://www.geeksforgeeks.org/optimal-substructure-property-in-dynamic-programming-dp-2/)
+ [How to solve a Dynamic Programming Problem ?](https://www.geeksforgeeks.org/solve-dynamic-programming-problem/)


