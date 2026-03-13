"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climbStairsv2(n: int) -> int:
    """
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
    """

    def fib(n):
        if n <= 1:
            return n
        return fib(n-1) + fib(n-2)

    return fib(n+1)

def climbStairsv1(n: int) -> int:
    one, two = 1, 1

    for i in range(n-1):
        prev = one
        one = one + two
        two = prev

    return one





climbStairsv1(n = 5)
# climbStairs(n = 10)
