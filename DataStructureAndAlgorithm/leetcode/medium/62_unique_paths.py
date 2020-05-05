class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cal_value = [[1 if i == 0 or j == 0 else 0 for i in range(m)] for j in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                cal_value[i][j] = cal_value[i - 1][j] + cal_value[i][j - 1]

        return cal_value[n - 1][m - 1]


if __name__ == '__main__':
    print("......", Solution().uniquePaths(7, 3))
