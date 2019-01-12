# Backpack

## 描述
在n个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为m，每个物品的大小为A[i]


## 样例
如果有4个物品[2, 3, 5, 7]

如果背包的大小为11，可以选择[2, 3, 5]装入背包，最多可以装满10的空间。

如果背包的大小为12，可以选择[2, 3, 7]装入背包，最多可以装满12的空间。

函数需要返回最多能装满的空间大小。

## 解答
第一版: 单纯的动态规划实现，但只通过了56%数据，内存就爆了
```python
def backPack(self, m, A):
    len_a = len(A)
    dp = [[0 for _ in range(m+1)] for _ in range(len_a)]
    for i in range(len_a):
        for j in range(m + 1):
            if A[i] > j:
                dp[i][j] = 0 if i < 1 else dp[i - 1][j]
            else:
                dp[i][j] = max(A[i], dp[i-1][j], dp[i-1][j-A[i]] + A[i])
    return dp[len_a-1][m]
```
第二版: 在第一版的基础上用了滚动数组来减小空间复杂度，通过了78%数据后，超时了
```python
def backPack(self, m, A):
    len_a = len(A)
    dp = [[0 for _ in range(m+1)] for _ in range(2)]
    for i in range(len_a):
        c_row = i % 2
        o_row = (i + 1) % 2
        for j in range(m + 1):
            if A[i] > j:
                dp[c_row][j] = dp[o_row][j]
            else:
                dp[c_row][j] = max(A[i], dp[o_row][j], dp[o_row][j-A[i]] + A[i])
    return dp[(len_a+1) % 2][m]
```
第三版: 在第二版的基础上对效率略做了优化，差不多提高了近25%～40%的效率，通过了所有测试数据
```python
def backPack(self, m, A):
    len_a = len(A)
    A.sort()
    dp = [[0 for _ in range(m + 1)] for _ in range(2)]
    for i in range(len_a):
        c_row = i % 2
        o_row = (i + 1) % 2
        dp_o_row = dp[o_row]
        dp[c_row] = dp_o_row.copy()
        dp_c_row = dp[c_row]
        ai = A[i]
        for j in range(ai, m + 1):
            dp_c_row[j] = max(dp_o_row[j], dp_o_row[j-ai] + ai)
    return dp[(len_a + 1) % 2][m]
```