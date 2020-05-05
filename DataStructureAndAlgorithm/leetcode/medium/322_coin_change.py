import sys


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        cac_value = [0]

        for i in range(1, amount + 1):
            cac_value.append(min(cac_value[i - c] + 1 if i - c >= 0 else sys.maxsize for c in coins))

        return -1 if cac_value[amount] >= sys.maxsize else cac_value[amount]


if __name__ == '__main__':
    print("......", Solution().coinChange([2], 3))

    test = [[1 if i == 0 or j == 0 else 0 for i in range(3)] for j in range(7)]
    print()
    """
        Time Complexity = O(N^2)
        Space Complexity = O(N)
        You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. 
        If that amount of money cannot be made up by any combination of the coins, return -1.
        Example:
        Input: coins = [1, 2, 5], amount = 11
        Output: 3 
        Explanation: 11 = 5 + 5 + 1
    """