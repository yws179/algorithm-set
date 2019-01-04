# 深度优先搜索DFS

为了实现DFS算法，我特意从LintCode上找题目来实现，可惜很多题目使用DFS都无法通过所有的测试数据。

### 622 青蛙跳（DFS通过90%的测试数据）

一只青蛙正要过河，这条河分成了 x 个单位，每个单位可能存在石头，青蛙可以跳到石头上，但它不能跳进水里。
按照顺序给出石头所在的位置，判断青蛙能否到达最后一块石头所在的位置。刚开始时青蛙在第一块石头上，假设青蛙第一次跳只能跳一个单位的长度。
如果青蛙最后一个跳 k 个单位，那么它下一次只能跳 `k - 1` ，`k` 或者 `k + 1`个单位。注意青蛙只能向前跳。

#### 样例

给出石头的位置为 [0,1,3,5,6,8,12,17]

总共8块石头。
第一块石头在 0 位置，第二块石头在 1 位置，第三块石头在 3 位置等等......
最后一块石头在 17 位置。

返回 true。青蛙可以通过跳 1 格到第二块石头，跳 2 格到第三块石头，跳 2 格到第四块石头，跳 3 格到第六块石头，跳 4 格到第七块石头，最后跳 5 格到第八块石头。

给出石头的位置为 `[0,1,2,3,4,8,9,11]`
返回 false。青蛙没有办法跳到最后一块石头因为第五块石头跟第六块石头的距离太大了。

```python
class Solution:

    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, stones):
        return self.dfs(0, 1, stones)

    def dfs(self, current, k, s):
        len_s = len(s)
        if current + 1 == len_s:
            return True
        next_x = s[current] + k
        next_s = self.get_next_stone_idx(next_x, current, s)
        if next_s is not None and k > 0 and next_s < len_s and s[next_s]:
            return self.dfs(next_s, k-1, s) or self.dfs(next_s, k, s) or self.dfs(next_s, k+1, s)
        return False

    def get_next_stone_idx(self, x, current_stone_idx, stones):
        for i in range(current_stone_idx, len(stones)):
            if stones[i] > x:
                return None
            if stones[i] == x:
                return i
        return None
```

### 1612 最小的行程（DFS通过70%的测试数据）

给定一个二维矩阵，找到从上到下的最小路径。只能向左下，下，右下移动

#### 样例

[
 1, 2, 3
 4, 5, 6
 7, 8, 9
]
最短的行程:1->4->7, 返回 12

```python
class Solution:
    
    def __init__(self):
        self.h = 0
        self.w = 0
        self.min_dist = float('inf')
    
    """
    @param matrix: 
    @return: Return the smallest path
    """
    def smallestPath(self, matrix):
        self.h = len(matrix)
        self.w = len(matrix[0])
        for i in range(self.w):
            self.dfs(i, 0, 0, matrix)
        return self.min_dist

    def dfs(self, x, y, dist, matrix):
        if x < 0 or y >= self.h or x >= self.w:
            return
        new_dist = dist + matrix[y][x]
        if new_dist > self.min_dist:
            return
        if y + 1 == self.h:
            if self.min_dist > new_dist:
                self.min_dist = new_dist
            return
        self.dfs(x - 1, y + 1, new_dist, matrix)
        self.dfs(x, y + 1, new_dist, matrix)
        self.dfs(x + 1, y + 1, new_dist, matrix)
```

