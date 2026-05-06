# Fibonacci Dynamic Programming

# 1. Naive recursion - slow but simple
def fib_recursive(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# 2. Memoization - using dictionary to store results
def fib_memoized(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fib_memoized(n - 1, memo) + fib_memoized(n - 2, memo)
    return memo[n]


# 3. Tabulation - build array from bottom up
def fib_tabulation(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# 4. Space optimized - only keep last two values
def fib_optimized(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    prev2 = 0
    prev1 = 1
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return prev1


if __name__ == "__main__":
    print("Fibonacci using different DP approaches:\n")
    
    # Test recursive
    print("Recursive approach:")
    for n in [5, 10, 15]:
        print(f"F({n}) = {fib_recursive(n)}")
    
    # Test memoization
    print("\nMemoization approach:")
    for n in [5, 10, 20]:
        print(f"F({n}) = {fib_memoized(n)}")
    
    # Test tabulation
    print("\nTabulation approach:")
    for n in [5, 10, 20]:
        print(f"F({n}) = {fib_tabulation(n)}")
    
    # Test optimized
    print("\nOptimized approach:")
    for n in [5, 10, 20, 30, 50]:
        print(f"F({n}) = {fib_optimized(n)}")
    
    # Show DP table example
    print("\nDP table for n=10:")
    n = 10
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp)
